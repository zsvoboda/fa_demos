# Enable strict mode and script error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Add-RawSidAcl {
    param (
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Sid,

        [string]$AccessMask = "0x1200a9"  # Read + Write
    )

    if (-not (Test-Path $Path)) {
        throw "The path '$Path' does not exist."
    }

    try {
        $acl = Get-Acl $Path
        $sddl = $acl.GetSecurityDescriptorSddlForm('All')

        # Validate SID format
        if ($Sid -notmatch '^S-\d-\d+-(\d+-?)+$') {
            throw "The SID '$Sid' is not in a valid format."
        }

        # Validate that SDDL ends with a closing parenthesis
        if ($sddl -notmatch '\)$') {
            throw "The SDDL string for '$Path' does not end in a valid ACE block: $sddl"
        }

        # Construct and inject new ACE
        $ace = "(A;;$AccessMask;;;$Sid)"
        $newSddl = $sddl -replace '\)$', "$ace)"

        Write-Host "Adding SID '$Sid' to '$Path' with access mask '$AccessMask'..."
        Write-Host "Current SDDL: $sddl"
        Write-Host "New SDDL: $newSddl"

        # Set updated ACL
        $acl.SetSecurityDescriptorSddlForm($newSddl)
        Set-Acl -Path $Path -AclObject $acl

        Write-Host "✅ Successfully added SID '$Sid' to '$Path'"
    }
    catch {
        Write-Error "❌ Error setting $Path permissions: $_"
    }
}

# Set up paths
$THIS_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ROOT_DIR = Resolve-Path "$THIS_DIR\.."
$SRC_DIR = Join-Path $ROOT_DIR "src"
$LIB_DIR = Join-Path $ROOT_DIR "lib"

# Set PYTHONPATH environment variable
${env:PYTHONPATH} = "$ROOT_DIR;$SRC_DIR;$LIB_DIR"

# Activate the virtual environment
& "$ROOT_DIR\.venv\Scripts\Activate.ps1"

# Load environment variables from .env
Get-Content "$ROOT_DIR\.env" | ForEach-Object {
    if ($_ -match "^\s*([^#][^=]*)=(.*)$") {
        $key = $matches[1].Trim()
        $val = $matches[2].Trim()
        Set-Item -Path "env:$key" -Value $val
    }
}

Write-Host "PYTHONPATH: ${env:PYTHONPATH}"

Write-Host "Setting up Flash Array..."

# Run setup script
& "python.exe" "$SRC_DIR\demos\multi_protocol\setup_array.py" setup

Write-Host "Setup completed."
Write-Host "Mapping the Z: drive to a share..."
net use "Z:" "\\${env:FA_DEMO_VIF_HOSTNAME}\multi" /USER:"${env:FA_DEMO_USER_DOMAIN}\win_user" "password"

# Clean up any existing files
Remove-Item "Z:\*" -Force -Recurse -ErrorAction SilentlyContinue

Write-Host "Now, let's create a shared directory."
New-Item -Path "Z:\shared_dir" -ItemType Directory | Out-Null

Write-Host "Setting permissions on the shared directory..."


if (${env:FA_DEMO_USE_AD} -eq "true") {
    $domainName = ${env:FA_DEMO_USER_DOMAIN}
} else {
    $domainName = ${env:FA_DEMO_VIF_HOSTNAME}
}
$domainController = ${env:FA_DEMO_AD_HOSTNAME}

try {
    $win_user_sid = (Get-ADGroup "win_users" -Server $domainController -Properties SID).SID.Value
    $nfs_daemon_sid = (Get-ADGroup "nfs_daemons" -Server $domainController -Properties SID).SID.Value
    if (-not $win_user_sid -or -not $nfs_daemon_sid) {
        Write-Host "❌ Failed to retrieve SIDs for win_users or nfs_daemons group."
        exit 1
    }
    Write-Host "✅ Retrieved win_users group's SID: $win_user_sid and nfs_daemons group's SID: $nfs_daemon_sid"
    Add-RawSidAcl -Path "Z:\shared_dir" -Sid "${win_user_sid}"
    Add-RawSidAcl -Path "Z:\shared_dir" -Sid "${nfs_daemon_sid}"

} catch {
    Write-Host "❌ Error setting Z:\shared_dir permissions: $_"
    exit 1
}

Write-Host "Creating a test file on the Z:\ drive..."
"Test content written from SMB mapped drive." | Out-File -Encoding ASCII "Z:\shared_dir\file_from_windows_smb_session.txt"

Write-Host "Now run the demo_multiprotocol.sh script from a Linux instance to test the multi-protocol functionality."
Read-Host "Then, press Enter to check access to a file created from the Linux NFS session..."

if (Test-Path "Z:\shared_dir\file_from_linux_nfs_session.txt") {
    Write-Host "File from Linux NFS session exists."
    Get-Content "Z:\shared_dir\file_from_windows_smb_session.txt"
} else {
    Write-Host "File from Linux NFS session does NOT exist."
}

Read-Host "Press Enter to clean up the environment..."
Write-Host "Cleaning up..."

Remove-Item -Path "Z:\shared_dir" -Recurse -Force -ErrorAction SilentlyContinue
net use Z: /DELETE

& "$ROOT_DIR\.venv\Scripts\python.exe" "$SRC_DIR\demos\multi_protocol\setup_array.py" cleanup

Write-Host "Cleanup completed."
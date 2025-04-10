# Enable strict mode and script error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Set up paths
$THIS_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ROOT_DIR = Resolve-Path "$THIS_DIR\.."
$SRC_DIR = Join-Path $ROOT_DIR "src"
$LIB_DIR = Join-Path $ROOT_DIR "lib"

# Set PYTHONPATH environment variable
${PYTHONPATH} = "$ROOT_DIR;$SRC_DIR;$LIB_DIR"

# Activate the virtual environment
& "$ROOT_DIR\.venv\Scripts\Activate.ps1"

# Load environment variables from .env
Get-Content "$ROOT_DIR\.env" | ForEach-Object {
    if ($_ -match "^\s*([^#][^=]*)=(.*)$") {
        $key = $matches[1].Trim()
        $val = $matches[2].Trim()
        Set-Item -Path "Env:$key" -Value $val
    }
}

Write-Host "Setting up Flash Array..."

# Run setup script
& "python.exe" "$SRC_DIR\demos\multi_protocol\setup_array.py" setup

Write-Host "Setup completed."
Write-Host "Mapping the Z: drive to a share..."
net use "Z:\" "\\${Env:FA_DEMO_VIF_HOSTNAME}\multi" /USER:"${Env:FA_DEMO_USER_DOMAIN}\win_user" "password"

# Clean up any existing files
Remove-Item "Z:\*" -Force -Recurse -ErrorAction SilentlyContinue

Write-Host "Now, let's create a shared directory."
New-Item -Path "Z:\shared_dir" -ItemType Directory | Out-Null

Write-Host "Setting permissions on the shared directory..."


if (${Env:FA_DEMO_USE_AD} -eq "true") {
    $domainName = ${Env:FA_DEMO_USER_DOMAIN}
} else {
    $domainName = ${Env:FA_DEMO_VIF_HOSTNAME}
}
$domainController = ${Env:FA_DEMO_AD_HOSTNAME}

try {
    $win_user_sid = (Get-ADUser "$domainName\win_user" -Server $domainController -Properties SID).SID.Value
    $nfs_daemon_sid = (Get-ADUser "$domainName\nfs_daemon" -Server $domainController -Properties SID).SID.Value
    if (-not $sid) {
        Write-Host "❌ Failed to retrieve SIDs for win_user or nfs_daemon."
        exit 1
    }
    Write-Host "✅ Retrieved win_user's SID: $sid and nfs_daemon SID: $nfs_daemon_sid"
    icacls "Z:\shared_dir" /grant *$win_user_sid`:(OI)(CI)RW
    icacls "Z:\shared_dir" /grant *$nfs_daemon_sid`:(OI)(CI)RW

} catch {
    Write-Host "❌ Error querying AD: $_"
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
@echo off
setlocal

set THIS_DIR=%~dp0
set SRC_DIR=%THIS_DIR%\..\src
set LIB_DIR=%THIS_DIR%\..\lib
set ROOT_DIR=%THIS_DIR%\..
set PYTHONPATH=%ROOT_DIR%;%SRC_DIR%;%LIB_DIR%

:: Activate the virtual environment
call %THIS_DIR%\..\.venv\Scripts\activate

for /f "delims=" %%x in (%THIS_DIR%..\.env) do set %%x
echo "Setting up Flash Array..."

%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\demos\multi_protocol\setup_array.py setup

echo "Setup completed."
echo "Mapping the Z:\ drive to a share."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\multi /USER:%FA_DEMO_USER_DOMAIN%\win_user password
del /f /q "Z:\*"

echo "Now, let's create a shared directory."
mkdir Z:\shared_dir
echo "Now, let's set the inherited permissions on the directory for win_users to allow access."

icacls "Z:\shared_dir" /grant "%FA_DEMO_USER_DOMAIN%\win_users:(OI)(CI)RW"
icacls "Z:\shared_dir" /grant "%FA_DEMO_USER_DOMAIN%\nfs_daemons:(OI)(CI)RW"

echo "Creating a test file on the Z:\ drive..."
echo Test content written from SMB mapped drive. > Z:\shared_dir\file_from_windows_smb_session.txt

echo "Now run the demo_multiprotocol.sh script from a Linux instance to test the multi-protocol functionality."
echo "Then, Press any key to check access to a file created from the Linux NFS session ..."

pause

if exist "Z:\shared_dir\file_from_linux_nfs_session.txt" (
    echo File from Linux NFS session exists.
    type "Z:\shared_dir\file_from_windows_smb_session.txt"
) else (
    echo File from Linux NFS session does NOT exist.
)

echo "Press a key to clean up the environment..."
pause
echo "Cleaning up..."
del /f /q "Z:\shared_dir"
NET USE Z: /DELETE

%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\demos\multi_protocol\setup_array.py cleanup

echo "Cleanup completed."
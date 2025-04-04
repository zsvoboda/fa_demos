@echo off
setlocal

set THIS_DIR=%~dp0
set SRC_DIR=%THIS_DIR%\..\src
set LIB_DIR=%THIS_DIR%\..\lib
set PYTHONPATH=%LIB_DIR%;%SRC_DIR%

for /f "delims=" %%x in (%THIS_DIR%..\.env) do set %%x
echo "Setting up Flash Array..."

python %SRC_DIR%\demos\multi_protocol\setup_array.py setup

echo "Setup completed."
echo "Mapping the Z:\ drive to a share."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\multi /USER:%FA_DEMO_USER_DOMAIN%\win_user password
del /q Z:\*

echo "Now, let's create a shared directory."
mkdir Z:\shared_dire
echo "Now, let's set the inherited permissions on the directory for win_users to allow access."
icacls Z:\shared_dire /inheritance:enable /grant "win_users:(OI)(CI)M"
echo "Creating a test file on the Z:\ drive..."
type "Test content written from SMB mapped drive." > Z:\shared_dire\file_from_windows_smb_session.txt

echo "Now run the demo_multiprotocol.sh script from a Linux instance to test the multi-protocol functionality."
echo "Then, Press any key to cleanup..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE

python %SRC_DIR%\demos\multi_protocol\setup_array.py cleanup

echo "Cleanup completed."
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

echo "Active DR Demo"
echo "=============="
echo.
echo "This demo showcases the Active-Passive Disaster Recovery (Active DR) functionality"
echo "between two FlashArrays, where data is replicated from a source array to a target array."
echo.
echo "Source Array: %FA_DEMO_HOSTNAME%"
echo "Target Array: %FA_DEMO_REMOTE_HOSTNAME%"
echo.

echo "Setting up Active DR..."
python %SRC_DIR%\demos\active_dr\setup_array.py setup

echo.
echo "Active DR setup completed."
echo "The following resources have been created:"
echo "- Pod 'replicated-source' on the source array"
echo "- File system 'replicated-source::file_system'"
echo "- NFS and SMB exports for the file system"
echo "- Replica link between source and target arrays"
echo.

echo "Mapping the Z:\ drive to the source array file system..."
NET USE Z: \\%FA_DEMO_HOSTNAME%\replicated_smb_share /USER:%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%
if errorlevel 1 (
    echo "Failed to map the Z:\ drive. Please check your credentials and network connectivity."
    goto cleanup
)

echo "Creating a test file on the source array file system..."
echo "This is a test file for Active DR replication." > Z:\test_replication.txt
if errorlevel 1 (
    echo "Failed to create the test file. Please check your permissions."
    goto cleanup
)

echo.
echo "Test file created successfully on the source array."
echo "Waiting for the file to replicate to the target array..."
echo "This typically takes a few minutes depending on your environment."

echo "Mapping the Y:\ drive to the target array file system..."
NET USE Y: \\%FA_DEMO_REMOTE_HOSTNAME%\replicated_smb_share /USER:%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%
if errorlevel 1 (
    echo "Failed to map the Y:\ drive. Please check your credentials and network connectivity."
    goto cleanup
)

echo "Checking if the test file has been replicated to the target array..."
if exist Y:\test_replication.txt (
    echo "Success! The test file has been replicated to the target array."
    echo "File content:"
    type Y:\test_replication.txt
) else (
    echo "The test file has not been replicated to the target array yet."
    echo "This could be due to replication delay or configuration issues."
)

echo "Press any key to clean up..."
pause

:cleanup
NET USE Z: /DELETE
NET USE Y: /DELETE
echo "Cleaning up..."
python %SRC_DIR%\demos\active_dr\setup_array.py cleanup

echo "Cleanup completed."

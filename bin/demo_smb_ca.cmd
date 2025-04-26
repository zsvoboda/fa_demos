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

echo "SMB Continuous Availability Demo"
echo "================================"
echo.
echo "This demo showcases the capabilities of SMB Continuous Availability (SMB CA),"
echo "a critical feature for enterprise environments requiring high availability"
echo "for Windows file shares."
echo.
echo "The demo demonstrates:"
echo "- Seamless transition of SMB clients during controller failover"
echo "- Preservation of file locks and open file handles"
echo "- Comparison between shares with and without SMB CA enabled"
echo.

echo "Setting up Flash Array..."

python %SRC_DIR%\demos\smb_ca\setup_array.py setup

echo "Setup completed."
echo "Please manually configure smb_ca_policy on the array to use SMB CA."
pause

echo "Mapping the Z:\ drive to a share without SMB CA setting."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\smb_no_ca /USER:%FA_DEMO_USER_DOMAIN%\%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%
del /q Z:\*

echo "Mapping the Y:\ drive to a share with SMB CA setting."
NET USE Y: \\%FA_DEMO_VIF_HOSTNAME%\smb_ca /USER:%FA_DEMO_USER_DOMAIN%\%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%
del /q Y:\*

echo "Now, let's copy a large file to the mapped drive Z:\ without SMB CA enabled."
pause

echo "Large file copy in progress on SMB mapped drive Z:\ with SMB CA disabled ..."
echo "This will take a while..."
%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\util\randcopy.py -n 6000000000 Z:\\test_file.bin

echo "Now, let's copy a large file to the mapped drive Y:\ with SMB CA enabled."
pause

echo "Large file copy in progress on SMB mapped drive Y:\ with SMB CA enabled ..."
echo "This will take a while..."
%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\util\randcopy.py -n 6000000000 Y:\\test_file.bin

echo "Click any key to clean up..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE
NET USE Y: /DELETE

python %SRC_DIR%\demos\smb_ca\setup_array.py cleanup

echo "Cleanup completed."

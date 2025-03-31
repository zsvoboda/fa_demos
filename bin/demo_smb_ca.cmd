@echo off
setlocal

set THIS_DIR=%~dp0
set SRC_DIR=%THIS_DIR%\..\src
set LIB_DIR=%THIS_DIR%\..\lib
set PYTHONPATH=%LIB_DIR%;%SRC_DIR%

for /f "delims=" %%x in (%THIS_DIR%..\.env) do set %%x
echo "Setting up Flash Array..."

python %PYTHONPATH%\demos\smb_ca\setup_array.py setup

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
python %SRC_DIR%\util\randcopy.py -n 6000000000 Z:\\test_file.bin

echo "Now, let's copy a large file to the mapped drive Y:\ with SMB CA enabled."
pause

echo "Large file copy in progress on SMB mapped drive Y:\ with SMB CA enabled ..."
echo "This will take a while..."
python %SRC_DIR%\util\randcopy.py -n 6000000000 Y:\\test_file.bin

echo "Click any key to clean up..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE
NET USE Y: /DELETE

python %SRC_DIR%\demos\smb_ca\setup_array.py cleanup

echo "Cleanup completed."
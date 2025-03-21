@echo off
setlocal

set THIS_DIR=%~dp0
set PYTHONPATH=%THIS_DIR%\..\src

for /f "delims=" %%x in (%THIS_DIR%..\.env) do set %%x
echo "Setting up Flash Array..."

python %PYTHONPATH%\demos\smb_ca\setup_array.py setup

echo "Mapping the Z:\ drive to a share without SMB CA setting."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\smb_no_ca /USER:%FA_DEMO_USER_DOMAIN%\%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%

del /q Z:\*

echo "Large file copy in progress on SMB mapped drive Z:\ with SMB CA disabled ..."
python %PYTHONPATH%\util\randcopy.py -n 6000000000 Z:\\test_file.bin


echo "Please configure smb_ca_policy on the array to use SMB CA."
pause

echo "Mapping the Y:\ drive to a share with SMB CA setting."
NET USE Y: \\%FA_DEMO_VIF_HOSTNAME%\smb_ca /USER:%FA_DEMO_USER_DOMAIN%\%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%

del /q Y:\*

echo "Large file copy in progress on SMB mapped drive Y:\ with SMB CA enabled ..."
python %PYTHONPATH%\util\randcopy.py -n 6000000000 Y:\\test_file.bin

echo "Click any key to clean up..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE:YES
NET USE Y: /DELETE:YES

python %PYTHONPATH%\demos\smb_ca\setup_array.py cleanup

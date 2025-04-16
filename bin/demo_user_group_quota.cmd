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

python %SRC_DIR%\demos\user_group_quota\setup_array.py setup

echo "Setup completed."

echo "Mapping the Z:\ drive to the FlashArray share."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\user_quota_share /USER:%FA_DEMO_USER_DOMAIN%\%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%
del /q Z:\*

echo "Now, let's copy a large file to the mapped drive Z:\."
pause

echo "Large file copy in progress on SMB mapped drive Z:\ ..."
echo "This will take a while..."
%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\util\randcopy.py -n 60000 Z:\\test_file.bin
%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\util\randcopy.py -n 60000 Z:\\test_file2.bin

echo "Click any key to clean up..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE

python %SRC_DIR%\demos\user_group_quota\setup_array.py cleanup

echo "Cleanup completed."
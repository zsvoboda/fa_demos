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

echo "User and Group Quota Demo"
echo "========================="
echo.
echo "This demo showcases the user and group quota functionality of FlashArray File Services,"
echo "which allows administrators to limit storage consumption by specific users or groups."
echo.
echo "The demo demonstrates:"
echo "- Setting up user and group quotas on a file system"
echo "- Monitoring storage usage against quota limits"
echo "- Behavior when quota limits are reached"
echo.

echo "Setting up Flash Array..."

python %SRC_DIR%\demos\user_group_quota\setup_array.py setup

echo "Setup completed."

echo "Mapping the Z:\ drive to the FlashArray share."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\user_quota_share /USER:%FA_DEMO_USER_DOMAIN%\%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%
del /q Z:\*

echo "Now, let's copy multiple 1M files to the mapped drive Z:\."
pause

echo "Multiple 100k files copy in progress on SMB mapped drive Z:\ ..."
for /l %%i in (1,1,300) do (
    %THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\util\randcopy.py -n 1048576 Z:\\test_file%%i.bin
    timeout /t 1 /nobreak >nul
)

echo "Click any key to clean up..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE

python %SRC_DIR%\demos\user_group_quota\setup_array.py cleanup

echo "Cleanup completed."

@echo off
setlocal

set THIS_DIR=%~dp0
set SRC_DIR=%THIS_DIR%\..\src
set LIB_DIR=%THIS_DIR%\..\lib
set PYTHONPATH=%LIB_DIR%;%SRC_DIR%

:: Activate the virtual environment
call %THIS_DIR%\..\.venv\Scripts\activate

for /f "delims=" %%x in (%THIS_DIR%..\.env) do set %%x
echo "Setting up Flash Array..."

python %SRC_DIR%\demos\user_group_quota\setup_array.py setup

echo "Setup completed..."
pause
echo "Cleaning up..."

python %SRC_DIR%\demos\user_group_quota\setup_array.py cleanup

echo "Cleanup completed."
@echo off

set THIS_DIR=%~dp0

:: Activate the virtual environment
call %THIS_DIR%\..\.venv\Scripts\activate

echo Virtual environment activated from %THIS_DIR%.venv
@echo off

set THIS_DIR=%~dp0

:: Activate the virtual environment
call %THIS_DIR%\..\.venv\Scripts\activate

%THIS_DIR%\..\.venv\Scripts\python -m pip install --upgrade pip
%THIS_DIR%\..\.venv\Scripts\python -m pip install -r requirements.txt
%THIS_DIR%\..\.venv\Scripts\python -m pip install %THIS_DIR%\..\pypureclient

echo Virtual environment activated from %THIS_DIR%..\.venv and all required packages installed.
@echo off

set THIS_DIR=%~dp0

:: Activate the virtual environment
call %THIS_DIR%..\.venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Virtual environment activated from %THIS_DIR%..\.venv and all required packages installed.
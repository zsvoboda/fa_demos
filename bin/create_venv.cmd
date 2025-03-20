@echo off

set THIS_DIR=%~dp0

:: Create a virtual environment in the bin directory
python -m venv %THIS_DIR%..\..venv

:: Activate the virtual environment
call %THIS_DIR%..\..venv\Scripts\activate

echo Virtual environment created and activated in %THIS_DIR%..\..venv
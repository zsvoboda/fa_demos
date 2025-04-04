@echo off

set THIS_DIR=%~dp0
set SRC_DIR=%THIS_DIR%\..\src
set LIB_DIR=%THIS_DIR%\..\lib
set PYTHONPATH=%LIB_DIR%;%SRC_DIR%

:: Activate the virtual environment
call %THIS_DIR%\..\.venv\Scripts\activate

%THIS_DIR%\..\.venv\Scripts\python %SRC_DIR%\util\randcopy.py %*
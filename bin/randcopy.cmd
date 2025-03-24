@echo off

set THIS_DIR=%~dp0
set PYTHONPATH=%THIS_DIR%\..\lib;%THIS_DIR%\..\src

python %PYTHONPATH%\util\randcopy.py %*
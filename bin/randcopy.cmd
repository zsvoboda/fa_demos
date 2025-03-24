@echo off

set THIS_DIR=%~dp0
set SRC_DIR=%THIS_DIR%\..\src
set LIB_DIR=%THIS_DIR%\..\lib
set PYTHONPATH=%LIB_DIR%;%SRC_DIR%


python %SRC_DIR%\util\randcopy.py %*
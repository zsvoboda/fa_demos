@echo off
setlocal


set THIS_DIR=%~dp0
set PYTHONPATH=%THIS_DIR%..\src

for /f "delims=" %%x in (%THIS_DIR%..\..\.env) do set %%x

python %PYTHONPATH%\demos\smb_ca\setup_array setup

echo "Please configure smb_ca_policy on the array to use SMB CA"
pause

NET USE Z: \\%FA_DEMO_HOSTNAME%\smb_no_ca /USER:%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%

del /q Z:\*

python %PYTHONPATH%\util\randcopy.py -n 10737418240 -d Z:\

NET USE Z: /DELETE

NET USE Z: \\%FA_DEMO_HOSTNAME%\smb_ca /USER:%FA_DEMO_USER_NAME% %FA_DEMO_USER_PASSWORD%

del /q Z:\*

python %PYTHONPATH%\util\randcopy.py -n 10737418240 -d Z:\

echo "File copied succesfully!"
pause

NET USE Z: /DELETE

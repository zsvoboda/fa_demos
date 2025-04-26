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

echo "Multi-Protocol Demo"
echo "==================="
echo.
echo "This demo showcases how Linux NFS and Windows SMB users can collaboratively"
echo "access and interact with the same shared directory for reading and writing files."
echo.
echo "The demo demonstrates:"
echo "- Unified storage accessible via both NFS and SMB protocols"
echo "- Consistent permissions across different operating systems"
echo "- Cross-platform file sharing and collaboration"
echo.

if /i "%FA_DEMO_USE_AD%"=="true" (
    echo "Using Active Directory for authentication."
    set FA_DEMO_WIN_USER_FQDN=%FA_DEMO_AD_DOMAIN%\win_user    
) else (
    echo "Using FA local users."
    set FA_DEMO_WIN_USER_FQDN="domain\win_user"
)

echo "Mapping the Z:\ drive to a share."
NET USE Z: \\%FA_DEMO_VIF_HOSTNAME%\multi /USER:%FA_DEMO_WIN_USER_FQDN% %FA_DEMO_USER_PASSWORD%
del /q Z:\*
if not exist Z:\shared_dir (
    mkdir Z:\shared_dir
)
echo "Testing if Z:\shared_dir\file_from_linux_nfs_session.txt exists..."
if exist Z:\shared_dir\file_from_linux_nfs_session.txt (
    echo "File exists. Printing its content:"
    type Z:\shared_dir\file_from_linux_nfs_session.txt
) else (
    echo "File Z:\shared_dir\file_from_linux_nfs_session.txt does not exist."
)

echo "Copying file to Z:\shared_dir\file_from_windows_smb_session.txt"
echo "This file was created from a Windows SMB session." > Z:\shared_dir\file_from_windows_smb_session.txt

echo "Click any key to clean up..."
pause

echo "Cleaning up..."
NET USE Z: /DELETE
echo "Cleanup completed."

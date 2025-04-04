#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRC_DIR=$THIS_DIR/../src
LIB_DIR=$THIS_DIR/../lib
export PYTHONPATH=$SRC_DIR:$LIB_DIR

set -a
source "$(dirname "$THIS_DIR")/.env"
set +a

sudo mkdir -p /mnt/multi
sudo chmod 777 /mnt/multi

sudo mount -t nfs -o nfsvers=4.1 ${FA_DEMO_VIF_HOSTNAME}:/multi /mnt/multi

echo "Test content written from NFS mounted drive." > /mnt/multi/shared_dir/file_from_linux_nfs_session.txt

read -n 1 -s -r -p "Press any key to check access to the file created from Windows SMB session ..."

if [ -f /mnt/multi/shared_dir/file_from_windows_smb_session.txt ]; then
    echo "File from Windows SMB session exists."
    echo "File content: $(cat /mnt/multi/shared_dir/file_from_windows_smb_session.txt)"
else
    echo "File from Windows SMB session does NOT exists."
fi

read -n 1 -s -r -p "Press any key to clean up ..."

sudo rm -f /mnt/multi/shared_dir/file_from_linux_nfs_session.txt
sudo umount /mnt/multi
sudo rmdir /mnt/multi
echo "Unmounted and removed /mnt/multi directory."
echo "Done."
#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRC_DIR=$THIS_DIR/../src
LIB_DIR=$THIS_DIR/../lib
ROOT_DIR=$THIS_DIR/..
export PYTHONPATH=$SRC_DIR:$ROOT_DIR:$LIB_DIR

set -a
source "$(dirname "$THIS_DIR")/.env"
set +a

# Create users and groups
echo "Creating users and groups ..."

if ! id "win_users" &>/dev/null; then
    groupadd --gid 9060 win_users  
    useradd --uid 9060 --gid 9060 win_user
fi

if ! id "nfs_daemons" &>/dev/null; then
    groupadd --gid 9050 nfs_daemons  
    useradd --uid 9050 --gid 9050 nfs_daemon
fi

python3 $SRC_DIR/demos/multi_protocol/setup_array.py "setup"

mkdir -p /mnt/multi
chmod 777 /mnt/multi

mount -t nfs -o nfsvers=4.1 ${FA_DEMO_VIF_HOSTNAME}:/multi /mnt/multi

mkdir -p /mnt/multi/shared_dir
chown nfs_daemon:nfs_daemons /mnt/multi/shared_dir
nfs4_setfacl -a A:g:win_users:RW:fd /mnt/multi/shared_dir
nfs4_setfacl -a A:g:nfs_daemons:RW:fd /mnt/multi/shared_dir

echo "Test content written from NFS mounted drive." > /mnt/multi/shared_dir/file_from_linux_nfs_session.txt

read -n 1 -s -r -p "Press any key to check access to the file created from Windows SMB session ..."

if [ -f /mnt/multi/shared_dir/file_from_windows_smb_session.txt ]; then
    echo "File from Windows SMB session exists."
    echo "File content: $(cat /mnt/multi/shared_dir/file_from_windows_smb_session.txt)"
else
    echo "File from Windows SMB session does NOT exists."
fi

read -n 1 -s -r -p "Press any key to clean up ..."

rmdir -f /mnt/multi/shared_dir
umount /mnt/multi
rmdir /mnt/multi
echo "Unmounted and removed /mnt/multi directory."

if id "win_users" &>/dev/null; then
    userdel -rf win_user
    groupdel -f win_users  
fi

if ! id "nfs_daemons" &>/dev/null; then
    userdel -rf nfs_daemon
    groupdel -f nfs_daemons 
fi

python3 $SRC_DIR/demos/multi_protocol/setup_array.py "cleanup"

echo "Done."
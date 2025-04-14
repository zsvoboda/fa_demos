#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRC_DIR=$THIS_DIR/../src
LIB_DIR=$THIS_DIR/../lib
ROOT_DIR=$THIS_DIR/..
export PYTHONPATH=$SRC_DIR:$ROOT_DIR:$LIB_DIR

set -a
source "$(dirname "$THIS_DIR")/.env"
set +a

. ./.venv/bin/activate

# Create users and groups
echo "Creating users and groups ..."

if ! id "win_users" &>/dev/null; then
    sudo groupadd --gid 9060 win_users  
    sudo useradd --uid 9060 --gid 9060 win_user
fi

if ! id "nfs_daemons" &>/dev/null; then
    sudo groupadd --gid 9050 nfs_daemons  
    sudo useradd --uid 9050 --gid 9050 nfs_daemon
fi

python3 $SRC_DIR/demos/multi_protocol/setup_array.py "setup"

sudo mkdir -p /mnt/multi
sudo chmod 777 /mnt/multi

sudo mount -t nfs -o nfsvers=4.1 ${FA_DEMO_VIF_HOSTNAME}:/multi /mnt/multi

sudo mkdir -p /mnt/multi/shared_dir

if [ "$FA_DEMO_USE_AD" = "true" ]; then
    echo "Configuring Active Directory integration ..."
    DEMO_DOMAIN="FA_DEMO_AD_DOMAIN_NAME"

else
    echo "Skipping Active Directory integration as FA_DEMO_USE_AD is not set to true."
    DEMO_DOMAIN="domain"
fi

echo "Setting up NFS ACLs for shared_dir ..."
echo nfs4_setfacl -a "A:gfd:win_users@${DEMO_DOMAIN}:RW" /mnt/multi/shared_dir
nfs4_setfacl -a "A:gfd:win_users@${DEMO_DOMAIN}:RW" /mnt/multi/shared_dir
echo nfs4_setfacl -a "A:gfd:nfs_daemons@${DEMO_DOMAIN}:RW" /mnt/multi/shared_dir
sudo nfs4_setfacl -a "A:gfd:nfs_daemons@${DEMO_DOMAIN}:RW" /mnt/multi/shared_dir

echo "Test content written from NFS mounted drive." > /mnt/multi/shared_dir/file_from_linux_nfs_session.txt

read -n 1 -s -r -p "Press any key to check access to the file created from Windows SMB session ..."

if [ -f /mnt/multi/shared_dir/file_from_windows_smb_session.txt ]; then
    echo "File from Windows SMB session exists."
    echo "File content: $(cat /mnt/multi/shared_dir/file_from_windows_smb_session.txt)"
else
    echo "File from Windows SMB session does NOT exists."
fi

read -n 1 -s -r -p "Press any key to clean up ..."

sudo rm -rf /mnt/multi/shared_dir
sudo umount /mnt/multi
sudo rmdir /mnt/multi
echo "Unmounted and removed /mnt/multi directory."

if id "win_users" &>/dev/null; then
    sudo userdel -rf win_user
    sudo groupdel -f win_users  
fi

if ! id "nfs_daemons" &>/dev/null; then
    sudo userdel -rf nfs_daemon
    sudo groupdel -f nfs_daemons 
fi

python3 $SRC_DIR/demos/multi_protocol/setup_array.py "cleanup"

echo "Done."
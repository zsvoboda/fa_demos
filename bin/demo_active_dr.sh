#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRC_DIR=$THIS_DIR/../src
LIB_DIR=$THIS_DIR/../lib
ROOT_DIR=$THIS_DIR/..
export PYTHONPATH=$SRC_DIR:$ROOT_DIR:$LIB_DIR

# Define cleanup function
cleanup_exit() {
    sudo umount /mnt/activedr_source
    echo "Source file system unmounted."

    sudo umount /mnt/activedr_target
    echo "Target file system unmounted."

    sudo rmdir /mnt/activedr_source /mnt/activedr_target
    echo "Mount points removed."

    echo "Cleaning up..."
    python3 $SRC_DIR/demos/active_dr/setup_array.py cleanup

    echo "Cleaning up..."
    python3 $SRC_DIR/demos/active_dr/setup_array.py cleanup
    echo "Cleanup completed."
    exit 1
}

set -a
source "$(dirname "$THIS_DIR")/.env"
set +a

. ./.venv/bin/activate

echo "Active DR Demo"
echo "=============="
echo
echo "This demo showcases the Active-Passive Disaster Recovery (Active DR) functionality"
echo "between two FlashArrays, where data is replicated from a source array to a target array."
echo
echo "Source Array: $FA_DEMO_HOSTNAME"
echo "Target Array: $FA_DEMO_REMOTE_HOSTNAME"
echo

echo "Setting up Active DR..."
python3 $SRC_DIR/demos/active_dr/setup_array.py setup

echo
echo "Active DR setup completed."
echo "The following resources have been created:"
echo "- Pod 'replicated-source' on the source array"
echo "- File system 'replicated-source::file_system'"
echo "- NFS and SMB exports for the file system"
echo "- Replica link between source and target arrays"
echo

echo "Creating mount points for source and target file systems..."
sudo mkdir -p /mnt/activedr_source
sudo chmod 777 /mnt/activedr_source

echo "Mounting the source array file system..."
sudo mount -t nfs -o nfsvers=4.1 ${FA_DEMO_VIF_HOSTNAME}:/replicated_nfs_export /mnt/activedr_source
if [ $? -ne 0 ]; then
    echo "Failed to mount the source file system. Please check your network connectivity."
    cleanup_exit
fi

echo "Creating a test file on the source array file system..."
echo "This is a test file for Active DR replication." > /mnt/activedr_source/test_replication.txt
if [ $? -ne 0 ]; then
    echo "Failed to create the test file. Please check your permissions."
    cleanup_exit
fi

echo
echo "Test file created successfully on the source array."
echo "Waiting for the file to replicate to the target array..."
echo "This typically takes a few minutes depending on your environment."
echo

read -n 1 -s -r -p "Press any key when you're ready to check if the file has been replicated to the target array..."
echo

echo "Creating mount point for target file system..."
sudo mkdir -p /mnt/activedr_target
sudo chmod 777 /mnt/activedr_target

echo "Mounting the target array file system..."
sudo mount -t nfs -o nfsvers=4.1 ${FA_DEMO_REMOTE_VIF_HOSTNAME}:/replicated-target /mnt/activedr_target
if [ $? -ne 0 ]; then
    echo "Failed to mount the target file system. Please check your network connectivity."
    cleanup_exit
fi

while true; do
    echo "Checking if the test file has been replicated to the target array..."
    if [ -f /mnt/activedr_target/test_replication.txt ]; then
        echo "Success! The test file has been replicated to the target array."
        echo "File content:"
        cat /mnt/activedr_target/test_replication.txt
    else
        echo "The test file has not been replicated to the target array yet."
        echo "This could be due to replication delay or configuration issues."
    fi

    echo
    echo "Options:"
    echo "1. Check again"
    echo "2. Quit"
    read -p "Enter your choice (1 or 2): " choice

    case $choice in
        1)
            echo "Checking again..."
            ;;
        2)
            echo "Exiting check loop..."
            break
            ;;
        *)
            echo "Invalid choice. Please enter 1 or 2."
            ;;
    esac
done

cleanup_exit



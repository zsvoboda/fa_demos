# Multi-Protocol Demo

This demo showcases how Linux NFS and Windows SMB users can collaboratively access and interact with the same shared directory for reading and writing files. It highlights the seamless integration of FlashArray File Services in mixed-protocol environments, enabling cross-platform file sharing and collaboration.

## Overview

FlashArray File Services provides a unified storage solution that supports both NFS and SMB protocols simultaneously. This capability is essential for organizations with heterogeneous environments where both Linux and Windows systems need to access the same data. The multi-protocol feature ensures consistent file access, permissions, and data integrity across different operating systems.

---

## Technical Background

Multi-protocol access in FlashArray File Services enables:

- **Unified Storage:** A single storage repository accessible via both NFS and SMB protocols
- **Consistent Permissions:** Mapping between POSIX permissions (Linux) and NTFS ACLs (Windows)
- **Identity Management:** Integration with Active Directory or local user authentication
- **Data Integrity:** Proper file locking and concurrent access management across protocols

This capability addresses the challenges of cross-platform file sharing in heterogeneous environments, eliminating the need for separate storage silos for different operating systems.

## Use Case Examples

1. **File Created via Windows SMB is Accessible via Linux NFS:**
    - A Windows user uploads a file to the shared directory using SMB.
    - A Linux process accesses the same file in the shared directory using NFS for reading or writing.

2. **File Created via Linux NFS is Accessible via Windows SMB:**
    - A Linux process uploads a file to the shared directory using NFS.
    - A Windows user accesses the same file in the shared directory using SMB for reading or writing.

3. **Collaborative Workflows:**
    - Development teams using different operating systems can collaborate on the same codebase.
    - Media production environments can process files using specialized tools on different platforms.
    - Enterprise applications can access the same data from both Windows and Linux servers.

## Prerequisites

- Linux system with NFS client capabilities
- Windows system with SMB client capabilities
- Network connectivity to the FlashArray
- Python environment installed and activated (see [readme](./readme.md) for setup instructions)
- Administrative access to the FlashArray for configuring export policies

## Environment Details

- **Authentication:** Users are authenticated against either local users and groups or Active Directory, depending on the `FA_DEMO_USE_AD=true|false` parameter in the [`./.env` file](./.env).
- **User Groups:**
  - `win_users` (GID=9060): Group for all Windows users.
  - `nfs_daemons` (GID=9050): Group for all Linux users.
- **Users:**
  - `win_user` (UID=9060): Member of the `win_users` group.
  - `nfs_daemon` (UID=9050): Member of the `nfs_daemons` group.

## Demo Configuration

### File System and Managed Directory Setup

The demo provisions a file system named `multi_protocol_file_system` with a shared directory called `shared_dir`. This directory serves as the central location for files accessed via both Linux NFS and Windows SMB.

- **Permissions Configuration:** Directory permissions are configured from the Linux side using the [`./bin/demo_multiprotocol.sh`](./bin/demo_multiprotocol.sh) script.
- **Setup Scripts:**
  - [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py): Python script for provisioning the file system and configuring export policies.

### Protocol Configuration

- **NFS Access:** All NFS access is squashed (`all-squash`) to the `nfs_daemon` user (UID=9050) and the `nfs_daemons` group (GID=9050). This ensures consistent ownership and permissions for files created via NFS.
- **Export Policies:** 
  - NFS and SMB export policies are defined and attached to the `multi_protocol_file_system:root` managed directory.

### NFS Export Policy and Export

The `nfs_multi_protocol_access_policy` NFS export policy is configured with the following settings:

- **Export Option:** `all-squash`, mapping all user access to the `nfs_daemon` user (UID=9050).
- **User Mapping:** Enabled by default, ensuring Linux access is authenticated. This can be disabled in the script if needed.
- **Protocol:** NFSv4.
- **Export Name:** `multi`.

### SMB Export Policy and Export

The `smb_multi_protocol_access_policy` SMB export policy is configured with the following settings:

- **Export Name:** `multi`.
- **Directory:** Attached to the `multi_protocol_file_system:root` managed directory.

Refer to the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) script for detailed configuration steps.

---

## Demo Setup and Execution

### Prerequisites

1. Clone the repository on both Windows and Linux systems:

    ```bash
    git clone https://github.com/zsvoboda/fa_demos.git
    ```

2. Edit the [`./.env`](./.env) file to configure the environment variables.

### Steps to Run the Demo

1. **Linux Setup:**
    - Run the [`./bin/demo_multiprotocol.sh`](./bin/demo_multiprotocol.sh) script on the Linux system:

      ```bash
      ./bin/demo_multiprotocol.sh
      ```

    - This script performs the following:
      - Configures the array by calling the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) script.
      - Mounts the NFS export and creates the top-level shared directory called `shared_dir`.
      - Sets up the `shared_dir` permissions using the `nfs4_setfacl` utility. It allows members of the `nfs_daemons` and `win_users` groups to read and write to the directory. Permissions are inherited by all underlying files and directories:
        - `nfs4_setfacl -a "A:gfd:nfs_daemons@domain:RW" /mnt/multi/shared_dir`
        - `nfs4_setfacl -a "A:gfd:win_users@domain:RW" /mnt/multi/shared_dir`
      - Creates a new file called `file_from_linux_nfs_session.txt` in the `shared_dir`.
      - Prompts the user to execute the Windows script.

2. **Windows Setup:**
    - When prompted by the Linux script, run the [`./bin/demo_multiprotocol.cmd`](./bin/demo_multiprotocol.cmd) script on the Windows system:

      ```cmd
      .\bin\demo_multiprotocol.cmd
      ```

    - This script performs the following:
      - Maps the FlashArray's SMB share.
      - Verifies access to the file created by the NFS session above.
      - Creates a new file called `file_from_windows_smb_session.txt` in the `shared_dir`.

3. **Verification:**
    - Test file creation and access from both Linux and Windows systems to validate the multi-protocol functionality.

---

## Troubleshooting Tips

- If you encounter permission issues when accessing files across protocols, verify that:
  - The directory permissions are correctly set using `nfs4_setfacl`
  - User and group mappings are properly configured
  - The export policies have the correct settings
- If the NFS mount fails, check that:
  - The NFS client is properly installed on your Linux system
  - The export policy allows access from your client's IP address
  - The correct NFS version is being used (NFSv4)
- If the SMB share is not accessible, verify that:
  - The Windows system can resolve the FlashArray hostname
  - The user credentials are correct
  - The SMB export policy is properly configured
- For general connectivity issues:
  - Check network connectivity between clients and the FlashArray
  - Verify that the environment variables in the `.env` file are correctly set
  - Ensure that the FlashArray is properly configured for file services

## Summary

This demo demonstrates the ability of FlashArray File Services to handle mixed-protocol environments effectively. By enabling seamless collaboration between Linux NFS and Windows SMB users, it provides a robust solution for applications requiring multi-protocol access, such as Epic. The setup ensures secure and consistent file access across platforms, making it an ideal choice for enterprise environments.

The multi-protocol capability eliminates the need for data duplication across separate storage systems, simplifies data management, and enhances collaboration between teams using different operating systems. This feature is particularly valuable in modern heterogeneous IT environments where cross-platform access to shared data is increasingly important.

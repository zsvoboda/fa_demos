# Multi-Protocol Demo

This demo demonstrates how Linux NFS and Windows SMB users can collaboratively access and interact with the same shared directory for reading and writing files.

---

## Use Case Examples

1. **File Created via Windows SMB is Accessible via Linux NFS:**
    - A Windows user uploads a file to the shared directory using SMB.
    - A Linux process can read and write the file in the shared directory using NFS.

2. **File Created via Linux NFS is Accessible via Windows SMB:**
    - A Linux process uploads a file to the shared directory using NFS.
    - A Windows user can read and write the file in the shared directory using SMB.

---

## Environment Details

- All users are authenticated against either local users and groups or Active Directory, depending on the `FA_DEMO_USE_AD=true|false` parameter defined in the [`./.env` file](./.env).
- There are two groups: `win_users` (GID=9060) for all Windows users and `nfs_daemons` (GID=9050) for all Linux users.
- There are two users: `win_user` (UID=9060), a member of the `win_users` group, and `nfs_daemon` (UID=9050), a member of the `nfs_daemons` group.

---

## Demo Introduction

### File System and Managed Directory Setup

The demo creates a file system named `multi_protocol_file_system`.

Refer to the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) Python script for more details.

The file system contains a `shared_dir` directory where files from both Linux NFS and Windows SMB are stored.

Permissions for the directory are configured from the Windows side. Refer to the [`./bin/demo_multiprotocol.cmd`](./bin/demo_multiprotocol.cmd) script. Permissions to read and write files in the `shared_dir` are granted accordingly.

For additional details, see the [`./bin/demo_setup.sh`](./bin/demo_setup.sh) script.

### Configuration

All NFS access is squashed (`all-squash`) to the `nfs_daemon` user (UID=9050) and the `nfs_daemons` group (GID=9050).

Refer to the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) Python script for more details.

### NFS Export Policy and Export

The `nfs_multi_protocol_access_policy` NFS export policy is defined on the FlashArray:

- The policy uses the `all-squash` NFS export option, mapping all user access to the `nfs_daemon` user (UID=9050).
- User mapping is enabled, meaning access from Linux is authenticated. The script can be modified to disable user mapping, in which case NFS access is not checked against Active Directory or the FlashArray local user database.
- The policy uses the NFSv4 protocol.

The NFS policy is attached to the `multi_protocol_file_system:root` managed directory and exported under the name `multi`.

### SMB Export Policy and Export

The `smb_multi_protocol_access_policy` SMB export policy is defined.

The SMB policy is attached to the `multi_protocol_file_system:root` managed directory and shared under the name `multi`.

Refer to the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) Python script for more details.

---

## Demo Setup and Execution

1. Clone this repository on both Windows and Linux:

    ```bash
    git clone https://github.com/zsvoboda/epic_demo.git
    ```

2. Edit the [`./.env`](./.env) file.

3. Run the [`./bin/demo_multiprotocol.cmd`](./bin/demo_multiprotocol.cmd) script from Windows:

    ```cmd
    .\bin\demo_multiprotocol.cmd
    ```

4. When prompted by the Windows script, run the [`./bin/demo_multiprotocol.sh`](./bin/demo_multiprotocol.sh) script from Linux.

---

## Summary

This demo showcases how FlashArray File Services can effectively and securely handle mixed-protocol environments, making it an ideal storage solution for applications like Epic that require multiprotocol access and seamless cross-platform collaboration.
# Multi-Protocol Demo

This demo illustrates how Linux NFS and Windows SMB users can collaboratively access and interact with the same share for reading and writing files.

---

## Use Case Examples

1. **File Created from Windows SMB is Accessible via Linux NFS:**
   - A Windows user uploads a file to the shared directory via SMB.
   - Linux process can read and write the file from the shared directory via NFS.

2. **File Created from Linux NFS is Accessible via Windows SMB:**
   - A Linux process uploads a file to the shared directory via NFS.
   - A Windows user can read and write the file from the shared directory via SMB.

---

## Environment Details

- All users are authenticated against Local users and groups or Active Directory depending on the `FA_DEMO_USE_AD=true|false` parameter defined in the [`./.env` file](./.env).
- There are two groups: `win_users` (GID=9060) for all Windows users and `nfs_daemons` (GID=9050) for all Linux users
- There are two users: `win_user` (UID=9060) that is member of the `win_users` group and `nfs_daemon` (UID=9050) that is member of the `nfs_daemons` group.

---

## Demo Introduction

### File System and Managed Directory Setup

The demo creates a file system called `multi_protocol_file_system`.

See the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) Python script for more details.

The File System contains a `shared_dir` directory where files from both Linux NFS and Windows SMB are stored.

Permissions for both directories are configured from the Windows side. See the [`./bin/demo_multiprotocol.cmd`](./bin/demo_multiprotocol.cmd). Permissions to read and write files in the `shared_dir` are granted to 

See the [`./bin/demo_setup.sh`](./bin/demo_setup.sh) script for more details.

### Configuration

All NFS access from NFS are squashed (`all-squash`) to the `nfs_daemon` user (UID=9050) and the `nfs_daemons` group (GID=9050)

See the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) Python script for more details.

### NFS Export Policy and Export

The `nfs_multi_protocol_access_policy` NFS export policy is defined on the FlashArray:

The policy utilizes the `all-squash` NFS export option, impersonating every user's access as the `nfs_daemon` user (UID=9050). User mapping is enabled, meaning access from Linux is authenticated. The script can be easily modified to disable user mapping. In that case, user access from NFS side is not checked against neither ActiveDirectory nor FlashArray local users database.

The policy uses the NFSv4 protocol.

The NFS policy is attached to the `multi_protocol_file_system:root` managed directory, and exported under name `multi`.

### SMB Export Policy and Export

The `smb_multi_protocol_access_policy` SMB export policies is defined.

The SMB policy is attached to the `multi_protocol_file_system:root` managed directory, and shared under name `multi`.

See the [`./src/demos/multi_protocol/setup_array.py`](./src/demos/multi_protocol/setup_array.py) Python script for more details.

---

## Demo Setup and Execution

1. Clone this repository on both Windows and Linux:

```bash
git clone https://github.com/zsvoboda/epic_demo.git
```

2. Edit the [./env](./.env)


3. Run the [./bin/demo_multiprotocol.cmd](./bin/demo_multiprotocol.cmd) from Windows

```cmd
.\bin\demo_multiprotocol.cmd
```

4. Run the [./bin/demo_multiprotocol.sh](./bin/demo_multiprotocol.sh) from Linux when prompted from the Windows script

## Summary
This demo illustrates how FlashArray File Services can effectively and securely handle mixed-protocol environments, making it a suitable storage solution for applications like Epic that require multiprotocol access and seamless cross-platform collaboration.
# Active DR Demo

This demo showcases the Active-Passive Disaster Recovery (Active DR) functionality between two FlashArrays, 
where data is replicated from a source array to a target array. It demonstrates how to set up ActiveDR replication 
for file services, ensuring data protection and business continuity.

---

## Use Case Examples

1. **Data Protection and Business Continuity:**
   - Protect critical file data by replicating it from a source to a target array.
   - Ensure business continuity in case of a disaster at the primary array.

---

## Environment Details

- **Authentication:** Users are authenticated against either local users.
- **Arrays:**
  - Source Array: The primary array where data is created and modified.
  - Target Array: The secondary array where data is replicated for disaster recovery purposes.

---

## Demo Overview

### Pod and File System Setup

The demo provisions a pod named `replicated-source` on the source array and creates a file system named 
`replicated-source::file_system`. This file system serves as the source for replication to the target array.

- **Setup Script:** [`./src/demos/active_dr/setup_array.py`](./src/demos/active_dr/setup_array.py): Python script for provisioning the pods, file system, and configuring replication.

### Configuration

#### Source Array Configuration

1. **Local User:** Creates a local user named 'demo' for authentication.
2. **Pod:** Creates a pod named 'replicated-source'.
3. **Snapshot Policy:** Creates a snapshot policy 'replicated-source::every_hour_snapshot_policy' with hourly snapshots kept for 24 hours.
4. **File System:** Creates a file system 'replicated-source::file_system' within the 'replicated-source' pod.
5. **Access Policies:**
   - NFS Policy: Creates 'replicated-source::nfs_access_policy' for NFS access.
   - SMB Policy: Creates 'replicated-source::smb_access_policy' for SMB access.
6. **Exports:** Exports the file system over both NFS and SMB.
7. **Snapshot Policy Attachment:** Attaches the snapshot policy to the root managed directory.

#### Replication Configuration

1. **Remote Array Connection:** Establishes a connection between the source and target arrays.
2. **Replica Link:** Creates a replica link between the 'replicated-source' pod on the source array and the 'replicated-target' pod on the target array.

---

## Demo Setup and Execution

### Prerequisites

1. Two FlashArrays (source and target) with file services enabled.
2. Python 3.8 or higher installed on your machine.
3. Clone the repository:

   ```bash
   git clone https://github.com/zsvoboda/fa_demos.git
   ```

4. Edit the [`./.env`](./.env) file to configure the environment variables, including:
   - `FA_DEMO_HOSTNAME`: Source array hostname or IP
   - `FA_DEMO_API_TOKEN`: Source array API token
   - `FA_DEMO_REMOTE_HOSTNAME`: Target array hostname or IP
   - `FA_DEMO_REMOTE_API_TOKEN`: Target array API token
   - `FA_DEMO_USER_NAME`: Demo user name
   - `FA_DEMO_USER_PASSWORD`: Demo user password

### Steps to Run the Demo

1. **Setup the Environment:**
   - Create and activate the virtual environment:

     On Unix:
     ```bash
     ./bin/create_venv.sh
     ./bin/install_python_packages.sh
     ```

     On Windows:
     ```cmd
     .\bin\create_venv.cmd
     .\bin\install_python_packages.cmd
     ```

2. **Run the Demo:**
   - Execute the setup_array.py script:

     ```bash
     python src/demos/active_dr/setup_array.py setup
     ```

   - This script performs the following:
     - Creates a local user 'demo' on the source array
     - Creates a pod 'replicated-source' on the source array
     - Creates a snapshot policy and attaches it to the file system
     - Creates a file system and exports it over NFS and SMB
     - Establishes a connection between the source and target arrays
     - Creates a replica link for replication

3. **Verification:**
   - Verify that the pod and file system are created on the source array
   - Verify that the replica link is established between the source and target arrays
   - The demo will automatically:
     - Mount/map the source array file system
     - Create a test file on the source array
     - Wait for replication to occur
     - Mount/map the target array file system
     - Check if the file has been replicated to the target array

4. **Cleanup:**
   - Execute the setup_array.py script:
     ```bash
     python src/demos/active_dr/setup_array.py cleanup
     ```

---

## Configuration Using CLI Commands

The following instructions describe in detail how to configure and then clean up the Active Disaster Recovery (DR) 
demonstration environment on a Pure Storage FlashArray instance using the command-line interface (CLI). 
We will cover both creating the necessary resources for the demo on the source array and tearing them down on both 
the source and target arrays.

---

### Setting Up on the Source Array
Perform the following steps on the **source** FlashArray to prepare the data and replication configuration.

#### Create and Enable a Local User
Create a new local administrator account named `demo` with a fixed UID and a secure password:

```bash
pureds local user create   --primary-group Administrators   --uid 1001   --password password
pureds local user enable demo
```

- The `--primary-group` flag adds the user to the `Administrators` group.
- The `--uid` parameter sets a consistent user ID of `1001`.
- The second command enables the newly created user account.

#### Create the Source Pod and Filesystem
Establish the source pod and create a file system named `replicated-source`:

```bash
purepod create replicated-source
purefs create replicated-source::file_system
```

- `purepod create` initializes a new pod named `replicated-source`.
- `purefs create` provisions a file system under that pod.

#### Configure Snapshot Policy
Create an hourly snapshot policy and assign it to the file system's root managed directory:

```bash
purepolicy snapshot create replicated-source::every_hour_snapshot_policy
purepolicy snapshot rule add   replicated-source::every_hour_snapshot_policy   --every 1h   --keep-for 1d   --client-name every_hour_snapshot

puredir snapshot add   --policy replicated-source::every_hour_snapshot_policy   replicated-source::file_system:root
```

- The snapshot policy runs every 1 hour and retains snapshots for 24 hours.
- `puredir snapshot add` applies the policy to the root managed directory of the file system.

#### Configure Access Policies for NFS and SMB
Create an NFS access policy allowing all clients full read-write access without root squashing, using NFSv3 and `AUTH_SYS` security:

```bash
purepolicy nfs create replicated-source::nfs_access_policy
purepolicy nfs rule add   replicated-source::nfs_access_policy   --client '*'   --no-root-squash   --version nfsv3   --security auth_sys   --rw
```

Create an SMB access policy allowing all clients:

```bash
purepolicy smb create replicated-source::smb_access_policy 
purepolicy smb rule add   replicated-source::smb_access_policy   --client '*' --anonymous-access-allowed
```

#### Export the Directory Over NFS and SMB
Export the file system root managed directory using the policies defined above:

```bash
puredir export create   --dir  replicated-source::file_system:root   --policy replicated-source::nfs_access_policy   replicated_nfs_export
puredir export create   --dir  replicated-source::file_system:root   --policy replicated-source::smb_access_policy   replicated_smb_share
```

- These commands create two exports: one for NFS (`replicated_nfs_export`) and one for SMB (`replicated_smb_share`).

#### Establish Asynchronous Replication to Target Array

1. On the **target** array, retrieve the replication connection key:

```bash
# On the target array management console:
purearray list --connection-key
```

2. Back on the **source** array, connect to the target using the management IP and the key from step 1:

```bash
purearray connect  --management-address <TARGET_MGMT_IP_ADDRESS>  --type async-replication  --connection-key <PASTED_KEY>
```

3. Still on the source array, create the replica link between pods. Replace `<TARGET_ARRAY_NAME>` with the name assigned by `purearray` (usually the hostname):

```bash
purepod replica-link create  --remote-pod replicated-target  --remote <TARGET_ARRAY_NAME>  replicated-source
```

4. Monitor the replication status until the link status shows `replicating`:

```bash
purepod replica-link list
```

---

### Setting Up on the Target Array

Once the replicated-source pod is linked to the target, configure policy mapping on the **target** array:

```bash
# Connect the NFS access policy from the source
purepod replica-link mapping policy connect   --remote-policy replicated-source::nfs_access_policy   replicated-target
# Connect the SMB access policy from the source
purepod replica-link mapping policy connect   --remote-policy replicated-source::smb_access_policy   replicated-target
```
- These commands ensure that the NFS and SMB export policies are enforced on the target side. Two new exports are created on the target array. 

---

### 3. Cleaning Up the Demo Environment

After you have completed your Active DR demonstration, remove all resources on both arrays to restore them to their 
original state.

#### 3.1 Cleanup on the Source Array

Execute the following commands on the **source** array:

1. Delete the NFS and SMB exports:

```bash
puredir export delete replicated_nfs_export
puredir export delete replicated_smb_share
```

2. Remove the replica link and destroy the source pod:

```bash
purepod replica-link delete --remote-pod replicated-target   replicated-source
purepod destroy replicated-source --destroy-contents
purepod eradicate replicated-source --eradicate-contents
```

3. Delete the `demo` user account:

```bash
pureds local user delete demo
```

#### Cleanup on the Target Array

Connect to the **target** array management console and execute:

1. Delete any exports created during policy mapping (if applicable):

```bash
puredir export delete replicated_nfs_export
puredir export delete replicated_smb_share
```

2. Destroy and eradicate the target pod:

```bash
purepod destroy replicated-target --destroy-contents
purepod eradicate replicated-target --eradicate-contents
```

## Summary
This demo demonstrates the Active DR functionality of FlashArray File Services, showcasing how to 
set up replication between two arrays for disaster recovery purposes. By replicating file data from 
a source array to a target array, organizations can ensure data protection and business continuity in case 
of a disaster at the primary site. The demo provides a comprehensive example of configuring pods, 
file systems, access policies, and replication links to enable Active DR for file services.

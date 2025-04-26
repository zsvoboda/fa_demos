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

## Summary

This demo demonstrates the Active DR functionality of FlashArray File Services, showcasing how to 
set up replication between two arrays for disaster recovery purposes. By replicating file data from 
a source array to a target array, organizations can ensure data protection and business continuity in case 
of a disaster at the primary site. The demo provides a comprehensive example of configuring pods, 
file systems, access policies, and replication links to enable Active DR for file services.

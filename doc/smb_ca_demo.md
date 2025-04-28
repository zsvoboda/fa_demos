# SMB Continuous Availability Demo

## Overview

This demonstration showcases the capabilities of SMB Continuous Availability (SMB CA), a critical feature for enterprise environments requiring high availability for Windows file shares. SMB CA allows for the seamless transition of SMB clients to a secondary controller in the event of a primary controller failure, ensuring uninterrupted access to data and applications.

## Technical Background

SMB Continuous Availability works by:
- Maintaining persistent handles between SMB clients and servers
- Enabling transparent failover between controllers
- Preserving file locks and open file handles during failover events
- Ensuring that applications remain unaware of the underlying infrastructure changes

This capability is particularly important for applications that maintain long-running connections to file shares, such as database applications, virtual machine storage, and enterprise software like Microsoft SQL Server.

## Prerequisites

- A Windows machine with network connectivity to the FlashArray
- Python environment installed and activated (see [readme](./readme.md) for setup instructions)
- Administrative access to the FlashArray for configuring SMB policies
- Sufficient permissions to map network drives and create files

## Demo Configuration

The demo configures two SMB shares on the target FlashArray to demonstrate the difference between SMB shares with and 
without Continuous Availability:

- __smb_ca__: An SMB share with SMB CA enabled
- __smb_no_ca__: An SMB share with SMB CA disabled

Both shares are created on the same FlashArray but with different configurations to highlight the benefits of SMB CA.

## Demo Steps

1. **Setup and Preparation**
   - Open the Command Prompt on a Windows machine
   - Navigate to the [bin directory](../bin) and execute the `demo_smb_ca.cmd` script
   - The script will set up the target FlashArray by creating the necessary file systems and SMB policies

2. **Manual Configuration**
   - When prompted, configure the `smb_ca_policy` on the FlashArray to enable SMB CA
   - This step demonstrates the administrative process for enabling the feature

3. **Network Drive Mapping**
   - The script automatically maps two network drives:
     - Z: drive to the `smb_no_ca` share (without Continuous Availability)
     - Y: drive to the `smb_ca` share (with Continuous Availability)

4. **Testing Without SMB CA**
   - The script initiates a large file copy (6GB) to the Z: drive
   - During this operation, you can simulate a controller failure by executing the `pureadm stop` command on the primary controller
   - Observe how the file copy operation is disrupted, demonstrating the vulnerability of standard SMB shares

5. **Testing With SMB CA**
   - The script then initiates the same large file copy to the Y: drive
   - During this operation, simulate a controller failure again
   - Observe how the file copy operation continues seamlessly, demonstrating the resilience provided by SMB CA

6. **Cleanup**
   - The script automatically unmaps the network drives and removes the created resources from the FlashArray

## Visual Guide

For a visual walkthrough of this demo, watch the [SMB CA Demo Video](../video/FlashArray.SMB.Continuous.Availability.Demo.mp4).

## Use Cases

SMB Continuous Availability is particularly valuable for:
- Mission-critical applications that cannot tolerate interruptions
- Environments where maintenance activities need to be performed without disrupting user access
- Disaster recovery scenarios requiring seamless failover
- Enterprise applications like SQL Server, Hyper-V, and file servers that rely on persistent connections

## Troubleshooting Tips

- If the demo fails to set up properly, check your network connectivity to the FlashArray
- Ensure that the environment variables in the `.env` file are correctly configured
- Verify that you have sufficient permissions on both the Windows machine and the FlashArray
- If the file copy operations don't behave as expected, check the FlashArray controller status and logs

## Configuration Using CLI Commands

This section provides detailed instructions for manually setting up and cleaning up the SMB CA demo environment using CLI commands on the FlashArray.

### Setup

First, create a local user account on the FlashArray that will be used for administrative operations during the demo:
```bash
pureds local user create --primary-group Administrators --uid 1001 --password demo
```
This command creates a user named `demo` with administrative privileges by setting the primary group to `Administrators`, assigning a unique user ID (UID) of 1001. Please set the user's password to `password`.

Next, enable the newly created user account:
```bash
pureds local user enable demo 
```
This activation step is necessary to allow the `demo` user to authenticate and perform operations on the array.

Create two separate file systems, one for each type of SMB share:
```bash
purefs create smb_ca_file_system
purefs create smb_no_ca_file_system
```
These commands create two distinct file systems named `smb_ca_file_system` and `smb_no_ca_file_system`. Each file system will later be associated with its respective SMB policy.

Now, define the SMB policies that will govern client access:
```bash
purepolicy smb create smb_ca_policy --continuous-availability
purepolicy smb rule add smb_ca_policy --client '*'
```
The first command creates an SMB policy named `smb_ca_policy` with the `--continuous-availability` option enabled, allowing SMB CA features. The second command adds a rule to this policy to permit access from all SMB clients (`'*'`).

Similarly, create a standard SMB policy without Continuous Availability:
```bash
purepolicy smb create smb_no_ca_policy
purepolicy smb rule add smb_no_ca_policy --client '*'
```
This standard policy `smb_no_ca_policy` allows SMB access but does not provide Continuous Availability features.

Finally, create SMB exports (shares) for both file systems:
```bash
puredir export create --dir smb_ca_file_system:root --policy smb_ca_policy smb_ca
puredir export create --dir smb_no_ca_file_system:root --policy smb_no_ca_policy smb_no_ca
```
These commands create two SMB exports named `smb_ca` and `smb_no_ca`, associating each export with the corresponding file system and SMB policy.

### Cleanup

After completing the demo, it is important to clean up the environment by removing the created resources:

First, delete the SMB exports:
```bash
puredir export delete smb_no_ca
puredir export delete smb_ca
```
These commands remove the `smb_no_ca` and `smb_ca` SMB exports from the FlashArray.

Then, destroy and eradicate the file systems:
```bash
purefs destroy smb_ca_file_system
purefs eradicate smb_ca_file_system
purefs destroy smb_no_ca_file_system
purefs eradicate smb_no_ca_file_system
```
The `destroy` commands mark the file systems for deletion, and the `eradicate` commands permanently remove them from the array.

Next, delete the SMB policies:
```bash
purepolicy smb delete smb_ca_policy
purepolicy smb delete smb_no_ca_policy
```
These commands remove the previously created SMB policies from the FlashArray configuration.

Finally, delete the local user account:
```bash
pureds local user delete demo
```
This command removes the `demo` user from the FlashArray, completing the cleanup process.
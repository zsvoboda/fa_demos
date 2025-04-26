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

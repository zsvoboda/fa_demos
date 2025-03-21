# SMB Continuous Availability Demo

This demonstration showcases the capabilities of SMB Continuous Availability (SMB CA). SMB CA allows for the seamless transition of SMB clients to a secondary controller in the event of a primary controller failure.

To start the demo, execute the `demo_smb_ca.cmd` script located in the [bin directory](./bin) from a Windows command prompt. Ensure that you have installed and activated the Python environment before running this demo. For more details, refer to the [readme](./doc/readme.md). Please note that this demo is only compatible with the Windows environment.

The demo configures two SMB shares on the target FlashArray:

- __smb_ca__: An SMB share with SMB CA enabled
- __smb_no_ca__: An SMB share with SMB CA disabled

You can watch the [SMB CA Demo Video](https://github.com/zsvoboda/fa_demos/raw/refs/heads/main/video/FlashArray.SMB.Continuous.Availability.Demo.mp4) for a visual guide.

### Demo Steps:

1. Open the Command Prompt on a Windows machine.
2. Navigate to the [bin directory](./bin) and execute the `demo_smb_ca.cmd` script.
3. The script will set up the target FlashArray and prompt you to configure the `smb_ca_policy` to enable SMB CA. Refer to the demo video for more details.
4. The script will then map both SMB shares (one with SMB CA enabled and the other with SMB CA disabled) and start copying a large file to the SMB share without SMB CA. You can simulate a primary controller failure by executing the `pureadm stop` command on the primary controller, which should disrupt the file copy operation.
5. Next, the script will perform the same file copy operation on the SMB CA enabled share. If you attempt to disrupt the copy operation, it will seamlessly continue on the secondary controller.
6. Finally, the demo will clean up all objects that it created during the process.

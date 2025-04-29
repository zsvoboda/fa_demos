# FlashArray Demos

This repository contains multiple FlashArray File Services demos. Each demo is documented in this folder.

## Prerequisites

You need a Linux, Mac, or Windows machine with Python 3.8 or higher. Sonme demos (SMB) require Windows environment. 

## Demo Setup

The [bin directory](../bin) contains bash and Windows command line scripts for running the demos in this repository.

To install the demo, execute the following scripts:

On Unix:

```bash
source ./bin/create_venv.sh
./bin/install_python_packages.sh
```

On Windows:

```cmd
call .\bin\create_venv.cmd
.\bin\install_python_packages.cmd
```

## Running a Demo

Before running a demo, you need to configure your environment.

## Configuring Your Environment

All configuration settings for these FlashArray demos are stored in the `.env` file, which should be located in the root directory of this repository. You need to create this file manually. Once created, fill in the correct values for all demo parameters:

```bash
FA_DEMO_HOSTNAME=<fa-array-management-hostname-or-ip>
FA_DEMO_REMOTE_HOSTNAME=<fa-target-array-management-hostname-or-ip>
FA_DEMO_API_TOKEN=<fa-api-token>
FA_DEMO_REMOTE_API_TOKEN=<fa-target-array-api-token>
FA_DEMO_VIF_HOSTNAME=<fa-array-vif-hostname-or-ip>
FA_DEMO_REMOTE_VIF_HOSTNAME=<fa-target-array-vif-hostname-or-ip>
FA_DEMO_AD_HOSTNAME=<active-directory-hostname-or-ip>
FA_DEMO_AD_DOMAIN_NAME=<active-directory-domain-name-without-suffix>
FA_DEMO_AD_DOMAIN_TOP_LEVEL_SUFFIX=<active-directory-suffix>
FA_DEMO_AD_DOMAIN_ADMIN_USER=<active-directory-user-with-admin-access>
FA_DEMO_AD_DOMAIN_ADMIN_PASSWORD=<active-directory-user-with-admin-access-password>
FA_DEMO_AD_DNS_DOMAIN_SUFFIX=<active-directory-dns-domain-suffix>
FA_DEMO_USER_NAME=<fa-file-services-demo-user-name>
FA_DEMO_USER_DOMAIN=<fa-file-services-demo-user-domain-name>
FA_DEMO_USER_PASSWORD=<fa-file-services-demo-user-password>
FA_DEMO_USE_AD=<true-if-using-active-directory-false-if-using-local-user>
```

After configuring the `.env` file, activate the virtual environment before starting a demo. Run the following script in each terminal or command line prompt when running multiple demos.

On Unix:

```bash
source ./bin/activate_venv.sh
```

On Windows:

```cmd
call ./bin/activate_venv.cmd
```

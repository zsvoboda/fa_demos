import sys
import os

from fa.flash_array import FlashArray
from pypureclient.flasharray import ReferenceWithType

import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from log import setup_logging

setup_logging()
_logger = logging.getLogger(__name__)

from load_env import load_env
load_env()


def setup(fa):
    
    # Create local user
    fa.create_local_user(
        name=os.getenv('FA_DEMO_USER_NAME', 'demo'), 
        uid=1001, 
        enabled=True,
        primary_group=ReferenceWithType(name='Administrators'), 
        password=os.getenv('FA_DEMO_USER_PASSWORD', 'password')
    )

    # Create filesystem
    fa.create_file_system('smb_ca_file_system')
    fa.create_file_system('smb_no_ca_file_system')

    fa.create_policy_smb(name='smb_ca_policy',)
    fa.create_policy_smb_rule(policy_name='smb_ca_policy', client='*')
    fa.export_managed_directory_smb(policy_name='smb_ca_policy',
                                    managed_directory_name='smb_ca_file_system:root',
                                    export_name='smb_ca')
    
    fa.create_policy_smb(name='smb_no_ca_policy')
    fa.create_policy_smb_rule(policy_name='smb_no_ca_policy', client='*')
    fa.export_managed_directory_smb(policy_name='smb_no_ca_policy',
                                    managed_directory_name='smb_no_ca_file_system:root',
                                    export_name='smb_no_ca')

def cleanup(fa):

    # Delete exports and policies
    fa.delete_export(export_name='smb_ca', policy_name='smb_ca_policy')
    fa.delete_export(export_name='smb_no_ca', policy_name='smn_no_ca_policy')

    # Desytroy and erradicate file system
    fa.destroy_file_system(name='smb_ca_file_system')
    fa.eradicate_file_system(name='smb_ca_file_system')
    fa.destroy_file_system(name='smb_no_ca_file_system')
    fa.eradicate_file_system(name='smb_no_ca_file_system')
    
    # Delete file system
    fa.delete_policy_smb(name='smb_ca_policy')
    fa.delete_policy_smb(name='smb_no_ca_policy')
    
    fa.delete_local_user(name=os.getenv('FA_DEMO_USER_NAME', 'demo'))


# Setup connection to FlashArray
FA_HOSTNAME = os.getenv("FA_DEMO_HOSTNAME")
FA_API_TOKEN = os.getenv("FA_DEMO_API_TOKEN")

fa = FlashArray(api_token=FA_API_TOKEN, array_host=FA_HOSTNAME)
fa.authenticate()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "cleanup":
        _logger.info(f"Cleaning up {FA_HOSTNAME} array ...")
        cleanup(fa)
    else:    
        _logger.info(f"Configuring {FA_HOSTNAME} array ...")
        setup(fa)

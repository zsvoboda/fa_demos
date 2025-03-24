import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fa.flash_array import FlashArray
from pypureclient.flasharray import ReferenceWithType

import logging
from log import setup_logging

setup_logging()
_logger = logging.getLogger(__name__)

from load_env import load_env
load_env()


def setup(fa):
    
    # Create local user
    try:
        fa.create_local_user(
            name=os.getenv('FA_DEMO_USER_NAME', 'demo'), 
            uid=1001, 
            enabled=True,
            primary_group=ReferenceWithType(name='Administrators'), 
            password=os.getenv('FA_DEMO_USER_PASSWORD', 'password')
        )
    except Exception as e:
        _logger.error(f"Error creating local user. Error message '{e}'.")

    # Create filesystem
    try:
        fa.create_file_system('smb_ca_file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'smb_ca_file_system'. Error message '{e}'.")
    
    try:
        fa.create_file_system('smb_no_ca_file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'smb_no_ca_file_system'. Error message '{e}'.")

    try:
        fa.create_policy_smb(name='smb_ca_policy', continuous_availability=True)
    except Exception as e:
        _logger.error(f"Error creating policy 'smb_ca_policy'. Error message '{e}'.")

    try:
        fa.create_policy_smb_rule(policy_name='smb_ca_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy rule for 'smb_ca_policy'. Error message '{e}'.")

    try:
        fa.export_managed_directory_smb(policy_name='smb_ca_policy',
                                        managed_directory_name='smb_ca_file_system:root',
                                        export_name='smb_ca')
    except Exception as e:
        _logger.error(f"Error exporting managed directory for 'smb_ca_policy'. Error message '{e}'.")

    try:
        fa.create_policy_smb(name='smb_no_ca_policy', continuous_availability=False)
    except Exception as e:
        _logger.error(f"Error creating policy 'smb_no_ca_policy'. Error message '{e}'.")

    try:
        fa.create_policy_smb_rule(policy_name='smb_no_ca_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy rule for 'smb_no_ca_policy'. Error message '{e}'.")

    try:
        fa.export_managed_directory_smb(policy_name='smb_no_ca_policy',
                                        managed_directory_name='smb_no_ca_file_system:root',
                                        export_name='smb_no_ca')
    except Exception as e:
        _logger.error(f"Error exporting managed directory for 'smb_no_ca_policy'. Error message '{e}'.")

def cleanup(fa):

    # Delete exports and policies
    try:
        fa.delete_export(export_name='smb_ca', policy_name='smb_ca_policy')
    except Exception as e:
        _logger.error(f"Error deleting export 'smb_ca'. Error message '{e}'.")

    try:
        fa.delete_export(export_name='smb_no_ca', policy_name='smb_no_ca_policy')
    except Exception as e:
        _logger.error(f"Error deleting export 'smb_no_ca'. Error message '{e}'.")

    # Destroy and eradicate file system
    try:
        fa.destroy_file_system(name='smb_ca_file_system')
        fa.eradicate_file_system(name='smb_ca_file_system')
    except Exception as e:
        _logger.error(f"Error destroying or eradicating file system 'smb_ca_file_system'. Error message '{e}'.")

    try:
        fa.destroy_file_system(name='smb_no_ca_file_system')
        fa.eradicate_file_system(name='smb_no_ca_file_system')
    except Exception as e:
        _logger.error(f"Error destroying or eradicating file system 'smb_no_ca_file_system'. Error message '{e}'.")

    # Delete policies
    try:
        fa.delete_policy_smb(name='smb_ca_policy')
    except Exception as e:
        _logger.error(f"Error deleting policy 'smb_ca_policy'. Error message '{e}'.")

    try:
        fa.delete_policy_smb(name='smb_no_ca_policy')
    except Exception as e:
        _logger.error(f"Error deleting policy 'smb_no_ca_policy'. Error message '{e}'.")

    # Delete local user
    try:
        fa.delete_local_user(name=os.getenv('FA_DEMO_USER_NAME', 'demo'))
    except Exception as e:
        _logger.error(f"Error deleting local user. Error message '{e}'.")


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

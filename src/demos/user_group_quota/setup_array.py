import sys
import os

from pypureclient.flasharray import ReferenceWithType

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fa.flash_array import FlashArray

import logging
from log import setup_logging

setup_logging()
_logger = logging.getLogger(__name__)

from load_env import load_env
import requests
load_env()

def create_policy_user_group_quota(_policy_name):
    
    FA_HOSTNAME = os.getenv("FA_DEMO_HOSTNAME")
    
    url = f'http://{FA_HOSTNAME}/2.X/policies/user-group-quota?names={_policy_name}'
    headers = {
        'user': 'root',
        'Content-Type': 'application/json'
    }
    data = {
        "location_context": None,
        "enabled": True
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        _logger.info("User group quota policy created successfully.")
    else:
        _logger.error(f"Failed to create user group quota policy. Status code: {response.status_code}, Response: {response.text}")
        raise Exception(f"Failed to create user group quota policy. Status code: {response.status_code}, Response: {response.text}")
    
def delete_policy_user_group_quota(_policy_name):
    FA_HOSTNAME = os.getenv("FA_DEMO_HOSTNAME")

    url = f'http://{FA_HOSTNAME}/2.X/policies/user-group-quota?names={_policy_name}'
    headers = {
        'user': 'root',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        _logger.info("User group quota policy deleted successfully.")
    else:
        _logger.error(f"Failed to delete user group quota policy. Status code: {response.status_code}, Response: {response.text}")
        raise Exception(f"Failed to delete user group quota policy. Status code: {response.status_code}, Response: {response.text}")

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
        fa.create_file_system('user_group_quota_file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'user_group_quota_file_system'. Error message '{e}'.")

    try:
        create_policy_user_group_quota(name='user_group_quota_policy')
    except Exception as e:
        _logger.error(f"Error creating policy 'user_group_quota_policy'. Error message '{e}'.")

    try:
        fa.export_managed_directory_smb(policy_name='smb-simple',
                                        managed_directory_name='user_group_quota_file_system:root',
                                        export_name='user_group_quota')
    except Exception as e:
        _logger.error(f"Error exporting managed directory for 'user_group_quota_policy'. Error message '{e}'.")

def cleanup(fa):

    # Delete exports and policies
    try:
        fa.delete_export(export_name='user_group_quota', policy_name='smb-simple')
    except Exception as e:
        _logger.error(f"Error deleting export 'user_group_quota'. Error message '{e}'.")

    # Destroy and eradicate file system
    try:
        fa.destroy_file_system(name='user_group_quota_file_system')
        fa.eradicate_file_system(name='user_group_quota_file_system')
    except Exception as e:
        _logger.error(f"Error destroying or eradicating file system 'user_group_quota_file_system'. Error message '{e}'.")

    # Delete policies
    try:
        fa.delete_policy_user_group_quota(name='user_group_quota_policy')
    except Exception as e:
        _logger.error(f"Error deleting policy 'user_group_quota_policy'. Error message '{e}'.")

    # Delete local user
    try:
        fa.delete_local_user(name=os.getenv('FA_DEMO_USER_NAME', 'demo'))
    except Exception as e:
        _logger.error(f"Error deleting local user. Error message '{e}'.")

if __name__ == '__main__':

    # Setup connection to FlashArray
    FA_HOSTNAME = os.getenv("FA_DEMO_HOSTNAME")
    FA_API_TOKEN = os.getenv("FA_DEMO_API_TOKEN")
    
    '''
    import socket
    import socks

    FA_DEMO_USE_SOCKS5_PROXY = os.getenv("FA_DEMO_USE_SOCKS5_PROXY")

    
    if FA_DEMO_USE_SOCKS5_PROXY == 'true':
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 1080)
        socket.socket = socks.socksocket
    '''

    fa = FlashArray(api_token=FA_API_TOKEN, array_host=FA_HOSTNAME)
    fa.authenticate()

    if len(sys.argv) > 1 and sys.argv[1] == "cleanup":
        _logger.info(f"Cleaning up {FA_HOSTNAME} array ...")
        cleanup(fa)
    else:    
        _logger.info(f"Configuring {FA_HOSTNAME} array ...")
        setup(fa)

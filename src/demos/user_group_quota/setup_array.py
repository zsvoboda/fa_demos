import sys
import os

from ad.active_directory import ActiveDirectory
from fa import FlashArray
from pypureclient.flasharray.FA_2_X import ReferenceWithType

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import logging
from log import setup_logging

setup_logging()
_logger = logging.getLogger(__name__)

from load_env import load_env

load_env()


def setup(fa):
    # Create local user
    try:
        _logger.info("Creating local users.")
        demo_user_name = os.getenv('FA_DEMO_USER_NAME', 'demo')
        fa.create_local_user(
            name=demo_user_name,
            uid=1001,
            enabled=True,
            primary_group=ReferenceWithType(name='Administrators'),
            password=os.getenv('FA_DEMO_USER_PASSWORD', 'password')
        )
        fa.create_local_group(
            name=f"VIP",
            gid=1002
        )
        fa.create_local_user(
            name=f"{demo_user_name}_vip",
            uid=1002,
            enabled=True,
            primary_group=ReferenceWithType(name='VIP'),
            password=os.getenv('FA_DEMO_USER_PASSWORD', 'password')
        )
    except Exception as e:
        _logger.error(f"Error creating local user. Error message '{e}'.")

    # Create filesystem
    try:
        _logger.info("Creating file system 'user_quota_file_system'.")
        fa.create_file_system('user_quota_file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'user_quota_file_system'. Error message '{e}'.")

    # Create NFS policies
    try:
        _logger.info("Creating NFS policy 'nfs_user_quota_access_policy'.")
        fa.create_nfs_policy(name='nfs_user_quota_access_policy', disable_user_mapping=False)
        fa.create_nfs_policy_rule(policy_name='nfs_user_quota_access_policy', client='*', access='no-root-squash',
                                  nfs_version='nfsv4', security='auth_sys',
                                  permission='rw')
    except Exception as e:
        _logger.error(f"Error creating policy 'nfs_user_quota_access_policy'. Error message '{e}'.")

    # Create SMB policies
    try:
        _logger.info("Creating SMB policy 'smb_user_quota_access_policy'.")
        fa.create_smb_policy(name='smb_user_quota_access_policy')
        fa.create_smb_policy_rule(policy_name='smb_user_quota_access_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy 'smb_user_quota_access_policy'. Error message '{e}'.")

    # Create Default User Quota policy
    try:
        _logger.info("Creating User Group Quota policy.")
        fa.create_user_group_quota_policy(name='user_quota_policy')
        fa.create_user_group_quota_policy_rule(
                policy_name='user_quota_policy',
                quota_limit = 3000 * 1024,
                quota_type = 'user-default',
                enforced = True,
                notifications = ['account'])
        vip_group =list(fa.get_local_group(name='VIP'))
        fa.create_user_group_quota_policy_rule(
            policy_name='user_quota_policy',
            quota_limit=30000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=vip_group[0].sid,
            enforced=True,
            notifications=['account'])
    except Exception as e:
        _logger.error(f"Error creating Default User Quota policy. Error message '{e}'.")

    # Attach the User Group Quota policy to the root managed directory
    try:
        _logger.info("Attaching User Group Quota policy to the root managed directory.")
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='user_quota_policy',
            managed_directory_name='user_quota_file_system:root'
        )
    except Exception as e:
        _logger.error(f"Error attaching User Group Quota policy to the root managed directory. Error message '{e}'.")

    # Export managed directory
    try:
        _logger.info("Exporting managed directory over NFS.")
        fa.attach_nfs_policy_to_directory(policy_name='nfs_user_quota_access_policy',
                                        managed_directory_name='user_quota_file_system:root',
                                        export_name='user_quota_export')

        _logger.info("Exporting managed directory over SMB.")
        fa.attach_smb_policy_to_directory(policy_name='smb_user_quota_access_policy',
                                        managed_directory_name='user_quota_file_system:root',
                                        export_name='user_quota_share')
    except Exception as e:
        _logger.error(f"Error exporting managed directory. Error message '{e}'.")


def cleanup(fa):

    # Delete exports and policies
    try:
        _logger.info("Deleting NFS and SMB exports.")
        fa.delete_directory_export(export_name='user_quota_export', policy_name='nfs_user_quota_access_policy')
        fa.delete_directory_export(export_name='user_quota_share', policy_name='smb_user_quota_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting NFS and SMB exports. Error message '{e}'.")

    # Delete file system
    try:
        _logger.info("Destroying file system 'user_quota_file_system'.")
        fa.destroy_file_system(name='user_quota_file_system')
        _logger.info("Eradicating file system 'user_quota_file_system'.")
        fa.eradicate_file_system(name='user_quota_file_system')
    except Exception as e:
        _logger.error(f"Error deleting file system 'user_quota_file_system'. Error message '{e}'.")

    # Delete export policies
    try:
        _logger.info("Deleting NFS and SMB policies.")
        fa.delete_nfs_policy(name='nfs_user_quota_access_policy')
        fa.delete_smb_policy(name='smb_user_quota_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting policies. Error message '{e}'.")

    # Delete User Group Quota Policies
    try:
        _logger.info("Deleting User Group Quota policies.")
        fa.delete_user_group_quota_policy(name='user_quota_policy')
    except Exception as e:
        _logger.error(f"Error deleting User Group Quota policy. Error message '{e}'.")

    # Delete local users
    try:
        _logger.info("Deleting local user 'demo'.")
        demo_user_name = os.getenv('FA_DEMO_USER_NAME', 'demo')
        fa.delete_local_user(name=demo_user_name)
        fa.delete_local_user(name=f"{demo_user_name}_vip")
        fa.delete_local_group(name="VIP")
    except Exception as e:
        _logger.error(f"Error deleting local user. Error message '{e}'.")


if __name__ == '__main__':

    # Setup SOCKS5 proxy

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

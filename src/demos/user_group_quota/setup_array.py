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
    # Create AD users
    
    ad = ActiveDirectory()

    # Ensure Organizational Units exist
    try:
        ad.ensure_ou_exists("Groups")
        ad.ensure_ou_exists("Users")
    except Exception as e:
        _logger.error(f"Error ensuring OU exists. Error message '{e}'.")

    # Create groups
    try:
        ad.create_group('fa_user_quota_demo_bronze_users', 9160, 'Bronze users')
        ad.create_group('fa_user_quota_demo_silver_users', 9260, 'Silver users')
        ad.create_group('fa_user_quota_demo_gold_users', 9360, 'Silver users')
    except Exception as e:
        _logger.error(f"Error creating groups. Error message '{e}'.")

    # Create users
    try:
        ad.create_user('fa_user_quota_demo_bronze_user', 9160, 'Bronze User')
        ad.create_user('fa_user_quota_demo_silver_user', 9260, 'Silver User')
        ad.create_user('fa_user_quota_demo_gold_user', 9360, 'Gold User')
    except Exception as e:
        _logger.error(f"Error creating users. Error message '{e}'.")

    # Assign users to groups
    try:
        ad.add_user_to_group('fa_user_quota_demo_bronze_user', 'fa_user_quota_demo_bronze_users')
        ad.add_user_to_group('fa_user_quota_demo_silver_user', 'fa_user_quota_demo_silver_users')
        ad.add_user_to_group('fa_user_quota_demo_gold_user', 'fa_user_quota_demo_gold_users')
    except Exception as e:
        _logger.error(f"Error assigning users to groups. Error message '{e}'.")
    
    
    # Create filesystem
    try:
        _logger.info("Creating file system 'fa_user_quota_demo_file_system'.")
        fa.create_file_system('fa_user_quota_demo_file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'fa_user_quota_demo_file_system'. Error message '{e}'.")

    # Create NFS policies
    try:
        _logger.info("Creating NFS policy 'fa_user_quota_demo_nfs_access_policy'.")
        fa.create_nfs_policy(name='fa_user_quota_demo_nfs_access_policy', disable_user_mapping=False)
        fa.create_nfs_policy_rule(policy_name='fa_user_quota_demo_nfs_access_policy', client='*', access='no-root-squash',
                                  nfs_version='nfsv4', security='auth_sys',
                                  permission='rw')
    except Exception as e:
        _logger.error(f"Error creating policy 'fa_user_quota_demo_smb_access_policy'. Error message '{e}'.")

    # Create SMB policies
    try:
        _logger.info("Creating SMB policy 'fa_user_quota_demo_smb_access_policy'.")
        fa.create_smb_policy(name='fa_user_quota_demo_smb_access_policy')
        fa.create_smb_policy_rule(policy_name='fa_user_quota_demo_smb_access_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy 'fa_user_quota_demo_smb_access_policy'. Error message '{e}'.")

    # Create Default User Quota policy
    try:
        _logger.info("Creating the user group quota policy 'fa_user_quota_demo_policy'.")
        fa.create_user_group_quota_policy(name='fa_user_quota_demo_policy')
        _logger.info("Creating the default user quota policy rule with limit 3MB.")
        fa.create_user_group_quota_policy_rule(
                policy_name='fa_user_quota_demo_policy',
                quota_limit = 3000 * 1024,
                quota_type = 'user-default',
                enforced = True,
                notifications = ['account'])
        _logger.info("Creating the group quota policy rule for bronze users with limit 30MB.")
        bronze_group =ad.search_objects(object_class='group', search_filter='(cn=fa_user_quota_demo_bronze_users)', attributes=['distinguishedName'])
        fa.create_user_group_quota_policy_rule(
            policy_name='fa_user_quota_demo_policy',
            quota_limit=30000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=bronze_group.sid,
            enforced=True,
            notifications=['account'])
        _logger.info("Creating the group quota policy rule for silver users with limit 100MB.")
        silver_group =ad.search_objects(object_class='group', search_filter='(cn=fa_user_quota_demo_silver_users)', attributes=['distinguishedName'])
        fa.create_user_group_quota_policy_rule(
            policy_name='fa_user_quota_demo_policy',
            quota_limit=100000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=silver_group.sid,
            enforced=True,
            notifications=['account'])
        _logger.info("Creating the group quota policy rule for gold users with limit 500MB.")
        gold_group =ad.search_objects(object_class='group', search_filter='(cn=fa_user_quota_demo_gold_users)', attributes=['distinguishedName'])
        fa.create_user_group_quota_policy_rule(
            policy_name='fa_user_quota_demo_policy',
            quota_limit=500000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=gold_group.sid,
            enforced=True,
            notifications=['account'])
    except Exception as e:
        _logger.error(f"Error creating Default User Quota policy. Error message '{e}'.")

    # Attach the User Group Quota policy to the root managed directory
    try:
        _logger.info("Attaching User Group Quota policy to the root managed directory.")
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='fa_user_quota_demo_policy',
            managed_directory_name='fa_user_quota_demo_file_system:root'
        )
    except Exception as e:
        _logger.error(f"Error attaching User Group Quota policy to the root managed directory. Error message '{e}'.")

    # Export managed directory
    try:
        _logger.info("Exporting managed directory over NFS.")
        fa.attach_nfs_policy_to_directory(policy_name='fa_user_quota_demo_nfs_access_policy',
                                        managed_directory_name='fa_user_quota_demo_file_system:root',
                                        export_name='user_quota_export')

        _logger.info("Exporting managed directory over SMB.")
        fa.attach_smb_policy_to_directory(policy_name='fa_user_quota_demo_smb_access_policy',
                                        managed_directory_name='fa_user_quota_demo_file_system:root',
                                        export_name='user_quota_share')
    except Exception as e:
        _logger.error(f"Error exporting managed directory. Error message '{e}'.")
        
    # Close the AD connection
    ad.close()



def cleanup(fa):

    # Delete exports and policies
    try:
        _logger.info("Deleting NFS and SMB exports.")
        fa.delete_directory_export(export_name='user_quota_export', policy_name='fa_user_quota_demo_nfs_access_policy')
        fa.delete_directory_export(export_name='user_quota_share', policy_name='fa_user_quota_demo_smb_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting NFS and SMB exports. Error message '{e}'.")

    # Delete file system
    try:
        _logger.info("Destroying file system 'fa_user_quota_demo_file_system'.")
        fa.destroy_file_system(name='fa_user_quota_demo_file_system')
        _logger.info("Eradicating file system 'fa_user_quota_demo_file_system'.")
        fa.eradicate_file_system(name='fa_user_quota_demo_file_system')
    except Exception as e:
        _logger.error(f"Error deleting file system 'fa_user_quota_demo_file_system'. Error message '{e}'.")

    # Delete export policies
    try:
        _logger.info("Deleting NFS and SMB policies.")
        fa.delete_nfs_policy(name='fa_user_quota_demo_nfs_access_policy')
        fa.delete_smb_policy(name='fa_user_quota_demo_smb_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting export policies. Error message '{e}'.")

    # Delete User Group Quota Policies
    try:
        _logger.info("Deleting User Group Quota policies.")
        fa.delete_user_group_quota_policy(name='fa_user_quota_demo_policy')
    except Exception as e:
        _logger.error(f"Error deleting User Group Quota policy. Error message '{e}'.")

    # Delete AD users and groups
    try:
        _logger.info("Deleting AD users and groups.")
        ad = ActiveDirectory()
        
        # Ensure Organizational Units exist
        _logger.info("Ensuring Organizational Units exist.")
        try:
            ad.ensure_ou_exists("Groups")
            ad.ensure_ou_exists("Users")
        except Exception as e:
            _logger.error(f"Error ensuring OU exists. Error message '{e}'.")
        
        # Delete AD users & groups
        _logger.info("Deleting AD users and groups.")
        try:
            ad.delete_object(f'CN=fa_user_quota_demo_bronze_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=fa_user_quota_demo_silver_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=fa_user_quota_demo_gold_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=fa_user_quota_demo_bronze_users,OU=Groups,{ad.base_dn}', 'Group')
            ad.delete_object(f'CN=fa_user_quota_demo_silver_users,OU=Groups,{ad.base_dn}', 'Group')
            ad.delete_object(f'CN=fa_user_quota_demo_gold_users,OU=Groups,{ad.base_dn}', 'Group')
        except Exception as e:
            _logger.error(f"Error deleting AD users and groups. Error message '{e}'.")
        
        # Close the connection
        ad.close()        
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

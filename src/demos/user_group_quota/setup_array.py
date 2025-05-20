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
        ad.create_group('bronze_users', 9160, 'Bronze users')
        ad.create_group('silver_users', 9260, 'Silver users')
        ad.create_group('gold_users', 9360, 'Silver users')
    except Exception as e:
        _logger.error(f"Error creating groups. Error message '{e}'.")

    # Create users
    try:
        ad.create_user('bronze_user', 9160, 'Bronze User')
        ad.create_user('silver_user', 9260, 'Silver User')
        ad.create_user('gold_user', 9360, 'Gold User')
        ad.create_user('platinum_user', 9460, 'Gold User')
    except Exception as e:
        _logger.error(f"Error creating users. Error message '{e}'.")

    # Assign users to groups
    try:
        ad.add_user_to_group('bronze_users', 'bronze_user')
        ad.add_user_to_group('silver_users', 'silver_user')
        ad.add_user_to_group('gold_users', 'gold_user')
    except Exception as e:
        _logger.error(f"Error assigning users to groups. Error message '{e}'.")
    
    
    # Create filesystem
    try:
        _logger.info("Creating file system 'home'.")
        fa.create_file_system('home')
    except Exception as e:
        _logger.error(f"Error creating file system 'home'. Error message '{e}'.")

    # Create platinum_private managed directory
    try:
        _logger.info("Creating managed directories.")
        fa.create_directory(name='home',file_system_name='home', path='/home')
        fa.create_directory(name='bronze', file_system_name='home', path='/home/bronze')
        fa.create_directory(name='silver', file_system_name='home', path='/home/silver')
        fa.create_directory(name='gold', file_system_name='home', path='/home/gold')
        fa.create_directory(name='platinum', file_system_name='home', path='/home/platinum')
    except Exception as e:
        _logger.error(f"Error creating managed directories. Error message '{e}'.")

    # Create NFS policies
    try:
        _logger.info("Creating NFS policy 'nfs_access_policy'.")
        fa.create_nfs_policy(name='nfs_access_policy', disable_user_mapping=False)
        fa.create_nfs_policy_rule(policy_name='nfs_access_policy', client='*', access='no-root-squash',
                                  nfs_version='nfsv4', security='auth_sys',
                                  permission='rw')
    except Exception as e:
        _logger.error(f"Error creating policy 'nfs_access_policy'. Error message '{e}'.")

    # Create SMB policies
    try:
        _logger.info("Creating SMB policy 'smb_access_policy'.")
        fa.create_smb_policy(name='smb_access_policy')
        fa.create_smb_policy_rule(policy_name='smb_access_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy 'smb_access_policy'. Error message '{e}'.")

    # Create Default User Quota policy
    try:
        _logger.info("Creating the default user quota policy 'user_quota_default' with limit 3MB .")
        fa.create_user_group_quota_policy(name='user_quota_default')
        fa.create_user_group_quota_policy_rule(
                policy_name='user_quota_default',
                quota_limit = 3000 * 1024,
                quota_type = 'user-default',
                enforced = True,
                notifications = ['account'])
        _logger.info("Creating the group quota policy 'user_quota_bronze' with limit 30MB for members of the 'bronze_users' group.")
        fa.create_user_group_quota_policy(name='user_quota_bronze')
        group = list(ad.search_objects(object_class='group', search_filter='(cn=bronze_users)', attributes=['objectSid']))
        fa.create_user_group_quota_policy_rule(
            policy_name='user_quota_bronze',
            quota_limit=30000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=group[0]['objectSid'],
            enforced=True,
            notifications=['account'])
        _logger.info("Creating the group quota policy 'user_quota_silver' with limit 100MB for members of the 'silver_users' group.")
        fa.create_user_group_quota_policy(name='user_quota_silver')
        group = list(
            ad.search_objects(object_class='group', search_filter='(cn=silver_users)', attributes=['objectSid']))
        fa.create_user_group_quota_policy_rule(
            policy_name='user_quota_silver',
            quota_limit=100000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=group[0]['objectSid'],
            enforced=True,
            notifications=['account'])
        _logger.info(
            "Creating the group quota policy 'user_quota_gold' with limit 500MB for members of the 'gold_users' group.")
        fa.create_user_group_quota_policy(name='user_quota_gold')
        group = list(
            ad.search_objects(object_class='group', search_filter='(cn=gold_users)', attributes=['objectSid']))
        fa.create_user_group_quota_policy_rule(
            policy_name='user_quota_gold',
            quota_limit=500000 * 1024,
            quota_type='user-group-member',
            quota_subject_sid=group[0]['objectSid'],
            enforced=True,
            notifications=['account'])
        _logger.info(
            "Creating the group quota policy 'user_quota_platinum' with limit 1GB for 'platinum_user'.")
        fa.create_user_group_quota_policy(name='user_quota_platinum')
        group = list(
            ad.search_objects(object_class='user', search_filter='(cn=platinum_user)', attributes=['objectSid']))
        fa.create_user_group_quota_policy_rule(
            policy_name='user_quota_platinum',
            quota_limit=1000000 * 1024,
            quota_type='user',
            quota_subject_sid=group[0]['objectSid'],
            enforced=True,
            notifications=['account'])
    except Exception as e:
        _logger.error(f"Error creating User Quota policies. Error message '{e}'.")

    # Attach the User Group Quota policy to the root managed directory
    try:
        _logger.info("Attaching User Group Quota policies to the root managed directory.")
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='user_quota_default',
            managed_directory_name='home:home'
        )
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='user_quota_bronze',
            managed_directory_name='home:bronze'
        )
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='user_quota_silver',
            managed_directory_name='home:silver'
        )
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='user_quota_gold',
            managed_directory_name='home:gold'
        )
        fa.attach_user_group_quota_policy_to_directory(
            policy_name='user_quota_platinum',
            managed_directory_name='home:platinum'
        )

    except Exception as e:
        _logger.error(f"Error attaching User Group Quota policies to the root managed directory. Error message '{e}'.")

    # Export managed directory
    try:
        _logger.info("Exporting managed directory over NFS.")
        fa.attach_nfs_policy_to_directory(policy_name='nfs_access_policy',
                                        managed_directory_name='home:home',
                                        export_name='user_quota_export')

        _logger.info("Exporting managed directory over SMB.")
        fa.attach_smb_policy_to_directory(policy_name='smb_access_policy',
                                        managed_directory_name='home:home',
                                        export_name='user_quota_share')
    except Exception as e:
        _logger.error(f"Error exporting managed directory. Error message '{e}'.")
        
    # Close the AD connection
    ad.close()



def cleanup(fa):

    # Delete exports
    try:
        _logger.info("Deleting NFS and SMB exports.")
        fa.delete_directory_export(export_name='user_quota_export', policy_name='nfs_access_policy')
        fa.delete_directory_export(export_name='user_quota_share', policy_name='smb_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting NFS and SMB exports. Error message '{e}'.")

    # Detach quota policies from managed directories
    try:
        _logger.info("Detaching User Group Quota policies from managed directories.")
        fa.detach_user_group_quota_policy_from_directory(managed_directory_name='home:home',
                                                        policy_name='user_quota_default')
        fa.detach_user_group_quota_policy_from_directory(managed_directory_name='home:bronze',
                                                        policy_name='user_quota_bronze')
        fa.detach_user_group_quota_policy_from_directory(managed_directory_name='home:silver',
                                                        policy_name='user_quota_silver')
        fa.detach_user_group_quota_policy_from_directory(managed_directory_name='home:gold',
                                                        policy_name='user_quota_gold')
        fa.detach_user_group_quota_policy_from_directory(managed_directory_name='home:platinum',
                                                        policy_name='user_quota_platinum')
    except Exception as e:
        _logger.error(f"Error detaching User Group Quota policies from managed directories. Error message '{e}'.")

    '''
    # Delete managed directories
    try:
        _logger.info("Deleting managed directories.")
        fa.delete_directory(name='home:home')
        fa.delete_directory(name='home:bronze')
        fa.delete_directory(name='home:silver')
        fa.delete_directory(name='home:gold')
        fa.delete_directory(name='home:platinum')
    except Exception as e:
        _logger.error(f"Error deleting managed directories. Error message '{e}'.")
    '''

    # Destroy file system
    try:
        _logger.info("Destroying file system 'home'.")
        fa.destroy_file_system(name='home')
        _logger.info("Eradicating file system 'home'.")
        fa.eradicate_file_system(name='home')
    except Exception as e:
        _logger.error(f"Error deleting file system 'home'. Error message '{e}'.")

    # Delete export policies
    try:
        _logger.info("Deleting NFS and SMB policies.")
        fa.delete_nfs_policy(name='nfs_access_policy')
        fa.delete_smb_policy(name='smb_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting export policies. Error message '{e}'.")

    # Delete User Group Quota Policies
    try:
        _logger.info("Deleting User Group Quota policies.")
        fa.delete_user_group_quota_policy(name='user_quota_default')
        fa.delete_user_group_quota_policy(name='user_quota_bronze')
        fa.delete_user_group_quota_policy(name='user_quota_silver')
        fa.delete_user_group_quota_policy(name='user_quota_gold')
        fa.delete_user_group_quota_policy(name='user_quota_platinum')
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
            ad.delete_object(f'CN=bronze_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=silver_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=gold_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=platinum_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=bronze_users,OU=Groups,{ad.base_dn}', 'Group')
            ad.delete_object(f'CN=silver_users,OU=Groups,{ad.base_dn}', 'Group')
            ad.delete_object(f'CN=gold_users,OU=Groups,{ad.base_dn}', 'Group')
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

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
    
    FA_DEMO_USE_AD = os.getenv("FA_DEMO_USE_AD")
    
    if FA_DEMO_USE_AD == 'true':
        ad = ActiveDirectory()

        # Ensure Organizational Units exist
        try:
            ad.ensure_ou_exists("Groups")
            ad.ensure_ou_exists("Users")
        except Exception as e:
            _logger.error(f"Error ensuring OU exists. Error message '{e}'.")

        # Create groups
        try:
            ad.create_group('win_users', 9060, 'Windows Users')
            ad.create_group('nfs_daemons', 9050, 'NFS Daemons')
        except Exception as e:
            _logger.error(f"Error creating groups. Error message '{e}'.")

        # Create users
        try:
            ad.create_user('win_user', 9060, 'Windows User')
            ad.create_user('nfs_daemon', 9050, 'NFS Daemon')
        except Exception as e:
            _logger.error(f"Error creating users. Error message '{e}'.")

        # Assign users to groups
        try:
            ad.add_user_to_group('win_users', 'win_user')
            ad.add_user_to_group('nfs_daemons', 'nfs_daemon')
        except Exception as e:
            _logger.error(f"Error assigning users to groups. Error message '{e}'.")
        
        # Close the connection
        ad.close()
    else:
        _logger.info("Creating all users and groups on the array.")
        # Create local groups
        fa.create_local_group(name='nfs_daemons',  gid=9050)
        fa.create_local_group(name='win_users', gid=9060)

        # Create local users
        fa.create_local_user(name='nfs_daemon', uid=9050, enabled=True,
                               primary_group=ReferenceWithType(name='nfs_daemons'), password='password')
        fa.create_local_user(name='win_user', uid=9060, enabled=True,
                               primary_group=ReferenceWithType(name='win_users'), password='password')
    
    # Create local user
    try:
        _logger.info("Creating local user demo.")
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
        _logger.info("Creating file system 'multi_protocol_file_system'.")
        fa.create_file_system('multi_protocol_file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'multi_protocol_file_system'. Error message '{e}'.")
    
    # Create NFS policies
    try:
        _logger.info("Creating NFS policy 'nfs_multi_protocol_access_policy'.")
        fa.create_nfs_policy(name='nfs_multi_protocol_access_policy', disable_user_mapping=False)
        fa.create_nfs_policy_rule(policy_name='nfs_multi_protocol_access_policy', client='*', access='all-squash',
                              anonuid='9050', anongid='9050', nfs_version='nfsv4', security='auth_sys',
                              permission='rw')
    except Exception as e:
        _logger.error(f"Error creating policy 'nfs_multi_protocol_access_policy'. Error message '{e}'.")
    
    # Create SMB policies
    try:
        _logger.info("Creating SMB policy 'smb_multi_protocol_access_policy'.")
        fa.create_smb_policy(name='smb_multi_protocol_access_policy')
        fa.create_smb_policy_rule(policy_name='smb_multi_protocol_access_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy 'smb_multi_protocol_access_policy'. Error message '{e}'.")

    # Export managed directory
    try:
        _logger.info("Exporting managed directory over NFS.")
        fa.attach_nfs_policy_to_directory(policy_name='nfs_multi_protocol_access_policy',
                                    managed_directory_name='multi_protocol_file_system:root',
                                    export_name='multi')
   
        _logger.info("Exporting managed directory over SMB.")
        fa.attach_smb_policy_to_directory(policy_name='smb_multi_protocol_access_policy',
                                    managed_directory_name='multi_protocol_file_system:root',
                                    export_name='multi')
    except Exception as e:
        _logger.error(f"Error exporting managed directory. Error message '{e}'.")


def cleanup(fa):
    
    FA_DEMO_USE_AD = os.getenv("FA_DEMO_USE_AD")
    
    if FA_DEMO_USE_AD == 'true':
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
            ad.delete_object(f'CN=win_user,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=nfs_daemon,CN=Users,{ad.base_dn}', 'User')
            ad.delete_object(f'CN=win_users,OU=Groups,{ad.base_dn}', 'Group')
            ad.delete_object(f'CN=nfs_daemons,OU=Groups,{ad.base_dn}', 'Group')
        except Exception as e:
            _logger.error(f"Error deleting AD objects. Error message '{e}'.")
        
        # Close the connection
        ad.close()        
    else:
        _logger.info("Active Directory is not being used. Deleting local users and groups.")
        # Delete local users
        fa.delete_local_user(name='nfs_daemon')
        fa.delete_local_user(name='win_user')

        # Delete local groups
        fa.delete_local_group(name='nfs_daemons')
        fa.delete_local_group(name='win_users')

     # Delete exports and policies
    try:
        _logger.info("Deleting NFS and SMB exports.")
        fa.delete_directory_export(export_name='multi', policy_name='nfs_multi_protocol_access_policy')
        fa.delete_directory_export(export_name='multi', policy_name='smb_multi_protocol_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting NFS and SMB exports. Error message '{e}'.")

    # Delete file system
    try:
        _logger.info("Destroying file system 'multi_protocol_file_system'.")
        fa.destroy_file_system(name='multi_protocol_file_system')
        _logger.info("Eradicating file system 'multi_protocol_file_system'.")
        fa.eradicate_file_system(name='multi_protocol_file_system')
    except Exception as e:
        _logger.error(f"Error deleting file system 'multi_protocol_file_system'. Error message '{e}'.")
    
    # Delete policies
    try: 
        _logger.info("Deleting NFS and SMB policies.")
        fa.delete_nfs_policy(name='nfs_multi_protocol_access_policy')
        fa.delete_smb_policy(name='smb_multi_protocol_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting policies. Error message '{e}'.")

    # Delete local user
    try:
        _logger.info("Deleting local user 'demo'.")
        fa.delete_local_user(name=os.getenv('FA_DEMO_USER_NAME', 'demo'))
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

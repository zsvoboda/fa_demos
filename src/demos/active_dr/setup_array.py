import sys
import os
import time

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


def setup(_fa_source, _fa_target):
    
    FA_DEMO_USE_AD = os.getenv("FA_DEMO_USE_AD")

    # Create local user
    try:
        _logger.info("Creating local user demo.")
        _fa_source.create_local_user(
            name=os.getenv('FA_DEMO_USER_NAME', 'demo'), 
            uid=1001, 
            enabled=True,
            primary_group=ReferenceWithType(name='Administrators'), 
            password=os.getenv('FA_DEMO_USER_PASSWORD', 'password')
        )
        _fa_target.create_local_user(
            name=os.getenv('FA_DEMO_USER_NAME', 'demo'), 
            uid=1001, 
            enabled=True,
            primary_group=ReferenceWithType(name='Administrators'), 
            password=os.getenv('FA_DEMO_USER_PASSWORD', 'password')
        )
    except Exception as e:
        _logger.error(f"Error creating local user. Error message '{e}'.")

    # Create source pod
    try:
        _logger.info("Creating replicated-source pod.")
        _fa_source.create_pod('replicated-source')
    except Exception as e:
        _logger.error(f"Error creating replicated-source pod. Error message '{e}'.")

    # Create Source Snapshot Policies
    try:
        _logger.info("Creating snapshot policy 'replicated-source::every_hour_snapshot_policy'.")
        _fa_source.create_snapshot_policy(name='replicated-source::every_hour_snapshot_policy')
        _fa_source.create_snapshot_policy_rule(
            policy_name='replicated-source::every_hour_snapshot_policy',
            client_name='every_hour_snapshot',
            every=1000*3600,
            keep_for=1000*3600*24
        )
    except Exception as e:
        _logger.error(f"Error creating source snapshot policy. Error message '{e}'.")
    '''
    # Create target pod
    try:
        _logger.info("Creating replicated-target pod.")
        _fa_target.create_pod('replicated-target')
    except Exception as e:
        _logger.error(f"Error creating replicated-target pod. Error message '{e}'.")

    # Demote target pod
    try:
        _logger.info("Demoting target pod.")
        _fa_target.demote_pod('replicated-target')
    except Exception as e:
        _logger.error(f"Error demoting target pod. Error message '{e}'.")
    '''

    # Create filesystem
    try:
        _logger.info("Creating file system 'replicated-source::file_system'.")
        _fa_source.create_file_system('replicated-source::file_system')
    except Exception as e:
        _logger.error(f"Error creating file system 'replicated-source::file_system'. Error message '{e}'.")
    
    # Create NFS policies
    try:
        _logger.info("Creating NFS policy 'replicated-source::nfs_access_policy'.")
        _fa_source.create_nfs_policy(name='replicated-source::nfs_access_policy', disable_user_mapping=False)
        _fa_source.create_nfs_policy_rule(policy_name='replicated-source::nfs_access_policy', client='*', access='no-root-squash',
                              anonuid='9050', anongid='9050', nfs_version='nfsv3', security='auth_sys',
                              permission='rw')
    except Exception as e:
        _logger.error(f"Error creating policy 'replicated-source::nfs_access_policy'. Error message '{e}'.")
    
    # Create SMB policies
    try:
        _logger.info("Creating SMB policy 'replicated-source::smb_access_policy'.")
        _fa_source.create_smb_policy(name='replicated-source::smb_access_policy')
        _fa_source.create_smb_policy_rule(policy_name='replicated-source::smb_access_policy', client='*')
    except Exception as e:
        _logger.error(f"Error creating policy 'replicated-source::smb_access_policy'. Error message '{e}'.")

    # Export managed directory
    try:
        _logger.info("Exporting managed directory over NFS.")
        _fa_source.attach_nfs_policy_to_directory(
            policy_name='replicated-source::nfs_access_policy',
            managed_directory_name='replicated-source::file_system:root',
            export_name='replicated_nfs_export'
        )
        _logger.info("Exporting managed directory over SMB.")
        _fa_source.attach_smb_policy_to_directory(
            policy_name='replicated-source::smb_access_policy',
            managed_directory_name='replicated-source::file_system:root',
            export_name='replicated_smb_share'
        )
    except Exception as e:
        _logger.error(f"Error exporting managed directory. Error message '{e}'.")

    # Attach snapshot policies to managed directory
    try:
        _logger.info("Attaching snapshot policy to the root managed directory.")
        _fa_source.attach_snapshot_policy_to_directory(
            policy_name='replicated-source::every_hour_snapshot_policy',
            managed_directory_name='replicated-source::file_system:root'
        )
    except Exception as e:
        _logger.error(f"Error attaching the snapshot policy. Error message '{e}'.")

    try:
        _logger.info("Creating source pod replica link.")
        # Get remote array connection key
        key = list(_fa_target.get_connection_key())[0]

        # Create remote array connection
        target_connection = list(_fa_source.connect_remote_array(
            remote_hostname=_fa_target.get_array_hostname(),
            remote_connection_key=key.connection_key
        ))[0]
        # Create replica link
        replica_link = _fa_source.create_pod_replica_link(
            remote_array_connection_name=target_connection.name,
            source_pod_name='replicated-source',
            target_pod_name='replicated-target'
        )
    except Exception as e:
        _logger.error(f"Error creating source replica link. Error message '{e}'.")

    mapped_policy_names = []
    # does policies include 'a','b','c'
    while not {'replicated-source::nfs_access_policy', 'replicated-source::smb_access_policy', 'replicated-source::every_hour_snapshot_policy'}.issubset(
            mapped_policy_names):
        mapped_policies = list(_fa_target.get_pod_replica_link_policy_mappings(source_pod_name='replicated-target', target_pod_name='replicated-source'))
        mapped_policy_names = set(map(lambda pm: pm.remote_policy.name, mapped_policies))
        mapped_policy_mappings = set(map(lambda pm: pm.mapping, mapped_policies))
        _logger.info("Waiting 10 more seconds for the policies to be replicated.")
        time.sleep(10)


    # Change the export policies mapping on the target array to connected
    try:
        _logger.info("Changing the export policies mapping on the target array.")

        _fa_target.change_pod_replica_link_policy_mapping(
            target_pod_name='replicated-target',
            policy_name='replicated-source::nfs_access_policy',
            policy_connection_status='connected'
        )
        _fa_target.change_pod_replica_link_policy_mapping(
            target_pod_name='replicated-target',
            policy_name='replicated-source::smb_access_policy',
            policy_connection_status='connected'
        )
    except Exception as e:
        _logger.error(f"Error changing the export policies mapping to connected on the target array. Error message '{e}'.")

def cleanup(_fa_source, _fa_target):
    
    FA_DEMO_USE_AD = os.getenv("FA_DEMO_USE_AD")

    # Delete the replica link
    try:
        _logger.info("Deleting replica link.")
        _fa_source.delete_pod_replica_link(
            source_pod_name='replicated-source',
            target_pod_name='replicated-target'
        )
    except Exception as e:
        _logger.error(f"Error deleting replica link. Error message '{e}'.")

    # Delete target exports
    try:
        _logger.info("Deleting target NFS and SMB exports.")
        _fa_target.delete_directory_export(export_name='replicated_nfs_export', policy_name='replicated-target::nfs_access_policy')
        _fa_target.delete_directory_export(export_name='replicated_smb_share', policy_name='replicated-target::smb_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting NFS and SMB exports. Error message '{e}'.")

    # Destroy and eradicate target pod
    try:
        _logger.info("Destroying and eradicating replicated-target pod.")
        _fa_target.destroy_pod(name='replicated-target', destroy_contents=True)
        _fa_target.eradicate_pod(name='replicated-target', eradicate_contents=True)
    except Exception as e:
        _logger.error(f"Error destroying or eradicating pod. Error message '{e}'.")

    # Delete source exports
    try:
        _logger.info("Deleting source NFS and SMB exports.")
        _fa_source.delete_directory_export(export_name='replicated_nfs_export',
                                           policy_name='replicated-source::nfs_access_policy')
        _fa_source.delete_directory_export(export_name='replicated_smb_share',
                                           policy_name='replicated-source::smb_access_policy')
    except Exception as e:
        _logger.error(f"Error deleting NFS and SMB exports. Error message '{e}'.")

    # Destroy and eradicate source pod
    try:
        _logger.info("Destroying and eradicating replicated-source pod.")
        _fa_source.destroy_pod(name='replicated-source', destroy_contents=True)
        _fa_source.eradicate_pod(name='replicated-source', eradicate_contents=True)
    except Exception as e:
        _logger.error(f"Error destroying or eradicating pod. Error message '{e}'.")

    # Delete local user
    try:
        _logger.info("Deleting local user 'demo'.")
        _fa_source.delete_local_user(name=os.getenv('FA_DEMO_USER_NAME', 'demo'))
        _fa_target.delete_local_user(name=os.getenv('FA_DEMO_USER_NAME', 'demo'))
    except Exception as e:
        _logger.error(f"Error deleting local user. Error message '{e}'.")

if __name__ == '__main__':

    # Setup SOCKS5 proxy

    FA_HOSTNAME = os.getenv("FA_DEMO_HOSTNAME")
    FA_API_TOKEN = os.getenv("FA_DEMO_API_TOKEN")

    FA_REMOTE_HOSTNAME = os.getenv("FA_DEMO_REMOTE_HOSTNAME")
    FA_REMOTE_API_TOKEN = os.getenv("FA_DEMO_REMOTE_API_TOKEN")
    
    '''
    import socket
    import socks

    FA_DEMO_USE_SOCKS5_PROXY = os.getenv("FA_DEMO_USE_SOCKS5_PROXY")

    
    if FA_DEMO_USE_SOCKS5_PROXY == 'true':
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 1080)
        socket.socket = socks.socksocket
    '''

    fa_source = FlashArray(api_token=FA_API_TOKEN, array_host=FA_HOSTNAME)
    fa_source.authenticate()

    fa_target = FlashArray(api_token=FA_REMOTE_API_TOKEN, array_host=FA_REMOTE_HOSTNAME)
    fa_target.authenticate()

    if len(sys.argv) > 1 and sys.argv[1] == "cleanup":
        _logger.info(f"Cleaning up {FA_HOSTNAME} array ...")
        cleanup(fa_source, fa_target)
    else:    
        _logger.info(f"Configuring {FA_HOSTNAME} array ...")
        setup(fa_source, fa_target)
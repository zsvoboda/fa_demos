import sys
import os
import pypureclient
from pypureclient.flasharray import FileSystem, Directory, Pod, Policy, PolicyRuleNfsClient, \
    PolicyRuleNfsClientPost, \
    PolicyRuleSmbClient, PolicyRuleSmbClientPost, PolicyRuleQuota, PolicyRuleQuotaPost, PolicyRuleSnapshot, \
    PolicyRuleSnapshotPost, PolicyMemberExportPost, PolicymemberexportpostMembers, ReferenceWithType, \
    PolicyMemberPost, PolicymemberpostMembers, LocalGroup, LocalUserPost, LocalUserPatch, PolicyNfsPost, ErrorResponse, \
    PolicySmbPatch, PolicyRuleUserGroupQuota, PolicyRuleUserGroupQuotaPost

import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log import setup_logging

setup_logging()
_logger = logging.getLogger(__name__)

from load_env import load_env
load_env()

class FlashArrayError(Exception):

    def __init__(self, api_response=None):
        super(FlashArrayError, self).__init__("Check the API response for error details.")
        self.response = api_response

def handle_response_with_items(response):
    if not isinstance(response, ErrorResponse) and 200 <= response.status_code < 300:
        return response.items
    else:
        if response.errors:
            for error in response.errors:
                _logger.error(f"Error: {error.message}")
        raise FlashArrayError(response)

def handle_response_with_value(response, value):
    if not isinstance(response, ErrorResponse) and 200 <= response.status_code < 300:
        return value
    else:
        if response.errors:
            for error in response.errors:
                _logger.error(f"Error: {error.message}")
        raise FlashArrayError(response)

def handle_response(response):
    if not isinstance(response, ErrorResponse) and 200 <= response.status_code < 300:
        return
    else:
        if response.errors:
            for error in response.errors:
                _logger.error(f"Error: {error.message}")
        raise FlashArrayError(response)


class FlashArray:
    """Class to represent a Pure Storage FlashArray"""

    def __init__(self, api_token, array_host):
        """Initialize the class"""
        self._api_token = api_token
        self._array_host = array_host
        self._client = None

    def authenticate(self):
        """Authenticate to the array"""
        self._client = pypureclient.flasharray.Client(self._array_host, api_token=self._api_token)

    def get_local_groups(self):
        """Return the array local groups"""
        r = self._client.get_directory_services_local_groups()
        return handle_response_with_items(r)

    def create_local_group(self, name, gid):
        """Create a new local group"""
        g = LocalGroup(name=name, gid=gid)
        r = self._client.post_directory_services_local_groups(local_group=g, names=[name])
        return handle_response_with_items(r)

    def delete_local_group(self, name):
        """Delete a local group"""
        r = self._client.delete_directory_services_local_groups(names=[name])
        return handle_response(r)

    def get_local_users(self):
        """Return the array local users"""
        r = self._client.get_directory_services_local_users()
        return handle_response_with_items(r)

    def create_local_user(self, name, uid, primary_group, enabled, password, email=None):
        """Create a new local user"""
        u = LocalUserPost(uid=uid, enabled=enabled, password=password, primary_group=primary_group, email=email)
        r = self._client.post_directory_services_local_users(local_user=u, names=[name])
        return handle_response_with_items(r)

    def delete_local_user(self, name):
        """Delete a local user"""
        r = self._client.delete_directory_services_local_users(names=[name])
        return handle_response(r)

    def get_pods(self):
        """Return the array pods"""
        r = self._client.get_pods()
        return handle_response_with_items(r)

    def get_pod(self, pod_id=None, name=None):
        """Return the array pods by name or id"""
        r = self._client.get_pods(names=[name] if name else None, ids=[pod_id] if pod_id else None)
        return (
            handle_response_with_value(r, list(filter(lambda x: (pod_id and x.id == pod_id) or
                                                                (name and x.name == name), r.items))))

    def create_pod(self, name):
        """Create a new pod"""
        p = Pod(name=name)
        r = self._client.post_pods(pod=p, names=[name])
        return handle_response_with_items(r)

    def destroy_pod(self, name, destroy_contents=False):
        """Destroy a pod"""
        p = Pod(destroyed=True)
        r = self._client.patch_pods(pod=p, destroy_contents=destroy_contents, names=[name])
        return handle_response_with_items(r)

    def eradicate_pod(self, name, eradicate_contents=False):
        """Eradicate a pod"""
        r = self._client.delete_pods(names=[name], eradicate_contents=eradicate_contents)
        return handle_response(r)

    def get_file_systems(self):
        """Return the array filesystems"""
        r = self._client.get_file_systems()
        return handle_response_with_items(r)

    def get_file_system(self, file_system_id=None, name=None):
        """Return the array filesystems by name or id"""
        r = self._client.get_file_systems(names=[name] if name else None,
                                          ids=[file_system_id] if file_system_id else None)
        return (
            handle_response_with_value(r, list(filter(lambda x: (file_system_id and x.id == file_system_id) or
                                                                (name and x.name == name), r.items))))

    def create_file_system(self, name):
        """Create a new filesystem"""
        """If the filesystem needs to created in a pod, use the pod prefix in it's name"""
        f = FileSystem(name=name)
        r = self._client.post_file_systems(f)
        return handle_response_with_items(r)

    def destroy_file_system(self, name):
        """Destroy a file system"""
        f = FileSystem(destroyed=True)
        r = self._client.patch_file_systems(file_system=f, names=[name])
        return handle_response_with_items(r)

    def eradicate_file_system(self, name):
        """Eradicate a file system"""
        r = self._client.delete_file_systems(names=[name])
        return handle_response(r)

    def get_directories(self, file_system_name=None, file_system_id=None):
        """Return the array managed directories"""
        r = self._client.get_directories(file_system_names=[file_system_name] if file_system_name else None,
                                         file_system_ids=[file_system_id] if file_system_id else None)
        return handle_response_with_items(r)

    def get_directory(self, managed_directory_id=None, name=None):
        """Return the array managed directories by name or id"""
        r = self._client.get_directories(names=[name] if name else None,
                                         ids=[managed_directory_id] if managed_directory_id else None)
        return (
            handle_response_with_value(r, list(filter(lambda x:
                                                      (managed_directory_id and x.id == managed_directory_id) or
                                                      (name and x.name == name), r.items))))

    def create_directory(self, name, file_system_name, path=None):
        """Create a new managed directory"""
        """If the managed directory needs to created in a pod, use the pod prefix in it's name"""
        d = Directory(file_system=file_system_name, directory_name=name, path=f'/{name}' if not path else path)
        r = self._client.post_directories(directory=d, file_system_names=[file_system_name])
        return handle_response_with_items(r)

    def delete_directory(self, name):
        """Eradicate a managed directory"""
        r = self._client.delete_directories(names=[name])
        return handle_response(r)

    # Policies
    def get_policies(self):
        """Return the array policies"""
        r = self._client.get_policies()
        return handle_response_with_items(r)

    def get_policy(self, policy_id=None, policy_name=None):
        """Return the array policies by name or id"""
        r = self._client.get_policies(names=[policy_name] if policy_name else None,
                                      ids=[policy_id] if policy_id else None)
        return (
            handle_response_with_value(r, list(filter(lambda x: (policy_id and x.id == policy_id) or
                                                                (policy_name and x.name == policy_name), r.items))))

    def create_policy(self, name, policy_type, enabled=True):
        if policy_type == 'nfs':
            return self.create_nfs_policy(name, enabled)
        elif policy_type == 'smb':
            return self.create_smb_policy(name, enabled)
        elif policy_type == 'quota':
            return self.create_directory_quota_policy(name, enabled)
        elif policy_type == 'snapshot':
            return self.create_snapshot_policy(name, enabled)
        elif policy_type == 'autodir':
            return self.create_autodir_policy(name, enabled)
        elif policy_type == 'user-group-quota':
            return self.create_user_group_quota_policy(name, enabled)
        else:
            raise FlashArrayError(f"Policy type {policy_type}' is not supported yet.")

    def delete_policy(self, policy_id=None, policy_name=None):
        """Delete policy"""
        p = self.get_policy(policy_id=policy_id if policy_id else None,
                            policy_name=policy_name if policy_name else None)
        if p:
            if p[0].policy_type == 'nfs':
                return self.delete_nfs_policy(policy_name)
            elif p[0].policy_type == 'smb':
                return self.delete_smb_policy(policy_name)
            elif p[0].policy_type == 'quota':
                return self.delete_directory_quota_policy(policy_name)
            elif p[0].policy_type == 'snapshot':
                return self.delete_snapshot_policy(policy_name)
            elif p[0].policy_type == 'autodir':
                return self.delete_autodir_policy(policy_name)
            elif p[0].policy_type == 'user-group-quota':
                return self.delete_user_group_quota_policy(policy_name)
            else:
                raise FlashArrayError(f"Policy type {p[0].policy_type}' is not supported yet.")
        else:
            raise FlashArrayError(f"Policy with name='{policy_name}' or id = '{policy_id}' not found.")

    def delete_policy_rule(self, rule_name=None, policy_name=None, policy_id=None):
        """ Delete policy rule """
        p = self.get_policy(policy_id=policy_id if policy_id else None,
                            policy_name=policy_name if policy_name else None)
        if p:
            if p[0].policy_type == 'nfs':
                return self.delete_nfs_policy_rule(rule_name, policy_name, policy_id)
            elif p[0].policy_type == 'smb':
                return self.delete_smb_policy_rule(rule_name, policy_name, policy_id)
            elif p[0].policy_type == 'quota':
                return self.delete_directory_quota_policy_rule(rule_name, policy_name, policy_id)
            elif p[0].policy_type == 'snapshot':
                return self.delete_snapshot_policy_rule(rule_name, policy_name, policy_id)
            elif p[0].policy_type == 'user-group-quota':
                return self.delete_user_group_quota_policy_rule(rule_name, policy_name, policy_id)
            else:
                raise FlashArrayError(f"Policy type {p[0].policy_type}' is not supported yet.")
        else:
            raise FlashArrayError(f"Policy with name='{policy_name}' or id = '{policy_id}' not found.")

    # Exports
    def get_directory_exports(self, directory_name=None, directory_id=None, policy_name=None, policy_id=None):
        """Return the array directory exports"""
        r = self._client.get_directory_exports(directory_names=[directory_name] if directory_name else None,
                                               directory_ids=[directory_id] if directory_id else None,
                                               policy_names=[policy_name] if policy_name else None,
                                               policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_directory_export(self, name=None):
        """Return the array directory exports by name or id"""
        r = self._client.get_directory_exports(export_names=[name] if name else None)
        return (
            handle_response_with_value(r, list(filter(lambda x: (name and x.export_name == name), r.items))))

    def delete_directory_export(self, export_name, policy_name):
        r = self._client.delete_directory_exports(export_names=[export_name], policy_names=[policy_name])
        return handle_response(r)

    # NFS Export policies
    def create_nfs_policy(self, name, enabled=True, disable_user_mapping=False):
        """Create a new NFS policy"""
        p = PolicyNfsPost(enabled=enabled, user_mapping_enabled=not disable_user_mapping)
        r = self._client.post_policies_nfs(policy=p, names=[name])
        return handle_response_with_items(r)

    def delete_nfs_policy(self, name=None, policy_id=None):
        """Delete NFS policy"""
        r = self._client.delete_policies_nfs(names=[name] if name else None, ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_nfs_policy_rules(self, policy_name=None, policy_id=None):
        """Return the array NFS policy rules"""
        r = self._client.get_policies_nfs_client_rules(policy_names=[policy_name] if policy_name else None,
                                                       policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def create_nfs_policy_rule(self, rule_name=None, client='*', access=None, permission=None, nfs_version=None,
                               security=None, anonuid=None, anongid=None, policy_name=None, policy_id=None):
        """Create a new NFS policy rule"""
        rule = PolicyRuleNfsClient(
            name=rule_name if rule_name else None,
            client=client if client else None,
            access=access if access else None,
            permission=permission if permission else None,
            nfs_version=nfs_version if nfs_version else None,
            security=security if security else None,
            anonuid=anonuid if anonuid else None,
            anongid=anongid if anongid else None)
        r = self._client.post_policies_nfs_client_rules(
            rules=PolicyRuleNfsClientPost(rules=[rule]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def delete_nfs_policy_rule(self, rule_name=None, policy_name=None, policy_id=None):
        """Delete the array NFS policy rules"""
        r = self._client.delete_policies_nfs_client_rules(
            names=[rule_name] if rule_name else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_nfs_policies_attached_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                           member_type=None):
        r = self._client.get_policies_nfs_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            member_types=[member_type] if member_type else ['directories'])
        return handle_response_with_items(r)

    def attach_nfs_policy_to_directory(self, export_name,
                                     managed_directory_name=None, managed_directory_id=None,
                                     policy_name=None, policy_id=None):
        r = self._client.post_policies_nfs_members(
            members=PolicyMemberExportPost(members=[
                PolicymemberexportpostMembers(
                    member=ReferenceWithType(
                        name=managed_directory_name if managed_directory_name else None,
                        id=managed_directory_id if managed_directory_id else None,
                        resource_type='directories'),
                    export_name=export_name)]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def detach_nfs_policy_from_directory(self, managed_directory_name=None, managed_directory_id=None,
                                            policy_name=None, policy_id=None):
        r = self._client.delete_policies_nfs_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            member_types=['directories'])
        return handle_response_with_items(r)

    # SMB Export policies
    def create_smb_policy(self, name, enabled=True, continuous_availability=True):
        """Create a new SMB policy"""
        p = PolicySmbPatch(name=name, enabled=enabled, continuous_availability_enabled=continuous_availability)
        r = self._client.post_policies_smb(policy=p, names=[name])
        return handle_response_with_items(r)

    def delete_smb_policy(self, name=None, policy_id=None):
        """Delete SMB policy"""
        r = self._client.delete_policies_smb(names=[name] if name else None, ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_smb_policy_rules(self, policy_name=None, policy_id=None):
        """Return the array SMB policy rules"""
        r = self._client.get_policies_smb_client_rules(policy_names=[policy_name] if policy_name else None,
                                                       policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def create_smb_policy_rule(self, rule_name=None, client='*', anonymous_access_allowed=None,
                               smb_encryption_required=None, policy_name=None, policy_id=None):
        """Create a new SMB policy rule"""
        rule = PolicyRuleSmbClient(
            name=rule_name if rule_name else None,
            client=client if client else None,
            anonymous_access_allowed=anonymous_access_allowed if anonymous_access_allowed else None,
            smb_encryption_required=smb_encryption_required if smb_encryption_required else None)
        r = self._client.post_policies_smb_client_rules(rules=PolicyRuleSmbClientPost(rules=[rule]),
                                                        policy_names=[policy_name] if policy_name else None,
                                                        policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def delete_smb_policy_rule(self, rule_name=None, policy_name=None, policy_id=None):
        """Delete the array SMB policy rules"""
        r = self._client.delete_policies_smb_client_rules(
            names=[rule_name] if rule_name else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_smb_policies_attached_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                           member_type=None):
        """Return the array SMB policies attached to a managed directory"""
        r = self._client.get_policies_smb_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            member_types=[member_type] if member_type else ['directories'])
        return handle_response_with_items(r)

    def attach_smb_policy_to_directory(self, export_name,
                                     managed_directory_name=None, managed_directory_id=None,
                                     policy_name=None, policy_id=None):
        """Attach SMB policy to managed directory"""
        r = self._client.post_policies_smb_members(
            members=PolicyMemberExportPost(members=[
                PolicymemberexportpostMembers(
                    member=ReferenceWithType(
                        name=managed_directory_name if managed_directory_name else None,
                        id=managed_directory_id if managed_directory_id else None,
                        resource_type='directories'),
                    export_name=export_name)]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def detach_smb_policy_from_directory(self, managed_directory_name=None, managed_directory_id=None,
                                            policy_name=None, policy_id=None):
        """Detach SMB policy from managed directory"""
        r = self._client.delete_policies_nfs_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            member_types=['directories'])
        return handle_response_with_items(r)

    # Directory quota policies
    def create_directory_quota_policy(self, name, enabled=True):
        """Create a new directory quota policy"""
        p = Policy(name=name, policy_type='quota', enabled=enabled)
        r = self._client.post_policies_quota(policy=p, names=[name])
        return handle_response_with_items(r)

    def delete_directory_quota_policy(self, name=None, policy_id=None):
        """Delete directory quota policy"""
        r = self._client.delete_policies_quota(names=[name] if name else None, ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_directory_quota_policy_rules(self, policy_name=None, policy_id=None):
        """Return the directory quota policy rules"""
        r = self._client.get_policies_quota_rules(policy_names=[policy_name] if policy_name else None,
                                                  policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def create_directory_quota_policy_rule(self, quota_limit, enforced, rule_name=None,
                                 notifications=None, policy_name=None, policy_id=None):
        """Create a new directory quota policy rule"""
        rule = PolicyRuleQuota(
            name=rule_name if rule_name else None,
            enforced=enforced if enforced else None,
            quota_limit=quota_limit if quota_limit else None,
            notifications=notifications if notifications else None)

        r = self._client.post_policies_quota_rules(rules=PolicyRuleQuotaPost(rules=[rule]),
                                                   policy_names=[policy_name] if policy_name else None,
                                                   policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def delete_directory_quota_policy_rule(self, rule_name=None, policy_name=None, policy_id=None):
        """Delete directory quota policy rules"""
        r = self._client.delete_policies_quota_rules(
            names=[rule_name] if rule_name else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_directory_quota_policies_attached_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                             member_type=None):
        """Return the array quota policies attached to a managed directory"""
        r = self._client.get_policies_quota_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            member_types=[member_type] if member_type else ['directories'])
        return handle_response_with_items(r)

    def attach_directory_quota_policy_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                    policy_name=None, policy_id=None, ignore_usage=True):
        """Attach quota policy to managed directory"""
        r = self._client.post_policies_quota_members(
            members=PolicyMemberPost(members=[
                PolicymemberpostMembers(
                    member=ReferenceWithType(
                        name=managed_directory_name if managed_directory_name else None,
                        id=managed_directory_id if managed_directory_id else None,
                        resource_type='directories'))]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            ignore_usage=ignore_usage
        )
        return handle_response_with_items(r)

    def detach_directory_quota_policy_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                              policy_name=None, policy_id=None):
        """Detach quota policy from managed directory"""
        r = self._client.delete_policies_quota_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            member_types=['directories'])
        return handle_response_with_items(r)

    # User & Group quota policies
    def create_user_group_quota_policy(self, name, enabled=True):
        """Create a new user & group quota policy"""
        p = Policy(name=name, policy_type='user-group-quota', enabled=enabled)
        r = self._client.post_policies_user_group_quota(policy=p, names=[name])
        return handle_response_with_items(r)

    def delete_user_group_quota_policy(self, name=None, policy_id=None):
        """Delete user & group quota policy"""
        r = self._client.delete_policies_user_group_quota(names=[name] if name else None, ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_user_group_quota_policy_rules(self, policy_name=None, policy_id=None):
        """Return user & group quota policy rules"""
        r = self._client.get_policies_user_group_quota_rules(policy_names=[policy_name] if policy_name else None,
                                                  policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def create_user_group_quota_policy_rule(self, quota_limit, quota_type='user-default', enforced=True, rule_name=None,
                                 notifications=None, policy_name=None, policy_id=None):
        """Create a new user & group quota policy rule"""
        rule = PolicyRuleUserGroupQuota(
            name=rule_name if rule_name else None,
            quota_type=quota_type,
            enforced=enforced if enforced else None,
            quota_limit=quota_limit if quota_limit else None,
            notifications=notifications if notifications else None
        )
        r = self._client.post_policies_user_group_quota_rules(rules=PolicyRuleUserGroupQuotaPost(rules=[rule]),
                                                   policy_names=[policy_name] if policy_name else None,
                                                   policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def delete_user_group_quota_policy_rule(self, rule_name=None, policy_name=None, policy_id=None):
        """Delete user & group quota policy rule"""
        r = self._client.delete_policies_user_group_quota_rules(
            names=[rule_name] if rule_name else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_user_group_quota_policies_attached_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                             member_type=None):
        """Return the array user & group quota policies attached to a managed directory"""
        r = self._client.get_policies_user_group_quota_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            member_types=[member_type] if member_type else ['directories'])
        return handle_response_with_items(r)

    def attach_user_group_quota_policy_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                    policy_name=None, policy_id=None, ignore_usage=True):
        """Attach user & group quota policy to managed directory"""
        r = self._client.post_policies_user_group_quota_members(
            members=PolicyMemberPost(members=[
                PolicymemberpostMembers(
                    member=ReferenceWithType(
                        name=managed_directory_name if managed_directory_name else None,
                        id=managed_directory_id if managed_directory_id else None,
                        resource_type='directories'))]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            ignore_usage=ignore_usage
        )
        return handle_response_with_items(r)

    def detach_user_group_quota_policy_from_directory(self, managed_directory_name=None, managed_directory_id=None,
                                              policy_name=None, policy_id=None):
        """Detach user & group quota policy from managed directory"""
        r = self._client.delete_policies_user_group_quota_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            member_types=['directories'])
        return handle_response_with_items(r)

    # Snapshot policies
    def create_snapshot_policy(self, name, enabled=True):
        """Create a new snapshot policy"""
        p = Policy(name=name, policy_type='snapshot', enabled=enabled)
        r = self._client.post_policies_snapshot(policy=p, names=[name])
        return handle_response_with_items(r)

    def delete_snapshot_policy(self, name=None, policy_id=None):
        """Delete snapshot policy"""
        r = self._client.delete_policies_snapshot(names=[name] if name else None,
                                                  ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_snapshot_policy_rules(self, policy_name=None, policy_id=None):
        """Return the array snapshot policy rules"""
        r = self._client.get_policies_snapshot_rules(policy_names=[policy_name] if policy_name else None,
                                                     policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def create_snapshot_policy_rule(self, client_name, every, keep_for, at=None, suffix=None, rule_name=None,
                                    policy_name=None, policy_id=None):
        """Create a new snapshot policy rule"""
        rule = PolicyRuleSnapshot(
            name=rule_name if rule_name else None,
            at=at if at else None,
            client_name=client_name if client_name else None,
            every=every if every else None,
            keep_for=keep_for if keep_for else None,
            suffix=suffix if suffix else None)

        r = self._client.post_policies_snapshot_rules(rules=PolicyRuleSnapshotPost(rules=[rule]),
                                                      policy_names=[policy_name] if policy_name else None,
                                                      policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def delete_snapshot_policy_rule(self, rule_name=None, policy_name=None, policy_id=None):
        """Delete the array snapshot policy rule"""
        r = self._client.delete_policies_snapshot_rules(
            names=[rule_name] if rule_name else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_snapshot_policies_attached_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                                member_type=None):
        r = self._client.get_policies_snapshot_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            member_types=[member_type] if member_type else ['directories'])
        return handle_response_with_items(r)

    def attach_snapshot_policy_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                       policy_name=None, policy_id=None):
        r = self._client.post_policies_snapshot_members(
            members=PolicyMemberPost(members=[
                PolicymemberpostMembers(
                    member=ReferenceWithType(
                        name=managed_directory_name if managed_directory_name else None,
                        id=managed_directory_id if managed_directory_id else None,
                        resource_type='directories'))]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def detach_snapshot_policy_from_directory(self, managed_directory_name=None, managed_directory_id=None,
                                                 policy_name=None, policy_id=None):
        r = self._client.delete_policies_snapshot_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            member_types=['directories'])
        return handle_response_with_items(r)


    # Autodir policies
    def create_autodir_policy(self, name, enabled=True):
        """Create a new autodir policy"""
        p = Policy(name=name, policy_type='autodir', enabled=enabled)
        r = self._client.post_policies_autodir(policy=p, names=[name])
        return handle_response_with_items(r)

    def delete_autodir_policy(self, name=None, policy_id=None):
        """Delete autodir policy"""
        r = self._client.delete_policies_autodir(names=[name] if name else None, ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def get_autodir_policies_attached_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                               member_type=None):
        r = self._client.get_policies_autodir_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            member_types=[member_type] if member_type else ['directories'])
        return handle_response_with_items(r)

    def attach_autodir_policy_to_directory(self, managed_directory_name=None, managed_directory_id=None,
                                      policy_name=None, policy_id=None):
        r = self._client.post_policies_autodir_members(
            members=PolicyMemberPost(members=[
                PolicymemberpostMembers(
                    member=ReferenceWithType(
                        name=managed_directory_name if managed_directory_name else None,
                        id=managed_directory_id if managed_directory_id else None,
                        resource_type='directories'))]),
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None)
        return handle_response_with_items(r)

    def detach_autodir_policy_from_directory(self, managed_directory_name=None, managed_directory_id=None,
                                                policy_name=None, policy_id=None):
        r = self._client.delete_policies_autodir_members(
            member_names=[managed_directory_name] if managed_directory_name else None,
            member_ids=[managed_directory_id] if managed_directory_id else None,
            policy_names=[policy_name] if policy_name else None,
            policy_ids=[policy_id] if policy_id else None,
            member_types=['directories'])
        return handle_response_with_items(r)

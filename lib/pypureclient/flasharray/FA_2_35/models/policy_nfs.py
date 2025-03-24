# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.35
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_35 import models

class PolicyNfs(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'destroyed': 'bool',
        'enabled': 'bool',
        'pod': 'Reference',
        'policy_type': 'str',
        'time_remaining': 'int',
        'nfs_version': 'list[str]',
        'policy_mapping': 'PolicyNfsPolicyMapping',
        'security': 'list[str]',
        'user_mapping_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'destroyed': 'destroyed',
        'enabled': 'enabled',
        'pod': 'pod',
        'policy_type': 'policy_type',
        'time_remaining': 'time_remaining',
        'nfs_version': 'nfs_version',
        'policy_mapping': 'policy_mapping',
        'security': 'security',
        'user_mapping_enabled': 'user_mapping_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        destroyed=None,  # type: bool
        enabled=None,  # type: bool
        pod=None,  # type: models.Reference
        policy_type=None,  # type: str
        time_remaining=None,  # type: int
        nfs_version=None,  # type: List[str]
        policy_mapping=None,  # type: models.PolicyNfsPolicyMapping
        security=None,  # type: List[str]
        user_mapping_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource. 
            name (str): A user-specified name. The name must be locally unique and can be changed. 
            destroyed (bool): Returns a value of `true` if the policy has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed policy is permanently eradicated. Once the `time_remaining` period has elapsed, the policy is permanently eradicated and can no longer be recovered. 
            enabled (bool): Returns a value of `true` if the policy is enabled. 
            pod (Reference): A reference to the pod. 
            policy_type (str): The type of policy. Valid values include `autodir`, `nfs`, `smb`, `snapshot`, and `quota`. 
            time_remaining (int): The amount of time left, measured in milliseconds, until the destroyed policy is permanently eradicated. 
            nfs_version (list[str]): NFS protocol version allowed for the export. If NFS version is allowed for all rules of the policy it is cascaded exactly as: `nfsv3`, `nfsv4`. If the NFS version is supported partially by the rules of the policy it will be cascaded as: `nfsv3-partial`, `nfsv4-partial`. If the NFS version is not supported by any rules or there are no rules of the policy then it will not be in the result array. If there are no rules in the policy the array will be empty. If there are two rules, one supporting `nfsv3` and the other supporting `nfsv3` and `nfsv4` then the array would contain `nfsv3` and `nfsv4-partial`. 
            policy_mapping (PolicyNfsPolicyMapping): Specifies the mapping of this policy across a pod replica link. If this policy is not inside a pod of a pod replica link, mapping is `null`. 
            security (list[str]): The security flavors to use for accessing files on this mount point. Values include `auth_sys`, `auth_sys-partial`, `krb5`, `krb5-partial`, `krb5i`, and `krb5p`. If the server does not support the requested flavor, the mount operation fails. If `auth_sys`, the client is trusted to specify the identity of the user. If `krb5`, cryptographic proof of the identity of the user is provided in each RPC request. Note that additional configuration besides adding this mount option is required in order to enable Kerberos security. If `krb5i`, integrity checking is added to krb5, to ensure the data has not been tampered with. If `krb5p`, integrity checking and encryption are added to `krb5`. This is the most secure setting, but it also involves the most performance overhead. If security option is allowed for all rules of the policy, it is cascaded exactly. Examples: `auth_sys`, `krb5`. If the security option is supported partially by the rules of the policy, it will be cascaded with the `-partial` suffix. Examples include: `auth_sys-partial`, `krb5-partial`. If the security option is not supported by any rules or there are no rules of the policy, then it will not be in the result array. If there are no rules in the policy the array of values will be empty. If there are two rules, one supporting auth_sys and the other supporting auth_sys and krb5 the array of values would contain `auth_sys` and `krb5-partial`. 
            user_mapping_enabled (bool): Returns `true` if user mapping is enabled on the policy. If `true`, FlashArray queries the joined AD/OpenLDAP server to find the user corresponding to the incoming UID. If `false`, users are defined by UID/GID pair. 
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if destroyed is not None:
            self.destroyed = destroyed
        if enabled is not None:
            self.enabled = enabled
        if pod is not None:
            self.pod = pod
        if policy_type is not None:
            self.policy_type = policy_type
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if nfs_version is not None:
            self.nfs_version = nfs_version
        if policy_mapping is not None:
            self.policy_mapping = policy_mapping
        if security is not None:
            self.security = security
        if user_mapping_enabled is not None:
            self.user_mapping_enabled = user_mapping_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfs`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfs`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfs`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfs`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(PolicyNfs, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyNfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

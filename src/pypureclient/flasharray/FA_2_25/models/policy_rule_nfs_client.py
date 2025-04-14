# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_25 import models

class PolicyRuleNfsClient(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access': 'str',
        'anongid': 'str',
        'anonuid': 'str',
        'client': 'str',
        'destroyed': 'bool',
        'name': 'str',
        'permission': 'str',
        'policy': 'FixedReferenceWithType',
        'time_remaining': 'int'
    }

    attribute_map = {
        'access': 'access',
        'anongid': 'anongid',
        'anonuid': 'anonuid',
        'client': 'client',
        'destroyed': 'destroyed',
        'name': 'name',
        'permission': 'permission',
        'policy': 'policy',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        access=None,  # type: str
        anongid=None,  # type: str
        anonuid=None,  # type: str
        client=None,  # type: str
        destroyed=None,  # type: bool
        name=None,  # type: str
        permission=None,  # type: str
        policy=None,  # type: models.FixedReferenceWithType
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            access (str): Specifies access control for the export. Valid values are `root-squash`, `all-squash`, and `no-root-squash`. `root-squash` prevents client users and groups with root privilege from mapping their root privilege to a file system. All users with UID 0 will have their UID mapped to anonuid. All users with GID 0 will have their GID mapped to anongid. `all-squash` maps all UIDs (including root) to anonuid and all GIDs (including root) to anongid. `no-root-squash` allows users and groups to access the file system with their UIDs and GIDs. The default is `root-squash` if not specified. 
            anongid (str): Any user whose GID is affected by an `access` of `root_squash` or `all_squash` will have their GID mapped to `anongid`. The default `anongid` is null, which means 65534. Use \"\" to clear. This value is ignored when user mapping is enabled - see User Guide for more details. 
            anonuid (str): Any user whose UID is affected by an `access` of `root_squash` or `all_squash` will have their UID mapped to `anonuid`. The default `anonuid` is null, which means 65534. Use \"\" to clear. 
            client (str): Specifies the clients that will be permitted to access the export. Accepted notation includes IP, IP mask, or hostname. The default is `*` if not specified. 
            destroyed (bool): Returns a value of `true` if the pod containing the NFS policy rule has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed policy is permanently eradicated. Once the `time_remaining` period has elapsed, the NFS policy rule is permanently eradicated and can no longer be recovered. 
            name (str): Name of this rule. The name is automatically generated by the system. 
            permission (str): Specifies which read-write client access permissions are allowed for the export. Valid values are `rw` and `ro`. The default is `rw` if not specified. 
            policy (FixedReferenceWithType): The policy to which this rule belongs.
            time_remaining (int): The amount of time left, in milliseconds, until the destroyed NFS policy rule is permanently eradicated. 
        """
        if access is not None:
            self.access = access
        if anongid is not None:
            self.anongid = anongid
        if anonuid is not None:
            self.anonuid = anonuid
        if client is not None:
            self.client = client
        if destroyed is not None:
            self.destroyed = destroyed
        if name is not None:
            self.name = name
        if permission is not None:
            self.permission = permission
        if policy is not None:
            self.policy = policy
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleNfsClient`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleNfsClient`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleNfsClient`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleNfsClient`".format(key))
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
        if issubclass(PolicyRuleNfsClient, dict):
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
        if not isinstance(other, PolicyRuleNfsClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

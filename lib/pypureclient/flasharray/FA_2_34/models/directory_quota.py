# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.34
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_34 import models

class DirectoryQuota(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'directory': 'FixedReferenceWithType',
        'enabled': 'bool',
        'enforced': 'bool',
        'path': 'str',
        'percentage_used': 'float',
        'policy': 'FixedReferenceWithType',
        'quota_limit': 'int',
        'rule_name': 'str',
        'usage': 'int'
    }

    attribute_map = {
        'directory': 'directory',
        'enabled': 'enabled',
        'enforced': 'enforced',
        'path': 'path',
        'percentage_used': 'percentage_used',
        'policy': 'policy',
        'quota_limit': 'quota_limit',
        'rule_name': 'rule_name',
        'usage': 'usage'
    }

    required_args = {
    }

    def __init__(
        self,
        directory=None,  # type: models.FixedReferenceWithType
        enabled=None,  # type: bool
        enforced=None,  # type: bool
        path=None,  # type: str
        percentage_used=None,  # type: float
        policy=None,  # type: models.FixedReferenceWithType
        quota_limit=None,  # type: int
        rule_name=None,  # type: str
        usage=None,  # type: int
    ):
        """
        Keyword args:
            directory (FixedReferenceWithType): The directory to which the quota applies.
            enabled (bool): Returns a value of `true` if the policy is enabled. 
            enforced (bool): Defines whether the quota rule is enforced or unenforced. If the quota rule is enforced and logical space usage exceeds the quota limit, any modification operations that result in a need for more space are blocked. If the quota rule is unenforced and logical space usage exceeds the quota limit, notification emails are sent to targets that are specified using the `notification` parameter. No client operations are blocked when an unenforced limit is exceeded. If set to `true`, the limit is enforced. If set to `false`, notification targets are informed when the usage exceeds 80 percent of the limit. 
            path (str): Absolute path of the directory in the file system. 
            percentage_used (float): The percentage of the space used in the directory with respect to the quota limit. 
            policy (FixedReferenceWithType): The effective quota policy that imposes the limit. This is the policy with the lowest limit. 
            quota_limit (int): Effective quota limit imposed by the quota policy rule attached to the directory, measured in bytes. 
            rule_name (str): Name of the rule that results in this quota and behavior being applied to this directory. 
            usage (int): The amount of logically written data for the directory, measured in bytes. 
        """
        if directory is not None:
            self.directory = directory
        if enabled is not None:
            self.enabled = enabled
        if enforced is not None:
            self.enforced = enforced
        if path is not None:
            self.path = path
        if percentage_used is not None:
            self.percentage_used = percentage_used
        if policy is not None:
            self.policy = policy
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if rule_name is not None:
            self.rule_name = rule_name
        if usage is not None:
            self.usage = usage

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryQuota`".format(key))
        if key == "percentage_used" and value is not None:
            if value < 0.0:
                raise ValueError("Invalid value for `percentage_used`, must be a value greater than or equal to `0.0`")
        if key == "quota_limit" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `quota_limit`, must be a value greater than or equal to `0`")
        if key == "usage" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usage`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryQuota`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryQuota`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryQuota`".format(key))
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
        if issubclass(DirectoryQuota, dict):
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
        if not isinstance(other, DirectoryQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

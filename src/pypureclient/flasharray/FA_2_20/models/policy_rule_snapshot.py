# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_20 import models

class PolicyRuleSnapshot(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'at': 'int',
        'client_name': 'str',
        'every': 'int',
        'keep_for': 'int',
        'name': 'str',
        'policy': 'FixedReferenceWithType',
        'suffix': 'str'
    }

    attribute_map = {
        'at': 'at',
        'client_name': 'client_name',
        'every': 'every',
        'keep_for': 'keep_for',
        'name': 'name',
        'policy': 'policy',
        'suffix': 'suffix'
    }

    required_args = {
    }

    def __init__(
        self,
        at=None,  # type: int
        client_name=None,  # type: str
        every=None,  # type: int
        keep_for=None,  # type: int
        name=None,  # type: str
        policy=None,  # type: models.FixedReferenceWithType
        suffix=None,  # type: str
    ):
        """
        Keyword args:
            at (int): Specifies the number of milliseconds since midnight at which to take a snapshot. The `at` value can only be set to an hour and must be between 0 and 82800000, inclusive. The `at` value can only be set on the rule with the smallest `every` value. The `at` value cannot be set if the `every` value is not measured in days. The `at` value can only be set for at most one rule in the same policy. 
            client_name (str): The snapshot client name. A full snapshot name is constructed in the form of `DIR.CLIENT_NAME.SUFFIX` where `DIR` is the managed directory name, `CLIENT_NAME` is the snapshot client name, and `SUFFIX` is the snapshot suffix. The client visible snapshot name is `CLIENT_NAME.SUFFIX`. 
            every (int): Specifies the interval between snapshots, in milliseconds. The `every` value for all rules must be multiples of one another. The `every` value must be unique for each rule in the same policy. The `every` value must be between 5 minutes and 1 year. 
            keep_for (int): Specifies the period that snapshots are retained before they are eradicated, in milliseconds. The `keep_for` value cannot be less than the `every` value of the rule. The `keep_for` value must be unique for each rule in the same policy. The `keep_for` value must be between 5 minutes and 1 year. The `keep_for` value cannot be less than the `keep_for` value of any rule in the same policy with a smaller `every` value. 
            name (str): Name of this rule. The name is automatically generated by the system. 
            policy (FixedReferenceWithType): The policy to which this rule belongs.
            suffix (str): The snapshot suffix name. A full snapshot name is constructed in the form of `DIR.CLIENT_NAME.SUFFIX` where `DIR` is the managed directory name, `CLIENT_NAME` is the snapshot client name, and `SUFFIX` is the snapshot suffix. The client-visible snapshot name is `CLIENT_NAME.SUFFIX`. The `suffix` value can only be set for one rule in the same policy. The `suffix` value can only be set on a rule with the same `keep_for` value and `every` value. The `suffix` value can only be set on the rule with the largest `keep_for` value. If not specified, defaults to a monotonically increasing number generated by the system. 
        """
        if at is not None:
            self.at = at
        if client_name is not None:
            self.client_name = client_name
        if every is not None:
            self.every = every
        if keep_for is not None:
            self.keep_for = keep_for
        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if suffix is not None:
            self.suffix = suffix

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSnapshot`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSnapshot`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSnapshot`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleSnapshot`".format(key))
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
        if issubclass(PolicyRuleSnapshot, dict):
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
        if not isinstance(other, PolicyRuleSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

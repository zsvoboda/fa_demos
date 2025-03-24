# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_38 import models

class PolicyMember(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'FixedReference',
        'destroyed': 'bool',
        'enabled': 'bool',
        'member': 'FixedReferenceWithType',
        'policy': 'FixedReferenceWithType',
        'time_remaining': 'int'
    }

    attribute_map = {
        'context': 'context',
        'destroyed': 'destroyed',
        'enabled': 'enabled',
        'member': 'member',
        'policy': 'policy',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        context=None,  # type: models.FixedReference
        destroyed=None,  # type: bool
        enabled=None,  # type: bool
        member=None,  # type: models.FixedReferenceWithType
        policy=None,  # type: models.FixedReferenceWithType
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            destroyed (bool): Returns a value of `true` if the member is destroyed. 
            enabled (bool): Returns a value of `true` if the policy is enabled. 
            member (FixedReferenceWithType): Reference to the resource that the policy is applied to.
            policy (FixedReferenceWithType): Reference to the policy.
            time_remaining (int): The amount of time left, in milliseconds, until the destroyed policy member is permanently eradicated. 
        """
        if context is not None:
            self.context = context
        if destroyed is not None:
            self.destroyed = destroyed
        if enabled is not None:
            self.enabled = enabled
        if member is not None:
            self.member = member
        if policy is not None:
            self.policy = policy
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyMember`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyMember`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyMember`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyMember`".format(key))
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
        if issubclass(PolicyMember, dict):
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
        if not isinstance(other, PolicyMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

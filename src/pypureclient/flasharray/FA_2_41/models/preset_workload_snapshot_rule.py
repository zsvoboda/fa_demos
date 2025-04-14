# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_41 import models

class PresetWorkloadSnapshotRule(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'at': 'str',
        'every': 'str',
        'keep_for': 'str'
    }

    attribute_map = {
        'at': 'at',
        'every': 'every',
        'keep_for': 'keep_for'
    }

    required_args = {
        'every',
        'keep_for',
    }

    def __init__(
        self,
        every,  # type: str
        keep_for,  # type: str
        at=None,  # type: str
    ):
        """
        Keyword args:
            at (str): Specifies the number of milliseconds since midnight at which to take a snapshot. The `at` value cannot be set if the `every` value is not measured in days. The `at` value can only be set on the first rule. 
            every (str, required): Specifies the interval between snapshots, in milliseconds. The `every` value for all rules must be multiples of one another. The `every` value must be between five minutes and 400 days for the first rule. The `every` value must be between five minutes and one day for the second rule. 
            keep_for (str, required): Specifies the period that snapshots are retained before they are eradicated, in milliseconds. The `keep_for` value must be between 10 minutes and 24855 days for the first rule, and a multiple of a second. The `keep_for` value must be between 10 minutes and 2147483647 days for the second rule, and must be greater than or equal to the `keep_for` value of the first rule. 
        """
        if at is not None:
            self.at = at
        self.every = every
        self.keep_for = keep_for

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadSnapshotRule`".format(key))
        if key == "every" and value is None:
            raise ValueError("Invalid value for `every`, must not be `None`")
        if key == "keep_for" and value is None:
            raise ValueError("Invalid value for `keep_for`, must not be `None`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadSnapshotRule`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadSnapshotRule`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadSnapshotRule`".format(key))
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
        if issubclass(PresetWorkloadSnapshotRule, dict):
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
        if not isinstance(other, PresetWorkloadSnapshotRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

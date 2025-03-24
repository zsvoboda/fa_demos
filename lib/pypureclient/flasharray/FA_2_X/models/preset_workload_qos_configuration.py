# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.X
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_X import models

class PresetWorkloadQosConfiguration(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bandwidth_limit': 'str',
        'iops_limit': 'str',
        'name': 'str'
    }

    attribute_map = {
        'bandwidth_limit': 'bandwidth_limit',
        'iops_limit': 'iops_limit',
        'name': 'name'
    }

    required_args = {
        'name',
    }

    def __init__(
        self,
        name,  # type: str
        bandwidth_limit=None,  # type: str
        iops_limit=None,  # type: str
    ):
        """
        Keyword args:
            bandwidth_limit (str): The QoS IOPs limit shared across all volumes in the placement. Between 100 and 100000000, inclusive. Supports parameterization. 
            iops_limit (str): The maximum QoS bandwidth limit shared across all volumes in the placement. Whenever throughput exceeds the bandwidth limit, throttling occurs. Measured in bytes per second. Between 1MB/s and 512 GB/s, inclusive. Supports parameterization. 
            name (str, required): The name of the QoS configuration, by which other configuration objects in the preset can reference it. Name must be unique across all configuration objects in the preset. 
        """
        if bandwidth_limit is not None:
            self.bandwidth_limit = bandwidth_limit
        if iops_limit is not None:
            self.iops_limit = iops_limit
        self.name = name

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadQosConfiguration`".format(key))
        if key == "name" and value is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadQosConfiguration`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadQosConfiguration`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadQosConfiguration`".format(key))
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
        if issubclass(PresetWorkloadQosConfiguration, dict):
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
        if not isinstance(other, PresetWorkloadQosConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_29 import models

class VolumeSnapshotPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'destroyed': 'bool',
        'suffix': 'str'
    }

    attribute_map = {
        'destroyed': 'destroyed',
        'suffix': 'suffix'
    }

    required_args = {
    }

    def __init__(
        self,
        destroyed=None,  # type: bool
        suffix=None,  # type: str
    ):
        """
        Keyword args:
            destroyed (bool): If set to `true`, destroys a resource. Once set to `true`, the `time_remaining` value will display the amount of time left until the destroyed resource is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed resource can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the resource is permanently eradicated and can no longer be recovered. 
            suffix (str): The suffix that is appended to the `source_name` value to generate the full volume snapshot name in the form `VOL.SUFFIX`. If the suffix is not specified, the system constructs the snapshot name in the form `VOL.NNN`, where `VOL` is the volume name, and `NNN` is a monotonically increasing number. 
        """
        if destroyed is not None:
            self.destroyed = destroyed
        if suffix is not None:
            self.suffix = suffix

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshotPost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshotPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshotPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshotPost`".format(key))
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
        if issubclass(VolumeSnapshotPost, dict):
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
        if not isinstance(other, VolumeSnapshotPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

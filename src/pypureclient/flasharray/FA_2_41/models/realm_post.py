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

class RealmPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'qos': 'ContainerQos',
        'quota_limit': 'int',
        'tags': 'list[NonCopyableTag]'
    }

    attribute_map = {
        'qos': 'qos',
        'quota_limit': 'quota_limit',
        'tags': 'tags'
    }

    required_args = {
    }

    def __init__(
        self,
        qos=None,  # type: models.ContainerQos
        quota_limit=None,  # type: int
        tags=None,  # type: List[models.NonCopyableTag]
    ):
        """
        Keyword args:
            qos (ContainerQos): Sets QoS limits.
            quota_limit (int): The logical quota limit of the realm, measured in bytes. Must be a multiple of 512. 
            tags (list[NonCopyableTag]): The list of tags to be upserted with the object. 
        """
        if qos is not None:
            self.qos = qos
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if tags is not None:
            self.tags = tags

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RealmPost`".format(key))
        if key == "quota_limit" and value is not None:
            if value > 4503599627370496:
                raise ValueError("Invalid value for `quota_limit`, value must be less than or equal to `4503599627370496`")
            if value < 1048576:
                raise ValueError("Invalid value for `quota_limit`, must be a value greater than or equal to `1048576`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RealmPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RealmPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RealmPost`".format(key))
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
        if issubclass(RealmPost, dict):
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
        if not isinstance(other, RealmPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

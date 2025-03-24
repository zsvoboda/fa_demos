# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_13 import models

class Tag(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'copyable': 'bool',
        'key': 'str',
        'namespace': 'str',
        'resource': 'FixedReference',
        'value': 'str'
    }

    attribute_map = {
        'copyable': 'copyable',
        'key': 'key',
        'namespace': 'namespace',
        'resource': 'resource',
        'value': 'value'
    }

    required_args = {
    }

    def __init__(
        self,
        copyable=None,  # type: bool
        key=None,  # type: str
        namespace=None,  # type: str
        resource=None,  # type: models.FixedReference
        value=None,  # type: str
    ):
        """
        Keyword args:
            copyable (bool): Specifies whether or not to include the tag when copying the parent resource. If set to `true`, the tag is included in resource copying. If set to `false`, the tag is not included. If not specified, defaults to `true`. 
            key (str): Key of the tag. Supports up to 64 Unicode characters. 
            namespace (str): Optional namespace of the tag. Namespace identifies the category of the tag. Omitting the namespace defaults to the namespace `default`. The `pure&#42;` namespaces are reserved for plugins and integration partners. It is recommended that customers avoid using reserved namespaces. 
            resource (FixedReference)
            value (str): Value of the tag. Supports up to 256 Unicode characters. 
        """
        if copyable is not None:
            self.copyable = copyable
        if key is not None:
            self.key = key
        if namespace is not None:
            self.namespace = namespace
        if resource is not None:
            self.resource = resource
        if value is not None:
            self.value = value

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Tag`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Tag`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Tag`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Tag`".format(key))
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
        if issubclass(Tag, dict):
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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

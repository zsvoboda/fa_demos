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

class DirectoryServiceCommon(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'FixedReferenceWithType',
        'base_dn': 'str',
        'bind_password': 'str',
        'bind_user': 'str',
        'enabled': 'bool',
        'services': 'list[str]',
        'uris': 'list[str]'
    }

    attribute_map = {
        'context': 'context',
        'base_dn': 'base_dn',
        'bind_password': 'bind_password',
        'bind_user': 'bind_user',
        'enabled': 'enabled',
        'services': 'services',
        'uris': 'uris'
    }

    required_args = {
    }

    def __init__(
        self,
        context=None,  # type: models.FixedReferenceWithType
        base_dn=None,  # type: str
        bind_password=None,  # type: str
        bind_user=None,  # type: str
        enabled=None,  # type: bool
        services=None,  # type: List[str]
        uris=None,  # type: List[str]
    ):
        """
        Keyword args:
            context (FixedReferenceWithType): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            base_dn (str): Base of the Distinguished Name (DN) of the directory service groups. 
            bind_password (str): Masked password used to query the directory.
            bind_user (str): Username used to query the directory.
            enabled (bool): Whether or not the directory service is enabled.
            services (list[str]): Services for which the directory service configuration is used. 
            uris (list[str]): List of URIs for the configured directory servers.
        """
        if context is not None:
            self.context = context
        if base_dn is not None:
            self.base_dn = base_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if bind_user is not None:
            self.bind_user = bind_user
        if enabled is not None:
            self.enabled = enabled
        if services is not None:
            self.services = services
        if uris is not None:
            self.uris = uris

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryServiceCommon`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryServiceCommon`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryServiceCommon`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryServiceCommon`".format(key))
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
        if issubclass(DirectoryServiceCommon, dict):
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
        if not isinstance(other, DirectoryServiceCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

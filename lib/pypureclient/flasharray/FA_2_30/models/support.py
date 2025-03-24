# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.30
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_30 import models

class Support(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'phonehome_enabled': 'bool',
        'proxy': 'str',
        'remote_assist_active': 'bool',
        'remote_assist_expires': 'int',
        'remote_assist_opened': 'int',
        'remote_assist_paths': 'list[SupportRemoteAssistPaths]',
        'remote_assist_status': 'str'
    }

    attribute_map = {
        'phonehome_enabled': 'phonehome_enabled',
        'proxy': 'proxy',
        'remote_assist_active': 'remote_assist_active',
        'remote_assist_expires': 'remote_assist_expires',
        'remote_assist_opened': 'remote_assist_opened',
        'remote_assist_paths': 'remote_assist_paths',
        'remote_assist_status': 'remote_assist_status'
    }

    required_args = {
    }

    def __init__(
        self,
        phonehome_enabled=None,  # type: bool
        proxy=None,  # type: str
        remote_assist_active=None,  # type: bool
        remote_assist_expires=None,  # type: int
        remote_assist_opened=None,  # type: int
        remote_assist_paths=None,  # type: List[models.SupportRemoteAssistPaths]
        remote_assist_status=None,  # type: str
    ):
        """
        Keyword args:
            phonehome_enabled (bool): The status of phonehome. If set to `true`, enables phonehome. If set to `false`, disables phonehome. 
            proxy (str): The value of the current proxy, which is used to connect to cloud services such as phonehome and remote assist. Specify the server name, including the scheme and proxy port number. 
            remote_assist_active (bool): The status of the remote assist session. If set to `true`, enables the remote assist session. If set to `false`, disables the remote assist session. 
            remote_assist_expires (int): The timestamp when the session expires, measured in milliseconds since the UNIX epoch. 
            remote_assist_opened (int): The timestamp when the session opened, measured in milliseconds since the UNIX epoch. 
            remote_assist_paths (list[SupportRemoteAssistPaths])
            remote_assist_status (str): The status of the remote assist session. Values include `connected`, `connecting`, `disconnected`, and `session-active`. 
        """
        if phonehome_enabled is not None:
            self.phonehome_enabled = phonehome_enabled
        if proxy is not None:
            self.proxy = proxy
        if remote_assist_active is not None:
            self.remote_assist_active = remote_assist_active
        if remote_assist_expires is not None:
            self.remote_assist_expires = remote_assist_expires
        if remote_assist_opened is not None:
            self.remote_assist_opened = remote_assist_opened
        if remote_assist_paths is not None:
            self.remote_assist_paths = remote_assist_paths
        if remote_assist_status is not None:
            self.remote_assist_status = remote_assist_status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Support`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Support`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Support`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Support`".format(key))
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
        if issubclass(Support, dict):
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
        if not isinstance(other, Support):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

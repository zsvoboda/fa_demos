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

class SupportRemoteAssistSessions(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_level': 'str',
        'active': 'bool',
        'duration': 'int',
        'expires': 'int',
        'opened': 'int',
        'paths': 'list[SupportRemoteAssistSessionsPaths]',
        'status': 'str'
    }

    attribute_map = {
        'access_level': 'access_level',
        'active': 'active',
        'duration': 'duration',
        'expires': 'expires',
        'opened': 'opened',
        'paths': 'paths',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        access_level=None,  # type: str
        active=None,  # type: bool
        duration=None,  # type: int
        expires=None,  # type: int
        opened=None,  # type: int
        paths=None,  # type: List[models.SupportRemoteAssistSessionsPaths]
        status=None,  # type: str
    ):
        """
        Keyword args:
            access_level (str): The access level for this RA session. This is set to default_access_level unless access_level_override is provided. Values include `restricted` and `elevated`. 
            active (bool): The status of a remote assist session. If set to `true`, enable the remote assist session. If set to `false`, disable the remote assist session. 
            duration (int): Specifies the duration of the remote assist session in milliseconds. This parameter should only be provided when establishing a new session. This parameter determines the length of time the session will remain active after it is initiated. Defaults to 86400000 (24h) with a min of 14400000 (4h) and a max of 172800000 (48h). 
            expires (int): The timestamp when the session expires, measured in milliseconds since the UNIX epoch. 
            opened (int): The timestamp when the session opened, measured in milliseconds since the UNIX epoch. 
            paths (list[SupportRemoteAssistSessionsPaths])
            status (str): The status of the remote assist session. Values include `connected`, `connecting`, `disconnected`, and `session-active`. 
        """
        if access_level is not None:
            self.access_level = access_level
        if active is not None:
            self.active = active
        if duration is not None:
            self.duration = duration
        if expires is not None:
            self.expires = expires
        if opened is not None:
            self.opened = opened
        if paths is not None:
            self.paths = paths
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SupportRemoteAssistSessions`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SupportRemoteAssistSessions`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SupportRemoteAssistSessions`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SupportRemoteAssistSessions`".format(key))
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
        if issubclass(SupportRemoteAssistSessions, dict):
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
        if not isinstance(other, SupportRemoteAssistSessions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

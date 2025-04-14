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

class LocalGroup(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'FixedReferenceWithType',
        'local_directory_service': 'FixedReferenceWithType',
        'realm': 'FixedReferenceWithType',
        'built_in': 'bool',
        'email': 'str',
        'gid': 'int',
        'name': 'str',
        'sid': 'str'
    }

    attribute_map = {
        'context': 'context',
        'local_directory_service': 'local_directory_service',
        'realm': 'realm',
        'built_in': 'built_in',
        'email': 'email',
        'gid': 'gid',
        'name': 'name',
        'sid': 'sid'
    }

    required_args = {
    }

    def __init__(
        self,
        context=None,  # type: models.FixedReferenceWithType
        local_directory_service=None,  # type: models.FixedReferenceWithType
        realm=None,  # type: models.FixedReferenceWithType
        built_in=None,  # type: bool
        email=None,  # type: str
        gid=None,  # type: int
        name=None,  # type: str
        sid=None,  # type: str
    ):
        """
        Keyword args:
            context (FixedReferenceWithType): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            local_directory_service (FixedReferenceWithType): Reference to the local directory service the object belongs to. 
            realm (FixedReferenceWithType): Reference to the realm the object belongs to. When the value is not present or set to `null` it means the object lives outside of a realm. 
            built_in (bool): Returns a value of `true` if the local group is built in. Returns a value of `false` if the group has been created manually. 
            email (str): The email address of the local group. 
            gid (int): The POSIX user ID of this object (group ID). 
            name (str): The local group name. 
            sid (str): The SID (security ID) of the local group. 
        """
        if context is not None:
            self.context = context
        if local_directory_service is not None:
            self.local_directory_service = local_directory_service
        if realm is not None:
            self.realm = realm
        if built_in is not None:
            self.built_in = built_in
        if email is not None:
            self.email = email
        if gid is not None:
            self.gid = gid
        if name is not None:
            self.name = name
        if sid is not None:
            self.sid = sid

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalGroup`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalGroup`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalGroup`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalGroup`".format(key))
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
        if issubclass(LocalGroup, dict):
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
        if not isinstance(other, LocalGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

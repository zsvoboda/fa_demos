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

class Saml2Sso(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'array_url': 'str',
        'enabled': 'bool',
        'idp': 'Saml2SsoIdp',
        'sp': 'Saml2SsoSp'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'array_url': 'array_url',
        'enabled': 'enabled',
        'idp': 'idp',
        'sp': 'sp'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        array_url=None,  # type: str
        enabled=None,  # type: bool
        idp=None,  # type: models.Saml2SsoIdp
        sp=None,  # type: models.Saml2SsoSp
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified. 
            name (str): Name of the resource. The name cannot be modified. 
            array_url (str): The URL of the array. 
            enabled (bool): If set to `true`, the SAML2 SSO configuration is enabled. 
            idp (Saml2SsoIdp)
            sp (Saml2SsoSp)
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if array_url is not None:
            self.array_url = array_url
        if enabled is not None:
            self.enabled = enabled
        if idp is not None:
            self.idp = idp
        if sp is not None:
            self.sp = sp

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Saml2Sso`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Saml2Sso`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Saml2Sso`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Saml2Sso`".format(key))
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
        if issubclass(Saml2Sso, dict):
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
        if not isinstance(other, Saml2Sso):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

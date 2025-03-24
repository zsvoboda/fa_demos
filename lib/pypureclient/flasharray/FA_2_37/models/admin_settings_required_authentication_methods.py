# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_37 import models

class AdminSettingsRequiredAuthenticationMethods(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ssh': 'list[str]',
        'web_ui': 'list[str]'
    }

    attribute_map = {
        'ssh': 'ssh',
        'web_ui': 'web_ui'
    }

    required_args = {
    }

    def __init__(
        self,
        ssh=None,  # type: List[str]
        web_ui=None,  # type: List[str]
    ):
        """
        Keyword args:
            ssh (list[str]): List of authentication methods that are required for SSH. Possible values include `password`, `key`, and `default`. `securid-am` is a possible value, but it cannot be changed through PATCH. If not specified, defaults to `default`. Specify `password` and `key` authentication methods to set up local multi-factor authentication for SSH. 
            web_ui (list[str]): List of authentication methods that are required for the web UI. Possible values include `password`, `webauthn`, and `default`. Other possible values include `saml2` and `securid-am` but these cannot be changed through PATCH. If not specified, defaults to `default`. Specify `password` and `webauthn` authentication methods to set up local multi-factor authentication for web UI. External multi-factor authentication is configured through SAML2 SSO endpoints. 
        """
        if ssh is not None:
            self.ssh = ssh
        if web_ui is not None:
            self.web_ui = web_ui

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AdminSettingsRequiredAuthenticationMethods`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AdminSettingsRequiredAuthenticationMethods`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AdminSettingsRequiredAuthenticationMethods`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AdminSettingsRequiredAuthenticationMethods`".format(key))
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
        if issubclass(AdminSettingsRequiredAuthenticationMethods, dict):
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
        if not isinstance(other, AdminSettingsRequiredAuthenticationMethods):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

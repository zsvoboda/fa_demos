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

class SmtpServer(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'body_prefix': 'str',
        'encryption_mode': 'str',
        'password': 'str',
        'relay_host': 'str',
        'sender_domain': 'str',
        'sender_username': 'str',
        'subject_prefix': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'body_prefix': 'body_prefix',
        'encryption_mode': 'encryption_mode',
        'password': 'password',
        'relay_host': 'relay_host',
        'sender_domain': 'sender_domain',
        'sender_username': 'sender_username',
        'subject_prefix': 'subject_prefix',
        'user_name': 'user_name'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        body_prefix=None,  # type: str
        encryption_mode=None,  # type: str
        password=None,  # type: str
        relay_host=None,  # type: str
        sender_domain=None,  # type: str
        sender_username=None,  # type: str
        subject_prefix=None,  # type: str
        user_name=None,  # type: str
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            body_prefix (str): Optional string added to the beginning of the email body when sending alert email messages. HTML tags are not allowed. 
            encryption_mode (str): Enforces an encryption mode when sending alert email messages. Valid values are `starttls`. Use \"\" to clear. 
            password (str): Password for the relay host, if needed. 
            relay_host (str): Relay server used as a forwarding point for email sent from the array. Can be set as a hostname, IPv4 address, or IPv6 address, with optional port numbers. The expected format for IPv4 is `ddd.ddd.ddd.ddd:PORT`. The expected format for IPv6 is `xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx` or, if a port number is specified, `[xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx]:PORT`. 
            sender_domain (str): Domain name appended to alert email messages. 
            sender_username (str): The local-part of the email address used when sending alert email messages. 
            subject_prefix (str): Optional string added to the beginning of the subject when sending alert email messages. HTML tags are not allowed. 
            user_name (str): User name for the relay host, if needed. 
        """
        if name is not None:
            self.name = name
        if body_prefix is not None:
            self.body_prefix = body_prefix
        if encryption_mode is not None:
            self.encryption_mode = encryption_mode
        if password is not None:
            self.password = password
        if relay_host is not None:
            self.relay_host = relay_host
        if sender_domain is not None:
            self.sender_domain = sender_domain
        if sender_username is not None:
            self.sender_username = sender_username
        if subject_prefix is not None:
            self.subject_prefix = subject_prefix
        if user_name is not None:
            self.user_name = user_name

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SmtpServer`".format(key))
        if key == "body_prefix" and value is not None:
            if len(value) > 256:
                raise ValueError("Invalid value for `body_prefix`, length must be less than or equal to `256`")
        if key == "subject_prefix" and value is not None:
            if len(value) > 64:
                raise ValueError("Invalid value for `subject_prefix`, length must be less than or equal to `64`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SmtpServer`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SmtpServer`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SmtpServer`".format(key))
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
        if issubclass(SmtpServer, dict):
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
        if not isinstance(other, SmtpServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

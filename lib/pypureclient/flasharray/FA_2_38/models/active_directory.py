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

class ActiveDirectory(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'computer_name': 'str',
        'directory_servers': 'list[str]',
        'domain': 'str',
        'kerberos_servers': 'list[str]',
        'tls': 'str'
    }

    attribute_map = {
        'name': 'name',
        'computer_name': 'computer_name',
        'directory_servers': 'directory_servers',
        'domain': 'domain',
        'kerberos_servers': 'kerberos_servers',
        'tls': 'tls'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        computer_name=None,  # type: str
        directory_servers=None,  # type: List[str]
        domain=None,  # type: str
        kerberos_servers=None,  # type: List[str]
        tls=None,  # type: str
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            computer_name (str): The name of the computer account in the Active Directory domain. 
            directory_servers (list[str]): A list of directory servers used for lookups related to user authorization. Servers must be specified in FQDN format. All specified servers must be registered to the domain appropriately in the configured DNS of the array and are only communicated with over the secure LDAP (LDAPS) protocol. If this field is `null`, the servers are resolved for the domain in DNS. 
            domain (str): The Active Directory domain joined.
            kerberos_servers (list[str]): A list of key distribution servers to use for Kerberos protocol. Servers must be specified in FQDN format. All specified servers must be registered to the domain appropriately in the configured DNS of the array. If this field is `null`, the servers are resolved for the domain in DNS. 
            tls (str): TLS mode for communication with domain controllers. Valid values are `required` and `optional`. `required` forces TLS communication with a domain controller. `optional` allows the use of non-TLS communication, TLS will still be preferred, if available. If not specified, defaults to `required`. 
        """
        if name is not None:
            self.name = name
        if computer_name is not None:
            self.computer_name = computer_name
        if directory_servers is not None:
            self.directory_servers = directory_servers
        if domain is not None:
            self.domain = domain
        if kerberos_servers is not None:
            self.kerberos_servers = kerberos_servers
        if tls is not None:
            self.tls = tls

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectory`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectory`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectory`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectory`".format(key))
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
        if issubclass(ActiveDirectory, dict):
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
        if not isinstance(other, ActiveDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

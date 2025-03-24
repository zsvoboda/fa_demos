# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_7 import models

class Port(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'iqn': 'str',
        'nqn': 'str',
        'portal': 'str',
        'wwn': 'str',
        'failover': 'str'
    }

    attribute_map = {
        'name': 'name',
        'iqn': 'iqn',
        'nqn': 'nqn',
        'portal': 'portal',
        'wwn': 'wwn',
        'failover': 'failover'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        iqn=None,  # type: str
        nqn=None,  # type: str
        portal=None,  # type: str
        wwn=None,  # type: str
        failover=None,  # type: str
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            iqn (str): The iSCSI Qualified Name (or `null` if target is not iSCSI).
            nqn (str): NVMe Qualified Name (or `null` if target is not NVMeoF).
            portal (str): IP and port number (or `null` if target is not iSCSI).
            wwn (str): Fibre Channel World Wide Name (or `null` if target is not Fibre Channel). 
            failover (str): If the array port has failed over, returns the name of the port to which this port has failed over. 
        """
        if name is not None:
            self.name = name
        if iqn is not None:
            self.iqn = iqn
        if nqn is not None:
            self.nqn = nqn
        if portal is not None:
            self.portal = portal
        if wwn is not None:
            self.wwn = wwn
        if failover is not None:
            self.failover = failover

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Port`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Port`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Port`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Port`".format(key))
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
        if issubclass(Port, dict):
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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

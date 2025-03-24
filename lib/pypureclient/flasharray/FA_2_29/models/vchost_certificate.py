# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_29 import models

class VchostCertificate(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'certificate': 'ReferenceNoIdWithType',
        'endpoints': 'list[str]',
        'id': 'str',
        'vchost': 'ReferenceWithType'
    }

    attribute_map = {
        'certificate': 'certificate',
        'endpoints': 'endpoints',
        'id': 'id',
        'vchost': 'vchost'
    }

    required_args = {
    }

    def __init__(
        self,
        certificate=None,  # type: models.ReferenceNoIdWithType
        endpoints=None,  # type: List[str]
        id=None,  # type: str
        vchost=None,  # type: models.ReferenceWithType
    ):
        """
        Keyword args:
            certificate (ReferenceNoIdWithType): A reference to the certificate that will be presented to clients accessing the referenced `vchost` using any of the network addresses defined by `endpoints`. 
            endpoints (list[str]): The IPv4 or IPv6 addresses of the endpoints to configure for the vchost, over which the configured certificate will be presented. 
            id (str): A globally unique, system-generated ID. The ID cannot be modified. 
            vchost (ReferenceWithType): The vchost by which the certificate is to be presented over the configured endpoints. 
        """
        if certificate is not None:
            self.certificate = certificate
        if endpoints is not None:
            self.endpoints = endpoints
        if id is not None:
            self.id = id
        if vchost is not None:
            self.vchost = vchost

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostCertificate`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostCertificate`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostCertificate`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostCertificate`".format(key))
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
        if issubclass(VchostCertificate, dict):
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
        if not isinstance(other, VchostCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

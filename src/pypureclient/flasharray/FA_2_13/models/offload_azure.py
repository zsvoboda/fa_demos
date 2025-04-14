# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_13 import models

class OffloadAzure(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_name': 'str',
        'container_name': 'str',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'container_name': 'container_name',
        'secret_access_key': 'secret_access_key'
    }

    required_args = {
    }

    def __init__(
        self,
        account_name=None,  # type: str
        container_name=None,  # type: str
        secret_access_key=None,  # type: str
    ):
        """
        Keyword args:
            account_name (str): The name of the existing Azure Blob storage account. 
            container_name (str): The name of the container in the Azure Blob storage account to where the data will be offloaded. The name must be a valid DNS name. If not specified, defaults to `offload`. 
            secret_access_key (str): The secret access key that goes with the account name (`account_name`) of the Azure Blob storage account. The secret access key is only accepted when creating the connection between the array and the Azure Blob storage account. The `account_name` and `container_name`, and `secret_access_key` parameters must be set together. 
        """
        if account_name is not None:
            self.account_name = account_name
        if container_name is not None:
            self.container_name = container_name
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadAzure`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadAzure`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadAzure`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OffloadAzure`".format(key))
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
        if issubclass(OffloadAzure, dict):
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
        if not isinstance(other, OffloadAzure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

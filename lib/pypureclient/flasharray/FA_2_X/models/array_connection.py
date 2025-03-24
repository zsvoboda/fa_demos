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

class ArrayConnection(object):
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
        'context': 'FixedReference',
        'encryption': 'str',
        'encryption_mode': 'str',
        'management_address': 'str',
        'os': 'str',
        'remote': 'ReferenceWithType',
        'replication_addresses': 'list[str]',
        'replication_transport': 'str',
        'status': 'str',
        'throttle': 'Throttle',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'context': 'context',
        'encryption': 'encryption',
        'encryption_mode': 'encryption_mode',
        'management_address': 'management_address',
        'os': 'os',
        'remote': 'remote',
        'replication_addresses': 'replication_addresses',
        'replication_transport': 'replication_transport',
        'status': 'status',
        'throttle': 'throttle',
        'type': 'type',
        'version': 'version'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        context=None,  # type: models.FixedReference
        encryption=None,  # type: str
        encryption_mode=None,  # type: str
        management_address=None,  # type: str
        os=None,  # type: str
        remote=None,  # type: models.ReferenceWithType
        replication_addresses=None,  # type: List[str]
        replication_transport=None,  # type: str
        status=None,  # type: str
        throttle=None,  # type: models.Throttle
        type=None,  # type: str
        version=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource. 
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            encryption (str): If `encrypted`, all traffic over this array connection will be encrypted. If `unencrypted`, all traffic over this array connection will be unencrypted. 
            encryption_mode (str): Cryptographic protocol, trust model, and encryption algorithm information. Will be `null` if `encrypted` is `false`. 
            management_address (str): Management IP address or FQDN of the target array. 
            os (str): The operating system of the connected array. 
            remote (ReferenceWithType): The remote array. 
            replication_addresses (list[str]): IP addresses of the target arrays when `replication_transport` is `ip`. WWNs of the target arrays when `replication_transport` is `fc`. 
            replication_transport (str): The protocol used to transport data between the local array and the remote array. Valid values are `ip` and `fc`. The default value is `ip`. 
            status (str): Status of the connection. Valid values include `connected`, `connecting`, `partially_connected`, and `unbalanced`. A status of `connected` indicates that arrays are communicating. A status of `connecting` indicates that the array is trying to establish a connection. A status of `partially_connected` indicates that some replication addresses are communicating but others are not. A status of `unbalanced` indicates that the arrays are communicating, but the set of paths is either not redundant or not symmetrical. 
            throttle (Throttle)
            type (str): The type of connection. Valid values include `async-replication`, `sync-replication`, and `fleet-management`. 
            version (str): The Purity version on the target array.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if encryption is not None:
            self.encryption = encryption
        if encryption_mode is not None:
            self.encryption_mode = encryption_mode
        if management_address is not None:
            self.management_address = management_address
        if os is not None:
            self.os = os
        if remote is not None:
            self.remote = remote
        if replication_addresses is not None:
            self.replication_addresses = replication_addresses
        if replication_transport is not None:
            self.replication_transport = replication_transport
        if status is not None:
            self.status = status
        if throttle is not None:
            self.throttle = throttle
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnection`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnection`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnection`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnection`".format(key))
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
        if issubclass(ArrayConnection, dict):
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
        if not isinstance(other, ArrayConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

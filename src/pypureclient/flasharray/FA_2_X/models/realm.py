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

class Realm(object):
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
        'context': 'FixedReferenceWithType',
        'created': 'int',
        'destroyed': 'bool',
        'eradication_config': 'ContainerEradicationConfig',
        'qos': 'ContainerQos',
        'quota_limit': 'int',
        'space': 'SpaceNoDeprecatedPhysicalOrEffective',
        'time_remaining': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'context': 'context',
        'created': 'created',
        'destroyed': 'destroyed',
        'eradication_config': 'eradication_config',
        'qos': 'qos',
        'quota_limit': 'quota_limit',
        'space': 'space',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        context=None,  # type: models.FixedReferenceWithType
        created=None,  # type: int
        destroyed=None,  # type: bool
        eradication_config=None,  # type: models.ContainerEradicationConfig
        qos=None,  # type: models.ContainerQos
        quota_limit=None,  # type: int
        space=None,  # type: models.SpaceNoDeprecatedPhysicalOrEffective
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource. 
            name (str): A user-specified name. The name must be locally unique and can be changed. 
            context (FixedReferenceWithType): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            created (int): Creation timestamp of the realm.
            destroyed (bool): Returns a value of `true` if the realm has been destroyed and is pending eradication. The realm cannot be modified while it is in the destroyed state. The `time_remaining` value displays the amount of time left until the destroyed realm is permanently eradicated. Once eradication has begun, the realm can no longer be recovered. Before the `time_remaining` period has elapsed, the destroyed realm can be recovered through the PATCH method. 
            eradication_config (ContainerEradicationConfig)
            qos (ContainerQos): Displays QoS limit information. 
            quota_limit (int): The logical quota limit of the realm, measured in bytes. 
            space (SpaceNoDeprecatedPhysicalOrEffective): Displays provisioned size and physical storage consumption information for the realm. 
            time_remaining (int): Time in milliseconds before the realm is eradicated. The value is `null` if not destroyed. 
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if eradication_config is not None:
            self.eradication_config = eradication_config
        if qos is not None:
            self.qos = qos
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if space is not None:
            self.space = space
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Realm`".format(key))
        if key == "quota_limit" and value is not None:
            if value > 4503599627370496:
                raise ValueError("Invalid value for `quota_limit`, value must be less than or equal to `4503599627370496`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Realm`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Realm`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Realm`".format(key))
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
        if issubclass(Realm, dict):
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
        if not isinstance(other, Realm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

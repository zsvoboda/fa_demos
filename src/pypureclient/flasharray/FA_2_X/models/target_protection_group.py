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

class TargetProtectionGroup(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'FixedReferenceWithType',
        'allowed': 'bool',
        'group': 'Reference',
        'member': 'ReferenceWithType',
        'status': 'str'
    }

    attribute_map = {
        'context': 'context',
        'allowed': 'allowed',
        'group': 'group',
        'member': 'member',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        context=None,  # type: models.FixedReferenceWithType
        allowed=None,  # type: bool
        group=None,  # type: models.Reference
        member=None,  # type: models.ReferenceWithType
        status=None,  # type: str
    ):
        """
        Keyword args:
            context (FixedReferenceWithType): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            allowed (bool): If set to `true`, the target array or pod allows the source array to replicate protection group data to the target. If set to `false`, the target array or pod does not allow the source array to replicate protection group data to the target. 
            group (Reference)
            member (ReferenceWithType)
            status (str): The replication status of the target. Valid values are `replicating`, `suspended`, and `disallowed`. If `allowed` is `true` and protection group data is replicating to the target, `status` will display `replicating`. If `allowed` is `true`, but replication is suspended due to the target being demoted, linked, stretched, etc., `status` will display `suspended`. Replication will be automatically resumed if the target becomes promoted or local only again. If `allowed` is `false`, `status` will display `disallowed`. 
        """
        if context is not None:
            self.context = context
        if allowed is not None:
            self.allowed = allowed
        if group is not None:
            self.group = group
        if member is not None:
            self.member = member
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `TargetProtectionGroup`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `TargetProtectionGroup`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `TargetProtectionGroup`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `TargetProtectionGroup`".format(key))
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
        if issubclass(TargetProtectionGroup, dict):
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
        if not isinstance(other, TargetProtectionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

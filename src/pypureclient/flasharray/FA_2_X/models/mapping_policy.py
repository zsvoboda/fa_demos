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

class MappingPolicy(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'context': 'FixedReferenceWithType',
        'direction': 'str',
        'local_policy': 'ReferenceWithType',
        'mapping': 'str',
        'pod_replica_link': 'PodReplicaLinkReference',
        'policy_type': 'str',
        'remote_policy': 'ReferenceWithType'
    }

    attribute_map = {
        'id': 'id',
        'context': 'context',
        'direction': 'direction',
        'local_policy': 'local_policy',
        'mapping': 'mapping',
        'pod_replica_link': 'pod_replica_link',
        'policy_type': 'policy_type',
        'remote_policy': 'remote_policy'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        context=None,  # type: models.FixedReferenceWithType
        direction=None,  # type: str
        local_policy=None,  # type: models.ReferenceWithType
        mapping=None,  # type: str
        pod_replica_link=None,  # type: models.PodReplicaLinkReference
        policy_type=None,  # type: str
        remote_policy=None,  # type: models.ReferenceWithType
    ):
        """
        Keyword args:
            id (str): A non-modifiable, globally unique ID chosen by the system. 
            context (FixedReferenceWithType): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            direction (str): The direction of replication. Valid values include `inbound` and `outbound`. 
            local_policy (ReferenceWithType): Reference to a local policy. 
            mapping (str): The mapping for this policy mapping. Valid values are `connected` and `disconnected`. 
            pod_replica_link (PodReplicaLinkReference): Reference to a pod replica link. 
            policy_type (str): The type of policies involved in this policy mapping. 
            remote_policy (ReferenceWithType): Reference to a remote policy. 
        """
        if id is not None:
            self.id = id
        if context is not None:
            self.context = context
        if direction is not None:
            self.direction = direction
        if local_policy is not None:
            self.local_policy = local_policy
        if mapping is not None:
            self.mapping = mapping
        if pod_replica_link is not None:
            self.pod_replica_link = pod_replica_link
        if policy_type is not None:
            self.policy_type = policy_type
        if remote_policy is not None:
            self.remote_policy = remote_policy

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `MappingPolicy`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `MappingPolicy`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `MappingPolicy`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `MappingPolicy`".format(key))
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
        if issubclass(MappingPolicy, dict):
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
        if not isinstance(other, MappingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

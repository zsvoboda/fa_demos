# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.31
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_31 import models

class PodPatch(object):
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
        'destroyed': 'bool',
        'failover_preferences': 'list[Reference]',
        'ignore_usage': 'bool',
        'mediator': 'str',
        'quota_limit': 'int',
        'requested_promotion_state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'destroyed': 'destroyed',
        'failover_preferences': 'failover_preferences',
        'ignore_usage': 'ignore_usage',
        'mediator': 'mediator',
        'quota_limit': 'quota_limit',
        'requested_promotion_state': 'requested_promotion_state'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        destroyed=None,  # type: bool
        failover_preferences=None,  # type: List[models.Reference]
        ignore_usage=None,  # type: bool
        mediator=None,  # type: str
        quota_limit=None,  # type: int
        requested_promotion_state=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource. 
            name (str): A user-specified name. The name must be locally unique and can be changed. 
            destroyed (bool): If set to `true`, the pod has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed pod is permanently eradicated. A pod can only be destroyed if it is empty, so before destroying a pod, ensure all volumes and protection groups inside the pod have been either moved out of the pod or destroyed. A stretched pod cannot be destroyed unless you unstretch it first. Before the `time_remaining` period has elapsed, the destroyed pod can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the pod is permanently eradicated and can no longer be recovered. 
            failover_preferences (list[Reference]): Determines which array within a stretched pod should be given priority to stay online should the arrays ever lose contact with each other. The current array and any peer arrays that are connected to the current array for synchronous replication can be added to a pod for failover preference. By default, `failover_preferences=null`, meaning no arrays have been configured for failover preference. Enter multiple arrays in comma-separated format. 
            ignore_usage (bool): Set to `true` to set a `quota_limit` that is lower than the existing usage. This ensures that no new volumes can be created until the existing usage drops below the `quota_limit`. If not specified, defaults to `false`. 
            mediator (str): Sets the URL of the mediator for this pod, replacing the URL of the current mediator. By default, the Pure1 Cloud Mediator (`purestorage`) serves as the mediator. 
            quota_limit (int): The logical quota limit of the pod, measured in bytes. Must be a multiple of 512. 
            requested_promotion_state (str): Patch `requested_promotion_state` to `demoted` to demote the pod so that it can be used as a link target for continuous replication between pods. Demoted pods do not accept write requests, and a destroyed version of the pod with `undo-demote` appended to the pod name is created on the array with the state of the pod when it was in the promoted state. Patch `requested_promotion_state` to `promoted` to start the process of promoting the pod. The `promotion_status` indicates when the pod has been successfully promoted. Promoted pods stop incorporating replicated data from the source pod and start accepting write requests. The replication process does not stop when the source pod continues replicating data to the pod. The space consumed by the unique replicated data is tracked by the `space.journal` field of the pod. 
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if destroyed is not None:
            self.destroyed = destroyed
        if failover_preferences is not None:
            self.failover_preferences = failover_preferences
        if ignore_usage is not None:
            self.ignore_usage = ignore_usage
        if mediator is not None:
            self.mediator = mediator
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if requested_promotion_state is not None:
            self.requested_promotion_state = requested_promotion_state

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodPatch`".format(key))
        if key == "quota_limit" and value is not None:
            if value > 4503599627370496:
                raise ValueError("Invalid value for `quota_limit`, value must be less than or equal to `4503599627370496`")
            if value < 1048576:
                raise ValueError("Invalid value for `quota_limit`, must be a value greater than or equal to `1048576`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodPatch`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodPatch`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodPatch`".format(key))
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
        if issubclass(PodPatch, dict):
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
        if not isinstance(other, PodPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

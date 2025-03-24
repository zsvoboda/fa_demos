# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.34
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_34 import models

class PodArrayStatus(object):
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
        'frozen_at': 'int',
        'mediator_status': 'str',
        'pre_elected': 'bool',
        'progress': 'float',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'frozen_at': 'frozen_at',
        'mediator_status': 'mediator_status',
        'pre_elected': 'pre_elected',
        'progress': 'progress',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        frozen_at=None,  # type: int
        mediator_status=None,  # type: str
        pre_elected=None,  # type: bool
        progress=None,  # type: float
        status=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified. 
            name (str): The resource name, such as volume name, pod name, snapshot name, and so on. 
            frozen_at (int): The timestamp of when the data on the pod was frozen when the array went offline. Measured in milliseconds since the UNIX epoch. Also known as the recovery point. If the pod is in sync, a value of `null` will be returned. 
            mediator_status (str): The status of the mediator, which determines whether it is available to mediate a high availability event. Valid values are `flummoxed`, `online`, `unknown`, and `unreachable`. Only mediators in the `online` status can mediate high availability events. If set to `flummoxed`, the array can reach a mediator, but it is talking to the wrong one. Verify that the DNS in the environment is properly configured. This status might also appear if the pod has been offline on one array for an extended period of time and the peer array is unreachable. If set to `online`, the array is successfully communicating with the mediator, and the mediator is available to mediate a high availability event. If set to `unreachable`, the array cannot reach the mediator, either due to network issues or because the mediator is down. When a mediator is unreachable, synchronous replication continues to function provided all arrays are healthy and communicating, but a high availability event without mediator access can result in an outage. 
            pre_elected (bool): If set to `true`, the array has been pre-elected to remain online in the rare event that the mediator is inaccessible on both arrays within the stretched pod, and then later, the arrays within the stretched pod become disconnected from each other. If set to `false`, either the array has been pre-elected to remain offline while its peer array remains online, or pre-election is not in effect. One and only one array within each pod is pre-elected at a given point in time, so while a pre-elected array is keeping the pod online, the pod on its non-elected peer array remains offline during the communication failure. Users cannot pre-elect arrays. 
            progress (float): The percentage progress of the pod resyncing process for this array. The percentage is displayed as a decimal value, starting at 0.00 and ending at 1.00. 
            status (str): The status of the array within the stretched pod. Valid values are `offline`, `online`, `resyncing`, `suspended`, and `unknown`. If set to `offline`, the array is experiencing problems and may not have the latest pod data. The array cannot handle I/O to the pod and cannot take over during a high availability event. If set to `online`, the array is online and has the latest pod data. The array can handle I/O to the pod and take over during a high availability event. If set to `suspended`, the array is experiencing a short connection glitch of the pod. This is a temporary status and would transition to either `online` or `offline` soon. `suspended` is a new status that is exposed, starting from version 6.6.0. If set to `resyncing`, the array is actively getting the latest pod data so that it becomes fully synchronized with its peer array. During the resyncing process, the array cannot handle I/O to the pod. Once the arrays are fully synchronized, the array changes to `online` status. If set to `unknown`, the status of the peer array is unknown because this array is offline and cannot determine the state of the pod on the peer array. Only the peer array can ever be in unknown status; this unknown status is unique to the local array and will differ when viewed from its peer array. 
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if frozen_at is not None:
            self.frozen_at = frozen_at
        if mediator_status is not None:
            self.mediator_status = mediator_status
        if pre_elected is not None:
            self.pre_elected = pre_elected
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
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
        if issubclass(PodArrayStatus, dict):
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
        if not isinstance(other, PodArrayStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

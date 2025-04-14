# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_41 import models

class PresetWorkloadPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'parameters': 'list[PresetWorkloadParameter]',
        'periodic_replication_configurations': 'list[PresetWorkloadPeriodicReplicationConfiguration]',
        'placement_configurations': 'list[PresetWorkloadPlacementConfiguration]',
        'qos_configurations': 'list[PresetWorkloadQosConfiguration]',
        'revision': 'int',
        'snapshot_configurations': 'list[PresetWorkloadSnapshotConfiguration]',
        'volume_configurations': 'list[PresetWorkloadVolumeConfiguration]',
        'workload_tags': 'list[PresetWorkloadWorkloadTag]',
        'workload_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'parameters': 'parameters',
        'periodic_replication_configurations': 'periodic_replication_configurations',
        'placement_configurations': 'placement_configurations',
        'qos_configurations': 'qos_configurations',
        'revision': 'revision',
        'snapshot_configurations': 'snapshot_configurations',
        'volume_configurations': 'volume_configurations',
        'workload_tags': 'workload_tags',
        'workload_type': 'workload_type'
    }

    required_args = {
        'placement_configurations',
        'volume_configurations',
        'workload_type',
    }

    def __init__(
        self,
        placement_configurations,  # type: List[models.PresetWorkloadPlacementConfiguration]
        volume_configurations,  # type: List[models.PresetWorkloadVolumeConfiguration]
        workload_type,  # type: str
        description=None,  # type: str
        parameters=None,  # type: List[models.PresetWorkloadParameter]
        periodic_replication_configurations=None,  # type: List[models.PresetWorkloadPeriodicReplicationConfiguration]
        qos_configurations=None,  # type: List[models.PresetWorkloadQosConfiguration]
        revision=None,  # type: int
        snapshot_configurations=None,  # type: List[models.PresetWorkloadSnapshotConfiguration]
        workload_tags=None,  # type: List[models.PresetWorkloadWorkloadTag]
    ):
        """
        Keyword args:
            description (str): A brief description of the workload the preset will configure. Supports up to 1KB of unicode characters. 
            parameters (list[PresetWorkloadParameter]): The parameters to prompt the user when they deploy workloads from the preset.
            periodic_replication_configurations (list[PresetWorkloadPeriodicReplicationConfiguration]): The periodic replication configurations that can be applied to storage resources (such as volumes) within the preset. 
            placement_configurations (list[PresetWorkloadPlacementConfiguration], required): The placement configurations that can be applied to storage resources (such as volumes) within the preset. All storage resources associated with the same placement will be colocated on the same array. 
            qos_configurations (list[PresetWorkloadQosConfiguration]): The QoS configurations that can be applied to storage resources (such as volumes) within the preset. 
            revision (int): A counter that is automatically incremented by the server when the preset is updated. 
            snapshot_configurations (list[PresetWorkloadSnapshotConfiguration]): The snapshot configurations that can be applied to storage resources (such as volumes) within the preset. 
            volume_configurations (list[PresetWorkloadVolumeConfiguration], required): The volumes that will be provisioned by the preset. 
            workload_tags (list[PresetWorkloadWorkloadTag]): The tags that will be associated with workloads provisioned by the preset.
            workload_type (str, required): The type of workload the preset will configure. Valid values include `VDI`, `File`, `MySQL` etc. 
        """
        if description is not None:
            self.description = description
        if parameters is not None:
            self.parameters = parameters
        if periodic_replication_configurations is not None:
            self.periodic_replication_configurations = periodic_replication_configurations
        self.placement_configurations = placement_configurations
        if qos_configurations is not None:
            self.qos_configurations = qos_configurations
        if revision is not None:
            self.revision = revision
        if snapshot_configurations is not None:
            self.snapshot_configurations = snapshot_configurations
        self.volume_configurations = volume_configurations
        if workload_tags is not None:
            self.workload_tags = workload_tags
        self.workload_type = workload_type

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPost`".format(key))
        if key == "placement_configurations" and value is None:
            raise ValueError("Invalid value for `placement_configurations`, must not be `None`")
        if key == "volume_configurations" and value is None:
            raise ValueError("Invalid value for `volume_configurations`, must not be `None`")
        if key == "workload_type" and value is None:
            raise ValueError("Invalid value for `workload_type`, must not be `None`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PresetWorkloadPost`".format(key))
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
        if issubclass(PresetWorkloadPost, dict):
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
        if not isinstance(other, PresetWorkloadPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

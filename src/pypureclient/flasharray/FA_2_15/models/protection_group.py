# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_15 import models

class ProtectionGroup(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'destroyed': 'bool',
        'eradication_config': 'ProtectionGroupEradicationConfig',
        'host_count': 'int',
        'host_group_count': 'int',
        'is_local': 'bool',
        'pod': 'FixedReference',
        'replication_schedule': 'ReplicationSchedule',
        'retention_lock': 'str',
        'snapshot_schedule': 'SnapshotSchedule',
        'source': 'FixedReference',
        'source_retention': 'RetentionPolicy',
        'space': 'Space',
        'target_count': 'int',
        'target_retention': 'RetentionPolicy',
        'time_remaining': 'int',
        'volume_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'destroyed': 'destroyed',
        'eradication_config': 'eradication_config',
        'host_count': 'host_count',
        'host_group_count': 'host_group_count',
        'is_local': 'is_local',
        'pod': 'pod',
        'replication_schedule': 'replication_schedule',
        'retention_lock': 'retention_lock',
        'snapshot_schedule': 'snapshot_schedule',
        'source': 'source',
        'source_retention': 'source_retention',
        'space': 'space',
        'target_count': 'target_count',
        'target_retention': 'target_retention',
        'time_remaining': 'time_remaining',
        'volume_count': 'volume_count'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        destroyed=None,  # type: bool
        eradication_config=None,  # type: models.ProtectionGroupEradicationConfig
        host_count=None,  # type: int
        host_group_count=None,  # type: int
        is_local=None,  # type: bool
        pod=None,  # type: models.FixedReference
        replication_schedule=None,  # type: models.ReplicationSchedule
        retention_lock=None,  # type: str
        snapshot_schedule=None,  # type: models.SnapshotSchedule
        source=None,  # type: models.FixedReference
        source_retention=None,  # type: models.RetentionPolicy
        space=None,  # type: models.Space
        target_count=None,  # type: int
        target_retention=None,  # type: models.RetentionPolicy
        time_remaining=None,  # type: int
        volume_count=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and can be changed. 
            destroyed (bool): Has this protection group been destroyed? To destroy a protection group, patch to `true`. To recover a destroyed protection group, patch to `false`. If not specified, defaults to `false`. 
            eradication_config (ProtectionGroupEradicationConfig)
            host_count (int): Number of hosts in this protection group.
            host_group_count (int): Number of host groups in this protection group.
            is_local (bool): If set to `true`, the protection group belongs to the local array. If set to `false`, the protection group belongs to the remote array. 
            pod (FixedReference): The pod in which the protection group resides.
            replication_schedule (ReplicationSchedule): The schedule settings for asynchronous replication.
            retention_lock (str): The valid values are `ratcheted` and `unlocked`. The default value for a newly created protection group is `unlocked`. Set `retention_lock` to `ratcheted` to enable SafeMode restrictions on the protection group. Contact Pure Technical Services to change `retention_lock` to `unlocked`. 
            snapshot_schedule (SnapshotSchedule): The schedule settings for protection group snapshots.
            source (FixedReference): The array or pod on which the protection group was created.
            source_retention (RetentionPolicy): The retention policy for the source array of the protection group. 
            space (Space): Returns provisioned size and physical storage consumption data for each protection group. 
            target_count (int): The number of targets to where this protection group replicates.
            target_retention (RetentionPolicy): The retention policy for the target(s) of the protection group. 
            time_remaining (int): The amount of time left until the destroyed protection group is permanently eradicated. Measured in milliseconds. Before the `time_remaining` period has elapsed, the destroyed protection group can be recovered by setting `destroyed=false`. 
            volume_count (int): The number of volumes in the protection group.
        """
        if name is not None:
            self.name = name
        if destroyed is not None:
            self.destroyed = destroyed
        if eradication_config is not None:
            self.eradication_config = eradication_config
        if host_count is not None:
            self.host_count = host_count
        if host_group_count is not None:
            self.host_group_count = host_group_count
        if is_local is not None:
            self.is_local = is_local
        if pod is not None:
            self.pod = pod
        if replication_schedule is not None:
            self.replication_schedule = replication_schedule
        if retention_lock is not None:
            self.retention_lock = retention_lock
        if snapshot_schedule is not None:
            self.snapshot_schedule = snapshot_schedule
        if source is not None:
            self.source = source
        if source_retention is not None:
            self.source_retention = source_retention
        if space is not None:
            self.space = space
        if target_count is not None:
            self.target_count = target_count
        if target_retention is not None:
            self.target_retention = target_retention
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if volume_count is not None:
            self.volume_count = volume_count

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroup`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroup`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroup`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroup`".format(key))
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
        if issubclass(ProtectionGroup, dict):
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
        if not isinstance(other, ProtectionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

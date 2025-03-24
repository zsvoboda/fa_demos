# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_37 import models

class Host(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'chap': 'Chap',
        'connection_count': 'int',
        'destroyed': 'bool',
        'host_group': 'ReferenceNoId',
        'iqns': 'list[str]',
        'is_local': 'bool',
        'nqns': 'list[str]',
        'personality': 'str',
        'port_connectivity': 'HostPortConnectivity',
        'preferred_arrays': 'list[Reference]',
        'space': 'Space',
        'time_remaining': 'int',
        'vlan': 'str',
        'wwns': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'chap': 'chap',
        'connection_count': 'connection_count',
        'destroyed': 'destroyed',
        'host_group': 'host_group',
        'iqns': 'iqns',
        'is_local': 'is_local',
        'nqns': 'nqns',
        'personality': 'personality',
        'port_connectivity': 'port_connectivity',
        'preferred_arrays': 'preferred_arrays',
        'space': 'space',
        'time_remaining': 'time_remaining',
        'vlan': 'vlan',
        'wwns': 'wwns'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        chap=None,  # type: models.Chap
        connection_count=None,  # type: int
        destroyed=None,  # type: bool
        host_group=None,  # type: models.ReferenceNoId
        iqns=None,  # type: List[str]
        is_local=None,  # type: bool
        nqns=None,  # type: List[str]
        personality=None,  # type: str
        port_connectivity=None,  # type: models.HostPortConnectivity
        preferred_arrays=None,  # type: List[models.Reference]
        space=None,  # type: models.Space
        time_remaining=None,  # type: int
        vlan=None,  # type: str
        wwns=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and can be changed. 
            chap (Chap)
            connection_count (int): The number of volumes connected to the specified host.
            destroyed (bool): Returns a value of `true` if the host has been destroyed with its container realm and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed host is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed host will be recovered if its container realm is recovered. Once the `time_remaining` period has elapsed, the host is permanently eradicated and can no longer be recovered. 
            host_group (ReferenceNoId): The host group to which the host should be associated.
            iqns (list[str]): The iSCSI qualified name (IQN) associated with the host. 
            is_local (bool): -> If set to `true`, the location reference is to the local array. If set to `false`, the location reference is to a remote location, such as a remote array or offload target.
            nqns (list[str]): The NVMe Qualified Name (NQN) associated with the host.
            personality (str): Determines how the system tunes the array to ensure that it works optimally with the host. Set `personality` to the name of the host operating system or virtual memory system. Valid values are `aix`, `esxi`, `hitachi-vsp`, `hpux`, `oracle-vm-server`, `solaris`, and `vms`. If your system is not listed as one of the valid host personalities, do not set the option. By default, the personality is not set. 
            port_connectivity (HostPortConnectivity)
            preferred_arrays (list[Reference]): For synchronous replication configurations, sets a host's preferred array to specify which array exposes active/optimized paths to that host. Enter multiple preferred arrays in comma-separated format. If a preferred array is set for a host, then the other arrays in the same pod will expose active/non-optimized paths to that host. If the host is in a host group, `preferred_arrays` cannot be set because host groups have their own preferred arrays. On a preferred array of a certain host, all the paths on all the ports (for both the primary and secondary controllers) are set up as A/O (active/optimized) paths, while on a non-preferred array, all the paths are A/N (Active/Non-optimized) paths. 
            space (Space): Displays provisioned (virtual) size and physical storage consumption information for the sum of all volumes connected to the specified host. 
            time_remaining (int): The amount of time left until the destroyed host is permanently eradicated, measured in milliseconds. 
            vlan (str): The VLAN ID that the host is associated with. If set to `any`, the host can access any VLAN. If set to `untagged`, the host can only access untagged VLANs. If set to a number between `1` and `4094`, the host can only access the specified VLAN with that number. 
            wwns (list[str]): The Fibre Channel World Wide Name (WWN) associated with the host.
        """
        if name is not None:
            self.name = name
        if chap is not None:
            self.chap = chap
        if connection_count is not None:
            self.connection_count = connection_count
        if destroyed is not None:
            self.destroyed = destroyed
        if host_group is not None:
            self.host_group = host_group
        if iqns is not None:
            self.iqns = iqns
        if is_local is not None:
            self.is_local = is_local
        if nqns is not None:
            self.nqns = nqns
        if personality is not None:
            self.personality = personality
        if port_connectivity is not None:
            self.port_connectivity = port_connectivity
        if preferred_arrays is not None:
            self.preferred_arrays = preferred_arrays
        if space is not None:
            self.space = space
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if vlan is not None:
            self.vlan = vlan
        if wwns is not None:
            self.wwns = wwns

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Host`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Host`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Host`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Host`".format(key))
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
        if issubclass(Host, dict):
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
        if not isinstance(other, Host):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

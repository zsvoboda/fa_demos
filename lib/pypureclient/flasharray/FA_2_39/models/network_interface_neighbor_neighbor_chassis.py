# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_39 import models

class NetworkInterfaceNeighborNeighborChassis(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'addresses': 'list[str]',
        'bridge': 'NetworkInterfaceNeighborCapability',
        'description': 'str',
        'docsis_cable_device': 'NetworkInterfaceNeighborCapability',
        'id': 'NetworkInterfaceNeighborNeighborChassisId',
        'name': 'str',
        'repeater': 'NetworkInterfaceNeighborCapability',
        'router': 'NetworkInterfaceNeighborCapability',
        'station_only': 'NetworkInterfaceNeighborCapability',
        'telephone': 'NetworkInterfaceNeighborCapability',
        'wlan_access_point': 'NetworkInterfaceNeighborCapability'
    }

    attribute_map = {
        'addresses': 'addresses',
        'bridge': 'bridge',
        'description': 'description',
        'docsis_cable_device': 'docsis_cable_device',
        'id': 'id',
        'name': 'name',
        'repeater': 'repeater',
        'router': 'router',
        'station_only': 'station_only',
        'telephone': 'telephone',
        'wlan_access_point': 'wlan_access_point'
    }

    required_args = {
    }

    def __init__(
        self,
        addresses=None,  # type: List[str]
        bridge=None,  # type: models.NetworkInterfaceNeighborCapability
        description=None,  # type: str
        docsis_cable_device=None,  # type: models.NetworkInterfaceNeighborCapability
        id=None,  # type: models.NetworkInterfaceNeighborNeighborChassisId
        name=None,  # type: str
        repeater=None,  # type: models.NetworkInterfaceNeighborCapability
        router=None,  # type: models.NetworkInterfaceNeighborCapability
        station_only=None,  # type: models.NetworkInterfaceNeighborCapability
        telephone=None,  # type: models.NetworkInterfaceNeighborCapability
        wlan_access_point=None,  # type: models.NetworkInterfaceNeighborCapability
    ):
        """
        Keyword args:
            addresses (list[str]): Management IP addresses of the neighbor.
            bridge (NetworkInterfaceNeighborCapability): Bridge capability of the neighbor system.
            description (str): The textual description of the neighbor. The description may include the full name and version identification of the system hardware type, software operating system, and networking software. 
            docsis_cable_device (NetworkInterfaceNeighborCapability): DOCSIS cable device capability of the neighbor system.
            id (NetworkInterfaceNeighborNeighborChassisId)
            name (str): Administratively assigned name of the neighbour.
            repeater (NetworkInterfaceNeighborCapability): Neighbor system's repeater capability.
            router (NetworkInterfaceNeighborCapability): IP router capability of the neighbor system.
            station_only (NetworkInterfaceNeighborCapability): Station only status of the neighbor system.
            telephone (NetworkInterfaceNeighborCapability): Telephone capability of the neighbor system.
            wlan_access_point (NetworkInterfaceNeighborCapability): WLAN access point capability of the neighbor system.
        """
        if addresses is not None:
            self.addresses = addresses
        if bridge is not None:
            self.bridge = bridge
        if description is not None:
            self.description = description
        if docsis_cable_device is not None:
            self.docsis_cable_device = docsis_cable_device
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if repeater is not None:
            self.repeater = repeater
        if router is not None:
            self.router = router
        if station_only is not None:
            self.station_only = station_only
        if telephone is not None:
            self.telephone = telephone
        if wlan_access_point is not None:
            self.wlan_access_point = wlan_access_point

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighborNeighborChassis`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighborNeighborChassis`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighborNeighborChassis`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighborNeighborChassis`".format(key))
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
        if issubclass(NetworkInterfaceNeighborNeighborChassis, dict):
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
        if not isinstance(other, NetworkInterfaceNeighborNeighborChassis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class Hardware(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'details': 'str',
        'identify_enabled': 'bool',
        'index': 'int',
        'model': 'str',
        'serial': 'str',
        'slot': 'int',
        'speed': 'int',
        'status': 'str',
        'temperature': 'int',
        'type': 'str',
        'voltage': 'int'
    }

    attribute_map = {
        'name': 'name',
        'details': 'details',
        'identify_enabled': 'identify_enabled',
        'index': 'index',
        'model': 'model',
        'serial': 'serial',
        'slot': 'slot',
        'speed': 'speed',
        'status': 'status',
        'temperature': 'temperature',
        'type': 'type',
        'voltage': 'voltage'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        details=None,  # type: str
        identify_enabled=None,  # type: bool
        index=None,  # type: int
        model=None,  # type: str
        serial=None,  # type: str
        slot=None,  # type: int
        speed=None,  # type: int
        status=None,  # type: str
        temperature=None,  # type: int
        type=None,  # type: str
        voltage=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            details (str): Details about the status of the component if not healthy. 
            identify_enabled (bool): If `true`, the ID LED is lit to visually identify the component. 
            index (int): Number that identifies the relative position of a hardware component within the array. 
            model (str): Model number of the hardware component. 
            serial (str): Serial number of the hardware component. 
            slot (int): Slot number occupied by the PCI Express card that hosts the component. 
            speed (int): Speed (in bytes per second) at which the component is operating. 
            status (str): Component status. Values include `critical`, `healthy`, `identifying`, `unhealthy`, `unknown`, and `unused`. 
            temperature (int): Temperature (in degrees Celsius) reported by the component. 
            type (str): Type of hardware component. Values include `bay`, `ct`, `ch`, `eth`, `fan`, `fb`, `fc`, `fm`, `ib`, `iom`, `nvb`, `pwr`, `sas`, `sh`, and `tmp`. 
            voltage (int): Voltage (in Volts) reported by the component. 
        """
        if name is not None:
            self.name = name
        if details is not None:
            self.details = details
        if identify_enabled is not None:
            self.identify_enabled = identify_enabled
        if index is not None:
            self.index = index
        if model is not None:
            self.model = model
        if serial is not None:
            self.serial = serial
        if slot is not None:
            self.slot = slot
        if speed is not None:
            self.speed = speed
        if status is not None:
            self.status = status
        if temperature is not None:
            self.temperature = temperature
        if type is not None:
            self.type = type
        if voltage is not None:
            self.voltage = voltage

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
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
        if issubclass(Hardware, dict):
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
        if not isinstance(other, Hardware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

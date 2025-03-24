# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.30
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_30 import models

class NetworkInterfacesPortDetails(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'interface_type': 'str',
        'rx_los': 'list[NetworkInterfacePortDetailsRxLos]',
        'rx_power': 'list[NetworkInterfacePortDetailsRxPower]',
        'static': 'NetworkInterfacePortDetailsStatic',
        'temperature': 'list[NetworkInterfacePortDetailsTemperature]',
        'tx_bias': 'list[NetworkInterfacePortDetailsTxBias]',
        'tx_fault': 'list[NetworkInterfacePortDetailsTxFault]',
        'tx_power': 'list[NetworkInterfacePortDetailsTxPower]',
        'voltage': 'list[NetworkInterfacePortDetailsVoltage]'
    }

    attribute_map = {
        'name': 'name',
        'interface_type': 'interface_type',
        'rx_los': 'rx_los',
        'rx_power': 'rx_power',
        'static': 'static',
        'temperature': 'temperature',
        'tx_bias': 'tx_bias',
        'tx_fault': 'tx_fault',
        'tx_power': 'tx_power',
        'voltage': 'voltage'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        interface_type=None,  # type: str
        rx_los=None,  # type: List[models.NetworkInterfacePortDetailsRxLos]
        rx_power=None,  # type: List[models.NetworkInterfacePortDetailsRxPower]
        static=None,  # type: models.NetworkInterfacePortDetailsStatic
        temperature=None,  # type: List[models.NetworkInterfacePortDetailsTemperature]
        tx_bias=None,  # type: List[models.NetworkInterfacePortDetailsTxBias]
        tx_fault=None,  # type: List[models.NetworkInterfacePortDetailsTxFault]
        tx_power=None,  # type: List[models.NetworkInterfacePortDetailsTxPower]
        voltage=None,  # type: List[models.NetworkInterfacePortDetailsVoltage]
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            interface_type (str): The interface type. Valid values are `eth` and `fc`. 
            rx_los (list[NetworkInterfacePortDetailsRxLos]): Displays status flags for Rx LOS. A value of `true` indicates Rx Loss-of-Signal. For four-lane modules, the array contains a flag for each channel. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
            rx_power (list[NetworkInterfacePortDetailsRxPower]): Displays real-time measurement of Rx input power and whether it is within range. For four-lane modules, the array contains a measurement and status for each channel. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
            static (NetworkInterfacePortDetailsStatic)
            temperature (list[NetworkInterfacePortDetailsTemperature]): Displays real-time measurement of transceiver temperature and range. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
            tx_bias (list[NetworkInterfacePortDetailsTxBias]): Displays real-time measurement of Tx bias current and whether it is within range. For four-lane modules, the array contains a measurement and status for each channel. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
            tx_fault (list[NetworkInterfacePortDetailsTxFault]): Displays status flags for Tx Fault. A value of `true` indicates transmitter/laser fault. For four-lane modules, the array contains a flag for each channel. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
            tx_power (list[NetworkInterfacePortDetailsTxPower]): Displays real-time measurement of Tx output power and whether it is within range. For four-lane modules, the array contains a measurement and status for each channel. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
            voltage (list[NetworkInterfacePortDetailsVoltage]): Displays real-time measurement of supply voltage and whether it is within range. If the transceiver does not support digital diagnostic monitoring, the array is empty. 
        """
        if name is not None:
            self.name = name
        if interface_type is not None:
            self.interface_type = interface_type
        if rx_los is not None:
            self.rx_los = rx_los
        if rx_power is not None:
            self.rx_power = rx_power
        if static is not None:
            self.static = static
        if temperature is not None:
            self.temperature = temperature
        if tx_bias is not None:
            self.tx_bias = tx_bias
        if tx_fault is not None:
            self.tx_fault = tx_fault
        if tx_power is not None:
            self.tx_power = tx_power
        if voltage is not None:
            self.voltage = voltage

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacesPortDetails`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacesPortDetails`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacesPortDetails`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacesPortDetails`".format(key))
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
        if issubclass(NetworkInterfacesPortDetails, dict):
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
        if not isinstance(other, NetworkInterfacesPortDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

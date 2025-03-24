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

class NetworkInterfacePortDetailsStatic(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cable_technology': 'list[str]',
        'connector_type': 'str',
        'encoding': 'str',
        'extended_identifier': 'str',
        'fc_link_lengths': 'list[str]',
        'fc_speeds': 'str',
        'fc_technology': 'list[str]',
        'fc_transmission_media': 'list[str]',
        'identifier': 'str',
        'link_length': 'str',
        'rate_identifier': 'str',
        'rx_power_thresholds': 'NetworkInterfacePortDetailsStaticRxPowerThresholds',
        'signaling_rate': 'str',
        'signaling_rate_max': 'str',
        'signaling_rate_min': 'str',
        'specifications': 'list[str]',
        'temperature_thresholds': 'NetworkInterfacePortDetailsStaticTemperatureThresholds',
        'tx_bias_thresholds': 'NetworkInterfacePortDetailsStaticTxBiasThresholds',
        'tx_power_thresholds': 'NetworkInterfacePortDetailsStaticTxPowerThresholds',
        'vendor_date_code': 'str',
        'vendor_name': 'str',
        'vendor_oui': 'str',
        'vendor_part_number': 'str',
        'vendor_revision': 'str',
        'vendor_serial_number': 'str',
        'voltage_thresholds': 'NetworkInterfacePortDetailsStaticVoltageThresholds',
        'wavelength': 'str'
    }

    attribute_map = {
        'cable_technology': 'cable_technology',
        'connector_type': 'connector_type',
        'encoding': 'encoding',
        'extended_identifier': 'extended_identifier',
        'fc_link_lengths': 'fc_link_lengths',
        'fc_speeds': 'fc_speeds',
        'fc_technology': 'fc_technology',
        'fc_transmission_media': 'fc_transmission_media',
        'identifier': 'identifier',
        'link_length': 'link_length',
        'rate_identifier': 'rate_identifier',
        'rx_power_thresholds': 'rx_power_thresholds',
        'signaling_rate': 'signaling_rate',
        'signaling_rate_max': 'signaling_rate_max',
        'signaling_rate_min': 'signaling_rate_min',
        'specifications': 'specifications',
        'temperature_thresholds': 'temperature_thresholds',
        'tx_bias_thresholds': 'tx_bias_thresholds',
        'tx_power_thresholds': 'tx_power_thresholds',
        'vendor_date_code': 'vendor_date_code',
        'vendor_name': 'vendor_name',
        'vendor_oui': 'vendor_oui',
        'vendor_part_number': 'vendor_part_number',
        'vendor_revision': 'vendor_revision',
        'vendor_serial_number': 'vendor_serial_number',
        'voltage_thresholds': 'voltage_thresholds',
        'wavelength': 'wavelength'
    }

    required_args = {
    }

    def __init__(
        self,
        cable_technology=None,  # type: List[str]
        connector_type=None,  # type: str
        encoding=None,  # type: str
        extended_identifier=None,  # type: str
        fc_link_lengths=None,  # type: List[str]
        fc_speeds=None,  # type: str
        fc_technology=None,  # type: List[str]
        fc_transmission_media=None,  # type: List[str]
        identifier=None,  # type: str
        link_length=None,  # type: str
        rate_identifier=None,  # type: str
        rx_power_thresholds=None,  # type: models.NetworkInterfacePortDetailsStaticRxPowerThresholds
        signaling_rate=None,  # type: str
        signaling_rate_max=None,  # type: str
        signaling_rate_min=None,  # type: str
        specifications=None,  # type: List[str]
        temperature_thresholds=None,  # type: models.NetworkInterfacePortDetailsStaticTemperatureThresholds
        tx_bias_thresholds=None,  # type: models.NetworkInterfacePortDetailsStaticTxBiasThresholds
        tx_power_thresholds=None,  # type: models.NetworkInterfacePortDetailsStaticTxPowerThresholds
        vendor_date_code=None,  # type: str
        vendor_name=None,  # type: str
        vendor_oui=None,  # type: str
        vendor_part_number=None,  # type: str
        vendor_revision=None,  # type: str
        vendor_serial_number=None,  # type: str
        voltage_thresholds=None,  # type: models.NetworkInterfacePortDetailsStaticVoltageThresholds
        wavelength=None,  # type: str
    ):
        """
        Keyword args:
            cable_technology (list[str]): The SFP+ cable technology supported by the transceiver. 
            connector_type (str): The media connector type of the transceiver. 
            encoding (str): The serial encoding algorithm of the transceiver. 
            extended_identifier (str): The extended identifier of the transceiver type. 
            fc_link_lengths (list[str]): The Fibre Channel distance capabilities supported by the transceiver. 
            fc_speeds (str): The Fibre Channel speeds supported by the transceiver. Speeds are in units of 100 MBytes/sec, which correspond to GFC (Gb/s).
            fc_technology (list[str]): The Fibre Channel technologies supported by the transceiver. 
            fc_transmission_media (list[str]): The Fibre Channel transmission media supported by the transceiver. 
            identifier (str): The transceiver type. 
            link_length (str): Link length and cable attenuation (for active or copper cables) for the specified transceiver. Values are comma-separated lists of fields and values, where each field is separated from its corresponding value by a colon. Valid fields include `Copper Cable Attenuation (12.9 GHz)`, `Copper Cable Attenuation (25.78 GHz)`, `Copper Cable`, `SMF`, `OM2`, `OM1`, `OM4`, and `OM3`. The unit for attenuation is dB, and the units for length are meters or kilometers. Unspecified fields are omitted. 
            rate_identifier (str): The type of rate select functionality of the transceiver. 
            rx_power_thresholds (NetworkInterfacePortDetailsStaticRxPowerThresholds)
            signaling_rate (str): The nominal signaling rate in MBd, rounded off to the nearest 100 MBd, or if greater than 25400 MBd, rounded off to the nearest 250 MBd. The value can be unspecified. 
            signaling_rate_max (str): The upper signaling rate limit at which the transceiver still meets its specifications, specified as a percentage above the nominal signaling rate. The value can be unspecified. 
            signaling_rate_min (str): The lower signaling rate limit at which the transceiver still meets its specifications, specified as a percentage below the nominal signaling rate. The value can be unspecified. 
            specifications (list[str]): The Ethernet, 10G Ethernet, ESCON, Infiniband, SONET, and other specifications supported by the transceiver. 
            temperature_thresholds (NetworkInterfacePortDetailsStaticTemperatureThresholds)
            tx_bias_thresholds (NetworkInterfacePortDetailsStaticTxBiasThresholds)
            tx_power_thresholds (NetworkInterfacePortDetailsStaticTxPowerThresholds)
            vendor_date_code (str): The SFP vendor's manufacturing date code. The first six characters are the date in YYMMDD format, and the last two characters are the vendor specific lot code. The last two characters are optional. 
            vendor_name (str): The SFP vendor name.
            vendor_oui (str): The SFP vendor IEEE company ID.
            vendor_part_number (str): The part number provided by the SFP vendor.
            vendor_revision (str): The revision level for the part number provided by the SFP vendor.
            vendor_serial_number (str): The serial number provided by the SFP vendor.
            voltage_thresholds (NetworkInterfacePortDetailsStaticVoltageThresholds)
            wavelength (str): Laser wavelength (for optical variants) at room temperature, in units of nm. For passive and active cable variants, the value is unspecified. 
        """
        if cable_technology is not None:
            self.cable_technology = cable_technology
        if connector_type is not None:
            self.connector_type = connector_type
        if encoding is not None:
            self.encoding = encoding
        if extended_identifier is not None:
            self.extended_identifier = extended_identifier
        if fc_link_lengths is not None:
            self.fc_link_lengths = fc_link_lengths
        if fc_speeds is not None:
            self.fc_speeds = fc_speeds
        if fc_technology is not None:
            self.fc_technology = fc_technology
        if fc_transmission_media is not None:
            self.fc_transmission_media = fc_transmission_media
        if identifier is not None:
            self.identifier = identifier
        if link_length is not None:
            self.link_length = link_length
        if rate_identifier is not None:
            self.rate_identifier = rate_identifier
        if rx_power_thresholds is not None:
            self.rx_power_thresholds = rx_power_thresholds
        if signaling_rate is not None:
            self.signaling_rate = signaling_rate
        if signaling_rate_max is not None:
            self.signaling_rate_max = signaling_rate_max
        if signaling_rate_min is not None:
            self.signaling_rate_min = signaling_rate_min
        if specifications is not None:
            self.specifications = specifications
        if temperature_thresholds is not None:
            self.temperature_thresholds = temperature_thresholds
        if tx_bias_thresholds is not None:
            self.tx_bias_thresholds = tx_bias_thresholds
        if tx_power_thresholds is not None:
            self.tx_power_thresholds = tx_power_thresholds
        if vendor_date_code is not None:
            self.vendor_date_code = vendor_date_code
        if vendor_name is not None:
            self.vendor_name = vendor_name
        if vendor_oui is not None:
            self.vendor_oui = vendor_oui
        if vendor_part_number is not None:
            self.vendor_part_number = vendor_part_number
        if vendor_revision is not None:
            self.vendor_revision = vendor_revision
        if vendor_serial_number is not None:
            self.vendor_serial_number = vendor_serial_number
        if voltage_thresholds is not None:
            self.voltage_thresholds = voltage_thresholds
        if wavelength is not None:
            self.wavelength = wavelength

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacePortDetailsStatic`".format(key))
        if key == "vendor_date_code" and value is not None:
            if len(value) > 8:
                raise ValueError("Invalid value for `vendor_date_code`, length must be less than or equal to `8`")
        if key == "vendor_name" and value is not None:
            if len(value) > 16:
                raise ValueError("Invalid value for `vendor_name`, length must be less than or equal to `16`")
        if key == "vendor_oui" and value is not None:
            if len(value) > 8:
                raise ValueError("Invalid value for `vendor_oui`, length must be less than or equal to `8`")
        if key == "vendor_part_number" and value is not None:
            if len(value) > 16:
                raise ValueError("Invalid value for `vendor_part_number`, length must be less than or equal to `16`")
        if key == "vendor_revision" and value is not None:
            if len(value) > 4:
                raise ValueError("Invalid value for `vendor_revision`, length must be less than or equal to `4`")
        if key == "vendor_serial_number" and value is not None:
            if len(value) > 16:
                raise ValueError("Invalid value for `vendor_serial_number`, length must be less than or equal to `16`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacePortDetailsStatic`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacePortDetailsStatic`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfacePortDetailsStatic`".format(key))
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
        if issubclass(NetworkInterfacePortDetailsStatic, dict):
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
        if not isinstance(other, NetworkInterfacePortDetailsStatic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class SyslogServerSettings(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'FixedReferenceWithType',
        'ca_certificate': 'str',
        'ca_certificate_ref': 'ReferenceWithType',
        'logging_severity': 'str',
        'tls_audit_enabled': 'bool'
    }

    attribute_map = {
        'context': 'context',
        'ca_certificate': 'ca_certificate',
        'ca_certificate_ref': 'ca_certificate_ref',
        'logging_severity': 'logging_severity',
        'tls_audit_enabled': 'tls_audit_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        context=None,  # type: models.FixedReferenceWithType
        ca_certificate=None,  # type: str
        ca_certificate_ref=None,  # type: models.ReferenceWithType
        logging_severity=None,  # type: str
        tls_audit_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            context (FixedReferenceWithType): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            ca_certificate (str): The certificate of the Certificate Authority (CA) that signed the directory servers' certificate(s), which is used to validate the authenticity of the configured servers. Deprecated, please use ca_certificate_ref instead. Setting this field will result in ca_certificate_ref being updated to _legacy_syslog_ca_certificate_<config_name>. 
            ca_certificate_ref (ReferenceWithType): A reference (ID, name, and resource type) to the certificate of the certificate authority (CA) that signed the certificate(s) of the directory server, which is used to validate the authenticity of the configured servers. 
            logging_severity (str): Returns the configured logging severity threshold for which events will be forwarded to the configured syslog servers. Default configuration is info level severity. Valid values are `debug`, `info`, and `notice`. 
            tls_audit_enabled (bool): Returns a value of `true` if messages that are necessary in order to audit TLS negotiations performed by the array are forwarded to the configured syslog servers. 
        """
        if context is not None:
            self.context = context
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if ca_certificate_ref is not None:
            self.ca_certificate_ref = ca_certificate_ref
        if logging_severity is not None:
            self.logging_severity = logging_severity
        if tls_audit_enabled is not None:
            self.tls_audit_enabled = tls_audit_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SyslogServerSettings`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SyslogServerSettings`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SyslogServerSettings`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SyslogServerSettings`".format(key))
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
        if issubclass(SyslogServerSettings, dict):
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
        if not isinstance(other, SyslogServerSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

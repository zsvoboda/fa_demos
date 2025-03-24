# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_40 import models

class CloudConfigModel(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current': 'str',
        'details': 'str',
        'override_checks': 'list[str]',
        'requested': 'str',
        'status': 'str',
        'step': 'str'
    }

    attribute_map = {
        'current': 'current',
        'details': 'details',
        'override_checks': 'override_checks',
        'requested': 'requested',
        'status': 'status',
        'step': 'step'
    }

    required_args = {
    }

    def __init__(
        self,
        current=None,  # type: str
        details=None,  # type: str
        override_checks=None,  # type: List[str]
        requested=None,  # type: str
        status=None,  # type: str
        step=None,  # type: str
    ):
        """
        Keyword args:
            current (str): The current model of the CBS array.
            details (str): Details about the hardware upgrade. This field can contain error details or progress information when the status is `upgrading`. The default value is an empty string. 
            override_checks (list[str]): A list of upgrade checks to be overridden.
            requested (str): A requested model of the CBS array.
            status (str): The status of the hardware upgrade process. Can be one of `idle`, `paused`, `upgrading`. 
            step (str): The current step of the hardware upgrade process. Can be `pre-upgrade-check`, `upgrade-ct0`, `failover` and so on. The default value is an empty string. 
        """
        if current is not None:
            self.current = current
        if details is not None:
            self.details = details
        if override_checks is not None:
            self.override_checks = override_checks
        if requested is not None:
            self.requested = requested
        if status is not None:
            self.status = status
        if step is not None:
            self.step = step

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CloudConfigModel`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CloudConfigModel`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CloudConfigModel`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CloudConfigModel`".format(key))
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
        if issubclass(CloudConfigModel, dict):
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
        if not isinstance(other, CloudConfigModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

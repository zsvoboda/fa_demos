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

class PolicyrulealertwatcherpostRules(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'str',
        'excluded_codes': 'list[int]',
        'included_codes': 'list[int]',
        'minimum_notification_severity': 'str'
    }

    attribute_map = {
        'email': 'email',
        'excluded_codes': 'excluded_codes',
        'included_codes': 'included_codes',
        'minimum_notification_severity': 'minimum_notification_severity'
    }

    required_args = {
    }

    def __init__(
        self,
        email=None,  # type: str
        excluded_codes=None,  # type: List[int]
        included_codes=None,  # type: List[int]
        minimum_notification_severity=None,  # type: str
    ):
        """
        Keyword args:
            email (str): The email address that will receive the alert notification emails. 
            excluded_codes (list[int]): An alert with one of these codes will not have emails sent to the recipient. Cannot be specified with `include_codes`. If specified while `include_codes` is already set, `include_codes` will be cleared. Use \"\" to clear. If both `exclude_codes` and `include_codes` are cleared, defaults to an empty list for `exclude_codes`. 
            included_codes (list[int]): An alert must have one of these codes in order for emails to be sent to the recipient. Cannot be specified with `exclude_codes`. If specified while `exclude_codes` is already set, `exclude_codes` will be cleared. Use \"\" to clear. If both `exclude_codes` and `include_codes` are cleared, defaults to an empty list for `exclude_codes`. 
            minimum_notification_severity (str): The minimum severity that an alert must have in order for emails to be sent to the recipient. Possible values include `info`, `warning`, and `critical`. If not specified, defaults to `info`. 
        """
        if email is not None:
            self.email = email
        if excluded_codes is not None:
            self.excluded_codes = excluded_codes
        if included_codes is not None:
            self.included_codes = included_codes
        if minimum_notification_severity is not None:
            self.minimum_notification_severity = minimum_notification_severity

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyrulealertwatcherpostRules`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyrulealertwatcherpostRules`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyrulealertwatcherpostRules`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyrulealertwatcherpostRules`".format(key))
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
        if issubclass(PolicyrulealertwatcherpostRules, dict):
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
        if not isinstance(other, PolicyrulealertwatcherpostRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

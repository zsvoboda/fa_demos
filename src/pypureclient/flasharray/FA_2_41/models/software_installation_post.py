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

class SoftwareInstallationPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mode': 'str',
        'override_checks': 'list[OverrideCheck]',
        'upgrade_parameters': 'list[UpgradeParameters]'
    }

    attribute_map = {
        'mode': 'mode',
        'override_checks': 'override_checks',
        'upgrade_parameters': 'upgrade_parameters'
    }

    required_args = {
    }

    def __init__(
        self,
        mode=None,  # type: str
        override_checks=None,  # type: List[models.OverrideCheck]
        upgrade_parameters=None,  # type: List[models.UpgradeParameters]
    ):
        """
        Keyword args:
            mode (str): Mode that the upgrade is in. Valid values are `check-only`, `interactive`, `semi-interactive`, and `one-click`. The `check_only` mode is deprecated. Use `/software-checks`. In this mode, the upgrade only runs pre-upgrade checks and returns. In `interactive` mode, the upgrade pauses at several points, at which users must enter certain commands to proceed. In `semi-interactive` mode, the upgrade pauses if there are any upgrade check failures and functions like `one-click` mode otherwise. In `one-click` mode, the upgrade proceeds automatically without pausing. 
            override_checks (list[OverrideCheck]): A list of upgrade checks whose failures are overridden during the upgrade. If any optional `args` are provided, they are validated later when the corresponding check script runs. 
            upgrade_parameters (list[UpgradeParameters]): A list of parameters to be sent to the upgrade process. These parameters can be used to change the behavior of the upgrade process in specific ways such as enabling or disabling features in the target version or changing the attributes of the appliance at upgrade time. When there is a need or option to set an upgrade parameter, Pure Storage will provide documentation for the specific parameter. If you have been provided documentation related to a specific upgrade parameter, follow the instructions in the documentation. Otherwise, do not set any upgrade parameters. 
        """
        if mode is not None:
            self.mode = mode
        if override_checks is not None:
            self.override_checks = override_checks
        if upgrade_parameters is not None:
            self.upgrade_parameters = upgrade_parameters

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallationPost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallationPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallationPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallationPost`".format(key))
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
        if issubclass(SoftwareInstallationPost, dict):
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
        if not isinstance(other, SoftwareInstallationPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

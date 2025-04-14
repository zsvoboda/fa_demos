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

class PolicyruleusergroupquotapostRules(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enforced': 'bool',
        'notifications': 'list[str]',
        'quota_limit': 'int',
        'quota_type': 'str',
        'subject': 'PolicyruleusergroupquotaSubject'
    }

    attribute_map = {
        'enforced': 'enforced',
        'notifications': 'notifications',
        'quota_limit': 'quota_limit',
        'quota_type': 'quota_type',
        'subject': 'subject'
    }

    required_args = {
    }

    def __init__(
        self,
        enforced=None,  # type: bool
        notifications=None,  # type: List[str]
        quota_limit=None,  # type: int
        quota_type=None,  # type: str
        subject=None,  # type: models.PolicyruleusergroupquotaSubject
    ):
        """
        Keyword args:
            enforced (bool): If set to `true`, this rule describes an enforced quota. An out-of-space warning is issued if logical space usage exceeds the limit value described in this rule. If set to `false`, this rule describes an unenforced quota. Alerts and/or notifications are issued when logical space usage exceeds the limit value described in this rule. If not specified, defaults to `false`. 
            notifications (list[str]): Targets to notify when usage approaches or exceeds the quota limit. Valid non-empty values are `account` or `none`. The `account` value specifies that the user or group owning the usage will be notified. `none` specifies that notifications are not sent. If not specified, we assume `none`. 
            quota_limit (int): Logical space limit of the quota (in bytes) assigned by the rule. This value cannot be negative. 
            quota_type (str): Specifies the type of quota rule. Valid values are `user-default`, `user`, `user-group-member`, `group-default` and `group`. Every user-group-quota rule requires a rule type and this field is mandatory. 
            subject (PolicyruleusergroupquotaSubject): The subject for which the rule applies. Rules of quota type `user`, `user-group-member`, `group` require a non-empty subject, while rules of quota type `user-default` and `group-default` do not have a subject. The subject identifies the accounts for which the quota rule applies. 
        """
        if enforced is not None:
            self.enforced = enforced
        if notifications is not None:
            self.notifications = notifications
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if quota_type is not None:
            self.quota_type = quota_type
        if subject is not None:
            self.subject = subject

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyruleusergroupquotapostRules`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyruleusergroupquotapostRules`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyruleusergroupquotapostRules`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyruleusergroupquotapostRules`".format(key))
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
        if issubclass(PolicyruleusergroupquotapostRules, dict):
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
        if not isinstance(other, PolicyruleusergroupquotapostRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

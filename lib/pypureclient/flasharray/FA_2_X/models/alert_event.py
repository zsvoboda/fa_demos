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

class AlertEvent(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'context': 'FixedReference',
        'actual': 'str',
        'alert': 'FixedReference',
        'code': 'int',
        'component_name': 'str',
        'component_type': 'str',
        'created': 'int',
        'expected': 'str',
        'issue': 'str',
        'knowledge_base_url': 'str',
        'severity': 'str',
        'state': 'str',
        'summary': 'str',
        'time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'context': 'context',
        'actual': 'actual',
        'alert': 'alert',
        'code': 'code',
        'component_name': 'component_name',
        'component_type': 'component_type',
        'created': 'created',
        'expected': 'expected',
        'issue': 'issue',
        'knowledge_base_url': 'knowledge_base_url',
        'severity': 'severity',
        'state': 'state',
        'summary': 'summary',
        'time': 'time'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        context=None,  # type: models.FixedReference
        actual=None,  # type: str
        alert=None,  # type: models.FixedReference
        code=None,  # type: int
        component_name=None,  # type: str
        component_type=None,  # type: str
        created=None,  # type: int
        expected=None,  # type: str
        issue=None,  # type: str
        knowledge_base_url=None,  # type: str
        severity=None,  # type: str
        state=None,  # type: str
        summary=None,  # type: str
        time=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified. 
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`. 
            actual (str): Actual condition at the time the alert is created.
            alert (FixedReference)
            code (int): The parent alert number.
            component_name (str): The component type of the alert.
            component_type (str): The component name of the alert.
            created (int): The time the parent alert was created.
            expected (str): Expected state and threshold under normal conditions.
            issue (str): Information about the alert cause.
            knowledge_base_url (str): The knowledge base URL of the alert.
            severity (str): The severity level of the alert. Valid values include `info`, `warning`, `critical`, and `hidden`. 
            state (str): The state of the alert. Valid values include `open`, `closing`, and `closed`. 
            summary (str): A summary of the alert.
            time (int): The time the event occurred.
        """
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if actual is not None:
            self.actual = actual
        if alert is not None:
            self.alert = alert
        if code is not None:
            self.code = code
        if component_name is not None:
            self.component_name = component_name
        if component_type is not None:
            self.component_type = component_type
        if created is not None:
            self.created = created
        if expected is not None:
            self.expected = expected
        if issue is not None:
            self.issue = issue
        if knowledge_base_url is not None:
            self.knowledge_base_url = knowledge_base_url
        if severity is not None:
            self.severity = severity
        if state is not None:
            self.state = state
        if summary is not None:
            self.summary = summary
        if time is not None:
            self.time = time

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertEvent`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertEvent`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertEvent`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `AlertEvent`".format(key))
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
        if issubclass(AlertEvent, dict):
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
        if not isinstance(other, AlertEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

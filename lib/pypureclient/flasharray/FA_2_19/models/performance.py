# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_19 import models

class Performance(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bytes_per_mirrored_write': 'int',
        'bytes_per_op': 'int',
        'bytes_per_read': 'int',
        'bytes_per_write': 'int',
        'mirrored_write_bytes_per_sec': 'int',
        'mirrored_writes_per_sec': 'int',
        'qos_rate_limit_usec_per_mirrored_write_op': 'int',
        'qos_rate_limit_usec_per_read_op': 'int',
        'qos_rate_limit_usec_per_write_op': 'int',
        'queue_usec_per_mirrored_write_op': 'int',
        'queue_usec_per_read_op': 'int',
        'queue_usec_per_write_op': 'int',
        'read_bytes_per_sec': 'int',
        'reads_per_sec': 'int',
        'san_usec_per_mirrored_write_op': 'int',
        'san_usec_per_read_op': 'int',
        'san_usec_per_write_op': 'int',
        'service_usec_per_mirrored_write_op': 'int',
        'service_usec_per_read_op': 'int',
        'service_usec_per_read_op_cache_reduction': 'float',
        'service_usec_per_write_op': 'int',
        'time': 'int',
        'usec_per_mirrored_write_op': 'int',
        'usec_per_read_op': 'int',
        'usec_per_write_op': 'int',
        'write_bytes_per_sec': 'int',
        'writes_per_sec': 'int'
    }

    attribute_map = {
        'bytes_per_mirrored_write': 'bytes_per_mirrored_write',
        'bytes_per_op': 'bytes_per_op',
        'bytes_per_read': 'bytes_per_read',
        'bytes_per_write': 'bytes_per_write',
        'mirrored_write_bytes_per_sec': 'mirrored_write_bytes_per_sec',
        'mirrored_writes_per_sec': 'mirrored_writes_per_sec',
        'qos_rate_limit_usec_per_mirrored_write_op': 'qos_rate_limit_usec_per_mirrored_write_op',
        'qos_rate_limit_usec_per_read_op': 'qos_rate_limit_usec_per_read_op',
        'qos_rate_limit_usec_per_write_op': 'qos_rate_limit_usec_per_write_op',
        'queue_usec_per_mirrored_write_op': 'queue_usec_per_mirrored_write_op',
        'queue_usec_per_read_op': 'queue_usec_per_read_op',
        'queue_usec_per_write_op': 'queue_usec_per_write_op',
        'read_bytes_per_sec': 'read_bytes_per_sec',
        'reads_per_sec': 'reads_per_sec',
        'san_usec_per_mirrored_write_op': 'san_usec_per_mirrored_write_op',
        'san_usec_per_read_op': 'san_usec_per_read_op',
        'san_usec_per_write_op': 'san_usec_per_write_op',
        'service_usec_per_mirrored_write_op': 'service_usec_per_mirrored_write_op',
        'service_usec_per_read_op': 'service_usec_per_read_op',
        'service_usec_per_read_op_cache_reduction': 'service_usec_per_read_op_cache_reduction',
        'service_usec_per_write_op': 'service_usec_per_write_op',
        'time': 'time',
        'usec_per_mirrored_write_op': 'usec_per_mirrored_write_op',
        'usec_per_read_op': 'usec_per_read_op',
        'usec_per_write_op': 'usec_per_write_op',
        'write_bytes_per_sec': 'write_bytes_per_sec',
        'writes_per_sec': 'writes_per_sec'
    }

    required_args = {
    }

    def __init__(
        self,
        bytes_per_mirrored_write=None,  # type: int
        bytes_per_op=None,  # type: int
        bytes_per_read=None,  # type: int
        bytes_per_write=None,  # type: int
        mirrored_write_bytes_per_sec=None,  # type: int
        mirrored_writes_per_sec=None,  # type: int
        qos_rate_limit_usec_per_mirrored_write_op=None,  # type: int
        qos_rate_limit_usec_per_read_op=None,  # type: int
        qos_rate_limit_usec_per_write_op=None,  # type: int
        queue_usec_per_mirrored_write_op=None,  # type: int
        queue_usec_per_read_op=None,  # type: int
        queue_usec_per_write_op=None,  # type: int
        read_bytes_per_sec=None,  # type: int
        reads_per_sec=None,  # type: int
        san_usec_per_mirrored_write_op=None,  # type: int
        san_usec_per_read_op=None,  # type: int
        san_usec_per_write_op=None,  # type: int
        service_usec_per_mirrored_write_op=None,  # type: int
        service_usec_per_read_op=None,  # type: int
        service_usec_per_read_op_cache_reduction=None,  # type: float
        service_usec_per_write_op=None,  # type: int
        time=None,  # type: int
        usec_per_mirrored_write_op=None,  # type: int
        usec_per_read_op=None,  # type: int
        usec_per_write_op=None,  # type: int
        write_bytes_per_sec=None,  # type: int
        writes_per_sec=None,  # type: int
    ):
        """
        Keyword args:
            bytes_per_mirrored_write (int): The average I/O size per mirrored write, measured in bytes. 
            bytes_per_op (int): The average I/O size for both read and write (all) operations. 
            bytes_per_read (int): The average I/O size per read, measured in bytes.
            bytes_per_write (int): The average I/O size per write, measured in bytes.
            mirrored_write_bytes_per_sec (int): The number of mirrored bytes written per second. 
            mirrored_writes_per_sec (int): The number of mirrored writes per second. 
            qos_rate_limit_usec_per_mirrored_write_op (int): The average time it takes the array to process a mirrored I/O write request, measured in microseconds. 
            qos_rate_limit_usec_per_read_op (int): The average time spent waiting due to QoS rate limiting for a read request, measured in microseconds. 
            qos_rate_limit_usec_per_write_op (int): The average time that a write I/O request spends waiting as a result of the volume reaching its QoS bandwidth limit, measured in microseconds. 
            queue_usec_per_mirrored_write_op (int): The average time that a mirrored write I/O request spends in the array waiting to be served, measured in microseconds. 
            queue_usec_per_read_op (int): The average time that a read I/O request spends in the array waiting to be served, measured in microseconds. 
            queue_usec_per_write_op (int): The average time that a write I/O request spends in the array waiting to be served, measured in microseconds. 
            read_bytes_per_sec (int): The number of bytes read per second.
            reads_per_sec (int): The number of read requests processed per second.
            san_usec_per_mirrored_write_op (int): The average time required to transfer data from the initiator to the array for a mirrored write request, measured in microseconds. 
            san_usec_per_read_op (int): The average time required to transfer data from the array to the initiator for a read request, measured in microseconds. 
            san_usec_per_write_op (int): The average time required to transfer data from the initiator to the array for a write request, measured in microseconds. 
            service_usec_per_mirrored_write_op (int): The average time required for the array to service a mirrored write request, measured in microseconds. 
            service_usec_per_read_op (int): The average time required for the array to service a read request, measured in microseconds. 
            service_usec_per_read_op_cache_reduction (float): The percentage reduction in `service_usec_per_read_op` due to data cache hits. For example, a value of 0.25 indicates that the value of `service_usec_per_read_op` is 25&#37; lower than it would have been without any data cache hits. 
            service_usec_per_write_op (int): The average time required for the array to service a write request, measured in microseconds. 
            time (int): The time when the sample performance data was taken, measured in milliseconds since the UNIX epoch. 
            usec_per_mirrored_write_op (int): The average time it takes the array to process a mirrored I/O write request, measured in microseconds. Beginning in Purity 6.3.14 and 6.4.10 and later, including later major versions (6.5.x, 6.6.x and beyond), queue time is included. The average time does not include SAN time or QoS rate limit time. 
            usec_per_read_op (int): The average time it takes the array to process an I/O read request, measured in microseconds. Beginning in Purity 6.3.14 and 6.4.10 and later, including later major versions (6.5.x, 6.6.x and beyond), queue time is included. The average time does not include SAN time or QoS rate limit time. 
            usec_per_write_op (int): The average time it takes the array to process an I/O write request, measured in microseconds. Beginning in Purity 6.3.14 and 6.4.10 and later, including later major versions (6.5.x, 6.6.x and beyond), queue time is included. The average time does not include SAN time or QoS rate limit time. 
            write_bytes_per_sec (int): The number of bytes written per second.
            writes_per_sec (int): The number of write requests processed per second.
        """
        if bytes_per_mirrored_write is not None:
            self.bytes_per_mirrored_write = bytes_per_mirrored_write
        if bytes_per_op is not None:
            self.bytes_per_op = bytes_per_op
        if bytes_per_read is not None:
            self.bytes_per_read = bytes_per_read
        if bytes_per_write is not None:
            self.bytes_per_write = bytes_per_write
        if mirrored_write_bytes_per_sec is not None:
            self.mirrored_write_bytes_per_sec = mirrored_write_bytes_per_sec
        if mirrored_writes_per_sec is not None:
            self.mirrored_writes_per_sec = mirrored_writes_per_sec
        if qos_rate_limit_usec_per_mirrored_write_op is not None:
            self.qos_rate_limit_usec_per_mirrored_write_op = qos_rate_limit_usec_per_mirrored_write_op
        if qos_rate_limit_usec_per_read_op is not None:
            self.qos_rate_limit_usec_per_read_op = qos_rate_limit_usec_per_read_op
        if qos_rate_limit_usec_per_write_op is not None:
            self.qos_rate_limit_usec_per_write_op = qos_rate_limit_usec_per_write_op
        if queue_usec_per_mirrored_write_op is not None:
            self.queue_usec_per_mirrored_write_op = queue_usec_per_mirrored_write_op
        if queue_usec_per_read_op is not None:
            self.queue_usec_per_read_op = queue_usec_per_read_op
        if queue_usec_per_write_op is not None:
            self.queue_usec_per_write_op = queue_usec_per_write_op
        if read_bytes_per_sec is not None:
            self.read_bytes_per_sec = read_bytes_per_sec
        if reads_per_sec is not None:
            self.reads_per_sec = reads_per_sec
        if san_usec_per_mirrored_write_op is not None:
            self.san_usec_per_mirrored_write_op = san_usec_per_mirrored_write_op
        if san_usec_per_read_op is not None:
            self.san_usec_per_read_op = san_usec_per_read_op
        if san_usec_per_write_op is not None:
            self.san_usec_per_write_op = san_usec_per_write_op
        if service_usec_per_mirrored_write_op is not None:
            self.service_usec_per_mirrored_write_op = service_usec_per_mirrored_write_op
        if service_usec_per_read_op is not None:
            self.service_usec_per_read_op = service_usec_per_read_op
        if service_usec_per_read_op_cache_reduction is not None:
            self.service_usec_per_read_op_cache_reduction = service_usec_per_read_op_cache_reduction
        if service_usec_per_write_op is not None:
            self.service_usec_per_write_op = service_usec_per_write_op
        if time is not None:
            self.time = time
        if usec_per_mirrored_write_op is not None:
            self.usec_per_mirrored_write_op = usec_per_mirrored_write_op
        if usec_per_read_op is not None:
            self.usec_per_read_op = usec_per_read_op
        if usec_per_write_op is not None:
            self.usec_per_write_op = usec_per_write_op
        if write_bytes_per_sec is not None:
            self.write_bytes_per_sec = write_bytes_per_sec
        if writes_per_sec is not None:
            self.writes_per_sec = writes_per_sec

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Performance`".format(key))
        if key == "bytes_per_mirrored_write" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_mirrored_write`, must be a value greater than or equal to `0`")
        if key == "bytes_per_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_op`, must be a value greater than or equal to `0`")
        if key == "bytes_per_read" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_read`, must be a value greater than or equal to `0`")
        if key == "bytes_per_write" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `bytes_per_write`, must be a value greater than or equal to `0`")
        if key == "mirrored_write_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `mirrored_write_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "mirrored_writes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `mirrored_writes_per_sec`, must be a value greater than or equal to `0`")
        if key == "qos_rate_limit_usec_per_mirrored_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `qos_rate_limit_usec_per_mirrored_write_op`, must be a value greater than or equal to `0`")
        if key == "qos_rate_limit_usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `qos_rate_limit_usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "qos_rate_limit_usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `qos_rate_limit_usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "queue_usec_per_mirrored_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `queue_usec_per_mirrored_write_op`, must be a value greater than or equal to `0`")
        if key == "queue_usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `queue_usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "queue_usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `queue_usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "read_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `read_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "reads_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `reads_per_sec`, must be a value greater than or equal to `0`")
        if key == "san_usec_per_mirrored_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `san_usec_per_mirrored_write_op`, must be a value greater than or equal to `0`")
        if key == "san_usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `san_usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "san_usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `san_usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "service_usec_per_mirrored_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `service_usec_per_mirrored_write_op`, must be a value greater than or equal to `0`")
        if key == "service_usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `service_usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "service_usec_per_read_op_cache_reduction" and value is not None:
            if value > 1.0:
                raise ValueError("Invalid value for `service_usec_per_read_op_cache_reduction`, value must be less than or equal to `1.0`")
            if value < 0.0:
                raise ValueError("Invalid value for `service_usec_per_read_op_cache_reduction`, must be a value greater than or equal to `0.0`")
        if key == "service_usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `service_usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_mirrored_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_mirrored_write_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_read_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_read_op`, must be a value greater than or equal to `0`")
        if key == "usec_per_write_op" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `usec_per_write_op`, must be a value greater than or equal to `0`")
        if key == "write_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `write_bytes_per_sec`, must be a value greater than or equal to `0`")
        if key == "writes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `writes_per_sec`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Performance`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Performance`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Performance`".format(key))
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
        if issubclass(Performance, dict):
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
        if not isinstance(other, Performance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

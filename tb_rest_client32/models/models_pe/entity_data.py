# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EntityData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_id': 'EntityId',
        'latest': 'dict(str, dict(str, TsValue))',
        'read_attrs': 'bool',
        'read_ts': 'bool',
        'timeseries': 'dict(str, list[TsValue])'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'latest': 'latest',
        'read_attrs': 'readAttrs',
        'read_ts': 'readTs',
        'timeseries': 'timeseries'
    }

    def __init__(self, entity_id=None, latest=None, read_attrs=None, read_ts=None, timeseries=None):  # noqa: E501
        """EntityData - a model defined in Swagger"""  # noqa: E501

        self._entity_id = None
        self._latest = None
        self._read_attrs = None
        self._read_ts = None
        self._timeseries = None
        self.discriminator = None

        if entity_id is not None:
            self.entity_id = entity_id
        if latest is not None:
            self.latest = latest
        if read_attrs is not None:
            self.read_attrs = read_attrs
        if read_ts is not None:
            self.read_ts = read_ts
        if timeseries is not None:
            self.timeseries = timeseries

    @property
    def entity_id(self):
        """Gets the entity_id of this EntityData.  # noqa: E501


        :return: The entity_id of this EntityData.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EntityData.


        :param entity_id: The entity_id of this EntityData.  # noqa: E501
        :type: EntityId
        """

        self._entity_id = entity_id

    @property
    def latest(self):
        """Gets the latest of this EntityData.  # noqa: E501


        :return: The latest of this EntityData.  # noqa: E501
        :rtype: dict(str, dict(str, TsValue))
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this EntityData.


        :param latest: The latest of this EntityData.  # noqa: E501
        :type: dict(str, dict(str, TsValue))
        """

        self._latest = latest

    @property
    def read_attrs(self):
        """Gets the read_attrs of this EntityData.  # noqa: E501


        :return: The read_attrs of this EntityData.  # noqa: E501
        :rtype: bool
        """
        return self._read_attrs

    @read_attrs.setter
    def read_attrs(self, read_attrs):
        """Sets the read_attrs of this EntityData.


        :param read_attrs: The read_attrs of this EntityData.  # noqa: E501
        :type: bool
        """

        self._read_attrs = read_attrs

    @property
    def read_ts(self):
        """Gets the read_ts of this EntityData.  # noqa: E501


        :return: The read_ts of this EntityData.  # noqa: E501
        :rtype: bool
        """
        return self._read_ts

    @read_ts.setter
    def read_ts(self, read_ts):
        """Sets the read_ts of this EntityData.


        :param read_ts: The read_ts of this EntityData.  # noqa: E501
        :type: bool
        """

        self._read_ts = read_ts

    @property
    def timeseries(self):
        """Gets the timeseries of this EntityData.  # noqa: E501


        :return: The timeseries of this EntityData.  # noqa: E501
        :rtype: dict(str, list[TsValue])
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this EntityData.


        :param timeseries: The timeseries of this EntityData.  # noqa: E501
        :type: dict(str, list[TsValue])
        """

        self._timeseries = timeseries

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EntityData, dict):
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
        if not isinstance(other, EntityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

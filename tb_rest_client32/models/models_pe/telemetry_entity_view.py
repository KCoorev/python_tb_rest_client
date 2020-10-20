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


class TelemetryEntityView(object):
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
        'attributes': 'AttributesEntityView',
        'timeseries': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'timeseries': 'timeseries'
    }

    def __init__(self, attributes=None, timeseries=None):  # noqa: E501
        """TelemetryEntityView - a model defined in Swagger"""  # noqa: E501

        self._attributes = None
        self._timeseries = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if timeseries is not None:
            self.timeseries = timeseries

    @property
    def attributes(self):
        """Gets the attributes of this TelemetryEntityView.  # noqa: E501


        :return: The attributes of this TelemetryEntityView.  # noqa: E501
        :rtype: AttributesEntityView
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TelemetryEntityView.


        :param attributes: The attributes of this TelemetryEntityView.  # noqa: E501
        :type: AttributesEntityView
        """

        self._attributes = attributes

    @property
    def timeseries(self):
        """Gets the timeseries of this TelemetryEntityView.  # noqa: E501


        :return: The timeseries of this TelemetryEntityView.  # noqa: E501
        :rtype: list[str]
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this TelemetryEntityView.


        :param timeseries: The timeseries of this TelemetryEntityView.  # noqa: E501
        :type: list[str]
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
        if issubclass(TelemetryEntityView, dict):
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
        if not isinstance(other, TelemetryEntityView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class DeviceProfile(object):
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
        'created_time': 'int',
        'default': 'bool',
        'default_rule_chain_id': 'RuleChainId',
        'description': 'str',
        'id': 'DeviceProfileId',
        'name': 'str',
        'profile_data': 'DeviceProfileData',
        'provision_device_key': 'str',
        'provision_type': 'str',
        'tenant_id': 'TenantId',
        'transport_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'created_time': 'createdTime',
        'default': 'default',
        'default_rule_chain_id': 'defaultRuleChainId',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'profile_data': 'profileData',
        'provision_device_key': 'provisionDeviceKey',
        'provision_type': 'provisionType',
        'tenant_id': 'tenantId',
        'transport_type': 'transportType',
        'type': 'type'
    }

    def __init__(self, created_time=None, default=None, default_rule_chain_id=None, description=None, id=None, name=None, profile_data=None, provision_device_key=None, provision_type=None, tenant_id=None, transport_type=None, type=None):  # noqa: E501
        """DeviceProfile - a model defined in Swagger"""  # noqa: E501

        self._created_time = None
        self._default = None
        self._default_rule_chain_id = None
        self._description = None
        self._id = None
        self._name = None
        self._profile_data = None
        self._provision_device_key = None
        self._provision_type = None
        self._tenant_id = None
        self._transport_type = None
        self._type = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if default is not None:
            self.default = default
        if default_rule_chain_id is not None:
            self.default_rule_chain_id = default_rule_chain_id
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if profile_data is not None:
            self.profile_data = profile_data
        if provision_device_key is not None:
            self.provision_device_key = provision_device_key
        if provision_type is not None:
            self.provision_type = provision_type
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if transport_type is not None:
            self.transport_type = transport_type
        if type is not None:
            self.type = type

    @property
    def created_time(self):
        """Gets the created_time of this DeviceProfile.  # noqa: E501


        :return: The created_time of this DeviceProfile.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this DeviceProfile.


        :param created_time: The created_time of this DeviceProfile.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def default(self):
        """Gets the default of this DeviceProfile.  # noqa: E501


        :return: The default of this DeviceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DeviceProfile.


        :param default: The default of this DeviceProfile.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def default_rule_chain_id(self):
        """Gets the default_rule_chain_id of this DeviceProfile.  # noqa: E501


        :return: The default_rule_chain_id of this DeviceProfile.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._default_rule_chain_id

    @default_rule_chain_id.setter
    def default_rule_chain_id(self, default_rule_chain_id):
        """Sets the default_rule_chain_id of this DeviceProfile.


        :param default_rule_chain_id: The default_rule_chain_id of this DeviceProfile.  # noqa: E501
        :type: RuleChainId
        """

        self._default_rule_chain_id = default_rule_chain_id

    @property
    def description(self):
        """Gets the description of this DeviceProfile.  # noqa: E501


        :return: The description of this DeviceProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceProfile.


        :param description: The description of this DeviceProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this DeviceProfile.  # noqa: E501


        :return: The id of this DeviceProfile.  # noqa: E501
        :rtype: DeviceProfileId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceProfile.


        :param id: The id of this DeviceProfile.  # noqa: E501
        :type: DeviceProfileId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeviceProfile.  # noqa: E501


        :return: The name of this DeviceProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceProfile.


        :param name: The name of this DeviceProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def profile_data(self):
        """Gets the profile_data of this DeviceProfile.  # noqa: E501


        :return: The profile_data of this DeviceProfile.  # noqa: E501
        :rtype: DeviceProfileData
        """
        return self._profile_data

    @profile_data.setter
    def profile_data(self, profile_data):
        """Sets the profile_data of this DeviceProfile.


        :param profile_data: The profile_data of this DeviceProfile.  # noqa: E501
        :type: DeviceProfileData
        """

        self._profile_data = profile_data

    @property
    def provision_device_key(self):
        """Gets the provision_device_key of this DeviceProfile.  # noqa: E501


        :return: The provision_device_key of this DeviceProfile.  # noqa: E501
        :rtype: str
        """
        return self._provision_device_key

    @provision_device_key.setter
    def provision_device_key(self, provision_device_key):
        """Sets the provision_device_key of this DeviceProfile.


        :param provision_device_key: The provision_device_key of this DeviceProfile.  # noqa: E501
        :type: str
        """

        self._provision_device_key = provision_device_key

    @property
    def provision_type(self):
        """Gets the provision_type of this DeviceProfile.  # noqa: E501


        :return: The provision_type of this DeviceProfile.  # noqa: E501
        :rtype: str
        """
        return self._provision_type

    @provision_type.setter
    def provision_type(self, provision_type):
        """Sets the provision_type of this DeviceProfile.


        :param provision_type: The provision_type of this DeviceProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISABLED", "ALLOW_CREATE_NEW_DEVICES", "CHECK_PRE_PROVISIONED_DEVICES"]  # noqa: E501
        if provision_type not in allowed_values:
            raise ValueError(
                "Invalid value for `provision_type` ({0}), must be one of {1}"  # noqa: E501
                .format(provision_type, allowed_values)
            )

        self._provision_type = provision_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DeviceProfile.  # noqa: E501


        :return: The tenant_id of this DeviceProfile.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DeviceProfile.


        :param tenant_id: The tenant_id of this DeviceProfile.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def transport_type(self):
        """Gets the transport_type of this DeviceProfile.  # noqa: E501


        :return: The transport_type of this DeviceProfile.  # noqa: E501
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """Sets the transport_type of this DeviceProfile.


        :param transport_type: The transport_type of this DeviceProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "MQTT", "LWM2M"]  # noqa: E501
        if transport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_type, allowed_values)
            )

        self._transport_type = transport_type

    @property
    def type(self):
        """Gets the type of this DeviceProfile.  # noqa: E501


        :return: The type of this DeviceProfile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceProfile.


        :param type: The type of this DeviceProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(DeviceProfile, dict):
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
        if not isinstance(other, DeviceProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

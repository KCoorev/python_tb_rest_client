# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import pprint
import re  # noqa: F401

import six


class TenantProfile(object):
    """NOTE: This class is auto generated by the swagger code generator program.
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
        'description': 'str',
        'id': 'TenantProfileId',
        'isolated_tb_core': 'bool',
        'isolated_tb_rule_engine': 'bool',
        'name': 'str',
        'profile_data': 'TenantProfileData'
    }

    attribute_map = {
        'created_time': 'createdTime',
        'default': 'default',
        'description': 'description',
        'id': 'id',
        'isolated_tb_core': 'isolatedTbCore',
        'isolated_tb_rule_engine': 'isolatedTbRuleEngine',
        'name': 'name',
        'profile_data': 'profileData'
    }

    def __init__(self, created_time=None, default=None, description=None, id=None, isolated_tb_core=None, isolated_tb_rule_engine=None, name=None, profile_data=None):  # noqa: E501
        """TenantProfile - a model defined in Swagger"""  # noqa: E501

        self._created_time = None
        self._default = None
        self._description = None
        self._id = None
        self._isolated_tb_core = None
        self._isolated_tb_rule_engine = None
        self._name = None
        self._profile_data = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if isolated_tb_core is not None:
            self.isolated_tb_core = isolated_tb_core
        if isolated_tb_rule_engine is not None:
            self.isolated_tb_rule_engine = isolated_tb_rule_engine
        if name is not None:
            self.name = name
        if profile_data is not None:
            self.profile_data = profile_data

    @property
    def created_time(self):
        """Gets the created_time of this TenantProfile.  # noqa: E501


        :return: The created_time of this TenantProfile.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this TenantProfile.


        :param created_time: The created_time of this TenantProfile.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def default(self):
        """Gets the default of this TenantProfile.  # noqa: E501


        :return: The default of this TenantProfile.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this TenantProfile.


        :param default: The default of this TenantProfile.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this TenantProfile.  # noqa: E501


        :return: The description of this TenantProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TenantProfile.


        :param description: The description of this TenantProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this TenantProfile.  # noqa: E501


        :return: The id of this TenantProfile.  # noqa: E501
        :rtype: TenantProfileId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantProfile.


        :param id: The id of this TenantProfile.  # noqa: E501
        :type: TenantProfileId
        """

        self._id = id

    @property
    def isolated_tb_core(self):
        """Gets the isolated_tb_core of this TenantProfile.  # noqa: E501


        :return: The isolated_tb_core of this TenantProfile.  # noqa: E501
        :rtype: bool
        """
        return self._isolated_tb_core

    @isolated_tb_core.setter
    def isolated_tb_core(self, isolated_tb_core):
        """Sets the isolated_tb_core of this TenantProfile.


        :param isolated_tb_core: The isolated_tb_core of this TenantProfile.  # noqa: E501
        :type: bool
        """

        self._isolated_tb_core = isolated_tb_core

    @property
    def isolated_tb_rule_engine(self):
        """Gets the isolated_tb_rule_engine of this TenantProfile.  # noqa: E501


        :return: The isolated_tb_rule_engine of this TenantProfile.  # noqa: E501
        :rtype: bool
        """
        return self._isolated_tb_rule_engine

    @isolated_tb_rule_engine.setter
    def isolated_tb_rule_engine(self, isolated_tb_rule_engine):
        """Sets the isolated_tb_rule_engine of this TenantProfile.


        :param isolated_tb_rule_engine: The isolated_tb_rule_engine of this TenantProfile.  # noqa: E501
        :type: bool
        """

        self._isolated_tb_rule_engine = isolated_tb_rule_engine

    @property
    def name(self):
        """Gets the name of this TenantProfile.  # noqa: E501


        :return: The name of this TenantProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantProfile.


        :param name: The name of this TenantProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def profile_data(self):
        """Gets the profile_data of this TenantProfile.  # noqa: E501


        :return: The profile_data of this TenantProfile.  # noqa: E501
        :rtype: TenantProfileData
        """
        return self._profile_data

    @profile_data.setter
    def profile_data(self, profile_data):
        """Sets the profile_data of this TenantProfile.


        :param profile_data: The profile_data of this TenantProfile.  # noqa: E501
        :type: TenantProfileData
        """

        self._profile_data = profile_data

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
        if issubclass(TenantProfile, dict):
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
        if not isinstance(other, TenantProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

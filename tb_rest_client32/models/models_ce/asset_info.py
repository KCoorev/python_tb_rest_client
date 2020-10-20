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


class AssetInfo(object):
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
        'additional_info': 'str',
        'created_time': 'int',
        'customer_id': 'CustomerId',
        'customer_is_public': 'bool',
        'customer_title': 'str',
        'id': 'AssetId',
        'label': 'str',
        'name': 'str',
        'tenant_id': 'TenantId',
        'type': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'created_time': 'createdTime',
        'customer_id': 'customerId',
        'customer_is_public': 'customerIsPublic',
        'customer_title': 'customerTitle',
        'id': 'id',
        'label': 'label',
        'name': 'name',
        'tenant_id': 'tenantId',
        'type': 'type'
    }

    def __init__(self, additional_info=None, created_time=None, customer_id=None, customer_is_public=None, customer_title=None, id=None, label=None, name=None, tenant_id=None, type=None):  # noqa: E501
        """AssetInfo - a model defined in Swagger"""  # noqa: E501

        self._additional_info = None
        self._created_time = None
        self._customer_id = None
        self._customer_is_public = None
        self._customer_title = None
        self._id = None
        self._label = None
        self._name = None
        self._tenant_id = None
        self._type = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if created_time is not None:
            self.created_time = created_time
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_is_public is not None:
            self.customer_is_public = customer_is_public
        if customer_title is not None:
            self.customer_title = customer_title
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this AssetInfo.  # noqa: E501


        :return: The additional_info of this AssetInfo.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this AssetInfo.


        :param additional_info: The additional_info of this AssetInfo.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def created_time(self):
        """Gets the created_time of this AssetInfo.  # noqa: E501


        :return: The created_time of this AssetInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AssetInfo.


        :param created_time: The created_time of this AssetInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def customer_id(self):
        """Gets the customer_id of this AssetInfo.  # noqa: E501


        :return: The customer_id of this AssetInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AssetInfo.


        :param customer_id: The customer_id of this AssetInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def customer_is_public(self):
        """Gets the customer_is_public of this AssetInfo.  # noqa: E501


        :return: The customer_is_public of this AssetInfo.  # noqa: E501
        :rtype: bool
        """
        return self._customer_is_public

    @customer_is_public.setter
    def customer_is_public(self, customer_is_public):
        """Sets the customer_is_public of this AssetInfo.


        :param customer_is_public: The customer_is_public of this AssetInfo.  # noqa: E501
        :type: bool
        """

        self._customer_is_public = customer_is_public

    @property
    def customer_title(self):
        """Gets the customer_title of this AssetInfo.  # noqa: E501


        :return: The customer_title of this AssetInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_title

    @customer_title.setter
    def customer_title(self, customer_title):
        """Sets the customer_title of this AssetInfo.


        :param customer_title: The customer_title of this AssetInfo.  # noqa: E501
        :type: str
        """

        self._customer_title = customer_title

    @property
    def id(self):
        """Gets the id of this AssetInfo.  # noqa: E501


        :return: The id of this AssetInfo.  # noqa: E501
        :rtype: AssetId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetInfo.


        :param id: The id of this AssetInfo.  # noqa: E501
        :type: AssetId
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this AssetInfo.  # noqa: E501


        :return: The label of this AssetInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AssetInfo.


        :param label: The label of this AssetInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this AssetInfo.  # noqa: E501


        :return: The name of this AssetInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetInfo.


        :param name: The name of this AssetInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AssetInfo.  # noqa: E501


        :return: The tenant_id of this AssetInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AssetInfo.


        :param tenant_id: The tenant_id of this AssetInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this AssetInfo.  # noqa: E501


        :return: The type of this AssetInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssetInfo.


        :param type: The type of this AssetInfo.  # noqa: E501
        :type: str
        """

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
        if issubclass(AssetInfo, dict):
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
        if not isinstance(other, AssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

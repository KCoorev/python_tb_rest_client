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


class MergedUserPermissions(object):
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
        'generic_permissions': 'dict(str, list[str])',
        'group_permissions': 'dict(str, MergedGroupPermissionInfo)',
        'read_attr_permissions': 'dict(str, MergedGroupTypePermissionInfo)',
        'read_entity_permissions': 'dict(str, MergedGroupTypePermissionInfo)',
        'read_group_permissions': 'dict(str, MergedGroupTypePermissionInfo)',
        'read_ts_permissions': 'dict(str, MergedGroupTypePermissionInfo)'
    }

    attribute_map = {
        'generic_permissions': 'genericPermissions',
        'group_permissions': 'groupPermissions',
        'read_attr_permissions': 'readAttrPermissions',
        'read_entity_permissions': 'readEntityPermissions',
        'read_group_permissions': 'readGroupPermissions',
        'read_ts_permissions': 'readTsPermissions'
    }

    def __init__(self, generic_permissions=None, group_permissions=None, read_attr_permissions=None, read_entity_permissions=None, read_group_permissions=None, read_ts_permissions=None):  # noqa: E501
        """MergedUserPermissions - a model defined in Swagger"""  # noqa: E501

        self._generic_permissions = None
        self._group_permissions = None
        self._read_attr_permissions = None
        self._read_entity_permissions = None
        self._read_group_permissions = None
        self._read_ts_permissions = None
        self.discriminator = None

        if generic_permissions is not None:
            self.generic_permissions = generic_permissions
        if group_permissions is not None:
            self.group_permissions = group_permissions
        if read_attr_permissions is not None:
            self.read_attr_permissions = read_attr_permissions
        if read_entity_permissions is not None:
            self.read_entity_permissions = read_entity_permissions
        if read_group_permissions is not None:
            self.read_group_permissions = read_group_permissions
        if read_ts_permissions is not None:
            self.read_ts_permissions = read_ts_permissions

    @property
    def generic_permissions(self):
        """Gets the generic_permissions of this MergedUserPermissions.  # noqa: E501


        :return: The generic_permissions of this MergedUserPermissions.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._generic_permissions

    @generic_permissions.setter
    def generic_permissions(self, generic_permissions):
        """Sets the generic_permissions of this MergedUserPermissions.


        :param generic_permissions: The generic_permissions of this MergedUserPermissions.  # noqa: E501
        :type: dict(str, list[str])
        """
        allowed_values = [ALL, CREATE, READ, WRITE, DELETE, RPC_CALL, READ_CREDENTIALS, WRITE_CREDENTIALS, READ_ATTRIBUTES, WRITE_ATTRIBUTES, READ_TELEMETRY, WRITE_TELEMETRY, ADD_TO_GROUP, REMOVE_FROM_GROUP, CHANGE_OWNER, IMPERSONATE, CLAIM_DEVICES, SHARE_GROUP, ASSIGN_TO_TENANT]  # noqa: E501
        if not set(generic_permissions.keys()).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid keys in `generic_permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(generic_permissions.keys()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._generic_permissions = generic_permissions

    @property
    def group_permissions(self):
        """Gets the group_permissions of this MergedUserPermissions.  # noqa: E501


        :return: The group_permissions of this MergedUserPermissions.  # noqa: E501
        :rtype: dict(str, MergedGroupPermissionInfo)
        """
        return self._group_permissions

    @group_permissions.setter
    def group_permissions(self, group_permissions):
        """Sets the group_permissions of this MergedUserPermissions.


        :param group_permissions: The group_permissions of this MergedUserPermissions.  # noqa: E501
        :type: dict(str, MergedGroupPermissionInfo)
        """

        self._group_permissions = group_permissions

    @property
    def read_attr_permissions(self):
        """Gets the read_attr_permissions of this MergedUserPermissions.  # noqa: E501


        :return: The read_attr_permissions of this MergedUserPermissions.  # noqa: E501
        :rtype: dict(str, MergedGroupTypePermissionInfo)
        """
        return self._read_attr_permissions

    @read_attr_permissions.setter
    def read_attr_permissions(self, read_attr_permissions):
        """Sets the read_attr_permissions of this MergedUserPermissions.


        :param read_attr_permissions: The read_attr_permissions of this MergedUserPermissions.  # noqa: E501
        :type: dict(str, MergedGroupTypePermissionInfo)
        """

        self._read_attr_permissions = read_attr_permissions

    @property
    def read_entity_permissions(self):
        """Gets the read_entity_permissions of this MergedUserPermissions.  # noqa: E501


        :return: The read_entity_permissions of this MergedUserPermissions.  # noqa: E501
        :rtype: dict(str, MergedGroupTypePermissionInfo)
        """
        return self._read_entity_permissions

    @read_entity_permissions.setter
    def read_entity_permissions(self, read_entity_permissions):
        """Sets the read_entity_permissions of this MergedUserPermissions.


        :param read_entity_permissions: The read_entity_permissions of this MergedUserPermissions.  # noqa: E501
        :type: dict(str, MergedGroupTypePermissionInfo)
        """

        self._read_entity_permissions = read_entity_permissions

    @property
    def read_group_permissions(self):
        """Gets the read_group_permissions of this MergedUserPermissions.  # noqa: E501


        :return: The read_group_permissions of this MergedUserPermissions.  # noqa: E501
        :rtype: dict(str, MergedGroupTypePermissionInfo)
        """
        return self._read_group_permissions

    @read_group_permissions.setter
    def read_group_permissions(self, read_group_permissions):
        """Sets the read_group_permissions of this MergedUserPermissions.


        :param read_group_permissions: The read_group_permissions of this MergedUserPermissions.  # noqa: E501
        :type: dict(str, MergedGroupTypePermissionInfo)
        """

        self._read_group_permissions = read_group_permissions

    @property
    def read_ts_permissions(self):
        """Gets the read_ts_permissions of this MergedUserPermissions.  # noqa: E501


        :return: The read_ts_permissions of this MergedUserPermissions.  # noqa: E501
        :rtype: dict(str, MergedGroupTypePermissionInfo)
        """
        return self._read_ts_permissions

    @read_ts_permissions.setter
    def read_ts_permissions(self, read_ts_permissions):
        """Sets the read_ts_permissions of this MergedUserPermissions.


        :param read_ts_permissions: The read_ts_permissions of this MergedUserPermissions.  # noqa: E501
        :type: dict(str, MergedGroupTypePermissionInfo)
        """

        self._read_ts_permissions = read_ts_permissions

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
        if issubclass(MergedUserPermissions, dict):
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
        if not isinstance(other, MergedUserPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
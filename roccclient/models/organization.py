# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from roccclient.configuration import Configuration


class Organization(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'organization_id': 'str',
        'name': 'str',
        'short_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'organization_id': 'organizationId',
        'name': 'name',
        'short_name': 'shortName',
        'url': 'url'
    }

    def __init__(self, organization_id=None, name=None, short_name=None, url=None, local_vars_configuration=None):  # noqa: E501
        """Organization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._organization_id = None
        self._name = None
        self._short_name = None
        self._url = None
        self.discriminator = None

        if organization_id is not None:
            self.organization_id = organization_id
        self.name = name
        if short_name is not None:
            self.short_name = short_name
        self.url = url

    @property
    def organization_id(self):
        """Gets the organization_id of this Organization.  # noqa: E501

        The ID of the organization  # noqa: E501

        :return: The organization_id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Organization.

        The ID of the organization  # noqa: E501

        :param organization_id: The organization_id of this Organization.  # noqa: E501
        :type organization_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                organization_id is not None and len(organization_id) > 60):
            raise ValueError("Invalid value for `organization_id`, length must be less than or equal to `60`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                organization_id is not None and len(organization_id) < 3):
            raise ValueError("Invalid value for `organization_id`, length must be greater than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                organization_id is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', organization_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `organization_id`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501

        The organization name  # noqa: E501

        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.

        The organization name  # noqa: E501

        :param name: The name of this Organization.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Organization.  # noqa: E501

        The organization short name  # noqa: E501

        :return: The short_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Organization.

        The organization short name  # noqa: E501

        :param short_name: The short_name of this Organization.  # noqa: E501
        :type short_name: str
        """

        self._short_name = short_name

    @property
    def url(self):
        """Gets the url of this Organization.  # noqa: E501

        The URL to the homepage of the organization  # noqa: E501

        :return: The url of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Organization.

        The URL to the homepage of the organization  # noqa: E501

        :param url: The url of this Organization.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Organization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Organization):
            return True

        return self.to_dict() != other.to_dict()

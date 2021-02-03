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


class PageOfOrganizationsAllOf(object):
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
        'organizations': 'list[Organization]'
    }

    attribute_map = {
        'organizations': 'organizations'
    }

    def __init__(self, organizations=None, local_vars_configuration=None):  # noqa: E501
        """PageOfOrganizationsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._organizations = None
        self.discriminator = None

        if organizations is not None:
            self.organizations = organizations

    @property
    def organizations(self):
        """Gets the organizations of this PageOfOrganizationsAllOf.  # noqa: E501

        An array of Organizations  # noqa: E501

        :return: The organizations of this PageOfOrganizationsAllOf.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this PageOfOrganizationsAllOf.

        An array of Organizations  # noqa: E501

        :param organizations: The organizations of this PageOfOrganizationsAllOf.  # noqa: E501
        :type organizations: list[Organization]
        """

        self._organizations = organizations

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
        if not isinstance(other, PageOfOrganizationsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageOfOrganizationsAllOf):
            return True

        return self.to_dict() != other.to_dict()

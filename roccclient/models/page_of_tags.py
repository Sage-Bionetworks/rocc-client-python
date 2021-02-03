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


class PageOfTags(object):
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
        'offset': 'int',
        'limit': 'int',
        'links': 'ResponsePageMetadataLinks',
        'total_results': 'int',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'links': 'links',
        'total_results': 'totalResults',
        'tags': 'tags'
    }

    def __init__(self, offset=None, limit=None, links=None, total_results=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """PageOfTags - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._offset = None
        self._limit = None
        self._links = None
        self._total_results = None
        self._tags = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.links = links
        if total_results is not None:
            self.total_results = total_results
        if tags is not None:
            self.tags = tags

    @property
    def offset(self):
        """Gets the offset of this PageOfTags.  # noqa: E501

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfTags.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfTags.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfTags.  # noqa: E501
        :type offset: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfTags.  # noqa: E501

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfTags.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfTags.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfTags.  # noqa: E501
        :type limit: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfTags.  # noqa: E501


        :return: The links of this PageOfTags.  # noqa: E501
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfTags.


        :param links: The links of this PageOfTags.  # noqa: E501
        :type links: ResponsePageMetadataLinks
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def total_results(self):
        """Gets the total_results of this PageOfTags.  # noqa: E501

        Total number of results in the result set  # noqa: E501

        :return: The total_results of this PageOfTags.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this PageOfTags.

        Total number of results in the result set  # noqa: E501

        :param total_results: The total_results of this PageOfTags.  # noqa: E501
        :type total_results: int
        """

        self._total_results = total_results

    @property
    def tags(self):
        """Gets the tags of this PageOfTags.  # noqa: E501

        An array of Tags  # noqa: E501

        :return: The tags of this PageOfTags.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PageOfTags.

        An array of Tags  # noqa: E501

        :param tags: The tags of this PageOfTags.  # noqa: E501
        :type tags: list[Tag]
        """

        self._tags = tags

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
        if not isinstance(other, PageOfTags):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageOfTags):
            return True

        return self.to_dict() != other.to_dict()

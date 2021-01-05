# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.3
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from roccclient.configuration import Configuration


class Challenge(object):
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
        'challenge_id': 'str',
        'name': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'url': 'str',
        'status': 'ChallengeStatus',
        'tags': 'list[str]',
        'challenge_results': 'ChallengeResults',
        'organizers': 'list[str]'
    }

    attribute_map = {
        'challenge_id': 'challengeId',
        'name': 'name',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'url': 'url',
        'status': 'status',
        'tags': 'tags',
        'challenge_results': 'challengeResults',
        'organizers': 'organizers'
    }

    def __init__(self, challenge_id=None, name=None, start_date=None, end_date=None, url=None, status=None, tags=None, challenge_results=None, organizers=None, local_vars_configuration=None):  # noqa: E501
        """Challenge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._challenge_id = None
        self._name = None
        self._start_date = None
        self._end_date = None
        self._url = None
        self._status = None
        self._tags = None
        self._challenge_results = None
        self._organizers = None
        self.discriminator = None

        if challenge_id is not None:
            self.challenge_id = challenge_id
        if name is not None:
            self.name = name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if challenge_results is not None:
            self.challenge_results = challenge_results
        if organizers is not None:
            self.organizers = organizers

    @property
    def challenge_id(self):
        """Gets the challenge_id of this Challenge.  # noqa: E501

        The ID of the challenge  # noqa: E501

        :return: The challenge_id of this Challenge.  # noqa: E501
        :rtype: str
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """Sets the challenge_id of this Challenge.

        The ID of the challenge  # noqa: E501

        :param challenge_id: The challenge_id of this Challenge.  # noqa: E501
        :type challenge_id: str
        """

        self._challenge_id = challenge_id

    @property
    def name(self):
        """Gets the name of this Challenge.  # noqa: E501

        The challenge name  # noqa: E501

        :return: The name of this Challenge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Challenge.

        The challenge name  # noqa: E501

        :param name: The name of this Challenge.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this Challenge.  # noqa: E501

        When the challenge started  # noqa: E501

        :return: The start_date of this Challenge.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Challenge.

        When the challenge started  # noqa: E501

        :param start_date: The start_date of this Challenge.  # noqa: E501
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Challenge.  # noqa: E501

        When the challenge ended  # noqa: E501

        :return: The end_date of this Challenge.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Challenge.

        When the challenge ended  # noqa: E501

        :param end_date: The end_date of this Challenge.  # noqa: E501
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def url(self):
        """Gets the url of this Challenge.  # noqa: E501

        The URL to the challenge website  # noqa: E501

        :return: The url of this Challenge.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Challenge.

        The URL to the challenge website  # noqa: E501

        :param url: The url of this Challenge.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this Challenge.  # noqa: E501


        :return: The status of this Challenge.  # noqa: E501
        :rtype: ChallengeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Challenge.


        :param status: The status of this Challenge.  # noqa: E501
        :type status: ChallengeStatus
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Challenge.  # noqa: E501

        The tags associated to the challenge  # noqa: E501

        :return: The tags of this Challenge.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Challenge.

        The tags associated to the challenge  # noqa: E501

        :param tags: The tags of this Challenge.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def challenge_results(self):
        """Gets the challenge_results of this Challenge.  # noqa: E501


        :return: The challenge_results of this Challenge.  # noqa: E501
        :rtype: ChallengeResults
        """
        return self._challenge_results

    @challenge_results.setter
    def challenge_results(self, challenge_results):
        """Sets the challenge_results of this Challenge.


        :param challenge_results: The challenge_results of this Challenge.  # noqa: E501
        :type challenge_results: ChallengeResults
        """

        self._challenge_results = challenge_results

    @property
    def organizers(self):
        """Gets the organizers of this Challenge.  # noqa: E501

        The organizers of the challenge  # noqa: E501

        :return: The organizers of this Challenge.  # noqa: E501
        :rtype: list[str]
        """
        return self._organizers

    @organizers.setter
    def organizers(self, organizers):
        """Sets the organizers of this Challenge.

        The organizers of the challenge  # noqa: E501

        :param organizers: The organizers of this Challenge.  # noqa: E501
        :type organizers: list[str]
        """

        self._organizers = organizers

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
        if not isinstance(other, Challenge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Challenge):
            return True

        return self.to_dict() != other.to_dict()

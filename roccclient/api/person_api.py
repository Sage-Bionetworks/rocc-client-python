# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.3
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from roccclient.api_client import ApiClient
from roccclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PersonApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_person(self, **kwargs):  # noqa: E501
        """Create a person  # noqa: E501

        Create a person with the specified name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_person(async_req=True)
        >>> result = thread.get()

        :param person:
        :type person: Person
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Person
        """
        kwargs['_return_http_data_only'] = True
        return self.create_person_with_http_info(**kwargs)  # noqa: E501

    def create_person_with_http_info(self, **kwargs):  # noqa: E501
        """Create a person  # noqa: E501

        Create a person with the specified name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_person_with_http_info(async_req=True)
        >>> result = thread.get()

        :param person:
        :type person: Person
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Person, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'person'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_person" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'person' in local_var_params:
            body_params = local_var_params['person']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/persons', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Person',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_person(self, person_id, **kwargs):  # noqa: E501
        """Delete a person  # noqa: E501

        Deletes the person specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_person(person_id, async_req=True)
        >>> result = thread.get()

        :param person_id: The ID of the person (required)
        :type person_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Person
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_person_with_http_info(person_id, **kwargs)  # noqa: E501

    def delete_person_with_http_info(self, person_id, **kwargs):  # noqa: E501
        """Delete a person  # noqa: E501

        Deletes the person specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_person_with_http_info(person_id, async_req=True)
        >>> result = thread.get()

        :param person_id: The ID of the person (required)
        :type person_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Person, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'person_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_person" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'person_id' is set
        if self.api_client.client_side_validation and ('person_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['person_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `person_id` when calling `delete_person`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'person_id' in local_var_params:
            path_params['personId'] = local_var_params['person_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/persons/{personId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Person',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_person(self, person_id, **kwargs):  # noqa: E501
        """Get a person  # noqa: E501

        Returns the person specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_person(person_id, async_req=True)
        >>> result = thread.get()

        :param person_id: The ID of the person (required)
        :type person_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Person
        """
        kwargs['_return_http_data_only'] = True
        return self.get_person_with_http_info(person_id, **kwargs)  # noqa: E501

    def get_person_with_http_info(self, person_id, **kwargs):  # noqa: E501
        """Get a person  # noqa: E501

        Returns the person specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_person_with_http_info(person_id, async_req=True)
        >>> result = thread.get()

        :param person_id: The ID of the person (required)
        :type person_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Person, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'person_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_person" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'person_id' is set
        if self.api_client.client_side_validation and ('person_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['person_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `person_id` when calling `get_person`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'person_id' in local_var_params:
            path_params['personId'] = local_var_params['person_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/persons/{personId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Person',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_persons(self, **kwargs):  # noqa: E501
        """Get all persons  # noqa: E501

        Returns the persons  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_persons(async_req=True)
        >>> result = thread.get()

        :param limit: Maximum number of results returned
        :type limit: int
        :param offset: Index of the first result that must be returned
        :type offset: int
        :param filter: Object that describes how to filter the results
        :type filter: PersonFilter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PageOfPersons
        """
        kwargs['_return_http_data_only'] = True
        return self.list_persons_with_http_info(**kwargs)  # noqa: E501

    def list_persons_with_http_info(self, **kwargs):  # noqa: E501
        """Get all persons  # noqa: E501

        Returns the persons  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_persons_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: Maximum number of results returned
        :type limit: int
        :param offset: Index of the first result that must be returned
        :type offset: int
        :param filter: Object that describes how to filter the results
        :type filter: PersonFilter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PageOfPersons, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset',
            'filter'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_persons" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_persons`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_persons`, must be a value greater than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `list_persons`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/persons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfPersons',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

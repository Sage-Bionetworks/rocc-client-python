# roccclient.PersonApi

All URIs are relative to *https://rocc.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_person**](PersonApi.md#create_person) | **POST** /persons | Create a person
[**delete_person**](PersonApi.md#delete_person) | **DELETE** /persons/{personId} | Delete a person
[**get_person**](PersonApi.md#get_person) | **GET** /persons/{personId} | Get a person
[**list_persons**](PersonApi.md#list_persons) | **GET** /persons | Get all persons


# **create_person**
> PersonCreateResponse create_person(person_create_request=person_create_request)

Create a person

Create a person with the specified name

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.PersonApi(api_client)
    person_create_request = roccclient.PersonCreateRequest() # PersonCreateRequest |  (optional)

    try:
        # Create a person
        api_response = api_instance.create_person(person_create_request=person_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PersonApi->create_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_create_request** | [**PersonCreateRequest**](PersonCreateRequest.md)|  | [optional] 

### Return type

[**PersonCreateResponse**](PersonCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid request |  -  |
**409** | The request conflicts with current state of the target resource |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person**
> object delete_person(person_id)

Delete a person

Deletes the person specified

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.PersonApi(api_client)
    person_id = 'person_id_example' # str | The ID of the person

    try:
        # Delete a person
        api_response = api_instance.delete_person(person_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PersonApi->delete_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The ID of the person | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> Person get_person(person_id)

Get a person

Returns the person specified

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.PersonApi(api_client)
    person_id = 'person_id_example' # str | The ID of the person

    try:
        # Get a person
        api_response = api_instance.get_person(person_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PersonApi->get_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The ID of the person | 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_persons**
> PageOfPersons list_persons(limit=limit, offset=offset, filter=filter)

Get all persons

Returns the persons

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.PersonApi(api_client)
    limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)
filter = roccclient.PersonFilter() # PersonFilter | Object that describes how to filter the results (optional)

    try:
        # Get all persons
        api_response = api_instance.list_persons(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PersonApi->list_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]
 **filter** | [**PersonFilter**](.md)| Object that describes how to filter the results | [optional] 

### Return type

[**PageOfPersons**](PageOfPersons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


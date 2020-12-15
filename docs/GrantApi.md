# roccclient.GrantApi

All URIs are relative to *https://rocc.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_grant**](GrantApi.md#create_grant) | **POST** /grants | Create a grant
[**delete_grant**](GrantApi.md#delete_grant) | **DELETE** /grants/{grantId} | Delete a grant
[**get_grant**](GrantApi.md#get_grant) | **GET** /grants/{grantId} | Get a grant
[**list_grants**](GrantApi.md#list_grants) | **GET** /grants | Get all grants


# **create_grant**
> Grant create_grant(grant=grant)

Create a grant

Create a grant with the specified name

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
    api_instance = roccclient.GrantApi(api_client)
    grant = roccclient.Grant() # Grant |  (optional)

    try:
        # Create a grant
        api_response = api_instance.create_grant(grant=grant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GrantApi->create_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant** | [**Grant**](Grant.md)|  | [optional] 

### Return type

[**Grant**](Grant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |
**409** | The request conflicts with current state of the target resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grant**
> Grant delete_grant(grant_id)

Delete a grant

Deletes the grant specified

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
    api_instance = roccclient.GrantApi(api_client)
    grant_id = 'grant_id_example' # str | The ID of the grant that is being created

    try:
        # Delete a grant
        api_response = api_instance.delete_grant(grant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GrantApi->delete_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**| The ID of the grant that is being created | 

### Return type

[**Grant**](Grant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grant**
> Grant get_grant(grant_id)

Get a grant

Returns the grant specified

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
    api_instance = roccclient.GrantApi(api_client)
    grant_id = 'grant_id_example' # str | The ID of the grant that is being created

    try:
        # Get a grant
        api_response = api_instance.get_grant(grant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GrantApi->get_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**| The ID of the grant that is being created | 

### Return type

[**Grant**](Grant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_grants**
> PageOfGrants list_grants(limit=limit, offset=offset)

Get all grants

Returns the grants

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
    api_instance = roccclient.GrantApi(api_client)
    limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # Get all grants
        api_response = api_instance.list_grants(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GrantApi->list_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

### Return type

[**PageOfGrants**](PageOfGrants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# roccclient.UserApi

All URIs are relative to *https://rocc.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /users | Create a user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{username} | Delete a user
[**get_user**](UserApi.md#get_user) | **GET** /users/{username} | Get a user
[**list_users**](UserApi.md#list_users) | **GET** /users | Get all users


# **create_user**
> UserCreateResponse create_user(username, user_create_request=user_create_request)

Create a user

Create a user with the specified username

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
    api_instance = roccclient.UserApi(api_client)
    username = 'username_example' # str | The username of the user that is being created
user_create_request = roccclient.UserCreateRequest() # UserCreateRequest |  (optional)

    try:
        # Create a user
        api_response = api_instance.create_user(username, user_create_request=user_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user that is being created | 
 **user_create_request** | [**UserCreateRequest**](UserCreateRequest.md)|  | [optional] 

### Return type

[**UserCreateResponse**](UserCreateResponse.md)

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

# **delete_user**
> object delete_user(username)

Delete a user

Deletes the user specified

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
    api_instance = roccclient.UserApi(api_client)
    username = 'username_example' # str | The username of the user

    try:
        # Delete a user
        api_response = api_instance.delete_user(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | 

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
**400** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(username)

Get a user

Returns the user specified

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
    api_instance = roccclient.UserApi(api_client)
    username = 'username_example' # str | The username of the user

    try:
        # Get a user
        api_response = api_instance.get_user(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | 

### Return type

[**User**](User.md)

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

# **list_users**
> PageOfUsers list_users(limit=limit, offset=offset)

Get all users

Returns the users

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
    api_instance = roccclient.UserApi(api_client)
    limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

    try:
        # Get all users
        api_response = api_instance.list_users(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]

### Return type

[**PageOfUsers**](PageOfUsers.md)

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


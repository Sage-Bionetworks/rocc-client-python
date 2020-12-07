# roccclient.UserApi

All URIs are relative to *https://rocc.org/api.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_by_name**](UserApi.md#get_user_by_name) | **GET** /users/{username} | Get user by user name


# **get_user_by_name**
> User get_user_by_name(username)

Get user by user name

Gets the user with the specified name

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api.dev/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.UserApi(api_client)
    username = 'username_example' # str | The username of the user who needs to be fetched

    try:
        # Get user by user name
        api_response = api_instance.get_user_by_name(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user who needs to be fetched | 

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
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


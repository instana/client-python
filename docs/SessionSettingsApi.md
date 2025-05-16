# instana_client.SessionSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_session_settings**](SessionSettingsApi.md#delete_session_settings) | **DELETE** /api/settings/session | Delete session settings
[**get_session_settings**](SessionSettingsApi.md#get_session_settings) | **GET** /api/settings/session | Get session settings
[**set_session_settings**](SessionSettingsApi.md#set_session_settings) | **PUT** /api/settings/session | Configure session settings


# **delete_session_settings**
> delete_session_settings()

Delete session settings

Delete tenant unit session settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.SessionSettingsApi(api_client)

    try:
        # Delete session settings
        api_instance.delete_session_settings()
    except Exception as e:
        print("Exception when calling SessionSettingsApi->delete_session_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_settings**
> SessionSettings get_session_settings()

Get session settings

Get the tenant unit session settings

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.session_settings import SessionSettings
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.SessionSettingsApi(api_client)

    try:
        # Get session settings
        api_response = api_instance.get_session_settings()
        print("The response of SessionSettingsApi->get_session_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->get_session_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SessionSettings**](SessionSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_session_settings**
> SessionSettings set_session_settings(session_settings=session_settings)

Configure session settings

Update individual tenant unit session settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.session_settings import SessionSettings
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.SessionSettingsApi(api_client)
    session_settings = {
  tokenLifeTimeInMillis: 28800000,
  idleTimeInMillis: 3600000
}
 # SessionSettings |  (optional)

    try:
        # Configure session settings
        api_response = api_instance.set_session_settings(session_settings=session_settings)
        print("The response of SessionSettingsApi->set_session_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionSettingsApi->set_session_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_settings** | [**SessionSettings**](SessionSettings.md)|  | [optional] 

### Return type

[**SessionSettings**](SessionSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


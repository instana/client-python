# instana_client.IPFilteringApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ip_filtering**](IPFilteringApi.md#delete_ip_filtering) | **DELETE** /api/settings/ip-filtering | Delete current ip-filtering
[**disable_ip_filtering**](IPFilteringApi.md#disable_ip_filtering) | **PATCH** /api/settings/ip-filtering/disable | Disable the current ip-filtering
[**get_ip_filtering**](IPFilteringApi.md#get_ip_filtering) | **GET** /api/settings/ip-filtering | Get current ip-filtering
[**upsert_ip_filtering**](IPFilteringApi.md#upsert_ip_filtering) | **PUT** /api/settings/ip-filtering | Upsert ip-filtering
[**verify_ip_filtering**](IPFilteringApi.md#verify_ip_filtering) | **PATCH** /api/settings/ip-filtering/verify | Verify current ip-filtering


# **delete_ip_filtering**
> delete_ip_filtering()

Delete current ip-filtering

Delete the currently configured ip-filtering for the current tenant unit.

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
    api_instance = instana_client.IPFilteringApi(api_client)

    try:
        # Delete current ip-filtering
        api_instance.delete_ip_filtering()
    except Exception as e:
        print("Exception when calling IPFilteringApi->delete_ip_filtering: %s\n" % e)
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
**204** | Successful - no content to return. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_ip_filtering**
> IPFiltering disable_ip_filtering()

Disable the current ip-filtering

Disable and retrieve the currently configured ip-filtering for the current tenant unit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.ip_filtering import IPFiltering
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
    api_instance = instana_client.IPFilteringApi(api_client)

    try:
        # Disable the current ip-filtering
        api_response = api_instance.disable_ip_filtering()
        print("The response of IPFilteringApi->disable_ip_filtering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->disable_ip_filtering: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IPFiltering**](IPFiltering.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_filtering**
> IPFiltering get_ip_filtering()

Get current ip-filtering

Retrieve currently configured ip-filtering for the current tenant unit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.ip_filtering import IPFiltering
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
    api_instance = instana_client.IPFilteringApi(api_client)

    try:
        # Get current ip-filtering
        api_response = api_instance.get_ip_filtering()
        print("The response of IPFilteringApi->get_ip_filtering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->get_ip_filtering: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IPFiltering**](IPFiltering.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_ip_filtering**
> IPFiltering upsert_ip_filtering(ip_filtering_upsert)

Upsert ip-filtering

Update or create ip-filtering for the current tenant unit. Enabled configurations will become temporarily active (5 minutes) and need to be verified within whilst being temporarily to become permanently active.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.ip_filtering import IPFiltering
from instana_client.models.ip_filtering_upsert import IPFilteringUpsert
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
    api_instance = instana_client.IPFilteringApi(api_client)
    ip_filtering_upsert = {"denyAll":false,"enabled":true,"supportAccessEnabled":true,"rules":[{"target":"127.0.0.1","block":true},{"target":"0:0:0:0:0:0:0:1","block":false}]} # IPFilteringUpsert | 

    try:
        # Upsert ip-filtering
        api_response = api_instance.upsert_ip_filtering(ip_filtering_upsert)
        print("The response of IPFilteringApi->upsert_ip_filtering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->upsert_ip_filtering: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filtering_upsert** | [**IPFilteringUpsert**](IPFilteringUpsert.md)|  | 

### Return type

[**IPFiltering**](IPFiltering.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_ip_filtering**
> IPFiltering verify_ip_filtering()

Verify current ip-filtering

Verify and retrieve the currently configured ip-filtering for the current tenant unit. This action is required to promote a configuration from temporary active to permanently active. This action can only be performed whilst the configuration is temporary active.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.ip_filtering import IPFiltering
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
    api_instance = instana_client.IPFilteringApi(api_client)

    try:
        # Verify current ip-filtering
        api_response = api_instance.verify_ip_filtering()
        print("The response of IPFilteringApi->verify_ip_filtering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPFilteringApi->verify_ip_filtering: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IPFiltering**](IPFiltering.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


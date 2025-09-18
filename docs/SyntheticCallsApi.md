# instana_client.SyntheticCallsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_synthetic_call**](SyntheticCallsApi.md#delete_synthetic_call) | **DELETE** /api/settings/synthetic-calls | Delete synthetic call configurations
[**get_synthetic_calls**](SyntheticCallsApi.md#get_synthetic_calls) | **GET** /api/settings/synthetic-calls | Synthetic call configurations
[**update_synthetic_call**](SyntheticCallsApi.md#update_synthetic_call) | **PUT** /api/settings/synthetic-calls | Update synthetic call configurations


# **delete_synthetic_call**
> delete_synthetic_call()

Delete synthetic call configurations

Use this API endpoint if one wants to delete all custom synthetic call configurations. 

This endpoint requires `CanConfigureServiceMapping` permission. 

One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`.
If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token.
There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.


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
    api_instance = instana_client.SyntheticCallsApi(api_client)

    try:
        # Delete synthetic call configurations
        api_instance.delete_synthetic_call()
    except Exception as e:
        print("Exception when calling SyntheticCallsApi->delete_synthetic_call: %s\n" % e)
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

# **get_synthetic_calls**
> SyntheticCallWithDefaultsConfig get_synthetic_calls()

Synthetic call configurations

Use this API endpoint if one wants to get all custom synthetic call configurations. 

This endpoint requires `CanConfigureServiceMapping` permission. 

One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`.
If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token.
There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_call_with_defaults_config import SyntheticCallWithDefaultsConfig
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
    api_instance = instana_client.SyntheticCallsApi(api_client)

    try:
        # Synthetic call configurations
        api_response = api_instance.get_synthetic_calls()
        print("The response of SyntheticCallsApi->get_synthetic_calls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticCallsApi->get_synthetic_calls: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SyntheticCallWithDefaultsConfig**](SyntheticCallWithDefaultsConfig.md)

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

# **update_synthetic_call**
> update_synthetic_call(synthetic_call_config)

Update synthetic call configurations

Use this API endpoint if one wants to get all custom synthetic call configurations. 

This endpoint requires `CanConfigureServiceMapping` permission. 

One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`.
If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token.
There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_call_config import SyntheticCallConfig
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
    api_instance = instana_client.SyntheticCallsApi(api_client)
    synthetic_call_config = instana_client.SyntheticCallConfig() # SyntheticCallConfig | 

    try:
        # Update synthetic call configurations
        api_instance.update_synthetic_call(synthetic_call_config)
    except Exception as e:
        print("Exception when calling SyntheticCallsApi->update_synthetic_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_call_config** | [**SyntheticCallConfig**](SyntheticCallConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


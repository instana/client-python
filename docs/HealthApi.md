# instana_client.HealthApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_state**](HealthApi.md#get_health_state) | **GET** /api/instana/health | Basic health traffic light
[**get_version**](HealthApi.md#get_version) | **GET** /api/instana/version | API version information


# **get_health_state**
> HealthState get_health_state()

Basic health traffic light

Get basic health of application.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.health_state import HealthState
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
    api_instance = instana_client.HealthApi(api_client)

    try:
        # Basic health traffic light
        api_response = api_instance.get_health_state()
        print("The response of HealthApi->get_health_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_health_state: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthState**](HealthState.md)

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

# **get_version**
> InstanaVersionInfo get_version()

API version information

Get lastest API version information.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.instana_version_info import InstanaVersionInfo
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
    api_instance = instana_client.HealthApi(api_client)

    try:
        # API version information
        api_response = api_instance.get_version()
        print("The response of HealthApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InstanaVersionInfo**](InstanaVersionInfo.md)

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


# instana_client.UsageApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_usage**](UsageApi.md#get_all_usage) | **GET** /api/instana/usage/api | API usage by customer
[**get_hosts_per_day**](UsageApi.md#get_hosts_per_day) | **GET** /api/instana/usage/hosts/{day}/{month}/{year} | Host count day / month / year
[**get_hosts_per_month**](UsageApi.md#get_hosts_per_month) | **GET** /api/instana/usage/hosts/{month}/{year} | Host count month / year
[**get_usage_per_day**](UsageApi.md#get_usage_per_day) | **GET** /api/instana/usage/api/{day}/{month}/{year} | API usage day / month / year
[**get_usage_per_month**](UsageApi.md#get_usage_per_month) | **GET** /api/instana/usage/api/{month}/{year} | API usage month / year


# **get_all_usage**
> List[UsageResult] get_all_usage()

API usage by customer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.usage_result import UsageResult
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
    api_instance = instana_client.UsageApi(api_client)

    try:
        # API usage by customer
        api_response = api_instance.get_all_usage()
        print("The response of UsageApi->get_all_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_all_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UsageResult]**](UsageResult.md)

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

# **get_hosts_per_day**
> List[UsageResult] get_hosts_per_day(day, month, year)

Host count day / month / year

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.usage_result import UsageResult
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
    api_instance = instana_client.UsageApi(api_client)
    day = 56 # int | 
    month = 56 # int | 
    year = 56 # int | 

    try:
        # Host count day / month / year
        api_response = api_instance.get_hosts_per_day(day, month, year)
        print("The response of UsageApi->get_hosts_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_hosts_per_day: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **int**|  | 
 **month** | **int**|  | 
 **year** | **int**|  | 

### Return type

[**List[UsageResult]**](UsageResult.md)

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

# **get_hosts_per_month**
> List[UsageResult] get_hosts_per_month(month, year)

Host count month / year

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.usage_result import UsageResult
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
    api_instance = instana_client.UsageApi(api_client)
    month = 56 # int | 
    year = 56 # int | 

    try:
        # Host count month / year
        api_response = api_instance.get_hosts_per_month(month, year)
        print("The response of UsageApi->get_hosts_per_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_hosts_per_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **int**|  | 
 **year** | **int**|  | 

### Return type

[**List[UsageResult]**](UsageResult.md)

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

# **get_usage_per_day**
> List[UsageResult] get_usage_per_day(day, month, year)

API usage day / month / year

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.usage_result import UsageResult
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
    api_instance = instana_client.UsageApi(api_client)
    day = 56 # int | 
    month = 56 # int | 
    year = 56 # int | 

    try:
        # API usage day / month / year
        api_response = api_instance.get_usage_per_day(day, month, year)
        print("The response of UsageApi->get_usage_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_per_day: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **int**|  | 
 **month** | **int**|  | 
 **year** | **int**|  | 

### Return type

[**List[UsageResult]**](UsageResult.md)

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

# **get_usage_per_month**
> List[UsageResult] get_usage_per_month(month, year)

API usage month / year

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.usage_result import UsageResult
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
    api_instance = instana_client.UsageApi(api_client)
    month = 56 # int | 
    year = 56 # int | 

    try:
        # API usage month / year
        api_response = api_instance.get_usage_per_month(month, year)
        print("The response of UsageApi->get_usage_per_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_per_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **int**|  | 
 **year** | **int**|  | 

### Return type

[**List[UsageResult]**](UsageResult.md)

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


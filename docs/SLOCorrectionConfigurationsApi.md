# instana_client.SLOCorrectionConfigurationsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_slo_correction_window_config**](SLOCorrectionConfigurationsApi.md#create_slo_correction_window_config) | **POST** /api/settings/correction | Create a new SLO Correction Window Config
[**delete_slo_correction_window_config**](SLOCorrectionConfigurationsApi.md#delete_slo_correction_window_config) | **DELETE** /api/settings/correction/{id} | Delete an existing SLO Correction Window Configuration
[**get_all_slo_correction_window_configs**](SLOCorrectionConfigurationsApi.md#get_all_slo_correction_window_configs) | **GET** /api/settings/correction | Get All SLO Correction Window Configs
[**get_slo_correction_window_config_by_id**](SLOCorrectionConfigurationsApi.md#get_slo_correction_window_config_by_id) | **GET** /api/settings/correction/{id} | Get an existing SLO Correction Window Config
[**update_slo_correction_window_config**](SLOCorrectionConfigurationsApi.md#update_slo_correction_window_config) | **PUT** /api/settings/correction/{id} | Update an existing SLO Correction Window Config


# **create_slo_correction_window_config**
> CorrectionConfiguration create_slo_correction_window_config(correction_configuration)

Create a new SLO Correction Window Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.correction_configuration import CorrectionConfiguration
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
    api_instance = instana_client.SLOCorrectionConfigurationsApi(api_client)
    correction_configuration = {"name":"New test for DST corrections Test-9","description":"This is to check report API","active":true,"scheduling":{"startTime":1749607200000,"duration":3,"durationUnit":"HOUR","recurrentRule":"FREQ=DAILY;INTERVAL=1"},"sloIds":["SLO4s-fs-GuT56c3v4KzQKBuQ"],"tags":["test","rrule"]} # CorrectionConfiguration | 

    try:
        # Create a new SLO Correction Window Config
        api_response = api_instance.create_slo_correction_window_config(correction_configuration)
        print("The response of SLOCorrectionConfigurationsApi->create_slo_correction_window_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLOCorrectionConfigurationsApi->create_slo_correction_window_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correction_configuration** | [**CorrectionConfiguration**](CorrectionConfiguration.md)|  | 

### Return type

[**CorrectionConfiguration**](CorrectionConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New SLO Correction Window Configuration Created Successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_slo_correction_window_config**
> delete_slo_correction_window_config(id)

Delete an existing SLO Correction Window Configuration

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
    api_instance = instana_client.SLOCorrectionConfigurationsApi(api_client)
    id = 'cvLxfzNJQriV86MQTqOu1g' # str | 

    try:
        # Delete an existing SLO Correction Window Configuration
        api_instance.delete_slo_correction_window_config(id)
    except Exception as e:
        print("Exception when calling SLOCorrectionConfigurationsApi->delete_slo_correction_window_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | SLO Correction Window Configuration Deleted Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_slo_correction_window_configs**
> PaginatedResult get_all_slo_correction_window_configs(page_size=page_size, page=page, order_by=order_by, order_direction=order_direction, query=query, tag=tag, id=id, slo_id=slo_id, refresh=refresh)

Get All SLO Correction Window Configs

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.paginated_result import PaginatedResult
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
    api_instance = instana_client.SLOCorrectionConfigurationsApi(api_client)
    page_size = 1 # int |  (optional)
    page = 1 # int |  (optional)
    order_by = 'name' # str |  (optional)
    order_direction = 'ASC' # str |  (optional)
    query = 'test Correction' # str |  (optional)
    tag = ['Testing'] # List[str] |  (optional)
    id = ['SSPTkTWoT1W0OpE_iQbfaA'] # List[str] |  (optional)
    slo_id = ['SLOdCTspkHlS_OzNOATQWgsuw'] # List[str] |  (optional)
    refresh = false # bool |  (optional)

    try:
        # Get All SLO Correction Window Configs
        api_response = api_instance.get_all_slo_correction_window_configs(page_size=page_size, page=page, order_by=order_by, order_direction=order_direction, query=query, tag=tag, id=id, slo_id=slo_id, refresh=refresh)
        print("The response of SLOCorrectionConfigurationsApi->get_all_slo_correction_window_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLOCorrectionConfigurationsApi->get_all_slo_correction_window_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **order_direction** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **tag** | [**List[str]**](str.md)|  | [optional] 
 **id** | [**List[str]**](str.md)|  | [optional] 
 **slo_id** | [**List[str]**](str.md)|  | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched list of the SLO Correction Window Configurations Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_correction_window_config_by_id**
> CorrectionConfiguration get_slo_correction_window_config_by_id(id, refresh=refresh)

Get an existing SLO Correction Window Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.correction_configuration import CorrectionConfiguration
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
    api_instance = instana_client.SLOCorrectionConfigurationsApi(api_client)
    id = 'dCTspkffgHlS_OzNOATQWgsuw' # str | 
    refresh = false # bool |  (optional)

    try:
        # Get an existing SLO Correction Window Config
        api_response = api_instance.get_slo_correction_window_config_by_id(id, refresh=refresh)
        print("The response of SLOCorrectionConfigurationsApi->get_slo_correction_window_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLOCorrectionConfigurationsApi->get_slo_correction_window_config_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**CorrectionConfiguration**](CorrectionConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched SLO Correction Window Configuration Successfully |  -  |
**404** | SLO Correction Window Configuration Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_slo_correction_window_config**
> CorrectionConfiguration update_slo_correction_window_config(id, correction_configuration)

Update an existing SLO Correction Window Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.correction_configuration import CorrectionConfiguration
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
    api_instance = instana_client.SLOCorrectionConfigurationsApi(api_client)
    id = 'cvLxfzNJQriV86MQTqOu1g' # str | 
    correction_configuration = {"name":"New test for DST corrections Test-9","description":"This is to check report API","active":true,"scheduling":{"startTime":1749607200000,"duration":3,"durationUnit":"HOUR","recurrentRule":"FREQ=DAILY;INTERVAL=1"},"sloIds":["SLO4s-fs-GuT56c3v4KzQKBuQ"],"tags":["test","rrule"]} # CorrectionConfiguration | 

    try:
        # Update an existing SLO Correction Window Config
        api_response = api_instance.update_slo_correction_window_config(id, correction_configuration)
        print("The response of SLOCorrectionConfigurationsApi->update_slo_correction_window_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLOCorrectionConfigurationsApi->update_slo_correction_window_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **correction_configuration** | [**CorrectionConfiguration**](CorrectionConfiguration.md)|  | 

### Return type

[**CorrectionConfiguration**](CorrectionConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated SLO Correction Window Configuration Successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


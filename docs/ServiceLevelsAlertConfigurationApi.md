# instana_client.ServiceLevelsAlertConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#create_service_levels_alert_config) | **POST** /api/events/settings/global-alert-configs/service-levels | Create Service levels Alert Config
[**delete_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#delete_service_levels_alert_config) | **DELETE** /api/events/settings/global-alert-configs/service-levels/{id} | Delete Service levels Alert Config
[**disable_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#disable_service_levels_alert_config) | **PUT** /api/events/settings/global-alert-configs/service-levels/{id}/disable | Disable Service levels Alert Config
[**enable_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#enable_service_levels_alert_config) | **PUT** /api/events/settings/global-alert-configs/service-levels/{id}/enable | Enable Service levels Alert Config
[**find_active_service_levels_alert_configs**](ServiceLevelsAlertConfigurationApi.md#find_active_service_levels_alert_configs) | **GET** /api/events/settings/global-alert-configs/service-levels | All Service levels Alert Configs
[**find_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#find_service_levels_alert_config) | **GET** /api/events/settings/global-alert-configs/service-levels/{id} | Get Service levels Alert Config
[**find_service_levels_alert_config_versions**](ServiceLevelsAlertConfigurationApi.md#find_service_levels_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/service-levels/{id}/versions | Get versions of Service levels Alert Config
[**restore_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#restore_service_levels_alert_config) | **PUT** /api/events/settings/global-alert-configs/service-levels/{id}/restore/{created} | Restore Service levels Alert Config
[**update_service_levels_alert_config**](ServiceLevelsAlertConfigurationApi.md#update_service_levels_alert_config) | **POST** /api/events/settings/global-alert-configs/service-levels/{id} | Update Service levels Alert Config


# **create_service_levels_alert_config**
> ServiceLevelseAlertConfigWithMetadata create_service_levels_alert_config(service_levels_alert_config)

Create Service levels Alert Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_levels_alert_config import ServiceLevelsAlertConfig
from instana_client.models.service_levelse_alert_config_with_metadata import ServiceLevelseAlertConfigWithMetadata
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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    service_levels_alert_config = {"alertChannelIds":[],"customPayloadFields":[{"key":"foo","id":"avvh9tbxpfRE65t","type":"staticString","value":"bar"}],"description":"Error Budget Remaining is less than or equal to 5%.","name":"Error Budget Remaining is low","rule":{"alertType":"ERROR_BUDGET","metric":"BURNED_PERCENTAGE"},"severity":5,"sloIds":["SLOEANnWh9tQOa2h88kGxK6wQ"],"threshold":{"type":"staticThreshold","value":0.05,"operator":">=","lastUpdated":1716454787342},"timeThreshold":{"timeWindow":600000},"triggering":true} # ServiceLevelsAlertConfig | Create Request Body

    try:
        # Create Service levels Alert Config
        api_response = api_instance.create_service_levels_alert_config(service_levels_alert_config)
        print("The response of ServiceLevelsAlertConfigurationApi->create_service_levels_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->create_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_levels_alert_config** | [**ServiceLevelsAlertConfig**](ServiceLevelsAlertConfig.md)| Create Request Body | 

### Return type

[**ServiceLevelseAlertConfigWithMetadata**](ServiceLevelseAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created new Service Levels Alert Configuration Successfully |  -  |
**400** | Service levels Alert Config with Website SLOs do not support triggering |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_levels_alert_config**
> delete_service_levels_alert_config(id)

Delete Service levels Alert Config

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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID

    try:
        # Delete Service levels Alert Config
        api_instance.delete_service_levels_alert_config(id)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->delete_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 

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
**204** | Service Levels Alert Configuration Deleted Successfully |  -  |
**404** | Service levels Alert Config with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_service_levels_alert_config**
> disable_service_levels_alert_config(id, body=body)

Disable Service levels Alert Config

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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID
    body = 'body_example' # str |  (optional)

    try:
        # Disable Service levels Alert Config
        api_instance.disable_service_levels_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->disable_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Service Levels Alert Configuration Disabled Successfully |  -  |
**404** | Service levels Alert Config with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_service_levels_alert_config**
> enable_service_levels_alert_config(id, body=body)

Enable Service levels Alert Config

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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID
    body = 'body_example' # str |  (optional)

    try:
        # Enable Service levels Alert Config
        api_instance.enable_service_levels_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->enable_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Service Levels Alert Configuration Enabled Successfully |  -  |
**404** | Service levels Alert Config with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_service_levels_alert_configs**
> List[ServiceLevelseAlertConfigWithMetadata] find_active_service_levels_alert_configs(slo_id=slo_id, alert_ids=alert_ids)

All Service levels Alert Configs

Configs are sorted descending by their created date.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_levelse_alert_config_with_metadata import ServiceLevelseAlertConfigWithMetadata
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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    slo_id = 'SLOEANnWh9tQOa2h88kGxK6wQ' # str | Service Levels Objective(SLO) Configuration ID (optional)
    alert_ids = ['ln3IGogYS-S7CPqcOQYTNA'] # List[str] | List of Service Levels Alert Configuration IDs (optional)

    try:
        # All Service levels Alert Configs
        api_response = api_instance.find_active_service_levels_alert_configs(slo_id=slo_id, alert_ids=alert_ids)
        print("The response of ServiceLevelsAlertConfigurationApi->find_active_service_levels_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->find_active_service_levels_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| Service Levels Objective(SLO) Configuration ID | [optional] 
 **alert_ids** | [**List[str]**](str.md)| List of Service Levels Alert Configuration IDs | [optional] 

### Return type

[**List[ServiceLevelseAlertConfigWithMetadata]**](ServiceLevelseAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched list of the Service Level Alert Configurations Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_service_levels_alert_config**
> ServiceLevelseAlertConfigWithMetadata find_service_levels_alert_config(id, valid_on=valid_on)

Get Service levels Alert Config

Find a Service levels Alert Config by ID. This will deliver deleted configs too.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_levelse_alert_config_with_metadata import ServiceLevelseAlertConfigWithMetadata
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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID
    valid_on = 1706617456952 # int | Service Levels Alert Version Creation Date (optional)

    try:
        # Get Service levels Alert Config
        api_response = api_instance.find_service_levels_alert_config(id, valid_on=valid_on)
        print("The response of ServiceLevelsAlertConfigurationApi->find_service_levels_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->find_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 
 **valid_on** | **int**| Service Levels Alert Version Creation Date | [optional] 

### Return type

[**ServiceLevelseAlertConfigWithMetadata**](ServiceLevelseAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched Service Level Alert Configuration Successfully |  -  |
**404** | Service levels Alert Config with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_service_levels_alert_config_versions**
> List[ConfigVersion] find_service_levels_alert_config_versions(id)

Get versions of Service levels Alert Config

Find all versions of a Service levels Alert Config by ID. This will deliver deleted configs too. Configs are sorted descending by their created date.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.config_version import ConfigVersion
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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID

    try:
        # Get versions of Service levels Alert Config
        api_response = api_instance.find_service_levels_alert_config_versions(id)
        print("The response of ServiceLevelsAlertConfigurationApi->find_service_levels_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->find_service_levels_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 

### Return type

[**List[ConfigVersion]**](ConfigVersion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched list of Service Level Alert Configuration Versions Successfully |  -  |
**404** | Service levels Alert Config with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_service_levels_alert_config**
> restore_service_levels_alert_config(id, created, body=body)

Restore Service levels Alert Config

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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID
    created = 1706617456952 # int | Service Levels Alert Version Creation Date
    body = 'body_example' # str |  (optional)

    try:
        # Restore Service levels Alert Config
        api_instance.restore_service_levels_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->restore_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 
 **created** | **int**| Service Levels Alert Version Creation Date | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Service Levels Alert Configuration Restored Successfully |  -  |
**404** | Service levels Alert Config with given ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_levels_alert_config**
> ServiceLevelseAlertConfigWithMetadata update_service_levels_alert_config(id, service_levels_alert_config)

Update Service levels Alert Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_levels_alert_config import ServiceLevelsAlertConfig
from instana_client.models.service_levelse_alert_config_with_metadata import ServiceLevelseAlertConfigWithMetadata
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
    api_instance = instana_client.ServiceLevelsAlertConfigurationApi(api_client)
    id = 'ln3IGogYS-S7CPqcOQYTNA' # str | Service Levels Alert Configuration ID
    service_levels_alert_config = {"alertChannelIds":[],"customPayloadFields":[{"key":"foo","id":"avvh9tbxpfRE65t","type":"staticString","value":"bar"}],"description":"Error Budget Remaining is less than or equal to 5%.","name":"Error Budget Remaining is low","rule":{"alertType":"ERROR_BUDGET","metric":"BURNED_PERCENTAGE"},"severity":5,"sloIds":["SLOEANnWh9tQOa2h88kGxK6wQ"],"threshold":{"type":"staticThreshold","value":0.05,"operator":">=","lastUpdated":1716454787342},"timeThreshold":{"timeWindow":600000},"triggering":true} # ServiceLevelsAlertConfig | Update Request Body

    try:
        # Update Service levels Alert Config
        api_response = api_instance.update_service_levels_alert_config(id, service_levels_alert_config)
        print("The response of ServiceLevelsAlertConfigurationApi->update_service_levels_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsAlertConfigurationApi->update_service_levels_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service Levels Alert Configuration ID | 
 **service_levels_alert_config** | [**ServiceLevelsAlertConfig**](ServiceLevelsAlertConfig.md)| Update Request Body | 

### Return type

[**ServiceLevelseAlertConfigWithMetadata**](ServiceLevelseAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Service Levels Alert Configuration Successfully |  -  |
**204** | Service Levels Smart Alert Configuration did not change |  -  |
**400** | Service levels Alert Config with Website SLOs do not support triggering |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


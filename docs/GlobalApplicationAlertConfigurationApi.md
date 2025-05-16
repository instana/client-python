# instana_client.GlobalApplicationAlertConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#create_global_application_alert_config) | **POST** /api/events/settings/global-alert-configs/applications | Create Global Smart Alert Config
[**delete_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#delete_global_application_alert_config) | **DELETE** /api/events/settings/global-alert-configs/applications/{id} | Delete Global Smart Alert Config
[**disable_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#disable_global_application_alert_config) | **PUT** /api/events/settings/global-alert-configs/applications/{id}/disable | Disable Global Smart Alert Config
[**enable_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#enable_global_application_alert_config) | **PUT** /api/events/settings/global-alert-configs/applications/{id}/enable | Enable Global Smart Alert Config
[**find_active_global_application_alert_configs**](GlobalApplicationAlertConfigurationApi.md#find_active_global_application_alert_configs) | **GET** /api/events/settings/global-alert-configs/applications | Get all Global Smart Alert Configs
[**find_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#find_global_application_alert_config) | **GET** /api/events/settings/global-alert-configs/applications/{id} | Get Global Smart Alert Config
[**find_global_application_alert_config_versions**](GlobalApplicationAlertConfigurationApi.md#find_global_application_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/applications/{id}/versions | Get Global Smart Alert Config Versions
[**restore_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#restore_global_application_alert_config) | **PUT** /api/events/settings/global-alert-configs/applications/{id}/restore/{created} | Restore Global Smart Alert Config
[**update_global_application_alert_config**](GlobalApplicationAlertConfigurationApi.md#update_global_application_alert_config) | **POST** /api/events/settings/global-alert-configs/applications/{id} | Update Global Smart Alert Config


# **create_global_application_alert_config**
> GlobalApplicationAlertConfigWithMetadata create_global_application_alert_config(global_applications_alert_config)

Create Global Smart Alert Config

Creates a new Global Smart Alert Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.global_application_alert_config_with_metadata import GlobalApplicationAlertConfigWithMetadata
from instana_client.models.global_applications_alert_config import GlobalApplicationsAlertConfig
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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    global_applications_alert_config = {"name":"Slow calls than usual","description":"Calls are slower or equal to 2 ms based on latency (90th).","boundaryScope":"INBOUND","applications":{"j02SxMRTSf-NCBXf5IdsjQ":{"applicationId":"j02SxMRTSf-NCBXf5IdsjQ","inclusive":true,"services":{}}},"applicationIds":["j02SxMRTSf-NCBXf5IdsjQ"],"severity":5,"triggering":false,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"includeInternal":false,"includeSynthetic":false,"rule":{"alertType":"slowness","aggregation":"P90","metricName":"latency"},"threshold":{"type":"staticThreshold","operator":">=","value":2,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"evaluationType":"PER_AP","customPayloadFields":[]} # GlobalApplicationsAlertConfig | 

    try:
        # Create Global Smart Alert Config
        api_response = api_instance.create_global_application_alert_config(global_applications_alert_config)
        print("The response of GlobalApplicationAlertConfigurationApi->create_global_application_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->create_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_applications_alert_config** | [**GlobalApplicationsAlertConfig**](GlobalApplicationsAlertConfig.md)|  | 

### Return type

[**GlobalApplicationAlertConfigWithMetadata**](GlobalApplicationAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Global Smart Alert Configuration created. |  -  |
**400** | Invalid Configuration. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_application_alert_config**
> delete_global_application_alert_config(id)

Delete Global Smart Alert Config

Deletes a Global Smart Alert Configuration.

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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to delete.

    try:
        # Delete Global Smart Alert Config
        api_instance.delete_global_application_alert_config(id)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->delete_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to delete. | 

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
**200** | Global Smart Alert Configuration deleted. |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_global_application_alert_config**
> disable_global_application_alert_config(id, body=body)

Disable Global Smart Alert Config

Disables a Global Smart Alert Configuration.

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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to disable.
    body = 'body_example' # str |  (optional)

    try:
        # Disable Global Smart Alert Config
        api_instance.disable_global_application_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->disable_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to disable. | 
 **body** | **str**|  | [optional] 

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
**200** | Global Smart Alert Configuration disabled. |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_global_application_alert_config**
> enable_global_application_alert_config(id, body=body)

Enable Global Smart Alert Config

Enables a Global Smart Alert Configuration.

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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to enable.
    body = 'body_example' # str |  (optional)

    try:
        # Enable Global Smart Alert Config
        api_instance.enable_global_application_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->enable_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to enable. | 
 **body** | **str**|  | [optional] 

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
**200** | Global Smart Alert Configuration enabled. |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_global_application_alert_configs**
> List[GlobalApplicationAlertConfigWithMetadata] find_active_global_application_alert_configs(application_id, alert_ids=alert_ids)

Get all Global Smart Alert Configs

Gets all Global Smart Alert Configuration. Configurations are sorted by creation date in descending order.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.global_application_alert_config_with_metadata import GlobalApplicationAlertConfigWithMetadata
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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    application_id = 'j02SxMRTSf-NCBXf5IdsjQ' # str | The ID of a specific global application.
    alert_ids = ['IYS1XOEcTNiT1eOD8pxgXg'] # List[str] | A list of Global Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. (optional)

    try:
        # Get all Global Smart Alert Configs
        api_response = api_instance.find_active_global_application_alert_configs(application_id, alert_ids=alert_ids)
        print("The response of GlobalApplicationAlertConfigurationApi->find_active_global_application_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->find_active_global_application_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The ID of a specific global application. | 
 **alert_ids** | [**List[str]**](str.md)| A list of Global Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. | [optional] 

### Return type

[**List[GlobalApplicationAlertConfigWithMetadata]**](GlobalApplicationAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions. |  -  |
**404** | The requested website doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_global_application_alert_config**
> GlobalApplicationAlertConfigWithMetadata find_global_application_alert_config(id, valid_on=valid_on)

Get Global Smart Alert Config

Gets a specific Global Smart Alert Configuration. This may return a deleted Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.global_application_alert_config_with_metadata import GlobalApplicationAlertConfigWithMetadata
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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to retrieve.
    valid_on = 1707305626330 # int | A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  (optional)

    try:
        # Get Global Smart Alert Config
        api_response = api_instance.find_global_application_alert_config(id, valid_on=valid_on)
        print("The response of GlobalApplicationAlertConfigurationApi->find_global_application_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->find_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to retrieve. | 
 **valid_on** | **int**| A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  | [optional] 

### Return type

[**GlobalApplicationAlertConfigWithMetadata**](GlobalApplicationAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions. |  -  |
**404** | The requested Configuration does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_global_application_alert_config_versions**
> List[ConfigVersion] find_global_application_alert_config_versions(id)

Get Global Smart Alert Config Versions

Gets all versions of a Global Smart Alert Configuration. This may return deleted Configurations. Configurations are sorted by creation date in descending order.

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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to retrieve.

    try:
        # Get Global Smart Alert Config Versions
        api_response = api_instance.find_global_application_alert_config_versions(id)
        print("The response of GlobalApplicationAlertConfigurationApi->find_global_application_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->find_global_application_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to retrieve. | 

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
**200** | OK |  -  |
**403** | Insufficient permissions. |  -  |
**404** | The requested Configuration does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_global_application_alert_config**
> restore_global_application_alert_config(id, created, body=body)

Restore Global Smart Alert Config

Restores a deleted Global Smart Alert Configuration.

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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to restore.
    created = 1707305626330 # int | Unix timestamp representing the creation time of a specific Global Smart Alert Configuration.
    body = 'body_example' # str |  (optional)

    try:
        # Restore Global Smart Alert Config
        api_instance.restore_global_application_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->restore_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to restore. | 
 **created** | **int**| Unix timestamp representing the creation time of a specific Global Smart Alert Configuration. | 
 **body** | **str**|  | [optional] 

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
**200** | Global Smart Alert Configuration restored. |  -  |
**400** | Invalid Configuration provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_application_alert_config**
> GlobalApplicationAlertConfigWithMetadata update_global_application_alert_config(id, global_applications_alert_config)

Update Global Smart Alert Config

Updates an existing Global Smart Alert Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.global_application_alert_config_with_metadata import GlobalApplicationAlertConfigWithMetadata
from instana_client.models.global_applications_alert_config import GlobalApplicationsAlertConfig
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
    api_instance = instana_client.GlobalApplicationAlertConfigurationApi(api_client)
    id = 'vlFnxhVTS3KVb-wsN26PeQ' # str | ID of a specific Global Smart Alert Configuration to update.
    global_applications_alert_config = {"name":"Slow calls than usual","description":"Calls are slower or equal to 2 ms based on latency (90th).","boundaryScope":"INBOUND","applications":{"j02SxMRTSf-NCBXf5IdsjQ":{"applicationId":"j02SxMRTSf-NCBXf5IdsjQ","inclusive":true,"services":{}}},"applicationIds":["j02SxMRTSf-NCBXf5IdsjQ"],"severity":5,"triggering":false,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"includeInternal":false,"includeSynthetic":false,"rule":{"alertType":"slowness","aggregation":"P90","metricName":"latency"},"threshold":{"type":"staticThreshold","operator":">=","value":2,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"evaluationType":"PER_AP","customPayloadFields":[]} # GlobalApplicationsAlertConfig | 

    try:
        # Update Global Smart Alert Config
        api_response = api_instance.update_global_application_alert_config(id, global_applications_alert_config)
        print("The response of GlobalApplicationAlertConfigurationApi->update_global_application_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApplicationAlertConfigurationApi->update_global_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Global Smart Alert Configuration to update. | 
 **global_applications_alert_config** | [**GlobalApplicationsAlertConfig**](GlobalApplicationsAlertConfig.md)|  | 

### Return type

[**GlobalApplicationAlertConfigWithMetadata**](GlobalApplicationAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Global Smart Alert Configuration updated. |  -  |
**204** | Global Smart Alert Configuration did not change. |  -  |
**400** | Invalid Application ID provided. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable entity. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


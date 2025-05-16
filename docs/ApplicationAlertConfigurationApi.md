# instana_client.ApplicationAlertConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_alert_config**](ApplicationAlertConfigurationApi.md#create_application_alert_config) | **POST** /api/events/settings/application-alert-configs | Create Smart Alert Config
[**delete_application_alert_config**](ApplicationAlertConfigurationApi.md#delete_application_alert_config) | **DELETE** /api/events/settings/application-alert-configs/{id} | Delete Smart Alert Config
[**disable_application_alert_config**](ApplicationAlertConfigurationApi.md#disable_application_alert_config) | **PUT** /api/events/settings/application-alert-configs/{id}/disable | Disable Smart Alert Config
[**enable_application_alert_config**](ApplicationAlertConfigurationApi.md#enable_application_alert_config) | **PUT** /api/events/settings/application-alert-configs/{id}/enable | Enable Application Alert Config
[**find_active_application_alert_configs**](ApplicationAlertConfigurationApi.md#find_active_application_alert_configs) | **GET** /api/events/settings/application-alert-configs | Get all Smart Alert Configs
[**find_application_alert_config**](ApplicationAlertConfigurationApi.md#find_application_alert_config) | **GET** /api/events/settings/application-alert-configs/{id} | Get Smart Alert Config
[**find_application_alert_config_versions**](ApplicationAlertConfigurationApi.md#find_application_alert_config_versions) | **GET** /api/events/settings/application-alert-configs/{id}/versions | Get Smart Alert Config Versions
[**restore_application_alert_config**](ApplicationAlertConfigurationApi.md#restore_application_alert_config) | **PUT** /api/events/settings/application-alert-configs/{id}/restore/{created} | Restore Smart Alert Config
[**update_application_alert_config**](ApplicationAlertConfigurationApi.md#update_application_alert_config) | **POST** /api/events/settings/application-alert-configs/{id} | Update Smart Alert Config
[**update_application_historic_baseline**](ApplicationAlertConfigurationApi.md#update_application_historic_baseline) | **POST** /api/events/settings/application-alert-configs/{id}/update-baseline | Recalculate Smart Alert Config Baseline


# **create_application_alert_config**
> ApplicationAlertConfigWithMetadata create_application_alert_config(application_alert_config)

Create Smart Alert Config

Creates a new Smart Alert Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_alert_config import ApplicationAlertConfig
from instana_client.models.application_alert_config_with_metadata import ApplicationAlertConfigWithMetadata
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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    application_alert_config = {"name":"Calls are slower than usual","description":"Calls are slower or equal to the expectation based on latency (90th).","boundaryScope":"INBOUND","applicationId":"ZOi0te_ERE-mRm-9zsbwdg","applications":{"ZOi0te_ERE-mRm-9zsbwdg":{"applicationId":"ZOi0te_ERE-mRm-9zsbwdg","inclusive":true,"services":{}}},"severity":5,"triggering":false,"tagFilterExpression":{"type":"TAG_FILTER","name":"endpoint.name","stringValue":null,"numberValue":null,"booleanValue":null,"key":null,"value":null,"operator":"NOT_EMPTY","entity":"DESTINATION"},"includeInternal":false,"includeSynthetic":false,"rule":{"alertType":"slowness","aggregation":"P90","metricName":"latency"},"threshold":{"type":"historicBaseline","operator":">=","seasonality":"DAILY","baseline":[[0,1,3],[600000,1,3]],"deviationFactor":3,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"evaluationType":"PER_AP","customPayloadFields":[]} # ApplicationAlertConfig | 

    try:
        # Create Smart Alert Config
        api_response = api_instance.create_application_alert_config(application_alert_config)
        print("The response of ApplicationAlertConfigurationApi->create_application_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->create_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_alert_config** | [**ApplicationAlertConfig**](ApplicationAlertConfig.md)|  | 

### Return type

[**ApplicationAlertConfigWithMetadata**](ApplicationAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Alert Configuration created. |  -  |
**400** | Invalid Configuration. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_alert_config**
> delete_application_alert_config(id)

Delete Smart Alert Config

Deletes an Smart Alert Configuration.

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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to delete.

    try:
        # Delete Smart Alert Config
        api_instance.delete_application_alert_config(id)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->delete_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to delete. | 

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
**200** | Smart Alert Configuration deleted. |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_application_alert_config**
> disable_application_alert_config(id, body=body)

Disable Smart Alert Config

Disables an Smart Alert Configuration.

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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to disable.
    body = 'body_example' # str |  (optional)

    try:
        # Disable Smart Alert Config
        api_instance.disable_application_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->disable_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to disable. | 
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
**200** | Smart Alert Configuration disabled. |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_application_alert_config**
> enable_application_alert_config(id, body=body)

Enable Application Alert Config

Enables an Smart Alert Configuration.

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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to enable.
    body = 'body_example' # str |  (optional)

    try:
        # Enable Application Alert Config
        api_instance.enable_application_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->enable_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to enable. | 
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
**200** | Smart Alert Configuration enabled. |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_application_alert_configs**
> List[ApplicationAlertConfigWithMetadata] find_active_application_alert_configs(application_id, alert_ids=alert_ids)

Get all Smart Alert Configs

Gets all the Smart Alert Configurations pertaining to a specific application. Configurations are sorted by creation date in descending order.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_alert_config_with_metadata import ApplicationAlertConfigWithMetadata
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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    application_id = 'IYS1XOEcTNiT1eOD8pxgXg' # str | The ID of a specific Application.
    alert_ids = ['IYS1XOEcTNiT1eOD8pxgXg'] # List[str] | A list of Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. (optional)

    try:
        # Get all Smart Alert Configs
        api_response = api_instance.find_active_application_alert_configs(application_id, alert_ids=alert_ids)
        print("The response of ApplicationAlertConfigurationApi->find_active_application_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->find_active_application_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The ID of a specific Application. | 
 **alert_ids** | [**List[str]**](str.md)| A list of Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. | [optional] 

### Return type

[**List[ApplicationAlertConfigWithMetadata]**](ApplicationAlertConfigWithMetadata.md)

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
**404** | The requested application doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_application_alert_config**
> ApplicationAlertConfigWithMetadata find_application_alert_config(id, valid_on=valid_on)

Get Smart Alert Config

Gets a specific Smart Alert Configuration. This may return a deleted Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_alert_config_with_metadata import ApplicationAlertConfigWithMetadata
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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to retrieve.
    valid_on = 1706617456952 # int | A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  (optional)

    try:
        # Get Smart Alert Config
        api_response = api_instance.find_application_alert_config(id, valid_on=valid_on)
        print("The response of ApplicationAlertConfigurationApi->find_application_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->find_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to retrieve. | 
 **valid_on** | **int**| A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  | [optional] 

### Return type

[**ApplicationAlertConfigWithMetadata**](ApplicationAlertConfigWithMetadata.md)

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

# **find_application_alert_config_versions**
> List[ConfigVersion] find_application_alert_config_versions(id)

Get Smart Alert Config Versions

Gets all versions of an Smart Alert Configuration. This may return deleted Configurations. Configurations are sorted by creation date in descending order.

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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to retrieve.

    try:
        # Get Smart Alert Config Versions
        api_response = api_instance.find_application_alert_config_versions(id)
        print("The response of ApplicationAlertConfigurationApi->find_application_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->find_application_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to retrieve. | 

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

# **restore_application_alert_config**
> restore_application_alert_config(id, created, body=body)

Restore Smart Alert Config

Restores a deleted Smart Alert Configuration.

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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to restore.
    created = 1707726529124 # int | Unix timestamp representing the creation time of a specific Smart Alert Configuration.
    body = 'body_example' # str |  (optional)

    try:
        # Restore Smart Alert Config
        api_instance.restore_application_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->restore_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to restore. | 
 **created** | **int**| Unix timestamp representing the creation time of a specific Smart Alert Configuration. | 
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
**200** | Smart Alert Configuration restored. |  -  |
**400** | Invalid Configuration provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_alert_config**
> ApplicationAlertConfigWithMetadata update_application_alert_config(id, application_alert_config)

Update Smart Alert Config

Updates an existing Smart Alert Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_alert_config import ApplicationAlertConfig
from instana_client.models.application_alert_config_with_metadata import ApplicationAlertConfigWithMetadata
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
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to update.
    application_alert_config = {"name":"Calls are slower than usual","description":"Calls are slower or equal to the expectation based on latency (90th).","boundaryScope":"INBOUND","applicationId":"ZOi0te_ERE-mRm-9zsbwdg","applications":{"ZOi0te_ERE-mRm-9zsbwdg":{"applicationId":"ZOi0te_ERE-mRm-9zsbwdg","inclusive":true,"services":{}}},"severity":5,"triggering":false,"tagFilterExpression":{"type":"TAG_FILTER","name":"endpoint.name","stringValue":null,"numberValue":null,"booleanValue":null,"key":null,"value":null,"operator":"NOT_EMPTY","entity":"DESTINATION"},"includeInternal":false,"includeSynthetic":false,"rule":{"alertType":"slowness","aggregation":"P90","metricName":"latency"},"threshold":{"type":"historicBaseline","operator":">=","seasonality":"DAILY","baseline":[[0,1,3],[600000,1,3]],"deviationFactor":3,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"evaluationType":"PER_AP","customPayloadFields":[]} # ApplicationAlertConfig | 

    try:
        # Update Smart Alert Config
        api_response = api_instance.update_application_alert_config(id, application_alert_config)
        print("The response of ApplicationAlertConfigurationApi->update_application_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->update_application_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to update. | 
 **application_alert_config** | [**ApplicationAlertConfig**](ApplicationAlertConfig.md)|  | 

### Return type

[**ApplicationAlertConfigWithMetadata**](ApplicationAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Alert Configuration updated. |  -  |
**204** | Smart Alert Configuration did not change. |  -  |
**400** | Invalid Application ID provided. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable entity. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_historic_baseline**
> update_application_historic_baseline(id)

Recalculate Smart Alert Config Baseline

Recalculates and updates the historic baseline (static seasonal threshold) of a Configuration. The `LastUpdated` field of the Configuration is changed to the current time.

### Example


```python
import instana_client
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)


# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.ApplicationAlertConfigurationApi(api_client)
    id = 'DKp0JArJRAiQIav9CoKSWQ' # str | ID of a specific Smart Alert Configuration to recalculate.

    try:
        # Recalculate Smart Alert Config Baseline
        api_instance.update_application_historic_baseline(id)
    except Exception as e:
        print("Exception when calling ApplicationAlertConfigurationApi->update_application_historic_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Smart Alert Configuration to recalculate. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Alert Configuration baseline recalculated |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


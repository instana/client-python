# instana_client.LogAlertConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_alert_config**](LogAlertConfigurationApi.md#create_log_alert_config) | **POST** /api/events/settings/global-alert-configs/logs | Create Log Alert Config
[**delete_log_alert_config**](LogAlertConfigurationApi.md#delete_log_alert_config) | **DELETE** /api/events/settings/global-alert-configs/logs/{id} | Delete Log Alert Config
[**disable_log_alert_config**](LogAlertConfigurationApi.md#disable_log_alert_config) | **PUT** /api/events/settings/global-alert-configs/logs/{id}/disable | Disable Log Alert Config
[**enable_log_alert_config**](LogAlertConfigurationApi.md#enable_log_alert_config) | **PUT** /api/events/settings/global-alert-configs/logs/{id}/enable | Enable Log Alert Config
[**find_active_log_alert_configs**](LogAlertConfigurationApi.md#find_active_log_alert_configs) | **GET** /api/events/settings/global-alert-configs/logs | All Log Alert Configs
[**find_log_alert_config**](LogAlertConfigurationApi.md#find_log_alert_config) | **GET** /api/events/settings/global-alert-configs/logs/{id} | Get Log Alert Config
[**find_log_alert_config_versions**](LogAlertConfigurationApi.md#find_log_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/logs/{id}/versions | Get versions of Log Alert Config
[**restore_log_alert_config**](LogAlertConfigurationApi.md#restore_log_alert_config) | **PUT** /api/events/settings/global-alert-configs/logs/{id}/restore/{created} | Restore Log Alert Config
[**update_log_alert_config**](LogAlertConfigurationApi.md#update_log_alert_config) | **POST** /api/events/settings/global-alert-configs/logs/{id} | Update Log Alert Config


# **create_log_alert_config**
> LogAlertConfigWithMetadata create_log_alert_config(log_alert_config)

Create Log Alert Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.log_alert_config import LogAlertConfig
from instana_client.models.log_alert_config_with_metadata import LogAlertConfigWithMetadata
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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    log_alert_config = instana_client.LogAlertConfig() # LogAlertConfig | 

    try:
        # Create Log Alert Config
        api_response = api_instance.create_log_alert_config(log_alert_config)
        print("The response of LogAlertConfigurationApi->create_log_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->create_log_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_alert_config** | [**LogAlertConfig**](LogAlertConfig.md)|  | 

### Return type

[**LogAlertConfigWithMetadata**](LogAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_alert_config**
> delete_log_alert_config(id)

Delete Log Alert Config

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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Log Alert Config
        api_instance.delete_log_alert_config(id)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->delete_log_alert_config: %s\n" % e)
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
**204** | Log Alert Configuration deleted. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_log_alert_config**
> disable_log_alert_config(id, body=body)

Disable Log Alert Config

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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Disable Log Alert Config
        api_instance.disable_log_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->disable_log_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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
**204** | Log Alert Configuration disabled. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_log_alert_config**
> enable_log_alert_config(id, body=body)

Enable Log Alert Config

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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Enable Log Alert Config
        api_instance.enable_log_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->enable_log_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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
**204** | Log Alert Configuration enabled. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_log_alert_configs**
> List[LogAlertConfigWithMetadata] find_active_log_alert_configs(alert_ids=alert_ids)

All Log Alert Configs

Configs are sorted descending by their created date.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.log_alert_config_with_metadata import LogAlertConfigWithMetadata
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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    alert_ids = ['alert_ids_example'] # List[str] |  (optional)

    try:
        # All Log Alert Configs
        api_response = api_instance.find_active_log_alert_configs(alert_ids=alert_ids)
        print("The response of LogAlertConfigurationApi->find_active_log_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->find_active_log_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[LogAlertConfigWithMetadata]**](LogAlertConfigWithMetadata.md)

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

# **find_log_alert_config**
> LogAlertConfigWithMetadata find_log_alert_config(id, valid_on=valid_on)

Get Log Alert Config

Find a Log Alert Config by ID. This will deliver deleted configs too.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.log_alert_config_with_metadata import LogAlertConfigWithMetadata
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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 
    valid_on = 56 # int |  (optional)

    try:
        # Get Log Alert Config
        api_response = api_instance.find_log_alert_config(id, valid_on=valid_on)
        print("The response of LogAlertConfigurationApi->find_log_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->find_log_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **valid_on** | **int**|  | [optional] 

### Return type

[**LogAlertConfigWithMetadata**](LogAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_log_alert_config_versions**
> List[ConfigVersion] find_log_alert_config_versions(id)

Get versions of Log Alert Config

Find all versions of a Log Alert Config by ID. This will deliver deleted configs too. Configs are sorted descending by their created date.

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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get versions of Log Alert Config
        api_response = api_instance.find_log_alert_config_versions(id)
        print("The response of LogAlertConfigurationApi->find_log_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->find_log_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_log_alert_config**
> restore_log_alert_config(id, created, body=body)

Restore Log Alert Config

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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 
    created = 56 # int | 
    body = 'body_example' # str |  (optional)

    try:
        # Restore Log Alert Config
        api_instance.restore_log_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->restore_log_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **created** | **int**|  | 
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
**204** | Log Alert Configuration restored. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_alert_config**
> LogAlertConfigWithMetadata update_log_alert_config(id, log_alert_config)

Update Log Alert Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.log_alert_config import LogAlertConfig
from instana_client.models.log_alert_config_with_metadata import LogAlertConfigWithMetadata
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
    api_instance = instana_client.LogAlertConfigurationApi(api_client)
    id = 'id_example' # str | 
    log_alert_config = instana_client.LogAlertConfig() # LogAlertConfig | 

    try:
        # Update Log Alert Config
        api_response = api_instance.update_log_alert_config(id, log_alert_config)
        print("The response of LogAlertConfigurationApi->update_log_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogAlertConfigurationApi->update_log_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **log_alert_config** | [**LogAlertConfig**](LogAlertConfig.md)|  | 

### Return type

[**LogAlertConfigWithMetadata**](LogAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log Smart Alert successfully updated |  -  |
**204** | Log Smart Alert did not change |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


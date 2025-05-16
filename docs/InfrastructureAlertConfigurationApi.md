# instana_client.InfrastructureAlertConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_infra_alert_config**](InfrastructureAlertConfigurationApi.md#create_infra_alert_config) | **POST** /api/events/settings/infra-alert-configs | Create Infra Alert Config
[**delete_infra_alert_config**](InfrastructureAlertConfigurationApi.md#delete_infra_alert_config) | **DELETE** /api/events/settings/infra-alert-configs/{id} | Delete Infra Alert Config
[**disable_infra_alert_config**](InfrastructureAlertConfigurationApi.md#disable_infra_alert_config) | **PUT** /api/events/settings/infra-alert-configs/{id}/disable | Disable Infra Alert Config
[**enable_infra_alert_config**](InfrastructureAlertConfigurationApi.md#enable_infra_alert_config) | **PUT** /api/events/settings/infra-alert-configs/{id}/enable | Enable Infra Alert Config
[**find_active_infra_alert_configs**](InfrastructureAlertConfigurationApi.md#find_active_infra_alert_configs) | **GET** /api/events/settings/infra-alert-configs | All Infra Alert Configs
[**find_infra_alert_config**](InfrastructureAlertConfigurationApi.md#find_infra_alert_config) | **GET** /api/events/settings/infra-alert-configs/{id} | Get Infra Alert Config
[**find_infra_alert_config_versions**](InfrastructureAlertConfigurationApi.md#find_infra_alert_config_versions) | **GET** /api/events/settings/infra-alert-configs/{id}/versions | Get versions of Infra Alert Config
[**restore_infra_alert_config**](InfrastructureAlertConfigurationApi.md#restore_infra_alert_config) | **PUT** /api/events/settings/infra-alert-configs/{id}/restore/{created} | Restore Infra Alert Config
[**update_infra_alert_config**](InfrastructureAlertConfigurationApi.md#update_infra_alert_config) | **POST** /api/events/settings/infra-alert-configs/{id} | Update Infra Alert Config


# **create_infra_alert_config**
> InfraAlertConfigWithMetadata create_infra_alert_config(infra_alert_config)

Create Infra Alert Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.infra_alert_config import InfraAlertConfig
from instana_client.models.infra_alert_config_with_metadata import InfraAlertConfigWithMetadata
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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    infra_alert_config = instana_client.InfraAlertConfig() # InfraAlertConfig | 

    try:
        # Create Infra Alert Config
        api_response = api_instance.create_infra_alert_config(infra_alert_config)
        print("The response of InfrastructureAlertConfigurationApi->create_infra_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->create_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_alert_config** | [**InfraAlertConfig**](InfraAlertConfig.md)|  | 

### Return type

[**InfraAlertConfigWithMetadata**](InfraAlertConfigWithMetadata.md)

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

# **delete_infra_alert_config**
> delete_infra_alert_config(id)

Delete Infra Alert Config

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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration to delete

    try:
        # Delete Infra Alert Config
        api_instance.delete_infra_alert_config(id)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->delete_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration to delete | 

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

# **disable_infra_alert_config**
> disable_infra_alert_config(id, body=body)

Disable Infra Alert Config

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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration to disable
    body = 'body_example' # str |  (optional)

    try:
        # Disable Infra Alert Config
        api_instance.disable_infra_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->disable_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration to disable | 
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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_infra_alert_config**
> enable_infra_alert_config(id, body=body)

Enable Infra Alert Config

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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration to enable
    body = 'body_example' # str |  (optional)

    try:
        # Enable Infra Alert Config
        api_instance.enable_infra_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->enable_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration to enable | 
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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_infra_alert_configs**
> List[InfraAlertConfigWithMetadata] find_active_infra_alert_configs(alert_ids=alert_ids)

All Infra Alert Configs

Configs are sorted descending by their created date.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.infra_alert_config_with_metadata import InfraAlertConfigWithMetadata
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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    alert_ids = ['[4kxgJAXdSDiu6swQaKXrJw, ZLo28grvQaiMqIaikJK1RQ]'] # List[str] | List of IDs of Infra Smart Alert configurations (optional)

    try:
        # All Infra Alert Configs
        api_response = api_instance.find_active_infra_alert_configs(alert_ids=alert_ids)
        print("The response of InfrastructureAlertConfigurationApi->find_active_infra_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->find_active_infra_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_ids** | [**List[str]**](str.md)| List of IDs of Infra Smart Alert configurations | [optional] 

### Return type

[**List[InfraAlertConfigWithMetadata]**](InfraAlertConfigWithMetadata.md)

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

# **find_infra_alert_config**
> InfraAlertConfigWithMetadata find_infra_alert_config(id, valid_on=valid_on)

Get Infra Alert Config

Find a Infra Alert Config by ID. This will deliver deleted configs too.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.infra_alert_config_with_metadata import InfraAlertConfigWithMetadata
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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration
    valid_on = 1722877985000 # int | A Unix timestamp representing a specific time the config was active. If no timestamp is provided, the latest active version will be retrieved.  (optional)

    try:
        # Get Infra Alert Config
        api_response = api_instance.find_infra_alert_config(id, valid_on=valid_on)
        print("The response of InfrastructureAlertConfigurationApi->find_infra_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->find_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration | 
 **valid_on** | **int**| A Unix timestamp representing a specific time the config was active. If no timestamp is provided, the latest active version will be retrieved.  | [optional] 

### Return type

[**InfraAlertConfigWithMetadata**](InfraAlertConfigWithMetadata.md)

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

# **find_infra_alert_config_versions**
> List[ConfigVersion] find_infra_alert_config_versions(id)

Get versions of Infra Alert Config

Find all versions of a Infra Alert Config by ID. This will deliver deleted configs too. Configs are sorted descending by their created date.

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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration

    try:
        # Get versions of Infra Alert Config
        api_response = api_instance.find_infra_alert_config_versions(id)
        print("The response of InfrastructureAlertConfigurationApi->find_infra_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->find_infra_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_infra_alert_config**
> restore_infra_alert_config(id, created, body=body)

Restore Infra Alert Config

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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration to restore
    created = 1722877985000 # int | A Unix Timestamp of when the alert was created
    body = 'body_example' # str |  (optional)

    try:
        # Restore Infra Alert Config
        api_instance.restore_infra_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->restore_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration to restore | 
 **created** | **int**| A Unix Timestamp of when the alert was created | 
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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infra_alert_config**
> InfraAlertConfigWithMetadata update_infra_alert_config(id, infra_alert_config)

Update Infra Alert Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.infra_alert_config import InfraAlertConfig
from instana_client.models.infra_alert_config_with_metadata import InfraAlertConfigWithMetadata
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
    api_instance = instana_client.InfrastructureAlertConfigurationApi(api_client)
    id = '4kxgJAXdSDiu6swQaKXrJw' # str | ID of the Infra Smart Alert configuration to update
    infra_alert_config = instana_client.InfraAlertConfig() # InfraAlertConfig | 

    try:
        # Update Infra Alert Config
        api_response = api_instance.update_infra_alert_config(id, infra_alert_config)
        print("The response of InfrastructureAlertConfigurationApi->update_infra_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAlertConfigurationApi->update_infra_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Infra Smart Alert configuration to update | 
 **infra_alert_config** | [**InfraAlertConfig**](InfraAlertConfig.md)|  | 

### Return type

[**InfraAlertConfigWithMetadata**](InfraAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra Smart Alert successfully updated |  -  |
**204** | Infra Smart Alert did not change |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


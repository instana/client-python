# instana_client.SyntheticAlertConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#create_synthetic_alert_config) | **POST** /api/events/settings/global-alert-configs/synthetics | Create Synthetic Smart Alert Config
[**delete_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#delete_synthetic_alert_config) | **DELETE** /api/events/settings/global-alert-configs/synthetics/{id} | Delete Synthetic Smart Alert Config
[**disable_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#disable_synthetic_alert_config) | **PUT** /api/events/settings/global-alert-configs/synthetics/{id}/disable | Disable Synthetic Smart Alert Config
[**enable_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#enable_synthetic_alert_config) | **PUT** /api/events/settings/global-alert-configs/synthetics/{id}/enable | Enable Synthetic Smart Alert Config
[**find_active_synthetic_alert_configs**](SyntheticAlertConfigurationApi.md#find_active_synthetic_alert_configs) | **GET** /api/events/settings/global-alert-configs/synthetics | Get all Synthetic Smart Alert Configs
[**find_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#find_synthetic_alert_config) | **GET** /api/events/settings/global-alert-configs/synthetics/{id} | Get Synthetic Smart Alert Config
[**find_synthetic_alert_config_versions**](SyntheticAlertConfigurationApi.md#find_synthetic_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/synthetics/{id}/versions | Get Synthetic Smart Alert Config Versions
[**restore_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#restore_synthetic_alert_config) | **PUT** /api/events/settings/global-alert-configs/synthetics/{id}/restore/{created} | Restore Synthetic Smart Alert Config
[**update_synthetic_alert_config**](SyntheticAlertConfigurationApi.md#update_synthetic_alert_config) | **POST** /api/events/settings/global-alert-configs/synthetics/{id} | Update Synthetic Smart Alert Config


# **create_synthetic_alert_config**
> SyntheticAlertConfigWithMetadata create_synthetic_alert_config(synthetic_alert_config)

Create Synthetic Smart Alert Config

Creates a new Synthetic Smart Alert Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_alert_config import SyntheticAlertConfig
from instana_client.models.synthetic_alert_config_with_metadata import SyntheticAlertConfigWithMetadata
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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    synthetic_alert_config = {"name":"2 consecutive failures of ${synthetic.testName} at locations${synthetic.locationLabel}","description":"Alert created without test but with AppId - Synthetic test failed for 2 consecutive times","syntheticTestIds":["ic25Vt1T5dgKzi0K7812","2gBxQz3oKtXgFXzRoQ6O"],"severity":5,"tagFilterExpression":{"type":"TAG_FILTER","name":"synthetic.applicationId","stringValue":"2BPCBLz_RBG8J6mjyuxm6w","numberValue":null,"booleanValue":null,"key":null,"value":"2BPCBLz_RBG8J6mjyuxm6w","operator":"EQUALS","entity":"NOT_APPLICABLE"},"rule":{"alertType":"failure","metricName":"status","aggregation":"SUM"},"alertChannelIds":["0o1ISHPfR8-N4iUK"],"timeThreshold":{"type":"violationsInSequence","violationsCount":2},"customPayloadFields":[]} # SyntheticAlertConfig | 

    try:
        # Create Synthetic Smart Alert Config
        api_response = api_instance.create_synthetic_alert_config(synthetic_alert_config)
        print("The response of SyntheticAlertConfigurationApi->create_synthetic_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->create_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_alert_config** | [**SyntheticAlertConfig**](SyntheticAlertConfig.md)|  | 

### Return type

[**SyntheticAlertConfigWithMetadata**](SyntheticAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synthetic Smart Alert Configuration created. |  -  |
**400** | Invalid configuration. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_synthetic_alert_config**
> delete_synthetic_alert_config(id)

Delete Synthetic Smart Alert Config

Deletes a Synthetic Smart Alert Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = '2K1YQIeaSQKIcIkHPH7D3g' # str | ID of a specific Synthetic Smart Alert Configuration to delete.

    try:
        # Delete Synthetic Smart Alert Config
        api_instance.delete_synthetic_alert_config(id)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->delete_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to delete. | 

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
**204** | Synthetic Smart Alert Configuration deleted. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_synthetic_alert_config**
> disable_synthetic_alert_config(id, body=body)

Disable Synthetic Smart Alert Config

Disables a Synthetic Smart Alert Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = '2K1YQIeaSQKIcIkHPH7D3g' # str | ID of a specific Synthetic Smart Alert Configuration to disable.
    body = 'body_example' # str |  (optional)

    try:
        # Disable Synthetic Smart Alert Config
        api_instance.disable_synthetic_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->disable_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to disable. | 
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
**204** | Synthetic Smart Alert Configuration disabled. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_synthetic_alert_config**
> enable_synthetic_alert_config(id, body=body)

Enable Synthetic Smart Alert Config

Enables a Synthetic Smart Alert Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = '2K1YQIeaSQKIcIkHPH7D3g' # str | ID of a specific Synthetic Smart Alert Configuration to enable.
    body = 'body_example' # str |  (optional)

    try:
        # Enable Synthetic Smart Alert Config
        api_instance.enable_synthetic_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->enable_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to enable. | 
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
**204** | Synthetic Smart Alert Configuration enabled. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration ID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_synthetic_alert_configs**
> List[SyntheticAlertConfigWithMetadata] find_active_synthetic_alert_configs(synthetic_test_id=synthetic_test_id, alert_ids=alert_ids)

Get all Synthetic Smart Alert Configs

Gets all the Synthetic Smart Alert Configuration pertaining to a specific synthetic test. Configurations are sorted by creation date in descending order.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_alert_config_with_metadata import SyntheticAlertConfigWithMetadata
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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    synthetic_test_id = 'ic25Vt1T5dgKzi0K7812' # str | The ID of a specific Synthetic Test.  (optional)
    alert_ids = ['smRTFp08juKWtn8I'] # List[str] | A list of Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. (optional)

    try:
        # Get all Synthetic Smart Alert Configs
        api_response = api_instance.find_active_synthetic_alert_configs(synthetic_test_id=synthetic_test_id, alert_ids=alert_ids)
        print("The response of SyntheticAlertConfigurationApi->find_active_synthetic_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->find_active_synthetic_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_test_id** | **str**| The ID of a specific Synthetic Test.  | [optional] 
 **alert_ids** | [**List[str]**](str.md)| A list of Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. | [optional] 

### Return type

[**List[SyntheticAlertConfigWithMetadata]**](SyntheticAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Returns empty result if syntheticTestId is invalid. |  -  |
**403** | Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_synthetic_alert_config**
> SyntheticAlertConfigWithMetadata find_synthetic_alert_config(id, valid_on=valid_on)

Get Synthetic Smart Alert Config

Gets a specific Synthetic Smart Alert Configuration. This may return a deleted Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_alert_config_with_metadata import SyntheticAlertConfigWithMetadata
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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = 'qgEwvI0vRfe3Al_D7T7LSA' # str | ID of a specific Synthetic Smart Alert Configuration to retrieve.
    valid_on = 1707149760053 # int | A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  (optional)

    try:
        # Get Synthetic Smart Alert Config
        api_response = api_instance.find_synthetic_alert_config(id, valid_on=valid_on)
        print("The response of SyntheticAlertConfigurationApi->find_synthetic_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->find_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to retrieve. | 
 **valid_on** | **int**| A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  | [optional] 

### Return type

[**SyntheticAlertConfigWithMetadata**](SyntheticAlertConfigWithMetadata.md)

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

# **find_synthetic_alert_config_versions**
> List[ConfigVersion] find_synthetic_alert_config_versions(id)

Get Synthetic Smart Alert Config Versions

Gets all versions of a Synthetic Smart Alert Configuration. This may return deleted Configurations. Configurations are sorted by creation date in descending order.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = 'qgEwvI0vRfe3Al_D7T7LSA' # str | ID of a specific Synthetic Smart Alert Configuration to retrieve.

    try:
        # Get Synthetic Smart Alert Config Versions
        api_response = api_instance.find_synthetic_alert_config_versions(id)
        print("The response of SyntheticAlertConfigurationApi->find_synthetic_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->find_synthetic_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to retrieve. | 

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

# **restore_synthetic_alert_config**
> restore_synthetic_alert_config(id, created, body=body)

Restore Synthetic Smart Alert Config

Restores a deleted Synthetic Smart Alert Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = '2K1YQIeaSQKIcIkHPH7D3g' # str | ID of a specific Synthetic Smart Alert Configuration to restore.
    created = 1707726529124 # int | Unix timestamp representing the creation time of a specific Synthetic Smart Alert Configuration.
    body = 'body_example' # str |  (optional)

    try:
        # Restore Synthetic Smart Alert Config
        api_instance.restore_synthetic_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->restore_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to restore. | 
 **created** | **int**| Unix timestamp representing the creation time of a specific Synthetic Smart Alert Configuration. | 
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
**204** | Synthetic Smart Alert Configuration restored. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Invalid Configuration provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_synthetic_alert_config**
> SyntheticAlertConfigWithMetadata update_synthetic_alert_config(id, synthetic_alert_config)

Update Synthetic Smart Alert Config

Updates an existing Synthetic Smart Alert Configuration.
For more information on Synthetic Alert Configuration please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-alert-configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_alert_config import SyntheticAlertConfig
from instana_client.models.synthetic_alert_config_with_metadata import SyntheticAlertConfigWithMetadata
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
    api_instance = instana_client.SyntheticAlertConfigurationApi(api_client)
    id = 'qgEwvI0vRfe3Al_D7T7LSA' # str | ID of a specific Synthetic Smart Alert Configuration to update.
    synthetic_alert_config = {"name":"2 consecutive failures of ${synthetic.testName} at locations${synthetic.locationLabel}","description":"Alert created without test but with AppId - Synthetic test failed for 2 consecutive times","syntheticTestIds":["ic25Vt1T5dgKzi0K7812","2gBxQz3oKtXgFXzRoQ6O"],"severity":5,"tagFilterExpression":{"type":"TAG_FILTER","name":"synthetic.applicationId","stringValue":"2BPCBLz_RBG8J6mjyuxm6w","numberValue":null,"booleanValue":null,"key":null,"value":"2BPCBLz_RBG8J6mjyuxm6w","operator":"EQUALS","entity":"NOT_APPLICABLE"},"rule":{"alertType":"failure","metricName":"status","aggregation":"SUM"},"alertChannelIds":["0o1ISHPfR8-N4iUK"],"timeThreshold":{"type":"violationsInSequence","violationsCount":2},"customPayloadFields":[]} # SyntheticAlertConfig | 

    try:
        # Update Synthetic Smart Alert Config
        api_response = api_instance.update_synthetic_alert_config(id, synthetic_alert_config)
        print("The response of SyntheticAlertConfigurationApi->update_synthetic_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticAlertConfigurationApi->update_synthetic_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Synthetic Smart Alert Configuration to update. | 
 **synthetic_alert_config** | [**SyntheticAlertConfig**](SyntheticAlertConfig.md)|  | 

### Return type

[**SyntheticAlertConfigWithMetadata**](SyntheticAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synthetic Smart Alert Configuration updated |  -  |
**204** | Synthetic Smart Alert Configuration did not change |  -  |
**400** | Invalid Configuration ID provided. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable entity. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


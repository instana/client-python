# instana_client.MaintenanceConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_maintenance_config**](MaintenanceConfigurationApi.md#delete_maintenance_config) | **DELETE** /api/settings/maintenance/{id} | Delete maintenance configuration
[**delete_maintenance_config_v2**](MaintenanceConfigurationApi.md#delete_maintenance_config_v2) | **DELETE** /api/settings/v2/maintenance/{id} | Delete maintenance configuration
[**get_maintenance_config**](MaintenanceConfigurationApi.md#get_maintenance_config) | **GET** /api/settings/maintenance/{id} | Maintenance configuration
[**get_maintenance_config_v2**](MaintenanceConfigurationApi.md#get_maintenance_config_v2) | **GET** /api/settings/v2/maintenance/{id} | Get maintenance configuration
[**get_maintenance_configs**](MaintenanceConfigurationApi.md#get_maintenance_configs) | **GET** /api/settings/maintenance | All maintenance configurations
[**get_maintenance_configs_v2**](MaintenanceConfigurationApi.md#get_maintenance_configs_v2) | **GET** /api/settings/v2/maintenance | All maintenance configurations
[**pause_recurrent_maintenance_configuration**](MaintenanceConfigurationApi.md#pause_recurrent_maintenance_configuration) | **PUT** /api/settings/v2/maintenance/{id}/pause | Pause maintenance configuration
[**put_maintenance_config**](MaintenanceConfigurationApi.md#put_maintenance_config) | **PUT** /api/settings/maintenance/{id} | Create or update maintenance configuration
[**put_maintenance_config_v2**](MaintenanceConfigurationApi.md#put_maintenance_config_v2) | **PUT** /api/settings/v2/maintenance/{id} | Create or update maintenance configuration
[**resume_recurrent_maintenance_configuration**](MaintenanceConfigurationApi.md#resume_recurrent_maintenance_configuration) | **PUT** /api/settings/v2/maintenance/{id}/resume | Resume maintenance configuration


# **delete_maintenance_config**
> delete_maintenance_config(id)

Delete maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = 'MPhKWoXRp0PBelqk' # str | ID of the Maintenance Window Configuration to delete.

    try:
        # Delete maintenance configuration
        api_instance.delete_maintenance_config(id)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->delete_maintenance_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Maintenance Window Configuration to delete. | 

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

# **delete_maintenance_config_v2**
> delete_maintenance_config_v2(id)

Delete maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = '8924aa6b' # str | Id of the Maintenance Window configuration to delete.

    try:
        # Delete maintenance configuration
        api_instance.delete_maintenance_config_v2(id)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->delete_maintenance_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Maintenance Window configuration to delete. | 

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

# **get_maintenance_config**
> MaintenanceConfigWithLastUpdated get_maintenance_config(id)

Maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.maintenance_config_with_last_updated import MaintenanceConfigWithLastUpdated
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = 'MPhKWoXRp0PBelqk' # str | ID of the Maintenance Window Configuration to get.

    try:
        # Maintenance configuration
        api_response = api_instance.get_maintenance_config(id)
        print("The response of MaintenanceConfigurationApi->get_maintenance_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->get_maintenance_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Maintenance Window Configuration to get. | 

### Return type

[**MaintenanceConfigWithLastUpdated**](MaintenanceConfigWithLastUpdated.md)

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

# **get_maintenance_config_v2**
> MaintenanceConfigV2WithStateAndOccurrence get_maintenance_config_v2(id)

Get maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.maintenance_config_v2_with_state_and_occurrence import MaintenanceConfigV2WithStateAndOccurrence
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = '8924aa6b' # str | Id of the Maintenance Window Configuration to get.

    try:
        # Get maintenance configuration
        api_response = api_instance.get_maintenance_config_v2(id)
        print("The response of MaintenanceConfigurationApi->get_maintenance_config_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->get_maintenance_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Maintenance Window Configuration to get. | 

### Return type

[**MaintenanceConfigV2WithStateAndOccurrence**](MaintenanceConfigV2WithStateAndOccurrence.md)

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

# **get_maintenance_configs**
> List[ValidatedMaintenanceConfigWithStatus] get_maintenance_configs()

All maintenance configurations


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.validated_maintenance_config_with_status import ValidatedMaintenanceConfigWithStatus
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)

    try:
        # All maintenance configurations
        api_response = api_instance.get_maintenance_configs()
        print("The response of MaintenanceConfigurationApi->get_maintenance_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->get_maintenance_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ValidatedMaintenanceConfigWithStatus]**](ValidatedMaintenanceConfigWithStatus.md)

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

# **get_maintenance_configs_v2**
> List[ValidatedMaintenanceConfigV2WithStateAndOccurrence] get_maintenance_configs_v2()

All maintenance configurations


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.validated_maintenance_config_v2_with_state_and_occurrence import ValidatedMaintenanceConfigV2WithStateAndOccurrence
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)

    try:
        # All maintenance configurations
        api_response = api_instance.get_maintenance_configs_v2()
        print("The response of MaintenanceConfigurationApi->get_maintenance_configs_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->get_maintenance_configs_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ValidatedMaintenanceConfigV2WithStateAndOccurrence]**](ValidatedMaintenanceConfigV2WithStateAndOccurrence.md)

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

# **pause_recurrent_maintenance_configuration**
> MaintenanceConfigV2WithStateAndOccurrence pause_recurrent_maintenance_configuration(id)

Pause maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.maintenance_config_v2_with_state_and_occurrence import MaintenanceConfigV2WithStateAndOccurrence
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = '8924aa6b' # str | Id of the Maintenance Window configuration to pause.

    try:
        # Pause maintenance configuration
        api_response = api_instance.pause_recurrent_maintenance_configuration(id)
        print("The response of MaintenanceConfigurationApi->pause_recurrent_maintenance_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->pause_recurrent_maintenance_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Maintenance Window configuration to pause. | 

### Return type

[**MaintenanceConfigV2WithStateAndOccurrence**](MaintenanceConfigV2WithStateAndOccurrence.md)

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

# **put_maintenance_config**
> put_maintenance_config(id, maintenance_config)

Create or update maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.maintenance_config import MaintenanceConfig
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = 'MPhKWoXRp0PBelqk' # str | ID of the Maintenance Window Configuration to update.
    maintenance_config = instana_client.MaintenanceConfig() # MaintenanceConfig | 

    try:
        # Create or update maintenance configuration
        api_instance.put_maintenance_config(id, maintenance_config)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->put_maintenance_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Maintenance Window Configuration to update. | 
 **maintenance_config** | [**MaintenanceConfig**](MaintenanceConfig.md)|  | 

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
**200** | Maintenance config has been created or updated, and successfully scheduled immediately if needed |  -  |
**202** | Maintenance config has been created or updated, but could not to be scheduled immediately. It will therefore be scheduled during the next auto-refresh with a delay of up to 4 minutes. |  -  |
**400** | Invalid JSON or mismatching IDs have been provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_maintenance_config_v2**
> put_maintenance_config_v2(id, maintenance_config_v2)

Create or update maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.maintenance_config_v2 import MaintenanceConfigV2
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = '8924aa6b' # str | Id of the Maintenance Window configuration to update.
    maintenance_config_v2 = instana_client.MaintenanceConfigV2() # MaintenanceConfigV2 | 

    try:
        # Create or update maintenance configuration
        api_instance.put_maintenance_config_v2(id, maintenance_config_v2)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->put_maintenance_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Maintenance Window configuration to update. | 
 **maintenance_config_v2** | [**MaintenanceConfigV2**](MaintenanceConfigV2.md)|  | 

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
**200** | Maintenance config has been created or updated, and successfully scheduled immediately if needed |  -  |
**202** | Maintenance config has been created or updated, but could not to be scheduled immediately. It will therefore be scheduled during the next auto-refresh with a delay of up to 4 minutes. |  -  |
**400** | The provided maintenance configuration is invalid. |  -  |
**422** | The provided maintenance configuration is incomplete or cannot be processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_recurrent_maintenance_configuration**
> MaintenanceConfigV2WithStateAndOccurrence resume_recurrent_maintenance_configuration(id)

Resume maintenance configuration


For more information on Maintenance Configurations please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#maintenance-configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.maintenance_config_v2_with_state_and_occurrence import MaintenanceConfigV2WithStateAndOccurrence
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
    api_instance = instana_client.MaintenanceConfigurationApi(api_client)
    id = '8924aa6b' # str | Id of the Maintenance Window configuration to resume.

    try:
        # Resume maintenance configuration
        api_response = api_instance.resume_recurrent_maintenance_configuration(id)
        print("The response of MaintenanceConfigurationApi->resume_recurrent_maintenance_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceConfigurationApi->resume_recurrent_maintenance_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Maintenance Window configuration to resume. | 

### Return type

[**MaintenanceConfigV2WithStateAndOccurrence**](MaintenanceConfigV2WithStateAndOccurrence.md)

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


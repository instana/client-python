# instana_client.ApdexSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_apdex_configuration**](ApdexSettingsApi.md#create_apdex_configuration) | **POST** /api/settings/apdex | Create Apdex Configuration
[**delete_apdex_configuration**](ApdexSettingsApi.md#delete_apdex_configuration) | **DELETE** /api/settings/apdex/{id} | Delete Apdex Configuration
[**get_all_apdex_configurations**](ApdexSettingsApi.md#get_all_apdex_configurations) | **GET** /api/settings/apdex | Get All Apdex Configurations
[**get_apdex_configuration**](ApdexSettingsApi.md#get_apdex_configuration) | **GET** /api/settings/apdex/{id} | Get Apdex Configuration
[**get_apdex_configurations_for_entity_type_and_id**](ApdexSettingsApi.md#get_apdex_configurations_for_entity_type_and_id) | **GET** /api/settings/apdex/{entityType}/{entityId} | Get all Apdex configurations for entity type and entity id


# **create_apdex_configuration**
> ApdexConfiguration create_apdex_configuration(apdex_configuration_input)

Create Apdex Configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_configuration import ApdexConfiguration
from instana_client.models.apdex_configuration_input import ApdexConfigurationInput
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
    api_instance = instana_client.ApdexSettingsApi(api_client)
    apdex_configuration_input = [{"apdexName":"Apdex Configuration One","apdexEntity":{"apdexType":"website","entityId":"XIZGGVT1TX2O-0OFeT2Yig","threshold":400,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"beaconType":"httpRequest"}}] # ApdexConfigurationInput | 

    try:
        # Create Apdex Configuration
        api_response = api_instance.create_apdex_configuration(apdex_configuration_input)
        print("The response of ApdexSettingsApi->create_apdex_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->create_apdex_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apdex_configuration_input** | [**ApdexConfigurationInput**](ApdexConfigurationInput.md)|  | 

### Return type

[**ApdexConfiguration**](ApdexConfiguration.md)

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

# **delete_apdex_configuration**
> delete_apdex_configuration(id)

Delete Apdex Configuration

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
    api_instance = instana_client.ApdexSettingsApi(api_client)
    id = 'NCAoNKqySWSK1U5GkmyZgQ' # str | Apdex Configuration ID

    try:
        # Delete Apdex Configuration
        api_instance.delete_apdex_configuration(id)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->delete_apdex_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Apdex Configuration ID | 

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
**204** | Apdex Configuration Deleted Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_apdex_configurations**
> List[ApdexConfiguration] get_all_apdex_configurations()

Get All Apdex Configurations

API to Get All Apdex Configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_configuration import ApdexConfiguration
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
    api_instance = instana_client.ApdexSettingsApi(api_client)

    try:
        # Get All Apdex Configurations
        api_response = api_instance.get_all_apdex_configurations()
        print("The response of ApdexSettingsApi->get_all_apdex_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_all_apdex_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApdexConfiguration]**](ApdexConfiguration.md)

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

# **get_apdex_configuration**
> ApdexConfiguration get_apdex_configuration(id)

Get Apdex Configuration

API to Get Apdex Configuration for specified ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_configuration import ApdexConfiguration
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
    api_instance = instana_client.ApdexSettingsApi(api_client)
    id = 'NCAoNKqySWSK1U5GkmyZgQ' # str | Apdex Configuration ID

    try:
        # Get Apdex Configuration
        api_response = api_instance.get_apdex_configuration(id)
        print("The response of ApdexSettingsApi->get_apdex_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_apdex_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Apdex Configuration ID | 

### Return type

[**ApdexConfiguration**](ApdexConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Apdex Configuration not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apdex_configurations_for_entity_type_and_id**
> List[ApdexConfiguration] get_apdex_configurations_for_entity_type_and_id(entity_type, entity_id)

Get all Apdex configurations for entity type and entity id

API to Get All Apdex Configurations for specified entity type and entity id.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_configuration import ApdexConfiguration
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
    api_instance = instana_client.ApdexSettingsApi(api_client)
    entity_type = 'APPLICATION' # str | Type of the Apdex Configuration, it could be APPLICATION or WEBSITE
    entity_id = 'XIZGGVT1TX2O-0OFeT2Yig' # str | Application or Website ID

    try:
        # Get all Apdex configurations for entity type and entity id
        api_response = api_instance.get_apdex_configurations_for_entity_type_and_id(entity_type, entity_id)
        print("The response of ApdexSettingsApi->get_apdex_configurations_for_entity_type_and_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_apdex_configurations_for_entity_type_and_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Type of the Apdex Configuration, it could be APPLICATION or WEBSITE | 
 **entity_id** | **str**| Application or Website ID | 

### Return type

[**List[ApdexConfiguration]**](ApdexConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


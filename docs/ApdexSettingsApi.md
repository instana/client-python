# instana_client.ApdexSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_apdex_configuration**](ApdexSettingsApi.md#create_apdex_configuration) | **POST** /api/settings/apdex | Create Apdex Configuration
[**create_apdex_configuration_v2**](ApdexSettingsApi.md#create_apdex_configuration_v2) | **POST** /api/settings/apdex/v2 | Create Apdex Configuration
[**delete_apdex_configuration**](ApdexSettingsApi.md#delete_apdex_configuration) | **DELETE** /api/settings/apdex/{id} | Delete Apdex Configuration
[**delete_apdex_configuration_v2**](ApdexSettingsApi.md#delete_apdex_configuration_v2) | **DELETE** /api/settings/apdex/v2/{id} | Delete Apdex Configuration
[**get_all_apdex_config_levels_v2**](ApdexSettingsApi.md#get_all_apdex_config_levels_v2) | **GET** /api/settings/apdex/v2/apdex-levels | Get All Apdex Levels
[**get_all_apdex_config_tags_v2**](ApdexSettingsApi.md#get_all_apdex_config_tags_v2) | **GET** /api/settings/apdex/v2/tags | Get All Apdex Config tags
[**get_all_apdex_configurations**](ApdexSettingsApi.md#get_all_apdex_configurations) | **GET** /api/settings/apdex | Get All Apdex Configurations
[**get_all_apdex_configurations_v2**](ApdexSettingsApi.md#get_all_apdex_configurations_v2) | **GET** /api/settings/apdex/v2 | Get All Apdex Configurations
[**get_apdex_configuration**](ApdexSettingsApi.md#get_apdex_configuration) | **GET** /api/settings/apdex/{id} | Get Apdex Configuration
[**get_apdex_configuration_v2**](ApdexSettingsApi.md#get_apdex_configuration_v2) | **GET** /api/settings/apdex/v2/{id} | Get Apdex Configuration
[**get_apdex_configurations_for_entity_type_and_id**](ApdexSettingsApi.md#get_apdex_configurations_for_entity_type_and_id) | **GET** /api/settings/apdex/{entityType}/{entityId} | Get all Apdex configurations for entity type and entity id
[**update_apdex_config_v2**](ApdexSettingsApi.md#update_apdex_config_v2) | **PUT** /api/settings/apdex/v2/{id} | Update an existing Apdex Config


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

# **create_apdex_configuration_v2**
> ApdexConfiguration create_apdex_configuration_v2(apdex_configuration_input)

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
        api_response = api_instance.create_apdex_configuration_v2(apdex_configuration_input)
        print("The response of ApdexSettingsApi->create_apdex_configuration_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->create_apdex_configuration_v2: %s\n" % e)
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

# **delete_apdex_configuration_v2**
> delete_apdex_configuration_v2(id)

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
        api_instance.delete_apdex_configuration_v2(id)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->delete_apdex_configuration_v2: %s\n" % e)
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

# **get_all_apdex_config_levels_v2**
> List[ApdexLevel] get_all_apdex_config_levels_v2()

Get All Apdex Levels

Returns the Apdex satisfaction level definitions with their thresholds

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_level import ApdexLevel
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
        # Get All Apdex Levels
        api_response = api_instance.get_all_apdex_config_levels_v2()
        print("The response of ApdexSettingsApi->get_all_apdex_config_levels_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_all_apdex_config_levels_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApdexLevel]**](ApdexLevel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched list of Apdex Levels Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_apdex_config_tags_v2**
> List[str] get_all_apdex_config_tags_v2(query=query, tag=tag, entity_type=entity_type)

Get All Apdex Config tags

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
    query = 'test Apdex' # str |  (optional)
    tag = ['Testing'] # List[str] |  (optional)
    entity_type = 'APPLICATION' # str |  (optional)

    try:
        # Get All Apdex Config tags
        api_response = api_instance.get_all_apdex_config_tags_v2(query=query, tag=tag, entity_type=entity_type)
        print("The response of ApdexSettingsApi->get_all_apdex_config_tags_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_all_apdex_config_tags_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **tag** | [**List[str]**](str.md)|  | [optional] 
 **entity_type** | **str**|  | [optional] 

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched list of Apdex Configuration tags Successfully |  -  |

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

# **get_all_apdex_configurations_v2**
> List[ApdexConfiguration] get_all_apdex_configurations_v2(page_size=page_size, page=page, order_by=order_by, order_direction=order_direction, query=query, grouped=grouped, refresh=refresh, var_from=var_from, to=to, entity_type=entity_type, entity_id=entity_id)

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
    page_size = 1 # int |  (optional)
    page = 1 # int |  (optional)
    order_by = 'name' # str |  (optional)
    order_direction = 'ASC' # str |  (optional)
    query = 'test' # str |  (optional)
    grouped = false # bool |  (optional)
    refresh = false # bool |  (optional)
    var_from = 1705411200000 # int |  (optional)
    to = 1705414800000 # int |  (optional)
    entity_type = 'APPLICATION' # str |  (optional)
    entity_id = 'XIZGGVT1TX2O-0OFeT2Yig' # str |  (optional)

    try:
        # Get All Apdex Configurations
        api_response = api_instance.get_all_apdex_configurations_v2(page_size=page_size, page=page, order_by=order_by, order_direction=order_direction, query=query, grouped=grouped, refresh=refresh, var_from=var_from, to=to, entity_type=entity_type, entity_id=entity_id)
        print("The response of ApdexSettingsApi->get_all_apdex_configurations_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_all_apdex_configurations_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **order_direction** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **grouped** | **bool**|  | [optional] 
 **refresh** | **bool**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **entity_type** | **str**|  | [optional] 
 **entity_id** | **str**|  | [optional] 

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

# **get_apdex_configuration_v2**
> ApdexConfiguration get_apdex_configuration_v2(id)

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
        api_response = api_instance.get_apdex_configuration_v2(id)
        print("The response of ApdexSettingsApi->get_apdex_configuration_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->get_apdex_configuration_v2: %s\n" % e)
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

# **update_apdex_config_v2**
> SLOConfigWithRBACTag update_apdex_config_v2(id, apdex_configuration)

Update an existing Apdex Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_configuration import ApdexConfiguration
from instana_client.models.slo_config_with_rbac_tag import SLOConfigWithRBACTag
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
    id = 'APD0jhg2CWmR_iPYtg-iTOzPw' # str | 
    apdex_configuration = [{"apdexName":"Apdex Configuration One","apdexEntity":{"apdexType":"website","entityId":"XIZGGVT1TX2O-0OFeT2Yig","threshold":400,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"beaconType":"httpRequest"}}] # ApdexConfiguration | 

    try:
        # Update an existing Apdex Config
        api_response = api_instance.update_apdex_config_v2(id, apdex_configuration)
        print("The response of ApdexSettingsApi->update_apdex_config_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexSettingsApi->update_apdex_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **apdex_configuration** | [**ApdexConfiguration**](ApdexConfiguration.md)|  | 

### Return type

[**SLOConfigWithRBACTag**](SLOConfigWithRBACTag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated SLO Configuration Successfully |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# instana_client.SLISettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sli_config**](SLISettingsApi.md#create_sli_config) | **POST** /api/settings/sli | Create SLI Config
[**create_sli_config_v2**](SLISettingsApi.md#create_sli_config_v2) | **POST** /api/settings/v2/sli | Create SLI Config
[**delete_sli_config**](SLISettingsApi.md#delete_sli_config) | **DELETE** /api/settings/sli/{id} | Delete SLI Config
[**delete_sli_config_v2**](SLISettingsApi.md#delete_sli_config_v2) | **DELETE** /api/settings/v2/sli/{id} | Delete SLI Config
[**get_all_sli_configs**](SLISettingsApi.md#get_all_sli_configs) | **GET** /api/settings/sli | Get All SLI Configs
[**get_all_sli_configs_v2**](SLISettingsApi.md#get_all_sli_configs_v2) | **GET** /api/settings/v2/sli | Get All SLI Configs
[**get_sli_config**](SLISettingsApi.md#get_sli_config) | **GET** /api/settings/sli/{id} | Get SLI Config
[**get_sli_config_v2**](SLISettingsApi.md#get_sli_config_v2) | **GET** /api/settings/v2/sli/{id} | Get SLI Config
[**get_sli_configs_for_entity_type_and_id_v2**](SLISettingsApi.md#get_sli_configs_for_entity_type_and_id_v2) | **GET** /api/settings/v2/sli/{entityType}/{entityId} | Get all SLI configs for entity type and entity id
[**update_sli_config**](SLISettingsApi.md#update_sli_config) | **PUT** /api/settings/sli/{id} | Update SLI Config


# **create_sli_config**
> SliConfigurationWithLastUpdated create_sli_config(sli_configuration)

Create SLI Config

This endpoint creates the Service Level Indicator Configuration  ## Mandatory Parameters:  - **id** A unique identifier for each SLI configuration  - **sliName:** Name for the SLI configuration  - **sliEntity:** Entity of the SLI configuration  ### SLI Entity specific parameters  Depending on the chosen `sliType` in the `sliEntity`, there are further required parameters:  #### Application SLI entity  This option can be used to create a Time-Based SLI  - **sliEntity.applicationId:** The Id of the Application Perspective  - **sliEntity.boundaryScope:** Boundary scope of the Application Perspective  - **metricConfiguration.metricName:** The metric name on which to compute the SLI  - **metricConfiguration.metricAggregation:** The aggregation of the metric  - **metricConfiguration.threshold:** Threshold for the metric  #### Availability SLI entity  This opetion can be used to create an Event-Based SLI  - **sliEntity.applicationId:** The Id of the Application Perspective  - **sliEntity.boundaryScope:** Boundary scope of the Application Perspective  ## Deprecated Parameters for Availability SLI entity:  - **sliEntity.serviceId:** The ID if the Service in he context of an Application Perspective  - **sliEntity.endpointId:** The ID of an Endpoint belonging to a Service  - **sliEntity.goodEventFilters:** The list of TagFilters to match good events / calls  - **sliEntity.badEventFilters:** The list of TagFilters to match bad events / calls  All of these filters can be included using the list of TagFilterExpressions via **sliEntity.goodEventFilterExpression** and **sliEntity.badEventFilterExpression**. These parameters will be removed in the upcoming releases. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration import SliConfiguration
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)
    sli_configuration = {"sliName":"test-application-sli","metricConfiguration":{"metricName":"latency","metricAggregation":"P90","threshold":555},"sliEntity":{"sliType":"application","applicationId":"btg-B709IU6o9QNXUS4TVw","serviceId":null,"endpointId":null,"boundaryScope":"INBOUND"}} # SliConfiguration | 

    try:
        # Create SLI Config
        api_response = api_instance.create_sli_config(sli_configuration)
        print("The response of SLISettingsApi->create_sli_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->create_sli_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sli_configuration** | [**SliConfiguration**](SliConfiguration.md)|  | 

### Return type

[**SliConfigurationWithLastUpdated**](SliConfigurationWithLastUpdated.md)

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

# **create_sli_config_v2**
> SliConfigurationWithLastUpdated create_sli_config_v2(sli_configuration)

Create SLI Config

This endpoint creates the Service Level Indicator Configuration  ## Mandatory Parameters:  - **id** A unique identifier for each SLI configuration  - **sliName:** Name for the SLI configuration  - **sliEntity:** Entity of the SLI configuration  ### SLI Entity specific parameters  Depending on the chosen `sliType` in the `sliEntity`, there are further required parameters:  #### Application SLI entity  This option can be used to create a Time-Based SLI  - **sliEntity.applicationId:** The Id of the Application Perspective  - **sliEntity.boundaryScope:** Boundary scope of the Application Perspective  - **metricConfiguration.metricName:** The metric name on which to compute the SLI  - **metricConfiguration.metricAggregation:** The aggregation of the metric  - **metricConfiguration.threshold:** Threshold for the metric  #### Availability SLI entity  This opetion can be used to create an Event-Based SLI  - **sliEntity.applicationId:** The Id of the Application Perspective  - **sliEntity.boundaryScope:** Boundary scope of the Application Perspective  ## Deprecated Parameters for Availability SLI entity:  - **sliEntity.serviceId:** The ID if the Service in he context of an Application Perspective  - **sliEntity.endpointId:** The ID of an Endpoint belonging to a Service  - **sliEntity.goodEventFilters:** The list of TagFilters to match good events / calls  - **sliEntity.badEventFilters:** The list of TagFilters to match bad events / calls  All of these filters can be included using the list of TagFilterExpressions via **sliEntity.goodEventFilterExpression** and **sliEntity.badEventFilterExpression**. These parameters will be removed in the upcoming releases. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration import SliConfiguration
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)
    sli_configuration = {"sliName":"test-application-sli","metricConfiguration":{"metricName":"latency","metricAggregation":"P90","threshold":555},"sliEntity":{"sliType":"application","applicationId":"btg-B709IU6o9QNXUS4TVw","serviceId":null,"endpointId":null,"boundaryScope":"INBOUND"}} # SliConfiguration | 

    try:
        # Create SLI Config
        api_response = api_instance.create_sli_config_v2(sli_configuration)
        print("The response of SLISettingsApi->create_sli_config_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->create_sli_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sli_configuration** | [**SliConfiguration**](SliConfiguration.md)|  | 

### Return type

[**SliConfigurationWithLastUpdated**](SliConfigurationWithLastUpdated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New SLI Configuration Created Successfully |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sli_config**
> delete_sli_config(id)

Delete SLI Config

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
    api_instance = instana_client.SLISettingsApi(api_client)
    id = '7iydEfqJQP6AKzd3yR3byw' # str | 

    try:
        # Delete SLI Config
        api_instance.delete_sli_config(id)
    except Exception as e:
        print("Exception when calling SLISettingsApi->delete_sli_config: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sli_config_v2**
> delete_sli_config_v2(id)

Delete SLI Config

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
    api_instance = instana_client.SLISettingsApi(api_client)
    id = 'HXcNRWhDSWiZs3HiUAKr7g' # str | ID of the Service Level Indicator (SLI)

    try:
        # Delete SLI Config
        api_instance.delete_sli_config_v2(id)
    except Exception as e:
        print("Exception when calling SLISettingsApi->delete_sli_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Service Level Indicator (SLI) | 

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
**204** | SLI Configuration Deleted Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sli_configs**
> List[SliConfigurationWithLastUpdated] get_all_sli_configs()

Get All SLI Configs

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)

    try:
        # Get All SLI Configs
        api_response = api_instance.get_all_sli_configs()
        print("The response of SLISettingsApi->get_all_sli_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->get_all_sli_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SliConfigurationWithLastUpdated]**](SliConfigurationWithLastUpdated.md)

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

# **get_all_sli_configs_v2**
> List[SliConfigurationWithLastUpdated] get_all_sli_configs_v2()

Get All SLI Configs

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)

    try:
        # Get All SLI Configs
        api_response = api_instance.get_all_sli_configs_v2()
        print("The response of SLISettingsApi->get_all_sli_configs_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->get_all_sli_configs_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SliConfigurationWithLastUpdated]**](SliConfigurationWithLastUpdated.md)

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

# **get_sli_config**
> SliConfigurationWithLastUpdated get_sli_config(id)

Get SLI Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)
    id = '3J0RDgfyQz-P_hVzbNNb4A' # str | 

    try:
        # Get SLI Config
        api_response = api_instance.get_sli_config(id)
        print("The response of SLISettingsApi->get_sli_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->get_sli_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SliConfigurationWithLastUpdated**](SliConfigurationWithLastUpdated.md)

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

# **get_sli_config_v2**
> SliConfigurationWithLastUpdated get_sli_config_v2(id)

Get SLI Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)
    id = 'HXcNRWhDSWiZs3HiUAKr7g' # str | ID of the Service Level Indicator (SLI)

    try:
        # Get SLI Config
        api_response = api_instance.get_sli_config_v2(id)
        print("The response of SLISettingsApi->get_sli_config_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->get_sli_config_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Service Level Indicator (SLI) | 

### Return type

[**SliConfigurationWithLastUpdated**](SliConfigurationWithLastUpdated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | SLI Configuration Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sli_configs_for_entity_type_and_id_v2**
> List[SliConfigurationWithLastUpdated] get_sli_configs_for_entity_type_and_id_v2(entity_type, entity_id)

Get all SLI configs for entity type and entity id

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)
    entity_type = 'entity_type_example' # str | Type of the Entity, whether it is an application or website
    entity_id = 'DkPX-x9VQuKBKopuilrkYw' # str | Unique ID of the Entity

    try:
        # Get all SLI configs for entity type and entity id
        api_response = api_instance.get_sli_configs_for_entity_type_and_id_v2(entity_type, entity_id)
        print("The response of SLISettingsApi->get_sli_configs_for_entity_type_and_id_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->get_sli_configs_for_entity_type_and_id_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Type of the Entity, whether it is an application or website | 
 **entity_id** | **str**| Unique ID of the Entity | 

### Return type

[**List[SliConfigurationWithLastUpdated]**](SliConfigurationWithLastUpdated.md)

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

# **update_sli_config**
> SliConfigurationWithLastUpdated update_sli_config(id, sli_configuration)

Update SLI Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_configuration import SliConfiguration
from instana_client.models.sli_configuration_with_last_updated import SliConfigurationWithLastUpdated
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
    api_instance = instana_client.SLISettingsApi(api_client)
    id = '3J0RDgfyQz-P_hVzbNNb4A' # str | 
    sli_configuration = {"id":"3J0RDgfyQz-P_hVzbNNb4A","sliName":"test-application-sli","initialEvaluationTimestamp":1732017600000,"metricConfiguration":{"metricName":"latency","metricAggregation":"P90","threshold":555},"sliEntity":{"sliType":"application","applicationId":"btg-B709IU6o9QNXUS4TVw","serviceId":null,"endpointId":null,"boundaryScope":"INBOUND"},"lastUpdated":1732017541059} # SliConfiguration | 

    try:
        # Update SLI Config
        api_response = api_instance.update_sli_config(id, sli_configuration)
        print("The response of SLISettingsApi->update_sli_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLISettingsApi->update_sli_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sli_configuration** | [**SliConfiguration**](SliConfiguration.md)|  | 

### Return type

[**SliConfigurationWithLastUpdated**](SliConfigurationWithLastUpdated.md)

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


# instana_client.ServiceLevelsObjectiveSLOConfigurationsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_slo_config**](ServiceLevelsObjectiveSLOConfigurationsApi.md#create_slo_config) | **POST** /api/settings/slo | Create a new SLO Config
[**delete_slo_config**](ServiceLevelsObjectiveSLOConfigurationsApi.md#delete_slo_config) | **DELETE** /api/settings/slo/{id} | Delete an existing SLO Config
[**get_all_slo_config_tags**](ServiceLevelsObjectiveSLOConfigurationsApi.md#get_all_slo_config_tags) | **GET** /api/settings/slo/tags | Get All SLO Config tags
[**get_all_slo_configs**](ServiceLevelsObjectiveSLOConfigurationsApi.md#get_all_slo_configs) | **GET** /api/settings/slo | Get All SLO Configs
[**get_slo_config_by_id**](ServiceLevelsObjectiveSLOConfigurationsApi.md#get_slo_config_by_id) | **GET** /api/settings/slo/{id} | Get an existing SLO Config
[**update_slo_config**](ServiceLevelsObjectiveSLOConfigurationsApi.md#update_slo_config) | **PUT** /api/settings/slo/{id} | Update an existing SLO Config


# **create_slo_config**
> ServiceLevelObjectiveConfiguration create_slo_config(service_level_objective_configuration)

Create a new SLO Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_level_objective_configuration import ServiceLevelObjectiveConfiguration
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
    api_instance = instana_client.ServiceLevelsObjectiveSLOConfigurationsApi(api_client)
    service_level_objective_configuration = {"name":"Stans test SLO 4","target":0.99,"entity":{"type":"application","applicationId":"VTNvC_sATZqMj4vSZfsjKA","serviceId":null,"endpointId":null,"boundaryScope":"INBOUND","includeInternal":false,"includeSynthetic":false,"tagFilterExpression":null},"indicator":{"type":"timeBased","blueprint":"latency","threshold":100,"aggregation":"P90"},"timeWindow":{"type":"rolling","duration":1,"durationUnit":"week"},"tags":["Stan","testing"]} # ServiceLevelObjectiveConfiguration | 

    try:
        # Create a new SLO Config
        api_response = api_instance.create_slo_config(service_level_objective_configuration)
        print("The response of ServiceLevelsObjectiveSLOConfigurationsApi->create_slo_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOConfigurationsApi->create_slo_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_level_objective_configuration** | [**ServiceLevelObjectiveConfiguration**](ServiceLevelObjectiveConfiguration.md)|  | 

### Return type

[**ServiceLevelObjectiveConfiguration**](ServiceLevelObjectiveConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New SLO Configuration Created Successfully |  -  |
**400** | Invalid Tag Filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_slo_config**
> delete_slo_config(id)

Delete an existing SLO Config

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
    api_instance = instana_client.ServiceLevelsObjectiveSLOConfigurationsApi(api_client)
    id = 'SLOdCTspkHlS_OzNOATQWgsuw' # str | 

    try:
        # Delete an existing SLO Config
        api_instance.delete_slo_config(id)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOConfigurationsApi->delete_slo_config: %s\n" % e)
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
**204** | SLO Configuration Deleted Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_slo_config_tags**
> List[str] get_all_slo_config_tags(query=query, tag=tag, entity_type=entity_type)

Get All SLO Config tags

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
    api_instance = instana_client.ServiceLevelsObjectiveSLOConfigurationsApi(api_client)
    query = 'test SLO' # str |  (optional)
    tag = ['Testing'] # List[str] |  (optional)
    entity_type = 'application' # str |  (optional)

    try:
        # Get All SLO Config tags
        api_response = api_instance.get_all_slo_config_tags(query=query, tag=tag, entity_type=entity_type)
        print("The response of ServiceLevelsObjectiveSLOConfigurationsApi->get_all_slo_config_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOConfigurationsApi->get_all_slo_config_tags: %s\n" % e)
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
**200** | Fetched list of SLO Configuration tags Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_slo_configs**
> PaginatedResult get_all_slo_configs(page_size=page_size, page=page, query=query, tag=tag, entity_type=entity_type, order_by=order_by, order_direction=order_direction, slo_ids=slo_ids, refresh=refresh)

Get All SLO Configs

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.paginated_result import PaginatedResult
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
    api_instance = instana_client.ServiceLevelsObjectiveSLOConfigurationsApi(api_client)
    page_size = 1 # int |  (optional)
    page = 1 # int |  (optional)
    query = 'test SLO' # str |  (optional)
    tag = ['Testing'] # List[str] |  (optional)
    entity_type = 'application' # str |  (optional)
    order_by = 'name' # str |  (optional)
    order_direction = 'ASC' # str |  (optional)
    slo_ids = ['SLOdCTspkHlS_OzNOATQWgsuw'] # List[str] |  (optional)
    refresh = false # bool |  (optional)

    try:
        # Get All SLO Configs
        api_response = api_instance.get_all_slo_configs(page_size=page_size, page=page, query=query, tag=tag, entity_type=entity_type, order_by=order_by, order_direction=order_direction, slo_ids=slo_ids, refresh=refresh)
        print("The response of ServiceLevelsObjectiveSLOConfigurationsApi->get_all_slo_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOConfigurationsApi->get_all_slo_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **query** | **str**|  | [optional] 
 **tag** | [**List[str]**](str.md)|  | [optional] 
 **entity_type** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **order_direction** | **str**|  | [optional] 
 **slo_ids** | [**List[str]**](str.md)|  | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched list of the SLO Configurations Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_config_by_id**
> ServiceLevelObjectiveConfiguration get_slo_config_by_id(id, refresh=refresh)

Get an existing SLO Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_level_objective_configuration import ServiceLevelObjectiveConfiguration
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
    api_instance = instana_client.ServiceLevelsObjectiveSLOConfigurationsApi(api_client)
    id = 'SLOdCTspkHlS_OzNOATQWgsuw' # str | 
    refresh = false # bool |  (optional)

    try:
        # Get an existing SLO Config
        api_response = api_instance.get_slo_config_by_id(id, refresh=refresh)
        print("The response of ServiceLevelsObjectiveSLOConfigurationsApi->get_slo_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOConfigurationsApi->get_slo_config_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ServiceLevelObjectiveConfiguration**](ServiceLevelObjectiveConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched SLO Configuration Successfully |  -  |
**404** | SLO Configuration Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_slo_config**
> ServiceLevelObjectiveConfiguration update_slo_config(id, service_level_objective_configuration)

Update an existing SLO Config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_level_objective_configuration import ServiceLevelObjectiveConfiguration
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
    api_instance = instana_client.ServiceLevelsObjectiveSLOConfigurationsApi(api_client)
    id = 'SLOdCTspkHlS_OzNOATQWgsuw' # str | 
    service_level_objective_configuration = {"name":"Stans test SLO 4","target":0.99,"entity":{"type":"application","applicationId":"VTNvC_sATZqMj4vSZfsjKA","serviceId":null,"endpointId":null,"boundaryScope":"INBOUND","includeInternal":false,"includeSynthetic":false,"tagFilterExpression":null},"indicator":{"type":"timeBased","blueprint":"latency","threshold":100,"aggregation":"P90"},"timeWindow":{"type":"rolling","duration":1,"durationUnit":"week"},"tags":["Stan","testing"]} # ServiceLevelObjectiveConfiguration | 

    try:
        # Update an existing SLO Config
        api_response = api_instance.update_slo_config(id, service_level_objective_configuration)
        print("The response of ServiceLevelsObjectiveSLOConfigurationsApi->update_slo_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOConfigurationsApi->update_slo_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **service_level_objective_configuration** | [**ServiceLevelObjectiveConfiguration**](ServiceLevelObjectiveConfiguration.md)|  | 

### Return type

[**ServiceLevelObjectiveConfiguration**](ServiceLevelObjectiveConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated SLO Configuration Successfully |  -  |
**404** | SLO Configuration Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


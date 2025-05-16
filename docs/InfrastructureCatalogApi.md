# instana_client.InfrastructureCatalogApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_payload_keys_by_plugin_id**](InfrastructureCatalogApi.md#get_available_payload_keys_by_plugin_id) | **GET** /api/infrastructure-monitoring/catalog/payloads/{pluginId} | Get payload keys for plugin
[**get_infrastructure_catalog_metrics**](InfrastructureCatalogApi.md#get_infrastructure_catalog_metrics) | **GET** /api/infrastructure-monitoring/catalog/metrics/{plugin} | Get metric catalog
[**get_infrastructure_catalog_plugins**](InfrastructureCatalogApi.md#get_infrastructure_catalog_plugins) | **GET** /api/infrastructure-monitoring/catalog/plugins | Get plugin catalog
[**get_infrastructure_catalog_plugins_with_custom_metrics**](InfrastructureCatalogApi.md#get_infrastructure_catalog_plugins_with_custom_metrics) | **GET** /api/infrastructure-monitoring/catalog/plugins-with-custom-metrics | Get all plugins with custom metrics catalog
[**get_infrastructure_catalog_search_fields**](InfrastructureCatalogApi.md#get_infrastructure_catalog_search_fields) | **GET** /api/infrastructure-monitoring/catalog/search | get search field catalog
[**get_tag_catalog**](InfrastructureCatalogApi.md#get_tag_catalog) | **GET** /api/infrastructure-monitoring/catalog/tags/{plugin} | Get available tags for a particular plugin
[**get_tag_catalog_all**](InfrastructureCatalogApi.md#get_tag_catalog_all) | **GET** /api/infrastructure-monitoring/catalog/tags | Get available tags


# **get_available_payload_keys_by_plugin_id**
> List[GetPayloadKeysResult] get_available_payload_keys_by_plugin_id(plugin_id)

Get payload keys for plugin

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_payload_keys_result import GetPayloadKeysResult
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)
    plugin_id = 'db2Database' # str | plugin id

    try:
        # Get payload keys for plugin
        api_response = api_instance.get_available_payload_keys_by_plugin_id(plugin_id)
        print("The response of InfrastructureCatalogApi->get_available_payload_keys_by_plugin_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_available_payload_keys_by_plugin_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| plugin id | 

### Return type

[**List[GetPayloadKeysResult]**](GetPayloadKeysResult.md)

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

# **get_infrastructure_catalog_metrics**
> List[MetricInstance] get_infrastructure_catalog_metrics(plugin, filter=filter)

Get metric catalog

This endpoint retrieves all available metric definitions of the requested plugin.  ### Path Parameters:  **plugin** The plugin id from [available plugins](#operation/getInfrastructureCatalogPlugins)  ### Optional Parameters:  **filter** You can restrict the returned metric definitions by passing a filter.  * `custom` to retrieve custom metric definitions only. * `builtin` to retrieve built-in metric definitions only. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.metric_instance import MetricInstance
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)
    plugin = 'plugin_example' # str | 
    filter = 'filter_example' # str |  (optional)

    try:
        # Get metric catalog
        api_response = api_instance.get_infrastructure_catalog_metrics(plugin, filter=filter)
        print("The response of InfrastructureCatalogApi->get_infrastructure_catalog_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_infrastructure_catalog_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin** | **str**|  | 
 **filter** | **str**|  | [optional] 

### Return type

[**List[MetricInstance]**](MetricInstance.md)

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

# **get_infrastructure_catalog_plugins**
> List[PluginResult] get_infrastructure_catalog_plugins()

Get plugin catalog

This endpoint retrieves all available plugin ids for your monitored system. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.plugin_result import PluginResult
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)

    try:
        # Get plugin catalog
        api_response = api_instance.get_infrastructure_catalog_plugins()
        print("The response of InfrastructureCatalogApi->get_infrastructure_catalog_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_infrastructure_catalog_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PluginResult]**](PluginResult.md)

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

# **get_infrastructure_catalog_plugins_with_custom_metrics**
> List[PluginResult] get_infrastructure_catalog_plugins_with_custom_metrics()

Get all plugins with custom metrics catalog

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.plugin_result import PluginResult
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)

    try:
        # Get all plugins with custom metrics catalog
        api_response = api_instance.get_infrastructure_catalog_plugins_with_custom_metrics()
        print("The response of InfrastructureCatalogApi->get_infrastructure_catalog_plugins_with_custom_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_infrastructure_catalog_plugins_with_custom_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PluginResult]**](PluginResult.md)

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

# **get_infrastructure_catalog_search_fields**
> List[SearchFieldResult] get_infrastructure_catalog_search_fields()

get search field catalog

This endpoint retrieves all available search keywords for dynamic focus queries.  These search fields can be accessed via lucene queries. Each field belongs to a context, e.g. to entity, trace or event data. Some fields contain a set of possible fixed values, in this case a deviant value is invalid.  ``` ?query={keyword}:{value} ``` 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.search_field_result import SearchFieldResult
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)

    try:
        # get search field catalog
        api_response = api_instance.get_infrastructure_catalog_search_fields()
        print("The response of InfrastructureCatalogApi->get_infrastructure_catalog_search_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_infrastructure_catalog_search_fields: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SearchFieldResult]**](SearchFieldResult.md)

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

# **get_tag_catalog**
> TagCatalog get_tag_catalog(plugin)

Get available tags for a particular plugin

This endpoint retrieves the tag catalog filtered by plugin.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.tag_catalog import TagCatalog
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)
    plugin = 'host' # str | plugin

    try:
        # Get available tags for a particular plugin
        api_response = api_instance.get_tag_catalog(plugin)
        print("The response of InfrastructureCatalogApi->get_tag_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_tag_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin** | **str**| plugin | 

### Return type

[**TagCatalog**](TagCatalog.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applciation/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_catalog_all**
> TagCatalog get_tag_catalog_all()

Get available tags

This endpoint retrieves the tag catalog.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.tag_catalog import TagCatalog
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
    api_instance = instana_client.InfrastructureCatalogApi(api_client)

    try:
        # Get available tags
        api_response = api_instance.get_tag_catalog_all()
        print("The response of InfrastructureCatalogApi->get_tag_catalog_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureCatalogApi->get_tag_catalog_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TagCatalog**](TagCatalog.md)

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


# instana_client.ApplicationCatalogApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_catalog_metrics**](ApplicationCatalogApi.md#get_application_catalog_metrics) | **GET** /api/application-monitoring/catalog/metrics | Get Metric catalog
[**get_application_tag_catalog**](ApplicationCatalogApi.md#get_application_tag_catalog) | **GET** /api/application-monitoring/catalog | Get application tag catalog
[**get_application_tags**](ApplicationCatalogApi.md#get_application_tags) | **GET** /api/application-monitoring/catalog/tags | Get application tags


# **get_application_catalog_metrics**
> List[MetricDescription] get_application_catalog_metrics()

Get Metric catalog


For more information on Application Catalog please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-catalog.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.metric_description import MetricDescription
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
    api_instance = instana_client.ApplicationCatalogApi(api_client)

    try:
        # Get Metric catalog
        api_response = api_instance.get_application_catalog_metrics()
        print("The response of ApplicationCatalogApi->get_application_catalog_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCatalogApi->get_application_catalog_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MetricDescription]**](MetricDescription.md)

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

# **get_application_tag_catalog**
> TagCatalog get_application_tag_catalog(var_from=var_from, data_source=data_source, use_case=use_case)

Get application tag catalog


For more information on Application Catalog please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-catalog.

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
    api_instance = instana_client.ApplicationCatalogApi(api_client)
    var_from = 56 # int | The start of the timestamp expreseed in Unix epoch time in milliseconds which will fetch list of queryable tags until current timestamp. Eg: `1719875833000` (1 July 2024 23:17:13 GMT) will fetch list of queryable tags from that time till current time.  (optional)
    data_source = 'data_source_example' # str | The source from where queryable tags should be fetched from. In Unbounded Analytics, Application Perspectives has 2 sources; `Calls` and `Traces`. (optional)
    use_case = 'use_case_example' # str | The subset of queryable tags that is available for a particular use case. For eg: If you select `dataSource` as `TRACES` and useCase as `Grouping`. The tags available for querying are `trace.endpoint.name` and `trace.service.name`. useCase is helpful when one wants to know which tags are supported for querying.  (optional)

    try:
        # Get application tag catalog
        api_response = api_instance.get_application_tag_catalog(var_from=var_from, data_source=data_source, use_case=use_case)
        print("The response of ApplicationCatalogApi->get_application_tag_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCatalogApi->get_application_tag_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**| The start of the timestamp expreseed in Unix epoch time in milliseconds which will fetch list of queryable tags until current timestamp. Eg: &#x60;1719875833000&#x60; (1 July 2024 23:17:13 GMT) will fetch list of queryable tags from that time till current time.  | [optional] 
 **data_source** | **str**| The source from where queryable tags should be fetched from. In Unbounded Analytics, Application Perspectives has 2 sources; &#x60;Calls&#x60; and &#x60;Traces&#x60;. | [optional] 
 **use_case** | **str**| The subset of queryable tags that is available for a particular use case. For eg: If you select &#x60;dataSource&#x60; as &#x60;TRACES&#x60; and useCase as &#x60;Grouping&#x60;. The tags available for querying are &#x60;trace.endpoint.name&#x60; and &#x60;trace.service.name&#x60;. useCase is helpful when one wants to know which tags are supported for querying.  | [optional] 

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

# **get_application_tags**
> List[Tag] get_application_tags(var_from=var_from, data_source=data_source, use_case=use_case)

Get application tags


For more information on Application Catalog please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-catalog.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.tag import Tag
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
    api_instance = instana_client.ApplicationCatalogApi(api_client)
    var_from = 56 # int | The start of the timestamp expreseed in Unix epoch time in milliseconds which will fetch list of queryable tags until current timestamp. Eg: `1719875833000` (1 July 2024 23:17:13 GMT) will fetch list of queryable tags from that time till current time.  (optional)
    data_source = 'data_source_example' # str | The source from where queryable tags should be fetched from. In Unbounded Analytics, Application Perspectives has 2 sources; `Calls` and `Traces`. (optional)
    use_case = 'use_case_example' # str | The subset of queryable tags that is available for a particular use case. For eg: If you select `dataSource` as `TRACES` and useCase as `Grouping`. The tags available for querying are `trace.endpoint.name` and `trace.service.name`. useCase is helpful when one wants to know which tags are supported for querying.  (optional)

    try:
        # Get application tags
        api_response = api_instance.get_application_tags(var_from=var_from, data_source=data_source, use_case=use_case)
        print("The response of ApplicationCatalogApi->get_application_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCatalogApi->get_application_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**| The start of the timestamp expreseed in Unix epoch time in milliseconds which will fetch list of queryable tags until current timestamp. Eg: &#x60;1719875833000&#x60; (1 July 2024 23:17:13 GMT) will fetch list of queryable tags from that time till current time.  | [optional] 
 **data_source** | **str**| The source from where queryable tags should be fetched from. In Unbounded Analytics, Application Perspectives has 2 sources; &#x60;Calls&#x60; and &#x60;Traces&#x60;. | [optional] 
 **use_case** | **str**| The subset of queryable tags that is available for a particular use case. For eg: If you select &#x60;dataSource&#x60; as &#x60;TRACES&#x60; and useCase as &#x60;Grouping&#x60;. The tags available for querying are &#x60;trace.endpoint.name&#x60; and &#x60;trace.service.name&#x60;. useCase is helpful when one wants to know which tags are supported for querying.  | [optional] 

### Return type

[**List[Tag]**](Tag.md)

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


# instana_client.InfrastructureAnalyzeApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_metrics**](InfrastructureAnalyzeApi.md#get_available_metrics) | **POST** /api/infrastructure-monitoring/analyze/metrics | Get available metrics
[**get_available_plugins**](InfrastructureAnalyzeApi.md#get_available_plugins) | **POST** /api/infrastructure-monitoring/analyze/entity-types | Get available entity types
[**get_entities**](InfrastructureAnalyzeApi.md#get_entities) | **POST** /api/infrastructure-monitoring/analyze/entities | Get infrastructure entities
[**get_entity_groups**](InfrastructureAnalyzeApi.md#get_entity_groups) | **POST** /api/infrastructure-monitoring/analyze/entity-groups | Get grouped infrastructure entities with aggregated metrics


# **get_available_metrics**
> AvailableMetrics get_available_metrics(get_available_metrics_query=get_available_metrics_query)

Get available metrics

This endpoint retrieves available metrics for an entity type.
For more information on Infrastructure Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Infrastructure#infrastructure-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.available_metrics import AvailableMetrics
from instana_client.models.get_available_metrics_query import GetAvailableMetricsQuery
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
    api_instance = instana_client.InfrastructureAnalyzeApi(api_client)
    get_available_metrics_query = {"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"timeFrame":{"to":1673969562715,"windowSize":3600000},"query":"","type":"jvmRuntimePlatform"} # GetAvailableMetricsQuery |  (optional)

    try:
        # Get available metrics
        api_response = api_instance.get_available_metrics(get_available_metrics_query=get_available_metrics_query)
        print("The response of InfrastructureAnalyzeApi->get_available_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAnalyzeApi->get_available_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_available_metrics_query** | [**GetAvailableMetricsQuery**](GetAvailableMetricsQuery.md)|  | [optional] 

### Return type

[**AvailableMetrics**](AvailableMetrics.md)

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

# **get_available_plugins**
> AvailablePlugins get_available_plugins(get_available_plugins_query=get_available_plugins_query)

Get available entity types

This endpoint retrieves available entity types.
For more information on Infrastructure Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Infrastructure#infrastructure-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.available_plugins import AvailablePlugins
from instana_client.models.get_available_plugins_query import GetAvailablePluginsQuery
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
    api_instance = instana_client.InfrastructureAnalyzeApi(api_client)
    get_available_plugins_query = {"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"timeFrame":{"to":1673969562715,"windowSize":3600000}} # GetAvailablePluginsQuery |  (optional)

    try:
        # Get available entity types
        api_response = api_instance.get_available_plugins(get_available_plugins_query=get_available_plugins_query)
        print("The response of InfrastructureAnalyzeApi->get_available_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAnalyzeApi->get_available_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_available_plugins_query** | [**GetAvailablePluginsQuery**](GetAvailablePluginsQuery.md)|  | [optional] 

### Return type

[**AvailablePlugins**](AvailablePlugins.md)

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

# **get_entities**
> InfrastructureEntitiesResult get_entities(get_infrastructure_query=get_infrastructure_query)

Get infrastructure entities

This endpoint retrieves entities for a given entity type along with the requested metrics.
For more information on Infrastructure Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Infrastructure#infrastructure-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_infrastructure_query import GetInfrastructureQuery
from instana_client.models.infrastructure_entities_result import InfrastructureEntitiesResult
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
    api_instance = instana_client.InfrastructureAnalyzeApi(api_client)
    get_infrastructure_query = {"tagFilterExpression":{"type":"TAG_FILTER","entity":"NOT_APPLICABLE","name":"label","operator":"EQUALS","value":"custom-metrics.jar"},"timeFrame":{"to":1673969562715,"windowSize":3600000},"pagination":{"retrievalSize":200},"type":"jvmRuntimePlatform","metrics":[{"metric":"memory.used","granularity":3600000,"aggregation":"MAX"},{"metric":"memory.used","granularity":600000,"aggregation":"MAX"},{"metric":"threads.blocked","granularity":3600000,"aggregation":"MEAN"},{"metric":"threads.blocked","granularity":600000,"aggregation":"MEAN"}]} # GetInfrastructureQuery |  (optional)

    try:
        # Get infrastructure entities
        api_response = api_instance.get_entities(get_infrastructure_query=get_infrastructure_query)
        print("The response of InfrastructureAnalyzeApi->get_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAnalyzeApi->get_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_infrastructure_query** | [**GetInfrastructureQuery**](GetInfrastructureQuery.md)|  | [optional] 

### Return type

[**InfrastructureEntitiesResult**](InfrastructureEntitiesResult.md)

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

# **get_entity_groups**
> InfrastructureGroupsResult get_entity_groups(get_infrastructure_groups_query=get_infrastructure_groups_query)

Get grouped infrastructure entities with aggregated metrics

This endpoint groups entities for a given entity type and aggregates metrics for these groups.
For more information on Infrastructure Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Infrastructure#infrastructure-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_infrastructure_groups_query import GetInfrastructureGroupsQuery
from instana_client.models.infrastructure_groups_result import InfrastructureGroupsResult
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
    api_instance = instana_client.InfrastructureAnalyzeApi(api_client)
    get_infrastructure_groups_query = {"timeFrame":{"to":1674075565075,"windowSize":3600000},"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"pagination":{"retrievalSize":20},"groupBy":["host.name"],"type":"jvmRuntimePlatform","metrics":[{"metric":"memory.used","granularity":3600000,"aggregation":"MEAN"},{"metric":"memory.used","granularity":600000,"aggregation":"MEAN"},{"metric":"threads.blocked","granularity":3600000,"aggregation":"MEAN"},{"metric":"threads.blocked","granularity":600000,"aggregation":"MEAN"}],"order":{"by":"label","direction":"ASC"}} # GetInfrastructureGroupsQuery |  (optional)

    try:
        # Get grouped infrastructure entities with aggregated metrics
        api_response = api_instance.get_entity_groups(get_infrastructure_groups_query=get_infrastructure_groups_query)
        print("The response of InfrastructureAnalyzeApi->get_entity_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureAnalyzeApi->get_entity_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_infrastructure_groups_query** | [**GetInfrastructureGroupsQuery**](GetInfrastructureGroupsQuery.md)|  | [optional] 

### Return type

[**InfrastructureGroupsResult**](InfrastructureGroupsResult.md)

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


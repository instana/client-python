# instana_client.ApplicationAnalyzeApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_call_details**](ApplicationAnalyzeApi.md#get_call_details) | **GET** /api/application-monitoring/v2/analyze/traces/{traceId}/calls/{callId}/details | Get call detail
[**get_call_group**](ApplicationAnalyzeApi.md#get_call_group) | **POST** /api/application-monitoring/analyze/call-groups | Get grouped call metrics
[**get_correlated_traces**](ApplicationAnalyzeApi.md#get_correlated_traces) | **GET** /api/application-monitoring/analyze/backend-correlation | Resolve Trace IDs from Monitoring Beacons.
[**get_trace_download**](ApplicationAnalyzeApi.md#get_trace_download) | **GET** /api/application-monitoring/v2/analyze/traces/{id} | Get trace detail
[**get_trace_groups**](ApplicationAnalyzeApi.md#get_trace_groups) | **POST** /api/application-monitoring/analyze/trace-groups | Get grouped trace metrics
[**get_traces**](ApplicationAnalyzeApi.md#get_traces) | **POST** /api/application-monitoring/analyze/traces | Get all traces


# **get_call_details**
> TraceActivityTreeNodeDetails get_call_details(trace_id, call_id)

Get call detail

Use this API endpoint to retrieve a vast information about a call present in a trace.

For more information on Application Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.trace_activity_tree_node_details import TraceActivityTreeNodeDetails
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
    api_instance = instana_client.ApplicationAnalyzeApi(api_client)
    trace_id = 'trace_id_example' # str | 
    call_id = 'call_id_example' # str | 

    try:
        # Get call detail
        api_response = api_instance.get_call_details(trace_id, call_id)
        print("The response of ApplicationAnalyzeApi->get_call_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAnalyzeApi->get_call_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**|  | 
 **call_id** | **str**|  | 

### Return type

[**TraceActivityTreeNodeDetails**](TraceActivityTreeNodeDetails.md)

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

# **get_call_group**
> CallGroupsResult get_call_group(fill_time_series=fill_time_series, get_call_groups=get_call_groups)

Get grouped call metrics


For more information on Application Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.call_groups_result import CallGroupsResult
from instana_client.models.get_call_groups import GetCallGroups
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
    api_instance = instana_client.ApplicationAnalyzeApi(api_client)
    fill_time_series = True # bool | If enabled, fill the missing data points in the metric result with timestamp and value 0. (optional)
    get_call_groups = {"group":{"groupbyTag":"service.name","groupbyTagEntity":"DESTINATION"},"metrics":[{"aggregation":"SUM","metric":"calls"},{"aggregation":"P75","metric":"latency","granularity":360}],"includeInternal":false,"includeSynthetic":false,"order":{"by":"calls","direction":"DESC"},"pagination":{"retrievalSize":20},"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"call.type","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"DATABASE"},{"type":"TAG_FILTER","name":"service.name","operator":"EQUALS","entity":"DESTINATION","value":"ratings"}]},"timeFrame":{"to":"1688366990000","windowSize":"600000"}} # GetCallGroups |  (optional)

    try:
        # Get grouped call metrics
        api_response = api_instance.get_call_group(fill_time_series=fill_time_series, get_call_groups=get_call_groups)
        print("The response of ApplicationAnalyzeApi->get_call_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAnalyzeApi->get_call_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**| If enabled, fill the missing data points in the metric result with timestamp and value 0. | [optional] 
 **get_call_groups** | [**GetCallGroups**](GetCallGroups.md)|  | [optional] 

### Return type

[**CallGroupsResult**](CallGroupsResult.md)

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

# **get_correlated_traces**
> List[BackendTraceReference] get_correlated_traces(correlation_id)

Resolve Trace IDs from Monitoring Beacons.

Resolves backend trace IDs using correlation IDs from website and mobile app monitoring beacons.
For more information on Application Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.backend_trace_reference import BackendTraceReference
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
    api_instance = instana_client.ApplicationAnalyzeApi(api_client)
    correlation_id = '0v7f55879ca12345' # str | Here, the `backendTraceId` is typically used which can be obtained from the `Get all beacons` API endpoint for website and mobile app monitoring. For XHR, fetch, or HTTP beacons, the `beaconId` retrieved from the same API endpoint can also serve as the `correlationId`. 

    try:
        # Resolve Trace IDs from Monitoring Beacons.
        api_response = api_instance.get_correlated_traces(correlation_id)
        print("The response of ApplicationAnalyzeApi->get_correlated_traces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAnalyzeApi->get_correlated_traces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_id** | **str**| Here, the &#x60;backendTraceId&#x60; is typically used which can be obtained from the &#x60;Get all beacons&#x60; API endpoint for website and mobile app monitoring. For XHR, fetch, or HTTP beacons, the &#x60;beaconId&#x60; retrieved from the same API endpoint can also serve as the &#x60;correlationId&#x60;.  | 

### Return type

[**List[BackendTraceReference]**](BackendTraceReference.md)

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

# **get_trace_download**
> TraceDownloadResult get_trace_download(id, retrieval_size=retrieval_size, offset=offset, ingestion_time=ingestion_time)

Get trace detail

Use this API endpoint if one wants to retrive comprehensive details of a particular trace.
For more information on Application Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.trace_download_result import TraceDownloadResult
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
    api_instance = instana_client.ApplicationAnalyzeApi(api_client)
    id = 'id_example' # str | 
    retrieval_size = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    ingestion_time = 56 # int |  (optional)

    try:
        # Get trace detail
        api_response = api_instance.get_trace_download(id, retrieval_size=retrieval_size, offset=offset, ingestion_time=ingestion_time)
        print("The response of ApplicationAnalyzeApi->get_trace_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAnalyzeApi->get_trace_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **retrieval_size** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **ingestion_time** | **int**|  | [optional] 

### Return type

[**TraceDownloadResult**](TraceDownloadResult.md)

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

# **get_trace_groups**
> TraceGroupsResult get_trace_groups(fill_time_series=fill_time_series, get_trace_groups=get_trace_groups)

Get grouped trace metrics

In this endpoint, the supported `groupbyTag` are `trace.endpoint.name` and `trace.service.name`. 
For more information on Application Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_trace_groups import GetTraceGroups
from instana_client.models.trace_groups_result import TraceGroupsResult
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
    api_instance = instana_client.ApplicationAnalyzeApi(api_client)
    fill_time_series = True # bool | If enabled, fill the missing data points in the metric result with timestamp and value 0. (optional)
    get_trace_groups = {"group":{"groupbyTag":"trace.endpoint.name","groupbyTagEntity":"NOT_APPLICABLE"},"metrics":[{"aggregation":"SUM","metric":"latency"}],"order":{"by":"latency","direction":"ASC"},"pagination":{"retrievalSize":20},"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"call.type","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"DATABASE"},{"type":"TAG_FILTER","name":"service.name","operator":"EQUALS","entity":"DESTINATION","value":"ratings"}]}} # GetTraceGroups |  (optional)

    try:
        # Get grouped trace metrics
        api_response = api_instance.get_trace_groups(fill_time_series=fill_time_series, get_trace_groups=get_trace_groups)
        print("The response of ApplicationAnalyzeApi->get_trace_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAnalyzeApi->get_trace_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**| If enabled, fill the missing data points in the metric result with timestamp and value 0. | [optional] 
 **get_trace_groups** | [**GetTraceGroups**](GetTraceGroups.md)|  | [optional] 

### Return type

[**TraceGroupsResult**](TraceGroupsResult.md)

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

# **get_traces**
> TraceResult get_traces(get_traces=get_traces)

Get all traces


For more information on Application Analyze please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-analyze.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_traces import GetTraces
from instana_client.models.trace_result import TraceResult
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
    api_instance = instana_client.ApplicationAnalyzeApi(api_client)
    get_traces = {"includeInternal":false,"includeSynthetic":false,"pagination":{"retrievalSize":1},"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"endpoint.name","operator":"EQUALS","entity":"DESTINATION","value":"GET /"},{"type":"TAG_FILTER","name":"service.name","operator":"EQUALS","entity":"DESTINATION","value":"groundskeeper"}]},"order":{"by":"traceLabel","direction":"DESC"}} # GetTraces |  (optional)

    try:
        # Get all traces
        api_response = api_instance.get_traces(get_traces=get_traces)
        print("The response of ApplicationAnalyzeApi->get_traces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationAnalyzeApi->get_traces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_traces** | [**GetTraces**](GetTraces.md)|  | [optional] 

### Return type

[**TraceResult**](TraceResult.md)

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


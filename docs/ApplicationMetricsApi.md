# instana_client.ApplicationMetricsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_data_metrics_v2**](ApplicationMetricsApi.md#get_application_data_metrics_v2) | **POST** /api/application-monitoring/v2/metrics | Get Application Data Metrics
[**get_application_metrics**](ApplicationMetricsApi.md#get_application_metrics) | **POST** /api/application-monitoring/metrics/applications | Get Application Metrics
[**get_endpoints_metrics**](ApplicationMetricsApi.md#get_endpoints_metrics) | **POST** /api/application-monitoring/metrics/endpoints | Get Endpoint metrics
[**get_services_metrics**](ApplicationMetricsApi.md#get_services_metrics) | **POST** /api/application-monitoring/metrics/services | Get Service metrics


# **get_application_data_metrics_v2**
> MetricAPIResult get_application_data_metrics_v2(get_application_metrics=get_application_metrics)

Get Application Data Metrics

Use this API endpoint if one wants to retrieve one or more supported aggregation of supported metrics for a combination of entities.
For eg: retrieve `MEAN` aggregation of `latency` metric for an Endpoint `GET /api/foo`, Service `payment` and Application Perspective `app`.
Consider this API endpoint an upgraded version of `Get Application Metrics`, `Get Endpoint metrics` and `Get Service metrics`.
For more information on supported metrics, refer `Get Metric catalog`.

For more information on Application Metrics please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_application_metrics import GetApplicationMetrics
from instana_client.models.metric_api_result import MetricAPIResult
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
    api_instance = instana_client.ApplicationMetricsApi(api_client)
    get_application_metrics = {"includeInternal":true,"includeSynthetic":true,"metrics":[{"aggregation":"MEAN","metric":"latency"}],"tagFilterExpression":{"type":"TAG_FILTER","name":"service.name","operator":"EQUALS","entity":"DESTINATION","value":"warehouse"},"timeFrame":{"to":1669190589000,"windowSize":3600000}} # GetApplicationMetrics |  (optional)

    try:
        # Get Application Data Metrics
        api_response = api_instance.get_application_data_metrics_v2(get_application_metrics=get_application_metrics)
        print("The response of ApplicationMetricsApi->get_application_data_metrics_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationMetricsApi->get_application_data_metrics_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_application_metrics** | [**GetApplicationMetrics**](GetApplicationMetrics.md)|  | [optional] 

### Return type

[**MetricAPIResult**](MetricAPIResult.md)

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

# **get_application_metrics**
> ApplicationMetricResult get_application_metrics(fill_time_series=fill_time_series, get_applications=get_applications)

Get Application Metrics

Use this API endpoint if one wants to retrieve one or more supported aggregation of supported metrics for an Application Perspective.
For eg: retrieve `MEAN` aggregation of `latency` metric for an Application Perspective `app`.
For more information on supported metrics, refer `Get Metric catalog`.

For more information on Application Metrics please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_metric_result import ApplicationMetricResult
from instana_client.models.get_applications import GetApplications
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
    api_instance = instana_client.ApplicationMetricsApi(api_client)
    fill_time_series = True # bool | If enabled, fill the missing data points in the metric result with timestamp and value 0. (optional)
    get_applications = {"metrics":[{"aggregation":"MEAN","metric":"latency"}],"order":{"by":"latency","direction":"DESC"},"pagination":{"page":1,"pageSize":1},"timeFrame":{"to":1646037122400,"windowSize":3600000}} # GetApplications |  (optional)

    try:
        # Get Application Metrics
        api_response = api_instance.get_application_metrics(fill_time_series=fill_time_series, get_applications=get_applications)
        print("The response of ApplicationMetricsApi->get_application_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationMetricsApi->get_application_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**| If enabled, fill the missing data points in the metric result with timestamp and value 0. | [optional] 
 **get_applications** | [**GetApplications**](GetApplications.md)|  | [optional] 

### Return type

[**ApplicationMetricResult**](ApplicationMetricResult.md)

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

# **get_endpoints_metrics**
> EndpointMetricResult get_endpoints_metrics(fill_time_series=fill_time_series, get_endpoints=get_endpoints)

Get Endpoint metrics

Use this API endpoint if one wants to retrieve one or more supported aggregation of supported metrics for an Endpoint.
For eg: retrieve `MEAN` aggregation of `latency` metric for an Endpoint `GET /api/foo`.
For more information on supported metrics, refer `Get Metric catalog`.

For more information on Application Metrics please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.endpoint_metric_result import EndpointMetricResult
from instana_client.models.get_endpoints import GetEndpoints
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
    api_instance = instana_client.ApplicationMetricsApi(api_client)
    fill_time_series = True # bool | If enabled, fill the missing data points in the metric result with timestamp and value 0. (optional)
    get_endpoints = {"applicationBoundaryScope":"ALL","endpointId":"murzTwzJlGyqc_CFtEKx8INVCfY","excludeSynthetic":true,"metrics":[{"aggregation":"MEAN","metric":"latency"}],"order":{"by":"latency.mean","direction":"ASC"},"pagination":{"page":1,"pageSize":1},"timeFrame":{"to":1669190589000,"windowSize":3600000}} # GetEndpoints |  (optional)

    try:
        # Get Endpoint metrics
        api_response = api_instance.get_endpoints_metrics(fill_time_series=fill_time_series, get_endpoints=get_endpoints)
        print("The response of ApplicationMetricsApi->get_endpoints_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationMetricsApi->get_endpoints_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**| If enabled, fill the missing data points in the metric result with timestamp and value 0. | [optional] 
 **get_endpoints** | [**GetEndpoints**](GetEndpoints.md)|  | [optional] 

### Return type

[**EndpointMetricResult**](EndpointMetricResult.md)

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

# **get_services_metrics**
> ServiceMetricResult get_services_metrics(fill_time_series=fill_time_series, include_snapshot_ids=include_snapshot_ids, get_services=get_services)

Get Service metrics

Use this API endpoint if one wants to retrieve one or more supported aggregation of supported metrics for a Service.
For eg: retrieve `MEAN` aggregation of `latency` metric for a Service `payment`.
For more information on supported metrics, refer `Get Metric catalog`.

For more information on Application Metrics please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Applications#application-metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_services import GetServices
from instana_client.models.service_metric_result import ServiceMetricResult
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
    api_instance = instana_client.ApplicationMetricsApi(api_client)
    fill_time_series = True # bool | If enabled, fill the missing data points in the metric result with timestamp and value 0. (optional)
    include_snapshot_ids = True # bool |  (optional)
    get_services = {"applicationBoundaryScope":"ALL","contextScope":"NONE","metrics":[{"aggregation":"mean","metric":"latency"}],"order":{"by":"latency.mean","direction":"DESC"},"pagination":{"page":1,"pageSize":1},"serviceId":"c467ca0fa21477fee3cde75a140b2963307388a7","technologies":["springbootApplicationContainer"],"timeFrame":{"to":1669190589000,"windowSize":3600000}} # GetServices |  (optional)

    try:
        # Get Service metrics
        api_response = api_instance.get_services_metrics(fill_time_series=fill_time_series, include_snapshot_ids=include_snapshot_ids, get_services=get_services)
        print("The response of ApplicationMetricsApi->get_services_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationMetricsApi->get_services_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**| If enabled, fill the missing data points in the metric result with timestamp and value 0. | [optional] 
 **include_snapshot_ids** | **bool**|  | [optional] 
 **get_services** | [**GetServices**](GetServices.md)|  | [optional] 

### Return type

[**ServiceMetricResult**](ServiceMetricResult.md)

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


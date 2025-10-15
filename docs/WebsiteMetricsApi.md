# instana_client.WebsiteMetricsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_beacon_metrics**](WebsiteMetricsApi.md#get_beacon_metrics) | **POST** /api/website-monitoring/metrics | Get beacon metrics
[**get_beacon_metrics_v2**](WebsiteMetricsApi.md#get_beacon_metrics_v2) | **POST** /api/website-monitoring/v2/metrics | Get beacon metrics
[**get_page_load**](WebsiteMetricsApi.md#get_page_load) | **GET** /api/website-monitoring/page-load{id}{timestamp} | Get page load


# **get_beacon_metrics**
> WebsiteMetricResult get_beacon_metrics(get_website_metrics=get_website_metrics)

Get beacon metrics

API request to get website monitoring beacon metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_website_metrics import GetWebsiteMetrics
from instana_client.models.website_metric_result import WebsiteMetricResult
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
    api_instance = instana_client.WebsiteMetricsApi(api_client)
    get_website_metrics = instana_client.GetWebsiteMetrics() # GetWebsiteMetrics |  (optional)

    try:
        # Get beacon metrics
        api_response = api_instance.get_beacon_metrics(get_website_metrics=get_website_metrics)
        print("The response of WebsiteMetricsApi->get_beacon_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMetricsApi->get_beacon_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_website_metrics** | [**GetWebsiteMetrics**](GetWebsiteMetrics.md)|  | [optional] 

### Return type

[**WebsiteMetricResult**](WebsiteMetricResult.md)

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

# **get_beacon_metrics_v2**
> MetricAPIResult get_beacon_metrics_v2(get_website_metrics_v2=get_website_metrics_v2)

Get beacon metrics

API request to get website monitoring beacon metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_website_metrics_v2 import GetWebsiteMetricsV2
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
    api_instance = instana_client.WebsiteMetricsApi(api_client)
    get_website_metrics_v2 = {"metrics":[{"metric":"beaconCount","aggregation":"SUM"}],"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"beacon.website.name","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"robot-shop"},{"type":"TAG_FILTER","name":"beacon.location.path","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"/"}]},"timeFrame":{"to":null,"windowSize":3600000},"type":"PAGELOAD"} # GetWebsiteMetricsV2 |  (optional)

    try:
        # Get beacon metrics
        api_response = api_instance.get_beacon_metrics_v2(get_website_metrics_v2=get_website_metrics_v2)
        print("The response of WebsiteMetricsApi->get_beacon_metrics_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMetricsApi->get_beacon_metrics_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_website_metrics_v2** | [**GetWebsiteMetricsV2**](GetWebsiteMetricsV2.md)|  | [optional] 

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
**401** | Unauthorized access - requires user authentication. |  -  |
**404** | Resource not found. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_load**
> List[WebsiteMonitoringBeacon] get_page_load(id, timestamp)

Get page load

API request to get website monitoring beacons for a page load.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website_monitoring_beacon import WebsiteMonitoringBeacon
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
    api_instance = instana_client.WebsiteMetricsApi(api_client)
    id = '63f5b070e8d9a597' # str | Identifier of the page load to be retrieved
    timestamp = 1707012285674 # int | Timestamp of the page load to be retrieved

    try:
        # Get page load
        api_response = api_instance.get_page_load(id, timestamp)
        print("The response of WebsiteMetricsApi->get_page_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMetricsApi->get_page_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the page load to be retrieved | 
 **timestamp** | **int**| Timestamp of the page load to be retrieved | 

### Return type

[**List[WebsiteMonitoringBeacon]**](WebsiteMonitoringBeacon.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# instana_client.MobileAppMetricsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mobile_app_beacon_metrics**](MobileAppMetricsApi.md#get_mobile_app_beacon_metrics) | **POST** /api/mobile-app-monitoring/metrics | Get mobile app beacon metrics
[**get_mobile_app_beacon_metrics_v2**](MobileAppMetricsApi.md#get_mobile_app_beacon_metrics_v2) | **POST** /api/mobile-app-monitoring/v2/metrics | Get beacon metrics
[**get_session**](MobileAppMetricsApi.md#get_session) | **GET** /api/mobile-app-monitoring/session{id}{timestamp} | Get mobile app session


# **get_mobile_app_beacon_metrics**
> MobileAppMetricResult get_mobile_app_beacon_metrics(get_mobile_app_metrics=get_mobile_app_metrics)

Get mobile app beacon metrics

API request to get mobile app monitoring beacon metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_mobile_app_metrics import GetMobileAppMetrics
from instana_client.models.mobile_app_metric_result import MobileAppMetricResult
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
    api_instance = instana_client.MobileAppMetricsApi(api_client)
    get_mobile_app_metrics = instana_client.GetMobileAppMetrics() # GetMobileAppMetrics |  (optional)

    try:
        # Get mobile app beacon metrics
        api_response = api_instance.get_mobile_app_beacon_metrics(get_mobile_app_metrics=get_mobile_app_metrics)
        print("The response of MobileAppMetricsApi->get_mobile_app_beacon_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppMetricsApi->get_mobile_app_beacon_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_mobile_app_metrics** | [**GetMobileAppMetrics**](GetMobileAppMetrics.md)|  | [optional] 

### Return type

[**MobileAppMetricResult**](MobileAppMetricResult.md)

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

# **get_mobile_app_beacon_metrics_v2**
> MetricAPIResult get_mobile_app_beacon_metrics_v2(get_mobile_app_metrics_v2=get_mobile_app_metrics_v2)

Get beacon metrics

API request to get mobile app monitoring beacon metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_mobile_app_metrics_v2 import GetMobileAppMetricsV2
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
    api_instance = instana_client.MobileAppMetricsApi(api_client)
    get_mobile_app_metrics_v2 = {"metrics":[{"metric":"beaconCount","aggregation":"SUM","granularity":60}],"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"mobileBeacon.mobileApp.name","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"robot-warehouse"},{"type":"TAG_FILTER","name":"mobileBeacon.view.name","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"Products"}]},"timeFrame":{"to":null,"windowSize":3600000},"type":"SESSION_START"} # GetMobileAppMetricsV2 |  (optional)

    try:
        # Get beacon metrics
        api_response = api_instance.get_mobile_app_beacon_metrics_v2(get_mobile_app_metrics_v2=get_mobile_app_metrics_v2)
        print("The response of MobileAppMetricsApi->get_mobile_app_beacon_metrics_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppMetricsApi->get_mobile_app_beacon_metrics_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_mobile_app_metrics_v2** | [**GetMobileAppMetricsV2**](GetMobileAppMetricsV2.md)|  | [optional] 

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
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> List[MobileAppMonitoringBeacon] get_session(id, timestamp)

Get mobile app session

API request to get a mobile app monitoring session.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app_monitoring_beacon import MobileAppMonitoringBeacon
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
    api_instance = instana_client.MobileAppMetricsApi(api_client)
    id = '9CA9E31D-B0F7-40EC-8D32-FE163A6557AE' # str | Identifier of the session to be retrieved
    timestamp = 1730595029980 # int | Timestamp of the session to be retrieved

    try:
        # Get mobile app session
        api_response = api_instance.get_session(id, timestamp)
        print("The response of MobileAppMetricsApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppMetricsApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the session to be retrieved | 
 **timestamp** | **int**| Timestamp of the session to be retrieved | 

### Return type

[**List[MobileAppMonitoringBeacon]**](MobileAppMonitoringBeacon.md)

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
**401** | Unauthorized access - requires user authentication. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


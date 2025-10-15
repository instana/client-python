# instana_client.SyntheticMetricsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics_result**](SyntheticMetricsApi.md#get_metrics_result) | **POST** /api/synthetics/metrics | Get Synthetic Metrics


# **get_metrics_result**
> MetricsResult get_metrics_result(get_metrics_result=get_metrics_result)

Get Synthetic Metrics

API request to retrieve Synthetic Metrics.
For more information on Synthetic Metrics please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_metrics_result import GetMetricsResult
from instana_client.models.metrics_result import MetricsResult
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
    api_instance = instana_client.SyntheticMetricsApi(api_client)
    get_metrics_result = {"pagination":{"page":1,"pageSize":3},"metrics":[{"metric":"synthetic.metricsResponseTime","aggregation":"SUM"}],"timeFrame":{"to":0,"windowSize":3600000},"groups":[{"groupbyTag":"synthetic.applicationId"},{"groupbyTag":"synthetic.tags","groupbyTagSecondLevelTag":"region"}]} # GetMetricsResult |  (optional)

    try:
        # Get Synthetic Metrics
        api_response = api_instance.get_metrics_result(get_metrics_result=get_metrics_result)
        print("The response of SyntheticMetricsApi->get_metrics_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticMetricsApi->get_metrics_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_metrics_result** | [**GetMetricsResult**](GetMetricsResult.md)|  | [optional] 

### Return type

[**MetricsResult**](MetricsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


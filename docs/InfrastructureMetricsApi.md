# instana_client.InfrastructureMetricsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_infrastructure_metrics**](InfrastructureMetricsApi.md#get_infrastructure_metrics) | **POST** /api/infrastructure-monitoring/metrics | Get infrastructure metrics


# **get_infrastructure_metrics**
> InfrastructureMetricResult get_infrastructure_metrics(offline=offline, get_combined_metrics=get_combined_metrics)

Get infrastructure metrics

- The **offline** parameter is used to allow deeper visibility into snapshots. Set to `false`, the query will return all snapshots that are still available on the given **to** timestamp. However, set to `true`, the query will return all snapshots that have been active within the time window, this must at least include the online result and snapshots terminated within this time.  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_combined_metrics import GetCombinedMetrics
from instana_client.models.infrastructure_metric_result import InfrastructureMetricResult
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
    api_instance = instana_client.InfrastructureMetricsApi(api_client)
    offline = True # bool |  (optional)
    get_combined_metrics = instana_client.GetCombinedMetrics() # GetCombinedMetrics |  (optional)

    try:
        # Get infrastructure metrics
        api_response = api_instance.get_infrastructure_metrics(offline=offline, get_combined_metrics=get_combined_metrics)
        print("The response of InfrastructureMetricsApi->get_infrastructure_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureMetricsApi->get_infrastructure_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offline** | **bool**|  | [optional] 
 **get_combined_metrics** | [**GetCombinedMetrics**](GetCombinedMetrics.md)|  | [optional] 

### Return type

[**InfrastructureMetricResult**](InfrastructureMetricResult.md)

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


# instana_client.LoggingAnalyzeApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_volume_usage**](LoggingAnalyzeApi.md#get_log_volume_usage) | **GET** /api/logging/logs/getLogVolumeUsage | Get Log Volume Usage


# **get_log_volume_usage**
> LogVolumeUsageResult get_log_volume_usage(from_ts, to_ts, grouping_tag=grouping_tag)

Get Log Volume Usage

Returns aggregated log volume usage data for a specified time range and optional grouping tag.
`fromTs` and `toTs` are required and must define a valid time range (i.e., `fromTs` <= `toTs`).
Refer to the query parameter description for valid `groupingTag` values.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.log_volume_usage_result import LogVolumeUsageResult
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
    api_instance = instana_client.LoggingAnalyzeApi(api_client)
    from_ts = 1682899200 # int | Start timestamp in seconds. Must be <= `toTs`.
    to_ts = 1682899201 # int | End timestamp in seconds. Must be >= `fromTs`.
    grouping_tag = 'zone' # str | Optional tag to group volume usage by. Valid groupingTag values are: `kubernetes_cluster_name`, `kubernetes_daemonset_name`, `kubernetes_namespace_name`, `kubernetes_deployment_name`, `host_name`, `zone`.  (optional)

    try:
        # Get Log Volume Usage
        api_response = api_instance.get_log_volume_usage(from_ts, to_ts, grouping_tag=grouping_tag)
        print("The response of LoggingAnalyzeApi->get_log_volume_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingAnalyzeApi->get_log_volume_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_ts** | **int**| Start timestamp in seconds. Must be &lt;&#x3D; &#x60;toTs&#x60;. | 
 **to_ts** | **int**| End timestamp in seconds. Must be &gt;&#x3D; &#x60;fromTs&#x60;. | 
 **grouping_tag** | **str**| Optional tag to group volume usage by. Valid groupingTag values are: &#x60;kubernetes_cluster_name&#x60;, &#x60;kubernetes_daemonset_name&#x60;, &#x60;kubernetes_namespace_name&#x60;, &#x60;kubernetes_deployment_name&#x60;, &#x60;host_name&#x60;, &#x60;zone&#x60;.  | [optional] 

### Return type

[**LogVolumeUsageResult**](LogVolumeUsageResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved log volume usage data |  -  |
**400** | Invalid request (e.g., missing or incorrect time parameters) |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


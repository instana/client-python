# instana_client.SLIReportApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sli**](SLIReportApi.md#get_sli) | **GET** /api/sli/report/{sliId} | Generate SLI report (Limitation: the Classic Edition API report can be available one hour after the SLI configuration created; other editions are around one minute.)


# **get_sli**
> List[SliReport] get_sli(sli_id, slo, var_from, to)

Generate SLI report (Limitation: the Classic Edition API report can be available one hour after the SLI configuration created; other editions are around one minute.)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.sli_report import SliReport
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
    api_instance = instana_client.SLIReportApi(api_client)
    sli_id = 'nCtEoR6NSPqG61QkIkwwCw' # str | ID of the Service Level Indicator (SLI)
    slo = 0.99 # float | Target SLO
    var_from = 1706713140000 # int | From Timestamp in milliseconds (13-digit)
    to = 1706713140000 # int | To Timestamp in milliseconds (13-digit)

    try:
        # Generate SLI report (Limitation: the Classic Edition API report can be available one hour after the SLI configuration created; other editions are around one minute.)
        api_response = api_instance.get_sli(sli_id, slo, var_from, to)
        print("The response of SLIReportApi->get_sli:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLIReportApi->get_sli: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sli_id** | **str**| ID of the Service Level Indicator (SLI) | 
 **slo** | **float**| Target SLO | 
 **var_from** | **int**| From Timestamp in milliseconds (13-digit) | 
 **to** | **int**| To Timestamp in milliseconds (13-digit) | 

### Return type

[**List[SliReport]**](SliReport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | There is no SLI configuration for the given ID or the report hasn&#39;t been generated yet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


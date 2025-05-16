# instana_client.ApdexReportApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_apdex_report**](ApdexReportApi.md#get_apdex_report) | **GET** /api/apdex/report/{apdexId} | Generate Apdex report


# **get_apdex_report**
> List[ApdexReport] get_apdex_report(apdex_id, var_from, to)

Generate Apdex report

Generate Apdex Report for a specified Apdex ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.apdex_report import ApdexReport
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
    api_instance = instana_client.ApdexReportApi(api_client)
    apdex_id = 'nCtEoR6NSPqG61QkIkwwCw' # str | Apdex Configuration ID
    var_from = 1706713140000 # int | Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds
    to = 1706813100000 # int | Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds

    try:
        # Generate Apdex report
        api_response = api_instance.get_apdex_report(apdex_id, var_from, to)
        print("The response of ApdexReportApi->get_apdex_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApdexReportApi->get_apdex_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apdex_id** | **str**| Apdex Configuration ID | 
 **var_from** | **int**| Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | 
 **to** | **int**| Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | 

### Return type

[**List[ApdexReport]**](ApdexReport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No Apdex configuration for the given ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


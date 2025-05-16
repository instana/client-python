# instana_client.ServiceLevelsObjectiveSLOReportApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_slo**](ServiceLevelsObjectiveSLOReportApi.md#get_slo) | **GET** /api/slo/report/{sloId} | Generate Service Levels report


# **get_slo**
> List[SloReport] get_slo(slo_id, var_from=var_from, to=to)

Generate Service Levels report

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.slo_report import SloReport
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
    api_instance = instana_client.ServiceLevelsObjectiveSLOReportApi(api_client)
    slo_id = 'SLOEANnWh9tQOa2h88kGxK6wQ' # str | Service Levels Objective(SLO) Configuration ID
    var_from = '1706713140000' # str | Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds (optional)
    to = '1706813100000' # str | Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds (optional)

    try:
        # Generate Service Levels report
        api_response = api_instance.get_slo(slo_id, var_from=var_from, to=to)
        print("The response of ServiceLevelsObjectiveSLOReportApi->get_slo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOReportApi->get_slo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| Service Levels Objective(SLO) Configuration ID | 
 **var_from** | **str**| Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
 **to** | **str**| Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 

### Return type

[**List[SloReport]**](SloReport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched SLO Configuration Report Successfully |  -  |
**404** | There is no SLO configuration for the given ID or the report hasn&#39;t been generated yet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


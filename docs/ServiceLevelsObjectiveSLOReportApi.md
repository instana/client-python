# instana_client.ServiceLevelsObjectiveSLOReportApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entities_slo**](ServiceLevelsObjectiveSLOReportApi.md#entities_slo) | **GET** /api/slo/entities/{sloId} | Get the entities monitored by a SLO (Service Level Objective) configuration
[**explain_slo**](ServiceLevelsObjectiveSLOReportApi.md#explain_slo) | **GET** /api/slo/explain/{sloId} | Explain Service Levels objective with more details.
[**get_slo**](ServiceLevelsObjectiveSLOReportApi.md#get_slo) | **GET** /api/slo/report/{sloId} | Generate Service Levels report
[**summarize_slo**](ServiceLevelsObjectiveSLOReportApi.md#summarize_slo) | **GET** /api/slo/summarize/{sloId} | Summarize Service Levels objective results.


# **entities_slo**
> List[str] entities_slo(slo_id, window_size=window_size, to=to, page_size=page_size, page=page)

Get the entities monitored by a SLO (Service Level Objective) configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
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
    window_size = 360000 # int | Size of the time window in which the monitored entities must be fetched, specified in milliseconds. If not provided or set to 0, the default value of 3600000 milliseconds (1 hour) is used. (optional)
    to = 1706813100000 # int | Ending point for the data retrieval, specified as a 13-digit Unix timestamp in milliseconds. If not provided or set to 0, the current system time will be used. (optional)
    page_size = 1 # int | Size of the Page (optional)
    page = 1 # int | Page Number (optional)

    try:
        # Get the entities monitored by a SLO (Service Level Objective) configuration
        api_response = api_instance.entities_slo(slo_id, window_size=window_size, to=to, page_size=page_size, page=page)
        print("The response of ServiceLevelsObjectiveSLOReportApi->entities_slo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOReportApi->entities_slo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| Service Levels Objective(SLO) Configuration ID | 
 **window_size** | **int**| Size of the time window in which the monitored entities must be fetched, specified in milliseconds. If not provided or set to 0, the default value of 3600000 milliseconds (1 hour) is used. | [optional] 
 **to** | **int**| Ending point for the data retrieval, specified as a 13-digit Unix timestamp in milliseconds. If not provided or set to 0, the current system time will be used. | [optional] 
 **page_size** | **int**| Size of the Page | [optional] 
 **page** | **int**| Page Number | [optional] 

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SLO entities retrieved Successfully |  -  |
**404** | There is no SLO configuration for the given ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explain_slo**
> List[str] explain_slo(slo_id, var_from=var_from, to=to)

Explain Service Levels objective with more details.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
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
        # Explain Service Levels objective with more details.
        api_response = api_instance.explain_slo(slo_id, var_from=var_from, to=to)
        print("The response of ServiceLevelsObjectiveSLOReportApi->explain_slo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOReportApi->explain_slo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| Service Levels Objective(SLO) Configuration ID | 
 **var_from** | **str**| Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
 **to** | **str**| Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Explain SLO Successfully |  -  |
**404** | There is no SLO configuration for the given ID or the explain result hasn&#39;t been generated yet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo**
> List[SloReport] get_slo(slo_id, var_from=var_from, to=to, exclude_correction_id=exclude_correction_id, include_correction_id=include_correction_id)

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
    slo_id = 'SLOEANnWh9tQOa2h88kGxK6wQ' # str | SLO Configuration ID
    var_from = '1706713140000' # str | Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds (optional)
    to = '1706813100000' # str | Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds (optional)
    exclude_correction_id = ['N1Xj6q8QTZu_cfJOGqy4mg'] # List[str] | IDs of Correction Configurations to be Excluded from the result (optional)
    include_correction_id = ['uvP7Z03pSUuybDT8-WHLDA'] # List[str] | IDs of Correction Configurations to be Included in the result (optional)

    try:
        # Generate Service Levels report
        api_response = api_instance.get_slo(slo_id, var_from=var_from, to=to, exclude_correction_id=exclude_correction_id, include_correction_id=include_correction_id)
        print("The response of ServiceLevelsObjectiveSLOReportApi->get_slo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOReportApi->get_slo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| SLO Configuration ID | 
 **var_from** | **str**| Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
 **to** | **str**| Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
 **exclude_correction_id** | [**List[str]**](str.md)| IDs of Correction Configurations to be Excluded from the result | [optional] 
 **include_correction_id** | [**List[str]**](str.md)| IDs of Correction Configurations to be Included in the result | [optional] 

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

# **summarize_slo**
> List[str] summarize_slo(slo_id, var_from=var_from, to=to)

Summarize Service Levels objective results.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
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
        # Summarize Service Levels objective results.
        api_response = api_instance.summarize_slo(slo_id, var_from=var_from, to=to)
        print("The response of ServiceLevelsObjectiveSLOReportApi->summarize_slo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsObjectiveSLOReportApi->summarize_slo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_id** | **str**| Service Levels Objective(SLO) Configuration ID | 
 **var_from** | **str**| Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
 **to** | **str**| Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summarize SLO Successfully |  -  |
**404** | There is no SLO configuration for the given ID or the summarization result hasn&#39;t been generated yet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


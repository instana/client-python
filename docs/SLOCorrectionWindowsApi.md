# instana_client.SLOCorrectionWindowsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_slo_correction**](SLOCorrectionWindowsApi.md#get_slo_correction) | **GET** /api/slo/correction | Generate SLO Correction Windows


# **get_slo_correction**
> List[Correction] get_slo_correction(var_from, to, slo_id=slo_id, exclude_correction_id=exclude_correction_id, include_correction_id=include_correction_id, tags=tags)

Generate SLO Correction Windows

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.correction import Correction
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
    api_instance = instana_client.SLOCorrectionWindowsApi(api_client)
    var_from = 1706713140000 # int | Correction starting timestamp in milliseconds (13-digit)
    to = 1706713140000 # int | Correction ending timestamp in milliseconds (13-digit)
    slo_id = ['SLOdCTspkHlS_OzNOATQWgsuw'] # List[str] |  (optional)
    exclude_correction_id = ['N1Xj6q8QTZu_cfJOGqy4mg'] # List[str] | IDs of Correction Configurations to be Excluded from the result (optional)
    include_correction_id = ['uvP7Z03pSUuybDT8-WHLDA'] # List[str] | IDs of Correction Configurations to be Included in the result (optional)
    tags = ['tags_example'] # List[str] |  (optional)

    try:
        # Generate SLO Correction Windows
        api_response = api_instance.get_slo_correction(var_from, to, slo_id=slo_id, exclude_correction_id=exclude_correction_id, include_correction_id=include_correction_id, tags=tags)
        print("The response of SLOCorrectionWindowsApi->get_slo_correction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SLOCorrectionWindowsApi->get_slo_correction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**| Correction starting timestamp in milliseconds (13-digit) | 
 **to** | **int**| Correction ending timestamp in milliseconds (13-digit) | 
 **slo_id** | [**List[str]**](str.md)|  | [optional] 
 **exclude_correction_id** | [**List[str]**](str.md)| IDs of Correction Configurations to be Excluded from the result | [optional] 
 **include_correction_id** | [**List[str]**](str.md)| IDs of Correction Configurations to be Included in the result | [optional] 
 **tags** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Correction]**](Correction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched SLO Correction Windows Successfully |  -  |
**404** | There is no SLO Correction Window |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


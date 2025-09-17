# instana_client.SyntheticTestPlaybackResultsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_summary_list**](SyntheticTestPlaybackResultsApi.md#get_location_summary_list) | **POST** /api/synthetics/results/locationsummarylist | Get a list of Synthetic locations with last run test on each location data
[**get_synthetic_result**](SyntheticTestPlaybackResultsApi.md#get_synthetic_result) | **POST** /api/synthetics/results | Get Synthetic test playback results
[**get_synthetic_result_analytic**](SyntheticTestPlaybackResultsApi.md#get_synthetic_result_analytic) | **POST** /api/synthetics/results/analytic | Get a list of Synthetic tests based on the specified analytic function
[**get_synthetic_result_detail_data**](SyntheticTestPlaybackResultsApi.md#get_synthetic_result_detail_data) | **GET** /api/synthetics/results/{testid}/{testresultid}/detail | Get Synthetic test playback result detail data
[**get_synthetic_result_detail_data_file**](SyntheticTestPlaybackResultsApi.md#get_synthetic_result_detail_data_file) | **GET** /api/synthetics/results/{testid}/{testresultid}/file | Download the synthetic test playback result detail data file
[**get_synthetic_result_list**](SyntheticTestPlaybackResultsApi.md#get_synthetic_result_list) | **POST** /api/synthetics/results/list | Get a list of Synthetic test playback results
[**get_synthetic_result_metadata**](SyntheticTestPlaybackResultsApi.md#get_synthetic_result_metadata) | **GET** /api/synthetics/results/{testid}/{testresultid} | Get Synthetic test playback detail result description(metadata)
[**get_test_summary_list**](SyntheticTestPlaybackResultsApi.md#get_test_summary_list) | **POST** /api/synthetics/results/testsummarylist | Get a list of Synthetic tests with success rate and average response time data


# **get_location_summary_list**
> TestResultListResult get_location_summary_list(get_test_result_base=get_test_result_base)

Get a list of Synthetic locations with last run test on each location data

Get summary information for Synthetic locations matching the specified parameters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_test_result_base import GetTestResultBase
from instana_client.models.test_result_list_result import TestResultListResult
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    get_test_result_base = {"timeFrame":{"to":null,"windowSize":300000},"pagination":{"page":1,"pageSize":3}} # GetTestResultBase |  (optional)

    try:
        # Get a list of Synthetic locations with last run test on each location data
        api_response = api_instance.get_location_summary_list(get_test_result_base=get_test_result_base)
        print("The response of SyntheticTestPlaybackResultsApi->get_location_summary_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_location_summary_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_test_result_base** | [**GetTestResultBase**](GetTestResultBase.md)|  | [optional] 

### Return type

[**TestResultListResult**](TestResultListResult.md)

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
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_result**
> TestResult get_synthetic_result(get_test_result=get_test_result)

Get Synthetic test playback results

Get a list of aggregated playback results metrics for Synthetic tests matching the specified parameters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_test_result import GetTestResult
from instana_client.models.test_result import TestResult
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    get_test_result = {"pagination":{"page":1,"pageSize":3},"metrics":[{"metric":"synthetic.metricsResponseTime","aggregation":"SUM"}],"order":{"by":"synthetic.startTime","direction":"DESC"},"timeFrame":{"to":0,"windowSize":144000000}} # GetTestResult |  (optional)

    try:
        # Get Synthetic test playback results
        api_response = api_instance.get_synthetic_result(get_test_result=get_test_result)
        print("The response of SyntheticTestPlaybackResultsApi->get_synthetic_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_synthetic_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_test_result** | [**GetTestResult**](GetTestResult.md)|  | [optional] 

### Return type

[**TestResult**](TestResult.md)

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
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_result_analytic**
> TestResultListResult get_synthetic_result_analytic(get_test_result_analytic=get_test_result_analytic)

Get a list of Synthetic tests based on the specified analytic function

Get a list of playback results metrics for Synthetic tests matching the specified parameters for the specified analytic

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_test_result_analytic import GetTestResultAnalytic
from instana_client.models.test_result_list_result import TestResultListResult
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    get_test_result_analytic = {"pagination":{"page":1,"pageSize":3},"syntheticMetrics":["synthetic.metricsResponseTime","status","synthetic.errors"],"order":{"by":"start_time","direction":"DESC"},"timeFrame":{"to":0,"windowSize":144000000},"TagFilterExpression":{"type":"EXPRESSION","elements":[{"type":"EXPRESSION","elements":[{"name":"synthetic.errors","stringValue":"Exception","operator":"CONTAINS"}],"logicalOperator":"OR"}],"logicalOperator":"OR"},"analyticFunction":"LAST_VALUE"} # GetTestResultAnalytic |  (optional)

    try:
        # Get a list of Synthetic tests based on the specified analytic function
        api_response = api_instance.get_synthetic_result_analytic(get_test_result_analytic=get_test_result_analytic)
        print("The response of SyntheticTestPlaybackResultsApi->get_synthetic_result_analytic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_synthetic_result_analytic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_test_result_analytic** | [**GetTestResultAnalytic**](GetTestResultAnalytic.md)|  | [optional] 

### Return type

[**TestResultListResult**](TestResultListResult.md)

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
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_result_detail_data**
> TestResultDetailData get_synthetic_result_detail_data(testid, testresultid, type, name=name, start_time=start_time)

Get Synthetic test playback result detail data

Download the contents of the Synthetic the playback result detail data file matching the specified file type

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.test_result_detail_data import TestResultDetailData
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    testid = 'AMl0Y7tsvpp8XXrXt1XO' # str | Test id of the test result detailed file contents to be retrieved
    testresultid = '5623c161-31d6-49b8-b314-91d4fb598f55' # str | Test result id of the  test result detailed file to be retrieved
    type = 'LOGS' # str | Type of the test result detailed file contents
    name = 'console.log' # str | Name of the test result detailed file, if more than one file available for the same type. Can be used when parameter type=LOGS (optional)
    start_time = 1730295066008 # int | Start time of the test result detailed file contents (optional)

    try:
        # Get Synthetic test playback result detail data
        api_response = api_instance.get_synthetic_result_detail_data(testid, testresultid, type, name=name, start_time=start_time)
        print("The response of SyntheticTestPlaybackResultsApi->get_synthetic_result_detail_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_synthetic_result_detail_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testid** | **str**| Test id of the test result detailed file contents to be retrieved | 
 **testresultid** | **str**| Test result id of the  test result detailed file to be retrieved | 
 **type** | **str**| Type of the test result detailed file contents | 
 **name** | **str**| Name of the test result detailed file, if more than one file available for the same type. Can be used when parameter type&#x3D;LOGS | [optional] 
 **start_time** | **int**| Start time of the test result detailed file contents | [optional] 

### Return type

[**TestResultDetailData**](TestResultDetailData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_result_detail_data_file**
> get_synthetic_result_detail_data_file(testid, testresultid, type, start_time=start_time)

Download the synthetic test playback result detail data file

Download a Synthetic the playback result detail data file matching the specified file type

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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    testid = 'AMl0Y7tsvpp8XXrXt1XO' # str | Test id of the test result detailed file to be retrieved
    testresultid = '5623c161-31d6-49b8-b314-91d4fb598f55' # str | Test result id of the  test result detailed file to be retrieved
    type = 'LOGS' # str | Type of the test result detailed file
    start_time = 1730295066008 # int | Start time of the test result detailed file (optional)

    try:
        # Download the synthetic test playback result detail data file
        api_instance.get_synthetic_result_detail_data_file(testid, testresultid, type, start_time=start_time)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_synthetic_result_detail_data_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testid** | **str**| Test id of the test result detailed file to be retrieved | 
 **testresultid** | **str**| Test result id of the  test result detailed file to be retrieved | 
 **type** | **str**| Type of the test result detailed file | 
 **start_time** | **int**| Start time of the test result detailed file | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_result_list**
> TestResultListResult get_synthetic_result_list(get_test_result_list=get_test_result_list)

Get a list of Synthetic test playback results

Get a list of playback results metrics for Synthetic tests matching the specified parameters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_test_result_list import GetTestResultList
from instana_client.models.test_result_list_result import TestResultListResult
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    get_test_result_list = {"pagination":{"page":1,"pageSize":3},"syntheticMetrics":["synthetic.metricsResponseTime","status","synthetic.errors"],"order":{"by":"start_time","direction":"DESC"},"timeFrame":{"to":0,"windowSize":144000000},"TagFilterExpression":{"type":"EXPRESSION","elements":[{"type":"EXPRESSION","elements":[{"name":"synthetic.errors","stringValue":"Exception","operator":"CONTAINS"}],"logicalOperator":"OR"}],"logicalOperator":"OR"}} # GetTestResultList |  (optional)

    try:
        # Get a list of Synthetic test playback results
        api_response = api_instance.get_synthetic_result_list(get_test_result_list=get_test_result_list)
        print("The response of SyntheticTestPlaybackResultsApi->get_synthetic_result_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_synthetic_result_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_test_result_list** | [**GetTestResultList**](GetTestResultList.md)|  | [optional] 

### Return type

[**TestResultListResult**](TestResultListResult.md)

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
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_result_metadata**
> TestResultMetadata get_synthetic_result_metadata(testid, testresultid, start_time=start_time)

Get Synthetic test playback detail result description(metadata)

Gets the list of detailed data file names associated to a Synthetic playback result

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.test_result_metadata import TestResultMetadata
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    testid = 'AMl0Y7tsvpp8XXrXt1XO' # str | Test id of the test result detailed description to be retrieved
    testresultid = '5623c161-31d6-49b8-b314-91d4fb598f55' # str | Test result id of the test result detailed description to be retrieved
    start_time = 1730295066008 # int | Start time of the test result detailed description (optional)

    try:
        # Get Synthetic test playback detail result description(metadata)
        api_response = api_instance.get_synthetic_result_metadata(testid, testresultid, start_time=start_time)
        print("The response of SyntheticTestPlaybackResultsApi->get_synthetic_result_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_synthetic_result_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testid** | **str**| Test id of the test result detailed description to be retrieved | 
 **testresultid** | **str**| Test result id of the test result detailed description to be retrieved | 
 **start_time** | **int**| Start time of the test result detailed description | [optional] 

### Return type

[**TestResultMetadata**](TestResultMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_summary_list**
> TestResultListResult get_test_summary_list(get_test_summary_result=get_test_summary_result)

Get a list of Synthetic tests with success rate and average response time data

Get a summary of the playback results metrics and success rate for Synthetic tests matching the specified parameters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_test_summary_result import GetTestSummaryResult
from instana_client.models.test_result_list_result import TestResultListResult
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
    api_instance = instana_client.SyntheticTestPlaybackResultsApi(api_client)
    get_test_summary_result = {"metrics":[{"aggregation":"MEAN","metric":"success_rate","granularity":600}],"TagFilterExpression":{"type":"EXPRESSION","elements":[{"name":"synthetic.testActive","booleanValue":true,"operator":"EQUALS"}],"logicalOperator":"AND"},"timeFrame":{"to":0,"windowSize":1800000},"pagination":{"page":1,"pageSize":3}} # GetTestSummaryResult |  (optional)

    try:
        # Get a list of Synthetic tests with success rate and average response time data
        api_response = api_instance.get_test_summary_list(get_test_summary_result=get_test_summary_result)
        print("The response of SyntheticTestPlaybackResultsApi->get_test_summary_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticTestPlaybackResultsApi->get_test_summary_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_test_summary_result** | [**GetTestSummaryResult**](GetTestSummaryResult.md)|  | [optional] 

### Return type

[**TestResultListResult**](TestResultListResult.md)

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
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


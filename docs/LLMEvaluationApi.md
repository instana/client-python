# instana_client.LLMEvaluationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_evaluation**](LLMEvaluationApi.md#create_evaluation) | **POST** /api/genai-monitoring/evaluations | Create a new evaluation definition
[**delete_evaluation**](LLMEvaluationApi.md#delete_evaluation) | **DELETE** /api/genai-monitoring/evaluations/{evaluationId} | Delete an evaluation
[**delete_evaluator**](LLMEvaluationApi.md#delete_evaluator) | **DELETE** /api/evaluator/{evaluatorId} | Delete evaluator
[**get_evaluation**](LLMEvaluationApi.md#get_evaluation) | **GET** /api/genai-monitoring/evaluations/{evaluationId} | Get evaluation details by ID
[**get_evaluation_runs**](LLMEvaluationApi.md#get_evaluation_runs) | **GET** /api/genai-monitoring/evaluations/runs | Get all evaluation runs
[**get_evaluations**](LLMEvaluationApi.md#get_evaluations) | **GET** /api/genai-monitoring/evaluations | Get all evaluations
[**get_evaluator**](LLMEvaluationApi.md#get_evaluator) | **GET** /api/evaluator/{evaluatorId} | Get evaluator by ID
[**get_evaluators**](LLMEvaluationApi.md#get_evaluators) | **GET** /api/evaluator | Get all evaluators
[**get_gateway_status**](LLMEvaluationApi.md#get_gateway_status) | **GET** /api/genai-monitoring/evaluations/gateway-status | Check gateway status for evaluation capability
[**reset_evaluator**](LLMEvaluationApi.md#reset_evaluator) | **POST** /api/evaluator/{evaluatorId}/reset | Reset built-in evaluator
[**run_evaluation**](LLMEvaluationApi.md#run_evaluation) | **POST** /api/genai-monitoring/evaluations/{evaluationId}/run | Run an evaluation
[**update_evaluation**](LLMEvaluationApi.md#update_evaluation) | **PUT** /api/genai-monitoring/evaluations/{evaluationId} | Update an evaluation
[**upsert_evaluator**](LLMEvaluationApi.md#upsert_evaluator) | **PUT** /api/evaluator | Create or update evaluator


# **create_evaluation**
> CreateEvaluationResponse create_evaluation(create_evaluation_request=create_evaluation_request)

Create a new evaluation definition

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.create_evaluation_request import CreateEvaluationRequest
from instana_client.models.create_evaluation_response import CreateEvaluationResponse
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    create_evaluation_request = instana_client.CreateEvaluationRequest() # CreateEvaluationRequest |  (optional)

    try:
        # Create a new evaluation definition
        api_response = api_instance.create_evaluation(create_evaluation_request=create_evaluation_request)
        print("The response of LLMEvaluationApi->create_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->create_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_evaluation_request** | [**CreateEvaluationRequest**](CreateEvaluationRequest.md)|  | [optional] 

### Return type

[**CreateEvaluationResponse**](CreateEvaluationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Evaluation created successfully |  -  |
**400** | Invalid request |  -  |
**500** | Failed to create evaluation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_evaluation**
> delete_evaluation(evaluation_id)

Delete an evaluation

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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluation_id = 'evaluation_id_example' # str | 

    try:
        # Delete an evaluation
        api_instance.delete_evaluation(evaluation_id)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->delete_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation deleted successfully |  -  |
**404** | Evaluation not found |  -  |
**500** | Failed to delete evaluation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_evaluator**
> delete_evaluator(evaluator_id)

Delete evaluator

Delete an evaluator configuration by its ID.

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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluator_id = '123e4567-e89b-12d3-a456-426614174000' # str | 

    try:
        # Delete evaluator
        api_instance.delete_evaluator(evaluator_id)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->delete_evaluator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluator_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - Successfully deleted |  -  |
**404** | Not Found - Evaluator does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation**
> EvaluationDetailResponse get_evaluation(evaluation_id)

Get evaluation details by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.evaluation_detail_response import EvaluationDetailResponse
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluation_id = 'evaluation_id_example' # str | 

    try:
        # Get evaluation details by ID
        api_response = api_instance.get_evaluation(evaluation_id)
        print("The response of LLMEvaluationApi->get_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->get_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_id** | **str**|  | 

### Return type

[**EvaluationDetailResponse**](EvaluationDetailResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation retrieved successfully |  -  |
**404** | Evaluation not found |  -  |
**500** | Failed to retrieve evaluation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation_runs**
> str get_evaluation_runs(window_size=window_size, to=to)

Get all evaluation runs

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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    window_size = 56 # int |  (optional)
    to = 56 # int |  (optional)

    try:
        # Get all evaluation runs
        api_response = api_instance.get_evaluation_runs(window_size=window_size, to=to)
        print("The response of LLMEvaluationApi->get_evaluation_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->get_evaluation_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_size** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation runs retrieved successfully |  -  |
**404** | Evaluation runs not found |  -  |
**500** | Failed to retrieve evaluation runs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluations**
> EvaluationListResponse get_evaluations(client_id=client_id)

Get all evaluations

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.evaluation_list_response import EvaluationListResponse
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    client_id = 'client_id_example' # str |  (optional)

    try:
        # Get all evaluations
        api_response = api_instance.get_evaluations(client_id=client_id)
        print("The response of LLMEvaluationApi->get_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->get_evaluations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 

### Return type

[**EvaluationListResponse**](EvaluationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluations retrieved successfully |  -  |
**500** | Failed to retrieve evaluations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluator**
> Evaluator get_evaluator(evaluator_id)

Get evaluator by ID

Fetch a specific evaluator by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.evaluator import Evaluator
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluator_id = '123e4567-e89b-12d3-a456-426614174000' # str | 

    try:
        # Get evaluator by ID
        api_response = api_instance.get_evaluator(evaluator_id)
        print("The response of LLMEvaluationApi->get_evaluator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->get_evaluator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluator_id** | **str**|  | 

### Return type

[**Evaluator**](Evaluator.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluators**
> Evaluator get_evaluators()

Get all evaluators

Fetch all evaluator configurations for the current tenant unit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.evaluator import Evaluator
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
    api_instance = instana_client.LLMEvaluationApi(api_client)

    try:
        # Get all evaluators
        api_response = api_instance.get_evaluators()
        print("The response of LLMEvaluationApi->get_evaluators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->get_evaluators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Evaluator**](Evaluator.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gateway_status**
> GatewayStatusResponse get_gateway_status()

Check gateway status for evaluation capability

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.gateway_status_response import GatewayStatusResponse
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
    api_instance = instana_client.LLMEvaluationApi(api_client)

    try:
        # Check gateway status for evaluation capability
        api_response = api_instance.get_gateway_status()
        print("The response of LLMEvaluationApi->get_gateway_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->get_gateway_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayStatusResponse**](GatewayStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gateway status retrieved successfully |  -  |
**500** | Failed to check gateway status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_evaluator**
> reset_evaluator(evaluator_id)

Reset built-in evaluator

Reset a built-in evaluator to its system default configuration by soft-deleting the user's customized version.

### Example


```python
import instana_client
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)


# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluator_id = '123e4567-e89b-12d3-a456-426614174000' # str | 

    try:
        # Reset built-in evaluator
        api_instance.reset_evaluator(evaluator_id)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->reset_evaluator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluator_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - Successfully reset |  -  |
**400** | Bad Request - Not a built-in evaluator |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_evaluation**
> RunEvaluationResponse run_evaluation(evaluation_id)

Run an evaluation

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.run_evaluation_response import RunEvaluationResponse
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluation_id = 'evaluation_id_example' # str | 

    try:
        # Run an evaluation
        api_response = api_instance.run_evaluation(evaluation_id)
        print("The response of LLMEvaluationApi->run_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->run_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_id** | **str**|  | 

### Return type

[**RunEvaluationResponse**](RunEvaluationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation run initiated successfully |  -  |
**400** | Invalid request or capability not enabled |  -  |
**404** | Evaluation not found |  -  |
**500** | Failed to run evaluation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_evaluation**
> update_evaluation(evaluation_id, update_evaluation_request=update_evaluation_request)

Update an evaluation

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.update_evaluation_request import UpdateEvaluationRequest
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluation_id = 'evaluation_id_example' # str | 
    update_evaluation_request = instana_client.UpdateEvaluationRequest() # UpdateEvaluationRequest |  (optional)

    try:
        # Update an evaluation
        api_instance.update_evaluation(evaluation_id, update_evaluation_request=update_evaluation_request)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->update_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_id** | **str**|  | 
 **update_evaluation_request** | [**UpdateEvaluationRequest**](UpdateEvaluationRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation updated successfully |  -  |
**404** | Evaluation not found |  -  |
**500** | Failed to update evaluation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_evaluator**
> Evaluator upsert_evaluator(evaluator=evaluator)

Create or update evaluator

Create a new evaluator or update an existing one. Returns the evaluator ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.evaluator import Evaluator
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
    api_instance = instana_client.LLMEvaluationApi(api_client)
    evaluator = {"evaluatorName":"Quality Evaluator","criteria":"Response quality and accuracy","threshold":0.85} # Evaluator |  (optional)

    try:
        # Create or update evaluator
        api_response = api_instance.upsert_evaluator(evaluator=evaluator)
        print("The response of LLMEvaluationApi->upsert_evaluator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMEvaluationApi->upsert_evaluator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluator** | [**Evaluator**](Evaluator.md)|  | [optional] 

### Return type

[**Evaluator**](Evaluator.md)

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


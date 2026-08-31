# instana_client.AIManagementApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_llm_egress_gateway**](AIManagementApi.md#add_llm_egress_gateway) | **POST** /api/llm/gateways | Create a new AI connection
[**delete_llm_egress_gateway**](AIManagementApi.md#delete_llm_egress_gateway) | **DELETE** /api/llm/gateways/{id} | Delete an AI connection
[**disable_llm_egress_gateway**](AIManagementApi.md#disable_llm_egress_gateway) | **PUT** /api/llm/gateways/{id}/disable | Disable an AI connection
[**enable_llm_egress_gateway**](AIManagementApi.md#enable_llm_egress_gateway) | **PUT** /api/llm/gateways/{id}/enable | Enable an AI connection
[**get_llm_capabilities**](AIManagementApi.md#get_llm_capabilities) | **GET** /api/llm/capabilities | Get all LLM capabilities
[**get_llm_egress_gateway_by_id**](AIManagementApi.md#get_llm_egress_gateway_by_id) | **GET** /api/llm/gateways/{id} | Get an AI connection by ID
[**get_llm_egress_gateways**](AIManagementApi.md#get_llm_egress_gateways) | **GET** /api/llm/gateways | Get all AI connections
[**test_llm_gateway**](AIManagementApi.md#test_llm_gateway) | **POST** /api/llm/gateways/test | Test AI connection connection parameters
[**update_llm_egress_gateway**](AIManagementApi.md#update_llm_egress_gateway) | **PUT** /api/llm/gateways/{id} | Update an existing AI connection.


# **add_llm_egress_gateway**
> LLMEgressGateway add_llm_egress_gateway(llm_egress_gateway)

Create a new AI connection

Create a new AI connection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_egress_gateway import LLMEgressGateway
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
    api_instance = instana_client.AIManagementApi(api_client)
    llm_egress_gateway = {"name":"Example LLM egress Handler","description":"This is a sample custom handler used for testing.","aiModel":"watsonx-gpt-4","supports":{"capabilities":["anomaly-detection","remediation"]},"metadata":{"source":"user","version":"1.0.0"},"endpointUrl":"https://example.com/handler","endpointApiKey":"secret-api-key","watsonxKey":"watsonx-123","watsonxProject":"project-xyz","watsonxUrl":"https://watsonx.example.com","instanaAgents":{"agents":["agent-1","agent-2"]}} # LLMEgressGateway | 

    try:
        # Create a new AI connection
        api_response = api_instance.add_llm_egress_gateway(llm_egress_gateway)
        print("The response of AIManagementApi->add_llm_egress_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIManagementApi->add_llm_egress_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **llm_egress_gateway** | [**LLMEgressGateway**](LLMEgressGateway.md)|  | 

### Return type

[**LLMEgressGateway**](LLMEgressGateway.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_llm_egress_gateway**
> delete_llm_egress_gateway(id)

Delete an AI connection

Delete an AI connection by ID.

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
    api_instance = instana_client.AIManagementApi(api_client)
    id = 'id_example' # str | AI connection ID

    try:
        # Delete an AI connection
        api_instance.delete_llm_egress_gateway(id)
    except Exception as e:
        print("Exception when calling AIManagementApi->delete_llm_egress_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AI connection ID | 

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_llm_egress_gateway**
> disable_llm_egress_gateway(id)

Disable an AI connection

Disable an AI connection by ID.

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
    api_instance = instana_client.AIManagementApi(api_client)
    id = 'id_example' # str | AI connection ID

    try:
        # Disable an AI connection
        api_instance.disable_llm_egress_gateway(id)
    except Exception as e:
        print("Exception when calling AIManagementApi->disable_llm_egress_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AI connection ID | 

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_llm_egress_gateway**
> enable_llm_egress_gateway(id)

Enable an AI connection

Enable an AI connection by ID. Any other enabled connection for the same capability will be automatically disabled.

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
    api_instance = instana_client.AIManagementApi(api_client)
    id = 'id_example' # str | AI connection ID

    try:
        # Enable an AI connection
        api_instance.enable_llm_egress_gateway(id)
    except Exception as e:
        print("Exception when calling AIManagementApi->enable_llm_egress_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AI connection ID | 

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_llm_capabilities**
> List[str] get_llm_capabilities()

Get all LLM capabilities

Retrieve all available LLM capabilities.

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
    api_instance = instana_client.AIManagementApi(api_client)

    try:
        # Get all LLM capabilities
        api_response = api_instance.get_llm_capabilities()
        print("The response of AIManagementApi->get_llm_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIManagementApi->get_llm_capabilities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_llm_egress_gateway_by_id**
> LLMEgressGateway get_llm_egress_gateway_by_id(id)

Get an AI connection by ID

Retrieve an AI connection by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_egress_gateway import LLMEgressGateway
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
    api_instance = instana_client.AIManagementApi(api_client)
    id = 'id_example' # str | AI connection ID

    try:
        # Get an AI connection by ID
        api_response = api_instance.get_llm_egress_gateway_by_id(id)
        print("The response of AIManagementApi->get_llm_egress_gateway_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIManagementApi->get_llm_egress_gateway_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AI connection ID | 

### Return type

[**LLMEgressGateway**](LLMEgressGateway.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_llm_egress_gateways**
> List[LLMEgressGateway] get_llm_egress_gateways(enabled=enabled, capability=capability)

Get all AI connections

Retrieve all AI connections. Optionally filter by enabled status or capability.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_egress_gateway import LLMEgressGateway
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
    api_instance = instana_client.AIManagementApi(api_client)
    enabled = True # bool | Filter by enabled status (true/false) (optional)
    capability = 'capability_example' # str | Filter by capability name (optional)

    try:
        # Get all AI connections
        api_response = api_instance.get_llm_egress_gateways(enabled=enabled, capability=capability)
        print("The response of AIManagementApi->get_llm_egress_gateways:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIManagementApi->get_llm_egress_gateways: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**| Filter by enabled status (true/false) | [optional] 
 **capability** | **str**| Filter by capability name | [optional] 

### Return type

[**List[LLMEgressGateway]**](LLMEgressGateway.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_llm_gateway**
> TestConnectionResponse test_llm_gateway(llm_gateway_test_connection_request)

Test AI connection connection parameters

Test AI connection connection parameters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_gateway_test_connection_request import LLMGatewayTestConnectionRequest
from instana_client.models.test_connection_response import TestConnectionResponse
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
    api_instance = instana_client.AIManagementApi(api_client)
    llm_gateway_test_connection_request = {"id":"WATSONX","connectionParameters":{"url":"https://watsonx.example.com","apiKey":"secret-api-key","project":"project-xyz"}} # LLMGatewayTestConnectionRequest | 

    try:
        # Test AI connection connection parameters
        api_response = api_instance.test_llm_gateway(llm_gateway_test_connection_request)
        print("The response of AIManagementApi->test_llm_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIManagementApi->test_llm_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **llm_gateway_test_connection_request** | [**LLMGatewayTestConnectionRequest**](LLMGatewayTestConnectionRequest.md)|  | 

### Return type

[**TestConnectionResponse**](TestConnectionResponse.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_llm_egress_gateway**
> LLMEgressGateway update_llm_egress_gateway(id, llm_egress_gateway)

Update an existing AI connection.

Update an existing AI connection by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_egress_gateway import LLMEgressGateway
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
    api_instance = instana_client.AIManagementApi(api_client)
    id = 'id_example' # str | AI connection ID
    llm_egress_gateway = {"name":"Example LLM egress Handler","description":"This is a sample custom handler used for testing.","aiModel":"watsonx-gpt-4","supports":{"capabilities":["anomaly-detection","remediation"]},"metadata":{"source":"user","version":"1.0.0"},"endpointUrl":"https://example.com/handler","endpointApiKey":"secret-api-key","watsonxKey":"watsonx-123","watsonxProject":"project-xyz","watsonxUrl":"https://watsonx.example.com","instanaAgents":{"agents":["agent-1","agent-2"]}} # LLMEgressGateway | 

    try:
        # Update an existing AI connection.
        api_response = api_instance.update_llm_egress_gateway(id, llm_egress_gateway)
        print("The response of AIManagementApi->update_llm_egress_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIManagementApi->update_llm_egress_gateway: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| AI connection ID | 
 **llm_egress_gateway** | [**LLMEgressGateway**](LLMEgressGateway.md)|  | 

### Return type

[**LLMEgressGateway**](LLMEgressGateway.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


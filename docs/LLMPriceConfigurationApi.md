# instana_client.LLMPriceConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_llm_model_price**](LLMPriceConfigurationApi.md#delete_llm_model_price) | **DELETE** /api/settings/llm-pricing/{provider}/{modelName} | Delete LLM model price
[**delete_llm_model_price_without_provider**](LLMPriceConfigurationApi.md#delete_llm_model_price_without_provider) | **DELETE** /api/settings/llm-pricing/model/{modelName} | Delete LLM model price without provider
[**get_all_llm_model_prices**](LLMPriceConfigurationApi.md#get_all_llm_model_prices) | **GET** /api/settings/llm-pricing | Get all LLM model prices
[**get_llm_model_currency**](LLMPriceConfigurationApi.md#get_llm_model_currency) | **GET** /api/settings/llm-pricing/currency | Get currency for LLM model prices
[**get_llm_model_price**](LLMPriceConfigurationApi.md#get_llm_model_price) | **GET** /api/settings/llm-pricing/{provider}/{modelName} | Get LLM model price
[**get_llm_model_price_without_provider**](LLMPriceConfigurationApi.md#get_llm_model_price_without_provider) | **GET** /api/settings/llm-pricing/model/{modelName} | Get LLM model price without provider
[**set_llm_model_currency**](LLMPriceConfigurationApi.md#set_llm_model_currency) | **PUT** /api/settings/llm-pricing/currency | Set currency for LLM model prices
[**upsert_llm_model_price**](LLMPriceConfigurationApi.md#upsert_llm_model_price) | **PUT** /api/settings/llm-pricing/{provider}/{modelName} | Upsert LLM model price
[**upsert_llm_model_price_without_provider**](LLMPriceConfigurationApi.md#upsert_llm_model_price_without_provider) | **PUT** /api/settings/llm-pricing/model/{modelName} | Upsert LLM model price without provider


# **delete_llm_model_price**
> delete_llm_model_price(provider, model_name, platform=platform)

Delete LLM model price

Delete a tenant-specific price configuration for a specific provider+model. Optionally specify a platform. Only user-defined prices can be deleted.

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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    provider = 'openai' # str | 
    model_name = 'gpt-4' # str | 
    platform = 'aws' # str |  (optional)

    try:
        # Delete LLM model price
        api_instance.delete_llm_model_price(provider, model_name, platform=platform)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->delete_llm_model_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **model_name** | **str**|  | 
 **platform** | **str**|  | [optional] 

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
**404** | Not Found - Price configuration does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_llm_model_price_without_provider**
> delete_llm_model_price_without_provider(model_name, platform=platform)

Delete LLM model price without provider

Delete a tenant-specific price configuration for a model without specifying provider. Optionally specify a platform. Only user-defined prices can be deleted.

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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    model_name = 'gpt-4' # str | 
    platform = 'aws' # str |  (optional)

    try:
        # Delete LLM model price without provider
        api_instance.delete_llm_model_price_without_provider(model_name, platform=platform)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->delete_llm_model_price_without_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 
 **platform** | **str**|  | [optional] 

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
**404** | Not Found - Price configuration does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_llm_model_prices**
> LlmModelPrice get_all_llm_model_prices()

Get all LLM model prices

Fetch all LLM price configurations for the current tenant unit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price import LlmModelPrice
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)

    try:
        # Get all LLM model prices
        api_response = api_instance.get_all_llm_model_prices()
        print("The response of LLMPriceConfigurationApi->get_all_llm_model_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->get_all_llm_model_prices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LlmModelPrice**](LlmModelPrice.md)

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

# **get_llm_model_currency**
> LlmModelPriceMetadata get_llm_model_currency()

Get currency for LLM model prices

Fetch the currency code used for LLM model pricing.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price_metadata import LlmModelPriceMetadata
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)

    try:
        # Get currency for LLM model prices
        api_response = api_instance.get_llm_model_currency()
        print("The response of LLMPriceConfigurationApi->get_llm_model_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->get_llm_model_currency: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LlmModelPriceMetadata**](LlmModelPriceMetadata.md)

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

# **get_llm_model_price**
> LlmModelPrice get_llm_model_price(provider, model_name, platform=platform)

Get LLM model price

Fetch the price for a specific provider+model. Optionally specify a platform for platform-specific pricing.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price import LlmModelPrice
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    provider = 'openai' # str | 
    model_name = 'gpt-4' # str | 
    platform = 'aws' # str |  (optional)

    try:
        # Get LLM model price
        api_response = api_instance.get_llm_model_price(provider, model_name, platform=platform)
        print("The response of LLMPriceConfigurationApi->get_llm_model_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->get_llm_model_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **model_name** | **str**|  | 
 **platform** | **str**|  | [optional] 

### Return type

[**LlmModelPrice**](LlmModelPrice.md)

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

# **get_llm_model_price_without_provider**
> LlmModelPrice get_llm_model_price_without_provider(model_name, platform=platform)

Get LLM model price without provider

Fetch the price for a model without specifying provider. Optionally specify a platform for platform-specific pricing.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price import LlmModelPrice
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    model_name = 'gpt-4' # str | 
    platform = 'aws' # str |  (optional)

    try:
        # Get LLM model price without provider
        api_response = api_instance.get_llm_model_price_without_provider(model_name, platform=platform)
        print("The response of LLMPriceConfigurationApi->get_llm_model_price_without_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->get_llm_model_price_without_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 
 **platform** | **str**|  | [optional] 

### Return type

[**LlmModelPrice**](LlmModelPrice.md)

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

# **set_llm_model_currency**
> LlmModelPriceMetadata set_llm_model_currency(llm_model_price_metadata=llm_model_price_metadata)

Set currency for LLM model prices

Set the currency code used for LLM model pricing.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price_metadata import LlmModelPriceMetadata
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    llm_model_price_metadata = {"currencyCode":"USD"} # LlmModelPriceMetadata |  (optional)

    try:
        # Set currency for LLM model prices
        api_response = api_instance.set_llm_model_currency(llm_model_price_metadata=llm_model_price_metadata)
        print("The response of LLMPriceConfigurationApi->set_llm_model_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->set_llm_model_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **llm_model_price_metadata** | [**LlmModelPriceMetadata**](LlmModelPriceMetadata.md)|  | [optional] 

### Return type

[**LlmModelPriceMetadata**](LlmModelPriceMetadata.md)

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

# **upsert_llm_model_price**
> upsert_llm_model_price(provider, model_name, platform=platform, llm_model_price=llm_model_price)

Upsert LLM model price

Create or update price for a specific provider+model. Optionally specify a platform for platform-specific pricing.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price import LlmModelPrice
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    provider = 'openai' # str | 
    model_name = 'gpt-4' # str | 
    platform = 'aws' # str |  (optional)
    llm_model_price = {"inputCost":0.5,"outputCost":1.5} # LlmModelPrice |  (optional)

    try:
        # Upsert LLM model price
        api_instance.upsert_llm_model_price(provider, model_name, platform=platform, llm_model_price=llm_model_price)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->upsert_llm_model_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **model_name** | **str**|  | 
 **platform** | **str**|  | [optional] 
 **llm_model_price** | [**LlmModelPrice**](LlmModelPrice.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_llm_model_price_without_provider**
> upsert_llm_model_price_without_provider(model_name, platform=platform, llm_model_price=llm_model_price)

Upsert LLM model price without provider

Create or update price for a model without specifying provider. Optionally specify a platform for platform-specific pricing.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.llm_model_price import LlmModelPrice
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
    api_instance = instana_client.LLMPriceConfigurationApi(api_client)
    model_name = 'gpt-4' # str | 
    platform = 'aws' # str |  (optional)
    llm_model_price = {"inputCost":0.5,"outputCost":1.5} # LlmModelPrice |  (optional)

    try:
        # Upsert LLM model price without provider
        api_instance.upsert_llm_model_price_without_provider(model_name, platform=platform, llm_model_price=llm_model_price)
    except Exception as e:
        print("Exception when calling LLMPriceConfigurationApi->upsert_llm_model_price_without_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 
 **platform** | **str**|  | [optional] 
 **llm_model_price** | [**LlmModelPrice**](LlmModelPrice.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


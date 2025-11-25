# instana_client.CustomEntitiesApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entities**](CustomEntitiesApi.md#create_custom_entities) | **POST** /api/custom-entitytypes | Create a Custom Entity type
[**delete_custom_entity**](CustomEntitiesApi.md#delete_custom_entity) | **DELETE** /api/custom-entitytypes/{id} | Delete a Custom Entity Type
[**get_custom_entity**](CustomEntitiesApi.md#get_custom_entity) | **GET** /api/custom-entitytypes/{id} | Get custom Entity Types
[**list_custom_entities**](CustomEntitiesApi.md#list_custom_entities) | **GET** /api/custom-entitytypes | List custom Entity Type Definition
[**update_custom_entity**](CustomEntitiesApi.md#update_custom_entity) | **PUT** /api/custom-entitytypes/{id} | Update a Custom Entity Type


# **create_custom_entities**
> CustomEntityWithMetadata create_custom_entities(custom_entity_model)

Create a Custom Entity type

This end point creates a custom entity type

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_entity_model import CustomEntityModel
from instana_client.models.custom_entity_with_metadata import CustomEntityWithMetadata
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
    api_instance = instana_client.CustomEntitiesApi(api_client)
    custom_entity_model = instana_client.CustomEntityModel() # CustomEntityModel | 

    try:
        # Create a Custom Entity type
        api_response = api_instance.create_custom_entities(custom_entity_model)
        print("The response of CustomEntitiesApi->create_custom_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->create_custom_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_entity_model** | [**CustomEntityModel**](CustomEntityModel.md)|  | 

### Return type

[**CustomEntityWithMetadata**](CustomEntityWithMetadata.md)

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

# **delete_custom_entity**
> CustomEntityWithMetadata delete_custom_entity(id, custom_entity_model)

Delete a Custom Entity Type

This end point deletes a custom Entity type definition

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_entity_model import CustomEntityModel
from instana_client.models.custom_entity_with_metadata import CustomEntityWithMetadata
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
    api_instance = instana_client.CustomEntitiesApi(api_client)
    id = 'id_example' # str | 
    custom_entity_model = instana_client.CustomEntityModel() # CustomEntityModel | 

    try:
        # Delete a Custom Entity Type
        api_response = api_instance.delete_custom_entity(id, custom_entity_model)
        print("The response of CustomEntitiesApi->delete_custom_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->delete_custom_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_entity_model** | [**CustomEntityModel**](CustomEntityModel.md)|  | 

### Return type

[**CustomEntityWithMetadata**](CustomEntityWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_entity**
> CustomEntityWithMetadata get_custom_entity(id)

Get custom Entity Types

This endpoint gets custom Entity Type by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_entity_with_metadata import CustomEntityWithMetadata
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
    api_instance = instana_client.CustomEntitiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get custom Entity Types
        api_response = api_instance.get_custom_entity(id)
        print("The response of CustomEntitiesApi->get_custom_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CustomEntityWithMetadata**](CustomEntityWithMetadata.md)

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

# **list_custom_entities**
> CustomEntityWithMetadata list_custom_entities()

List custom Entity Type Definition

This end point lists custom Entity Type Definition

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_entity_with_metadata import CustomEntityWithMetadata
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
    api_instance = instana_client.CustomEntitiesApi(api_client)

    try:
        # List custom Entity Type Definition
        api_response = api_instance.list_custom_entities()
        print("The response of CustomEntitiesApi->list_custom_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->list_custom_entities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomEntityWithMetadata**](CustomEntityWithMetadata.md)

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

# **update_custom_entity**
> CustomEntityWithMetadata update_custom_entity(id, custom_entity_model)

Update a Custom Entity Type

This end points updates the definition of a custom entity type

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_entity_model import CustomEntityModel
from instana_client.models.custom_entity_with_metadata import CustomEntityWithMetadata
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
    api_instance = instana_client.CustomEntitiesApi(api_client)
    id = 'id_example' # str | 
    custom_entity_model = instana_client.CustomEntityModel() # CustomEntityModel | 

    try:
        # Update a Custom Entity Type
        api_response = api_instance.update_custom_entity(id, custom_entity_model)
        print("The response of CustomEntitiesApi->update_custom_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->update_custom_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_entity_model** | [**CustomEntityModel**](CustomEntityModel.md)|  | 

### Return type

[**CustomEntityWithMetadata**](CustomEntityWithMetadata.md)

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


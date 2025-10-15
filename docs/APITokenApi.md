# instana_client.APITokenApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_token**](APITokenApi.md#delete_api_token) | **DELETE** /api/settings/api-tokens/{internalId} | Delete API token
[**get_api_token**](APITokenApi.md#get_api_token) | **GET** /api/settings/api-tokens/{internalId} | Get API token
[**get_api_tokens**](APITokenApi.md#get_api_tokens) | **GET** /api/settings/api-tokens | Get all API Tokens
[**post_api_token**](APITokenApi.md#post_api_token) | **POST** /api/settings/api-tokens | Create an API token
[**put_api_token**](APITokenApi.md#put_api_token) | **PUT** /api/settings/api-tokens/{internalId} | Create or update an API token


# **delete_api_token**
> delete_api_token(internal_id)

Delete API token

Delete the Api Token
For more information on APIToken please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#apitoken.

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
    api_instance = instana_client.APITokenApi(api_client)
    internal_id = 'internal_id_example' # str | 

    try:
        # Delete API token
        api_instance.delete_api_token(internal_id)
    except Exception as e:
        print("Exception when calling APITokenApi->delete_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token**
> ApiToken get_api_token(internal_id)

Get API token

Returns API Token details, including the set of permissions
For more information on APIToken please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#apitoken.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_token import ApiToken
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
    api_instance = instana_client.APITokenApi(api_client)
    internal_id = 'internal_id_example' # str | 

    try:
        # Get API token
        api_response = api_instance.get_api_token(internal_id)
        print("The response of APITokenApi->get_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokenApi->get_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_id** | **str**|  | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **get_api_tokens**
> List[ApiToken] get_api_tokens()

Get all API Tokens

Get the list of API Tokens for this Tenant-Unit
For more information on APIToken please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#apitoken.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_token import ApiToken
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
    api_instance = instana_client.APITokenApi(api_client)

    try:
        # Get all API Tokens
        api_response = api_instance.get_api_tokens()
        print("The response of APITokenApi->get_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokenApi->get_api_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiToken]**](ApiToken.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No API Tokens found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_token**
> ApiToken post_api_token(api_token)

Create an API token

Create an API Token on the Tenant-Unit. Each API Token entry also contains a set of permissions
For more information on APIToken please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#apitoken.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_token import ApiToken
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
    api_instance = instana_client.APITokenApi(api_client)
    api_token = {
  "accessGrantingToken": "accessGrantingToken",
  "name": "tokenName",
  "internalId": "internalId",
  "canViewAuditLog": true,
  "canConfigureSessionSettings": true,
  "canConfigureApplications": true,
  "canConfigureAgents": true,
  "canConfigureUsers": true,
  "canConfigureEventsAndAlerts": true,
}
 # ApiToken | 

    try:
        # Create an API token
        api_response = api_instance.post_api_token(api_token)
        print("The response of APITokenApi->post_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokenApi->post_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | [**ApiToken**](ApiToken.md)|  | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **put_api_token**
> ApiToken put_api_token(internal_id, api_token)

Create or update an API token

Update API Token- Change Token name and associated permissions
For more information on APIToken please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#apitoken.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_token import ApiToken
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
    api_instance = instana_client.APITokenApi(api_client)
    internal_id = 'internal_id_example' # str | 
    api_token = {
  "accessGrantingToken": "accessGrantingToken",
  "name": "tokenName",
  "internalId": "internalId",
  "canViewAuditLog": true,
  "canConfigureSessionSettings": true,
  "canConfigureApplications": true,
  "canConfigureAgents": true,
  "canConfigureUsers": true,
  "canConfigureEventsAndAlerts": true,
}
 # ApiToken | 

    try:
        # Create or update an API token
        api_response = api_instance.put_api_token(internal_id, api_token)
        print("The response of APITokenApi->put_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokenApi->put_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_id** | **str**|  | 
 **api_token** | [**ApiToken**](ApiToken.md)|  | 

### Return type

[**ApiToken**](ApiToken.md)

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


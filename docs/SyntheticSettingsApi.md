# instana_client.SyntheticSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_synthetic_credential**](SyntheticSettingsApi.md#create_synthetic_credential) | **POST** /api/synthetics/settings/credentials | Create a Synthetic Credential
[**create_synthetic_test**](SyntheticSettingsApi.md#create_synthetic_test) | **POST** /api/synthetics/settings/tests | Create a Synthetic test
[**delete_synthetic_credential**](SyntheticSettingsApi.md#delete_synthetic_credential) | **DELETE** /api/synthetics/settings/credentials/{name} | Delete Synthetic credential
[**delete_synthetic_location**](SyntheticSettingsApi.md#delete_synthetic_location) | **DELETE** /api/synthetics/settings/locations/{id} | Delete Synthetic location
[**delete_synthetic_test**](SyntheticSettingsApi.md#delete_synthetic_test) | **DELETE** /api/synthetics/settings/tests/{id} | Delete a Synthetic test
[**get_one_synthetic_credential_associations**](SyntheticSettingsApi.md#get_one_synthetic_credential_associations) | **GET** /api/synthetics/settings/credentials/associations/{name} | A Synthetic Credential with Name and Associations
[**get_synthetic_credential_associations**](SyntheticSettingsApi.md#get_synthetic_credential_associations) | **GET** /api/synthetics/settings/credentials/associations | All Synthetic Credential Names and Associations
[**get_synthetic_credential_names**](SyntheticSettingsApi.md#get_synthetic_credential_names) | **GET** /api/synthetics/settings/credentials | All Synthetic Credential Names
[**get_synthetic_datacenter**](SyntheticSettingsApi.md#get_synthetic_datacenter) | **GET** /api/synthetics/settings/datacenters/{datacenterId} | Synthetic datacenter
[**get_synthetic_datacenters**](SyntheticSettingsApi.md#get_synthetic_datacenters) | **GET** /api/synthetics/settings/datacenters | All Synthetic datacenters
[**get_synthetic_location**](SyntheticSettingsApi.md#get_synthetic_location) | **GET** /api/synthetics/settings/locations/{id} | Synthetic location
[**get_synthetic_locations**](SyntheticSettingsApi.md#get_synthetic_locations) | **GET** /api/synthetics/settings/locations | All Synthetic locations
[**get_synthetic_test**](SyntheticSettingsApi.md#get_synthetic_test) | **GET** /api/synthetics/settings/tests/{id} | A Synthetic test
[**get_synthetic_tests**](SyntheticSettingsApi.md#get_synthetic_tests) | **GET** /api/synthetics/settings/tests | All Synthetic tests
[**patch_synthetic_credential**](SyntheticSettingsApi.md#patch_synthetic_credential) | **PATCH** /api/synthetics/settings/credentials/{name} | Patch a Synthetic Credential
[**patch_synthetic_test**](SyntheticSettingsApi.md#patch_synthetic_test) | **PATCH** /api/synthetics/settings/tests/{id} | Patch a Synthetic test
[**update_synthetic_credential**](SyntheticSettingsApi.md#update_synthetic_credential) | **PUT** /api/synthetics/settings/credentials/{name} | Update a Synthetic Credential
[**update_synthetic_test**](SyntheticSettingsApi.md#update_synthetic_test) | **PUT** /api/synthetics/settings/tests/{id} | Update a Synthetic test


# **create_synthetic_credential**
> create_synthetic_credential(synthetic_credential)

Create a Synthetic Credential

API request to create Synthetic Credentials.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_credential import SyntheticCredential
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    synthetic_credential = {"credentialName":"userPassword","credentialValue":"123456"} # SyntheticCredential | 

    try:
        # Create a Synthetic Credential
        api_instance.create_synthetic_credential(synthetic_credential)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->create_synthetic_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_credential** | [**SyntheticCredential**](SyntheticCredential.md)|  | 

### Return type

void (empty response body)

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

# **create_synthetic_test**
> SyntheticTest create_synthetic_test(synthetic_test)

Create a Synthetic test

This API endpoint creates a Synthetic Test.  **Note:** The **DNSAction** Synthetic type is not supported.  ## Optional Parameters:  - **id** Users are allowed to specify their own id for the test. A test id can contain letters, numbers, underscores, colons and hyphens. Maximum length is 128.  ## Sample script and payload:  - A sample script to create an API Simple test  ``` curl -k -v -X POST \\ https://<Host>/api/synthetics/settings/tests \\ -H 'authorization: apiToken <Token>' \\ -H 'content-type: application/json' \\ -d '{     \"id\":\"test_id:12134-89\",     \"label\":\"Test_SimplePing\",     \"description\":\"this is to test a simple ping API\",     \"serviceId\":\"serviceId001\",     \"applicationId\":\"applicationId001\",     \"active\":true,     \"testFrequency\":1,     \"playbackMode\":\"Simultaneous\",     \"locations\":[         \"saas_instana_test\"     ],     \"configuration\":{         \"syntheticType\":\"HTTPAction\",         \"url\":\"https://httpbin.org/post\",         \"operation\":\"POST\",         \"headers\":{             \"Content-Type\":\"text/plain\"         },         \"body\":\"Hello World!\",         \"validationString\":\"Hello World!\"     },     \"customProperties\":{         \"Team\":\"DevTeam\",         \"Purpose\":\"Demo\"     }   }' ```

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test import SyntheticTest
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    synthetic_test = {"label":"Test_SimplePing","description":"this is to test a simple ping API","serviceId":"serviceId001","applicationId":"applicationId001","active":true,"testFrequency":1,"playbackMode":"Simultaneous","locations":["saas_instana_test"],"configuration":{"syntheticType":"HTTPAction","url":"https://httpbin.org/post","operation":"POST","headers":{"Content-Type":"text/plain"},"body":"Hello World!","validationString":"Hello World!"},"customProperties":{"Team":"DevTeam","Purpose":"Demo"}} # SyntheticTest | 

    try:
        # Create a Synthetic test
        api_response = api_instance.create_synthetic_test(synthetic_test)
        print("The response of SyntheticSettingsApi->create_synthetic_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->create_synthetic_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_test** | [**SyntheticTest**](SyntheticTest.md)|  | 

### Return type

[**SyntheticTest**](SyntheticTest.md)

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

# **delete_synthetic_credential**
> delete_synthetic_credential(name)

Delete Synthetic credential

API request to delete a Synthetic Credential.

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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    name = 'password4test' # str | Name of the credential to be deleted

    try:
        # Delete Synthetic credential
        api_instance.delete_synthetic_credential(name)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->delete_synthetic_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the credential to be deleted | 

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
**200** | OK |  -  |
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_synthetic_location**
> delete_synthetic_location(id)

Delete Synthetic location

This API endpoint deletes a synthetic location.  Note: Users cannot use this API to delete managed locations. 

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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    id = '55bzhnXQ9uqwld4Ha3bD' # str | Identifier of the location to be deleted

    try:
        # Delete Synthetic location
        api_instance.delete_synthetic_location(id)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->delete_synthetic_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the location to be deleted | 

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
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_synthetic_test**
> delete_synthetic_test(id)

Delete a Synthetic test

API request to delete a Synthetic Test.

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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    id = 'ic25Vt1T5dgKzi0K7812' # str | Id of the synthetic test to be deleted

    try:
        # Delete a Synthetic test
        api_instance.delete_synthetic_test(id)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->delete_synthetic_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the synthetic test to be deleted | 

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
**200** | OK |  -  |
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_synthetic_credential_associations**
> SyntheticCredential get_one_synthetic_credential_associations(name)

A Synthetic Credential with Name and Associations

API request to retrieve a Synthetic Credential with matching name.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_credential import SyntheticCredential
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    name = 'password4test' # str | Name of the credential to be retrieved

    try:
        # A Synthetic Credential with Name and Associations
        api_response = api_instance.get_one_synthetic_credential_associations(name)
        print("The response of SyntheticSettingsApi->get_one_synthetic_credential_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_one_synthetic_credential_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the credential to be retrieved | 

### Return type

[**SyntheticCredential**](SyntheticCredential.md)

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

# **get_synthetic_credential_associations**
> List[SyntheticCredential] get_synthetic_credential_associations()

All Synthetic Credential Names and Associations

API request to retrieve all Synthetic Credentials.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_credential import SyntheticCredential
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)

    try:
        # All Synthetic Credential Names and Associations
        api_response = api_instance.get_synthetic_credential_associations()
        print("The response of SyntheticSettingsApi->get_synthetic_credential_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_credential_associations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SyntheticCredential]**](SyntheticCredential.md)

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

# **get_synthetic_credential_names**
> List[str] get_synthetic_credential_names()

All Synthetic Credential Names

API request to retrieve the names of all Synthetic Credentials.

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
    api_instance = instana_client.SyntheticSettingsApi(api_client)

    try:
        # All Synthetic Credential Names
        api_response = api_instance.get_synthetic_credential_names()
        print("The response of SyntheticSettingsApi->get_synthetic_credential_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_credential_names: %s\n" % e)
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
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_datacenter**
> SyntheticDatacenter get_synthetic_datacenter(datacenter_id)

Synthetic datacenter

API request to retrieve a Synthetic Datacenter with matching id.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_datacenter import SyntheticDatacenter
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    datacenter_id = 'aws-us-east-1-NVirginia' # str | Id of the datacenter to be retrieved

    try:
        # Synthetic datacenter
        api_response = api_instance.get_synthetic_datacenter(datacenter_id)
        print("The response of SyntheticSettingsApi->get_synthetic_datacenter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_datacenter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| Id of the datacenter to be retrieved | 

### Return type

[**SyntheticDatacenter**](SyntheticDatacenter.md)

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

# **get_synthetic_datacenters**
> List[SyntheticDatacenter] get_synthetic_datacenters()

All Synthetic datacenters

API request to retrieve all Synthetic Datacenters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_datacenter import SyntheticDatacenter
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)

    try:
        # All Synthetic datacenters
        api_response = api_instance.get_synthetic_datacenters()
        print("The response of SyntheticSettingsApi->get_synthetic_datacenters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_datacenters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SyntheticDatacenter]**](SyntheticDatacenter.md)

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
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_location**
> SyntheticLocation get_synthetic_location(id)

Synthetic location

API request to retrieve a Synthetic Location with matching id.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_location import SyntheticLocation
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    id = 'OjJPXWHmsE9deLzanNAW' # str | Identifier of the location to be retrieved

    try:
        # Synthetic location
        api_response = api_instance.get_synthetic_location(id)
        print("The response of SyntheticSettingsApi->get_synthetic_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the location to be retrieved | 

### Return type

[**SyntheticLocation**](SyntheticLocation.md)

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
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synthetic_locations**
> List[SyntheticLocation] get_synthetic_locations(sort=sort, offset=offset, limit=limit, filter=filter)

All Synthetic locations

This endpoint retrieves Synthetic Locations.  ## Optional Parameters:  - **filter** Filters the Synthetic Locations to retrieve only the ones that match the specified filter condition.    Users are allowed to specify more than one filter parameter, and they will be combined in a single expression using logical operator 'AND'.   The filter parameter is formatted as '**_{\\<attribute>\\<operator>\\<value}_**'. For example, '_{label=MyPoP}_'    ### Supported filter attributes and operators:  | | = | != | \\> | < | \\>= | <= | Example | |-|---|----|---|---|---|-|--------------------------------------------------------| | label | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={label=MyPoP} | | displayLabel | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={displayLabel=My PoP} | | popVersion | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={popVersion=1.1.9} | | description | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={description=My Test PoP} | | locationType | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={locationType=Private} | | playbackCapabilities.syntheticType | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={playbackCapabilities.syntheticType=HTTPAction} | | playbackCapabilities.browserType | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={playbackCapabilities.browserType=chrome} | | configuration.clusterName | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={configuration.clusterName=qa_cluster} | | configuration.namespace | &check; | &check; | - | - | - | - | /api/synthetics/settings/locations?filter={configuration.namespace=test_pop} | | customProperties.\\<all properties> | &check; | &check; | - | - | - | - | /api/ynthetics/settings/locations?filter={customProperty.usage=Test} | | createdAt | &check; | &check; | &check; | &check; | &check; | &check; | /api/synthetics/settings/locations?filter={createdAt>1715190462000} | | modifiedAt | &check; | &check; | &check; | &check; | &check; | &check; | /api/synthetics/settings/locations?filter={modifiedAt<=1715190462000} | | observerdAt | &check; | &check; | &check; | &check; | &check; | &check; | /api/synthetics/settings/locations?filter={observedAt>=1715190462000} |  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_location import SyntheticLocation
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    sort = '+label' # str | Defines the attribute by which the returned synthetic locations will be ordered by. Order using '+' means ASC and '-' means DESC (optional)
    offset = 1 # int | Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic locations (optional)
    limit = 10 # int | Defines the size of a page - the number of synthetic locations that will be returned by the query (optional)
    filter = '{locationType=Managed}' # str | Defines the attributes by which the returned synthetic locations will be filtered by. Multiple filter parameters are allowed. See 'Supported filter attributes and operators' for complete list of supported attributes and operators. (optional)

    try:
        # All Synthetic locations
        api_response = api_instance.get_synthetic_locations(sort=sort, offset=offset, limit=limit, filter=filter)
        print("The response of SyntheticSettingsApi->get_synthetic_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Defines the attribute by which the returned synthetic locations will be ordered by. Order using &#39;+&#39; means ASC and &#39;-&#39; means DESC | [optional] 
 **offset** | **int**| Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic locations | [optional] 
 **limit** | **int**| Defines the size of a page - the number of synthetic locations that will be returned by the query | [optional] 
 **filter** | **str**| Defines the attributes by which the returned synthetic locations will be filtered by. Multiple filter parameters are allowed. See &#39;Supported filter attributes and operators&#39; for complete list of supported attributes and operators. | [optional] 

### Return type

[**List[SyntheticLocation]**](SyntheticLocation.md)

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

# **get_synthetic_test**
> SyntheticTest get_synthetic_test(id)

A Synthetic test

API request to retrieve a Synthetic Test with matching id.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test import SyntheticTest
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    id = 'EFNRoPd39SgZBkULeQIf' # str | Id of the synthetic test to be retrieved

    try:
        # A Synthetic test
        api_response = api_instance.get_synthetic_test(id)
        print("The response of SyntheticSettingsApi->get_synthetic_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the synthetic test to be retrieved | 

### Return type

[**SyntheticTest**](SyntheticTest.md)

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

# **get_synthetic_tests**
> List[SyntheticTest] get_synthetic_tests(application_id=application_id, location_id=location_id, sort=sort, offset=offset, limit=limit, filter=filter)

All Synthetic tests

This endpoint retrieves Synthetic Tests.  ## Optional Parameters:  - **locationId** Filters the Synthetic Tests to retrieve only the ones that are associated to the specified PoP location ID. - **filter** Filters the Synthetic Tests to retrieve only the ones that match the specified filter condition.    Users are allowed to specify more than one filter parameter, and they will be combined in a single expression using logical operator 'AND'.   The filter parameter is formatted as '**_{\\<attribute>\\<operator>\\<value}_**'. For example, '_{label=MyTest}_'    ### Supported filter attributes and operators:  | | = | != | \\> | < | \\>= | <= | Example | |-|---|----|---|---|---|-|---------| | label | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={label=ABC} | | description | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={description=MyTest} | | active | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={active=true} | | testFrequency | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={testFrequency=5} | | applicationId | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={applicationId=APP_ID} | | locations | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={locations=POP_ID} | | locationLabels | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={locationLabels=MyPoP} | | locationDisplayLabels | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={locationDisplayLabels=My PoP} | | configuration.\\<any property of type string> | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={configurtion.syntheticType=HTTPAction} | | customProperties.\\<all properties> | &check; | &check; | - | - | - | - | /api/synthetics/settings/tests?filter={customProperty.usage=Test} | | createdAt | &check; | &check; | &check; | &check; | &check; | &check; | /api/synthetics/settings/tests?filter={createdAt>1715190462000} | | modifiedAt | &check; | &check; | &check; | &check; | &check; | &check; | /api/synthetics/settings/tests?filter={modifiedAt<=1715190462000} |  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test import SyntheticTest
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    application_id = 'pWoK4onRRN-POTz1RU62UQ' # str | Defines the application id by which the returned synthetic tests will be filtered by.  (optional)
    location_id = '18WyhtDb5jpVOsjlNdeV' # str | Defines the location id by which the returned synthetic tests will be filtered by.  (optional)
    sort = '+label' # str | Defines the attribute by which the returned synthetic tests will be ordered by. Order using '+' means ASC and '-' means DESC (optional)
    offset = 1 # int | Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic tests (optional)
    limit = 10 # int | Defines the size of a page - the number of synthetic tests that will be returned by the query (optional)
    filter = '{label=MyTest}' # str | Defines the attributes by which the returned synthetic tests will be filtered by. Multiple filter parameters are allowed. See 'Supported filter attributes and operators' for complete list of supported attributes and operators. (optional)

    try:
        # All Synthetic tests
        api_response = api_instance.get_synthetic_tests(application_id=application_id, location_id=location_id, sort=sort, offset=offset, limit=limit, filter=filter)
        print("The response of SyntheticSettingsApi->get_synthetic_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Defines the application id by which the returned synthetic tests will be filtered by.  | [optional] 
 **location_id** | **str**| Defines the location id by which the returned synthetic tests will be filtered by.  | [optional] 
 **sort** | **str**| Defines the attribute by which the returned synthetic tests will be ordered by. Order using &#39;+&#39; means ASC and &#39;-&#39; means DESC | [optional] 
 **offset** | **int**| Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic tests | [optional] 
 **limit** | **int**| Defines the size of a page - the number of synthetic tests that will be returned by the query | [optional] 
 **filter** | **str**| Defines the attributes by which the returned synthetic tests will be filtered by. Multiple filter parameters are allowed. See &#39;Supported filter attributes and operators&#39; for complete list of supported attributes and operators. | [optional] 

### Return type

[**List[SyntheticTest]**](SyntheticTest.md)

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
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_synthetic_credential**
> patch_synthetic_credential(name, synthetic_credential)

Patch a Synthetic Credential

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_credential import SyntheticCredential
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    name = 'password4test' # str | Name of the credential to be patched
    synthetic_credential = {"credentialValue":"password4test","applications":["f4KX5zd8RW2pERKKFUCZgQ"]} # SyntheticCredential | 

    try:
        # Patch a Synthetic Credential
        api_instance.patch_synthetic_credential(name, synthetic_credential)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->patch_synthetic_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the credential to be patched | 
 **synthetic_credential** | [**SyntheticCredential**](SyntheticCredential.md)|  | 

### Return type

void (empty response body)

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

# **patch_synthetic_test**
> patch_synthetic_test(id, synthetic_test)

Patch a Synthetic test

This API endpoint updates selected attributes of a Synthetic Test.  - All attributes listed as in the schema, including the required ones, are optional for this call. - Synthetic Test configuration properties set to null will be removed from the configuration. - Patching an array attribute will replace the entire array with the full set of values provided. - For major updates to the Synthetic Test or to remove main attributes, see \"Update a Synthetic test\"  ## Sample script and payload:  - A sample script to patch a simple HTTP Script Test to enable it and to switch from multi-scripts to single script.  ``` curl -k -v -X PATCH \\ https://<Host>/api/synthetics/settings/tests/Ilfs9bW97KkTxuyGtxBF \\ -H 'authorization: apiToken <Token>' \\ -H 'content-type: application/json' \\ -d '{     \"active\" : true,     \"configuration\" : {        \"scripts\" : null,       \"script\" : \"//script goes here\"     }   }' ```

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test import SyntheticTest
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    id = 'ic25Vt1T5dgKzi0K7812' # str | Id of the synthetic test to be patched
    synthetic_test = {"active":true,"configuration":{"scripts":null,"script":"//script goes here"}} # SyntheticTest | 

    try:
        # Patch a Synthetic test
        api_instance.patch_synthetic_test(id, synthetic_test)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->patch_synthetic_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the synthetic test to be patched | 
 **synthetic_test** | [**SyntheticTest**](SyntheticTest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_synthetic_credential**
> update_synthetic_credential(name, synthetic_credential)

Update a Synthetic Credential

API request to update Synthetic Credentials.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_credential import SyntheticCredential
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    name = 'password4db2' # str | Name of the credential to be updated
    synthetic_credential = {"credentialName":"password4db2","credentialValue":"123456","applications":["f4KX5zd8RW2pERKKFUCZgQ"]} # SyntheticCredential | 

    try:
        # Update a Synthetic Credential
        api_instance.update_synthetic_credential(name, synthetic_credential)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->update_synthetic_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the credential to be updated | 
 **synthetic_credential** | [**SyntheticCredential**](SyntheticCredential.md)|  | 

### Return type

void (empty response body)

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

# **update_synthetic_test**
> update_synthetic_test(id, synthetic_test)

Update a Synthetic test

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test import SyntheticTest
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
    api_instance = instana_client.SyntheticSettingsApi(api_client)
    id = 'ic25Vt1T5dgKzi0K7812' # str | Id of the synthetic test to be updated
    synthetic_test = {"id":"ic25Vt1T5dgKzi0K7812","label":"Test_SimplePing","description":"this is to test a simple ping API","serviceId":"serviceId001","applicationId":"applicationId001","active":true,"testFrequency":1,"playbackMode":"Simultaneous","locations":["saas_instana_test"],"configuration":{"syntheticType":"HTTPAction","url":"https://httpbin.org/post","operation":"POST","headers":{"Content-Type":"text/plain"},"body":"Hello World!","validationString":"Hello World!"},"customProperties":{"Team":"DevTeam","Purpose":"Demo"}} # SyntheticTest | 

    try:
        # Update a Synthetic test
        api_instance.update_synthetic_test(id, synthetic_test)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->update_synthetic_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the synthetic test to be updated | 
 **synthetic_test** | [**SyntheticTest**](SyntheticTest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# instana_client.SyntheticSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_synthetic_tests**](SyntheticSettingsApi.md#bulk_delete_synthetic_tests) | **POST** /api/synthetics/settings/tests/bulk-delete | Delete Synthetic tests
[**bulk_update_synthetic_tests**](SyntheticSettingsApi.md#bulk_update_synthetic_tests) | **POST** /api/synthetics/settings/tests/bulk-update | Update Synthetic tests
[**create_synthetic_credential**](SyntheticSettingsApi.md#create_synthetic_credential) | **POST** /api/synthetics/settings/credentials | Create a Synthetic credential
[**create_synthetic_test**](SyntheticSettingsApi.md#create_synthetic_test) | **POST** /api/synthetics/settings/tests | Create a Synthetic test
[**create_synthetic_test_cicd**](SyntheticSettingsApi.md#create_synthetic_test_cicd) | **POST** /api/synthetics/settings/tests/ci-cd | Create a Synthetic test CI/CD
[**delete_synthetic_credential**](SyntheticSettingsApi.md#delete_synthetic_credential) | **DELETE** /api/synthetics/settings/credentials/{name} | Delete a Synthetic credential
[**delete_synthetic_location**](SyntheticSettingsApi.md#delete_synthetic_location) | **DELETE** /api/synthetics/settings/locations/{id} | Delete a Synthetic location
[**delete_synthetic_test**](SyntheticSettingsApi.md#delete_synthetic_test) | **DELETE** /api/synthetics/settings/tests/{id} | Delete a Synthetic test
[**get_one_synthetic_credential_associations**](SyntheticSettingsApi.md#get_one_synthetic_credential_associations) | **GET** /api/synthetics/settings/credentials/associations/{name} | A Synthetic credential
[**get_synthetic_credential_associations**](SyntheticSettingsApi.md#get_synthetic_credential_associations) | **GET** /api/synthetics/settings/credentials/associations | All Synthetic credentials
[**get_synthetic_credential_names**](SyntheticSettingsApi.md#get_synthetic_credential_names) | **GET** /api/synthetics/settings/credentials | All Synthetic credential names
[**get_synthetic_datacenter**](SyntheticSettingsApi.md#get_synthetic_datacenter) | **GET** /api/synthetics/settings/datacenters/{datacenterId} | A Synthetic datacenter
[**get_synthetic_datacenters**](SyntheticSettingsApi.md#get_synthetic_datacenters) | **GET** /api/synthetics/settings/datacenters | All Synthetic datacenters
[**get_synthetic_location**](SyntheticSettingsApi.md#get_synthetic_location) | **GET** /api/synthetics/settings/locations/{id} | A Synthetic location
[**get_synthetic_locations**](SyntheticSettingsApi.md#get_synthetic_locations) | **GET** /api/synthetics/settings/locations | All Synthetic locations
[**get_synthetic_test**](SyntheticSettingsApi.md#get_synthetic_test) | **GET** /api/synthetics/settings/tests/{id} | A Synthetic test
[**get_synthetic_test_cicd**](SyntheticSettingsApi.md#get_synthetic_test_cicd) | **GET** /api/synthetics/settings/tests/ci-cd/{testResultId} | A Synthetic test CI/CD.
[**get_synthetic_test_cicds**](SyntheticSettingsApi.md#get_synthetic_test_cicds) | **GET** /api/synthetics/settings/tests/ci-cd | All Synthetic test CI/CDs
[**get_synthetic_tests**](SyntheticSettingsApi.md#get_synthetic_tests) | **GET** /api/synthetics/settings/tests | All Synthetic tests
[**patch_synthetic_credential**](SyntheticSettingsApi.md#patch_synthetic_credential) | **PATCH** /api/synthetics/settings/credentials/{name} | Patch a Synthetic credential
[**patch_synthetic_test**](SyntheticSettingsApi.md#patch_synthetic_test) | **PATCH** /api/synthetics/settings/tests/{id} | Patch a Synthetic test
[**update_synthetic_credential**](SyntheticSettingsApi.md#update_synthetic_credential) | **PUT** /api/synthetics/settings/credentials/{name} | Update a Synthetic credential
[**update_synthetic_test**](SyntheticSettingsApi.md#update_synthetic_test) | **PUT** /api/synthetics/settings/tests/{id} | Update a Synthetic test


# **bulk_delete_synthetic_tests**
> List[SyntheticBulkResponse] bulk_delete_synthetic_tests(request_body)

Delete Synthetic tests

API request to delete a list of Synthetic Tests.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_bulk_response import SyntheticBulkResponse
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
    request_body = ["ic25Vt1T5dgKzi0K7812","EFNRoPd39SgZBkULeQIf","kaj02pbxbW0XmQP9qu4b","FrhxAJzKdsXU6V4WxWrY"] # List[str] | 

    try:
        # Delete Synthetic tests
        api_response = api_instance.bulk_delete_synthetic_tests(request_body)
        print("The response of SyntheticSettingsApi->bulk_delete_synthetic_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->bulk_delete_synthetic_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**List[SyntheticBulkResponse]**](SyntheticBulkResponse.md)

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

# **bulk_update_synthetic_tests**
> List[SyntheticBulkResponse] bulk_update_synthetic_tests(synthetic_test_update)

Update Synthetic tests

API request to update a list of Synthetic Tests.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_bulk_response import SyntheticBulkResponse
from instana_client.models.synthetic_test_update import SyntheticTestUpdate
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
    synthetic_test_update = {
    "ids" : [
      "ic25Vt1T5dgKzi0K7812",
      "EFNRoPd39SgZBkULeQIf",
      "kaj02pbxbW0XmQP9qu4b",
      "FrhxAJzKdsXU6V4WxWrY"
    ],
    "locations": {
      "add": [ "hGyJAQCTnMbpmWrYfbq6", "RMtD8XkRHmxG5N0IT418" ],
      "remove": ["AOsPYuhGjpFHpNgWub90"],
    },
    "applications": {
      "add": [ "XRVRqG3zLNDKlJUho90j" ]
    },
    "configuration": {
      "timeout": "1s"
    },
    "customProperties": {
      "add": {
        "property1": "Test"
      },
      "remove": ["property2", "property3"],
    }
{
 # SyntheticTestUpdate | 

    try:
        # Update Synthetic tests
        api_response = api_instance.bulk_update_synthetic_tests(synthetic_test_update)
        print("The response of SyntheticSettingsApi->bulk_update_synthetic_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->bulk_update_synthetic_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_test_update** | [**SyntheticTestUpdate**](SyntheticTestUpdate.md)|  | 

### Return type

[**List[SyntheticBulkResponse]**](SyntheticBulkResponse.md)

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

# **create_synthetic_credential**
> create_synthetic_credential(synthetic_credential)

Create a Synthetic credential

API request to create a Synthetic Credential.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    synthetic_credential = {"credentialName":"userPassword","credentialValue":"123456","rbacTags":[{"id":"test","displayName":"test"}]} # SyntheticCredential | 

    try:
        # Create a Synthetic credential
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

API request to create a Synthetic Test.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    synthetic_test = {"label":"Test_SimplePing","description":"this is to test a simple ping API","applicationId":"applicationId001","active":true,"testFrequency":1,"playbackMode":"Simultaneous","locations":["saas_instana_test"],"configuration":{"syntheticType":"HTTPAction","url":"https://httpbin.org/post","operation":"POST","headers":{"Content-Type":"text/plain"},"body":"Hello World!","validationString":"Hello World!"},"customProperties":{"Team":"DevTeam","Purpose":"Demo"},"rbacTags":[{"id":"test","displayName":"test"}]} # SyntheticTest | 

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
**201** | Successful - resource created |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_synthetic_test_cicd**
> List[SyntheticTestCICDResponse] create_synthetic_test_cicd(synthetic_test_cicd)

Create a Synthetic test CI/CD

API request to create a Synthetic Test CI/CD.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test_cicd import SyntheticTestCICD
from instana_client.models.synthetic_test_cicd_response import SyntheticTestCICDResponse
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
    synthetic_test_cicd = [{"testId":"K331gkuCbelN1HI5y1wl","customization":{"locations":["8mCxCPOI7oEmMSee4ec0","lalQTzq7MwO6hZ6c6xDd"],"configuration":{"timeout":"100ms","retries":2},"customProperties":{"Team":"DevTeam","Purpose":"Demo"}}}] # List[SyntheticTestCICD] | 

    try:
        # Create a Synthetic test CI/CD
        api_response = api_instance.create_synthetic_test_cicd(synthetic_test_cicd)
        print("The response of SyntheticSettingsApi->create_synthetic_test_cicd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->create_synthetic_test_cicd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synthetic_test_cicd** | [**List[SyntheticTestCICD]**](SyntheticTestCICD.md)|  | 

### Return type

[**List[SyntheticTestCICDResponse]**](SyntheticTestCICDResponse.md)

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

Delete a Synthetic credential

API request to delete a Synthetic Credential.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # Delete a Synthetic credential
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_synthetic_location**
> delete_synthetic_location(id)

Delete a Synthetic location

API request to delete a Synthetic Location with matching id.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # Delete a Synthetic location
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
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_synthetic_credential_associations**
> SyntheticCredential get_one_synthetic_credential_associations(name)

A Synthetic credential

API request to retrieve a Synthetic Credential with matching name.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # A Synthetic credential
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

All Synthetic credentials

API request to retrieve all Synthetic Credentials.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # All Synthetic credentials
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

All Synthetic credential names

API request to retrieve the names of all Synthetic Credentials.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # All Synthetic credential names
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

A Synthetic datacenter

API request to retrieve a Synthetic Datacenter with matching id.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # A Synthetic datacenter
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
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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

A Synthetic location

API request to retrieve a Synthetic Location with matching id.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
        # A Synthetic location
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

API request to retrieve Synthetic Locations.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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

# **get_synthetic_test_cicd**
> SyntheticTestCICDItem get_synthetic_test_cicd(test_result_id)

A Synthetic test CI/CD.

API request to retrieve the Synthetic Test CI/CD identified by the given test result id.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test_cicd_item import SyntheticTestCICDItem
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
    test_result_id = '0cf1324b-3022-4116-ae03-6c868daa43d4' # str | The synthetic test result id of the CI/CD to be retrieved

    try:
        # A Synthetic test CI/CD.
        api_response = api_instance.get_synthetic_test_cicd(test_result_id)
        print("The response of SyntheticSettingsApi->get_synthetic_test_cicd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_test_cicd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_result_id** | **str**| The synthetic test result id of the CI/CD to be retrieved | 

### Return type

[**SyntheticTestCICDItem**](SyntheticTestCICDItem.md)

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

# **get_synthetic_test_cicds**
> List[SyntheticTestCICDItem] get_synthetic_test_cicds(filter=filter, offset=offset, limit=limit)

All Synthetic test CI/CDs

API request to retrieve the Synthetic Test CI/CDs
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.synthetic_test_cicd_item import SyntheticTestCICDItem
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
    filter = '{runType=OnDemand}' # str | Defines the attributes by which the returned synthetic test CI/CDs will be filtered by. Multiple filter parameters are allowed. See 'Supported filter attributes and operators' for complete list of supported attributes and operators. (optional)
    offset = 1 # int | Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic test CI/CDs (optional)
    limit = 10 # int | Defines the size of a page - the number of synthetic test CI/CDs that will be returned by the query (optional)

    try:
        # All Synthetic test CI/CDs
        api_response = api_instance.get_synthetic_test_cicds(filter=filter, offset=offset, limit=limit)
        print("The response of SyntheticSettingsApi->get_synthetic_test_cicds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntheticSettingsApi->get_synthetic_test_cicds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Defines the attributes by which the returned synthetic test CI/CDs will be filtered by. Multiple filter parameters are allowed. See &#39;Supported filter attributes and operators&#39; for complete list of supported attributes and operators. | [optional] 
 **offset** | **int**| Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic test CI/CDs | [optional] 
 **limit** | **int**| Defines the size of a page - the number of synthetic test CI/CDs that will be returned by the query | [optional] 

### Return type

[**List[SyntheticTestCICDItem]**](SyntheticTestCICDItem.md)

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

# **get_synthetic_tests**
> List[SyntheticTest] get_synthetic_tests(application_id=application_id, location_id=location_id, credential_name=credential_name, sort=sort, offset=offset, limit=limit, filter=filter)

All Synthetic tests

API request to retrieve Synthetic Tests.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    credential_name = 'adminPassword' # str | Defines the credential name by which the returned synthetic tests will be filtered by.  (optional)
    sort = '+label' # str | Defines the attribute by which the returned synthetic tests will be ordered by. Order using '+' means ASC and '-' means DESC (optional)
    offset = 1 # int | Used in conjunction with limit. Defines how many pages will be skipped before returning the synthetic tests (optional)
    limit = 10 # int | Defines the size of a page - the number of synthetic tests that will be returned by the query (optional)
    filter = '{label=MyTest}' # str | Defines the attributes by which the returned synthetic tests will be filtered by. Multiple filter parameters are allowed. See 'Supported filter attributes and operators' for complete list of supported attributes and operators. (optional)

    try:
        # All Synthetic tests
        api_response = api_instance.get_synthetic_tests(application_id=application_id, location_id=location_id, credential_name=credential_name, sort=sort, offset=offset, limit=limit, filter=filter)
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
 **credential_name** | **str**| Defines the credential name by which the returned synthetic tests will be filtered by.  | [optional] 
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

Patch a Synthetic credential

API request to patch attributes of a Synthetic Credential.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    synthetic_credential = {"credentialValue":"password4test","applications":["f4KX5zd8RW2pERKKFUCZgQ"],"rbacTags":[{"id":"test","displayName":"test"}]} # SyntheticCredential | 

    try:
        # Patch a Synthetic credential
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

API request to update a Synthetic Test.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    synthetic_test = {"active":true,"configuration":{"scripts":null,"script":"//script goes here"},"rbacTags":[{"id":"test","displayName":"test"}]} # SyntheticTest | 

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

Update a Synthetic credential

API request to update a Synthetic Credential.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    synthetic_credential = {"credentialName":"password4db2","credentialValue":"123456","applications":["f4KX5zd8RW2pERKKFUCZgQ"],"rbacTags":[{"id":"test","displayName":"test"}]} # SyntheticCredential | 

    try:
        # Update a Synthetic credential
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
**201** | Successful - resource created |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_synthetic_test**
> update_synthetic_test(id, synthetic_test)

Update a Synthetic test

API request to update a Synthetic Test.
For more information on Synthetic Settings please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Synthetic+Monitoring#synthetic-settings.

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
    synthetic_test = {"id":"ic25Vt1T5dgKzi0K7812","label":"Test_SimplePing","description":"this is to test a simple ping API","applicationId":"applicationId001","active":true,"testFrequency":1,"playbackMode":"Simultaneous","locations":["saas_instana_test"],"configuration":{"syntheticType":"HTTPAction","url":"https://httpbin.org/post","operation":"POST","headers":{"Content-Type":"text/plain"},"body":"Hello World!","validationString":"Hello World!"},"customProperties":{"Team":"DevTeam","Purpose":"Demo"},"rbacTags":[{"id":"JxrVZtRtTUGug71K1oYMcw","displayName":"tests"}]} # SyntheticTest | 

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


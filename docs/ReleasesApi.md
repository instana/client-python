# instana_client.ReleasesApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_release**](ReleasesApi.md#delete_release) | **DELETE** /api/releases/{releaseId} | Delete release
[**get_all_releases**](ReleasesApi.md#get_all_releases) | **GET** /api/releases | Get all releases
[**get_release**](ReleasesApi.md#get_release) | **GET** /api/releases/{releaseId} | Get release
[**post_release**](ReleasesApi.md#post_release) | **POST** /api/releases | Create release
[**put_release**](ReleasesApi.md#put_release) | **PUT** /api/releases/{releaseId} | Update release


# **delete_release**
> delete_release(release_id)

Delete release

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
    api_instance = instana_client.ReleasesApi(api_client)
    release_id = 'release_id_example' # str | 

    try:
        # Delete release
        api_instance.delete_release(release_id)
    except Exception as e:
        print("Exception when calling ReleasesApi->delete_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  | 

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

# **get_all_releases**
> List[ReleaseWithMetadata] get_all_releases(var_from=var_from, to=to, max_results=max_results)

Get all releases

This endpoint exposes the Releases functionality.  These APIs can be used to create, update, delete and fetch already existing releases.  ## Mandatory Parameters:  **releaseId:** A unique identifier assigned to each release.  ## Optional Parameters:  **name:** Name of the exact release you want to retrieve, eg. \"Release-161\", \"Release-162\".  **start:** Start time of the particular release (as UNIX timestamp in milliseconds).  **from:** Filters the releases to retrieve only the releases which have \"start\" time greater than or equal to this value (as UNIX timestamp in milliseconds).  **to:** Filters the releases to retrieve only the releases which have \"start\" time lesser than or equal to this value (as UNIX timestamp in milliseconds).  **maxResults:** Maximum number of releases to be retrieved.  ## Defaults:  **from, to, maxResults:** By default these parameters are not set.  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.release_with_metadata import ReleaseWithMetadata
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
    api_instance = instana_client.ReleasesApi(api_client)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    max_results = 56 # int |  (optional)

    try:
        # Get all releases
        api_response = api_instance.get_all_releases(var_from=var_from, to=to, max_results=max_results)
        print("The response of ReleasesApi->get_all_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_all_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **max_results** | **int**|  | [optional] 

### Return type

[**List[ReleaseWithMetadata]**](ReleaseWithMetadata.md)

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

# **get_release**
> ReleaseWithMetadata get_release(release_id)

Get release

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.release_with_metadata import ReleaseWithMetadata
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
    api_instance = instana_client.ReleasesApi(api_client)
    release_id = 'XK1e1TF3T9SHKugndn_soQ' # str | Release ID

    try:
        # Get release
        api_response = api_instance.get_release(release_id)
        print("The response of ReleasesApi->get_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**| Release ID | 

### Return type

[**ReleaseWithMetadata**](ReleaseWithMetadata.md)

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

# **post_release**
> ReleaseWithMetadata post_release(release)

Create release

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.release import Release
from instana_client.models.release_with_metadata import ReleaseWithMetadata
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
    api_instance = instana_client.ReleasesApi(api_client)
    release = instana_client.Release() # Release | 

    try:
        # Create release
        api_response = api_instance.post_release(release)
        print("The response of ReleasesApi->post_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->post_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release** | [**Release**](Release.md)|  | 

### Return type

[**ReleaseWithMetadata**](ReleaseWithMetadata.md)

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

# **put_release**
> ReleaseWithMetadata put_release(release_id, release)

Update release

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.release import Release
from instana_client.models.release_with_metadata import ReleaseWithMetadata
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
    api_instance = instana_client.ReleasesApi(api_client)
    release_id = 'release_id_example' # str | 
    release = instana_client.Release() # Release | 

    try:
        # Update release
        api_response = api_instance.put_release(release_id, release)
        print("The response of ReleasesApi->put_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->put_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  | 
 **release** | [**Release**](Release.md)|  | 

### Return type

[**ReleaseWithMetadata**](ReleaseWithMetadata.md)

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


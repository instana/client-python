# instana_client.CustomDashboardsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_dashboard**](CustomDashboardsApi.md#add_custom_dashboard) | **POST** /api/custom-dashboard | Add custom dashboard
[**delete_custom_dashboard**](CustomDashboardsApi.md#delete_custom_dashboard) | **DELETE** /api/custom-dashboard/{customDashboardId} | Remove custom dashboard
[**get_custom_dashboard**](CustomDashboardsApi.md#get_custom_dashboard) | **GET** /api/custom-dashboard/{customDashboardId} | Get custom dashboard
[**get_custom_dashboards**](CustomDashboardsApi.md#get_custom_dashboards) | **GET** /api/custom-dashboard | Get accessible custom dashboards
[**get_shareable_api_tokens**](CustomDashboardsApi.md#get_shareable_api_tokens) | **GET** /api/custom-dashboard/shareable-api-tokens | Get all API tokens.
[**get_shareable_users**](CustomDashboardsApi.md#get_shareable_users) | **GET** /api/custom-dashboard/shareable-users | Get all users (without invitations).
[**update_custom_dashboard**](CustomDashboardsApi.md#update_custom_dashboard) | **PUT** /api/custom-dashboard/{customDashboardId} | Update custom dashboard


# **add_custom_dashboard**
> CustomDashboard add_custom_dashboard(custom_dashboard=custom_dashboard)

Add custom dashboard

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_dashboard import CustomDashboard
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
    api_instance = instana_client.CustomDashboardsApi(api_client)
    custom_dashboard = instana_client.CustomDashboard() # CustomDashboard |  (optional)

    try:
        # Add custom dashboard
        api_response = api_instance.add_custom_dashboard(custom_dashboard=custom_dashboard)
        print("The response of CustomDashboardsApi->add_custom_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->add_custom_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_dashboard** | [**CustomDashboard**](CustomDashboard.md)|  | [optional] 

### Return type

[**CustomDashboard**](CustomDashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | When attempting to share dashboards without the canCreatePublicCustomDashboards permission. |  -  |
**422** | When the custom dashboard payload is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_dashboard**
> delete_custom_dashboard(custom_dashboard_id)

Remove custom dashboard

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
    api_instance = instana_client.CustomDashboardsApi(api_client)
    custom_dashboard_id = 'custom_dashboard_id_example' # str | 

    try:
        # Remove custom dashboard
        api_instance.delete_custom_dashboard(custom_dashboard_id)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->delete_custom_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_dashboard_id** | **str**|  | 

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
**204** | Custom dashboard successfully removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_dashboard**
> CustomDashboard get_custom_dashboard(custom_dashboard_id)

Get custom dashboard

Get all Custom Dashboard Info for specified customDashboardId.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_dashboard import CustomDashboard
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
    api_instance = instana_client.CustomDashboardsApi(api_client)
    custom_dashboard_id = 'alHaYV5aSkKku_wcg53teQ' # str | customDashboardId

    try:
        # Get custom dashboard
        api_response = api_instance.get_custom_dashboard(custom_dashboard_id)
        print("The response of CustomDashboardsApi->get_custom_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->get_custom_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_dashboard_id** | **str**| customDashboardId | 

### Return type

[**CustomDashboard**](CustomDashboard.md)

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

# **get_custom_dashboards**
> List[CustomDashboardPreview] get_custom_dashboards(query=query, page_size=page_size, page=page, with_total_hits=with_total_hits)

Get accessible custom dashboards

Get all accessible custom dashboards details.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_dashboard_preview import CustomDashboardPreview
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
    api_instance = instana_client.CustomDashboardsApi(api_client)
    query = 'BeeInstana' # str | query (optional)
    page_size = 2 # int | pageSize (optional)
    page = 1 # int | page (optional)
    with_total_hits = false # bool | withTotalHits (optional)

    try:
        # Get accessible custom dashboards
        api_response = api_instance.get_custom_dashboards(query=query, page_size=page_size, page=page, with_total_hits=with_total_hits)
        print("The response of CustomDashboardsApi->get_custom_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->get_custom_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | [optional] 
 **page_size** | **int**| pageSize | [optional] 
 **page** | **int**| page | [optional] 
 **with_total_hits** | **bool**| withTotalHits | [optional] 

### Return type

[**List[CustomDashboardPreview]**](CustomDashboardPreview.md)

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

# **get_shareable_api_tokens**
> List[DashboardApiToken] get_shareable_api_tokens()

Get all API tokens.

Get all API tokens that have access to shareable custom dashboards.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.dashboard_api_token import DashboardApiToken
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
    api_instance = instana_client.CustomDashboardsApi(api_client)

    try:
        # Get all API tokens.
        api_response = api_instance.get_shareable_api_tokens()
        print("The response of CustomDashboardsApi->get_shareable_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->get_shareable_api_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DashboardApiToken]**](DashboardApiToken.md)

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

# **get_shareable_users**
> List[UserBasicResult] get_shareable_users()

Get all users (without invitations).

Get all users (without invitations) that have access to shareable custom dashboards.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.user_basic_result import UserBasicResult
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
    api_instance = instana_client.CustomDashboardsApi(api_client)

    try:
        # Get all users (without invitations).
        api_response = api_instance.get_shareable_users()
        print("The response of CustomDashboardsApi->get_shareable_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->get_shareable_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserBasicResult]**](UserBasicResult.md)

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

# **update_custom_dashboard**
> CustomDashboard update_custom_dashboard(custom_dashboard_id, custom_dashboard=custom_dashboard)

Update custom dashboard

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_dashboard import CustomDashboard
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
    api_instance = instana_client.CustomDashboardsApi(api_client)
    custom_dashboard_id = 'custom_dashboard_id_example' # str | 
    custom_dashboard = instana_client.CustomDashboard() # CustomDashboard |  (optional)

    try:
        # Update custom dashboard
        api_response = api_instance.update_custom_dashboard(custom_dashboard_id, custom_dashboard=custom_dashboard)
        print("The response of CustomDashboardsApi->update_custom_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDashboardsApi->update_custom_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_dashboard_id** | **str**|  | 
 **custom_dashboard** | [**CustomDashboard**](CustomDashboard.md)|  | [optional] 

### Return type

[**CustomDashboard**](CustomDashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | When attempting to share dashboards without the canCreatePublicCustomDashboards permission. |  -  |
**422** | When the custom dashboard payload is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# instana_client.ApplicationResourcesApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_endpoints**](ApplicationResourcesApi.md#get_application_endpoints) | **GET** /api/application-monitoring/applications/services/endpoints | Get endpoints
[**get_application_services**](ApplicationResourcesApi.md#get_application_services) | **GET** /api/application-monitoring/applications/services | Get applications/services
[**get_applications**](ApplicationResourcesApi.md#get_applications) | **GET** /api/application-monitoring/applications | Get applications
[**get_services**](ApplicationResourcesApi.md#get_services) | **GET** /api/application-monitoring/services | Get services


# **get_application_endpoints**
> EndpointResult get_application_endpoints(name_filter=name_filter, types=types, technologies=technologies, window_size=window_size, to=to, page=page, page_size=page_size, application_boundary_scope=application_boundary_scope)

Get endpoints

Use this API endpoint if one wants to retrieve a list of Endpoints. A use case could be to view the endpoint id of an Endpoint. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.endpoint_result import EndpointResult
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
    api_instance = instana_client.ApplicationResourcesApi(api_client)
    name_filter = 'name_filter_example' # str | Name of service (optional)
    types = ['types_example'] # List[str] | Type of Endpoint (optional)
    technologies = ['technologies_example'] # List[str] | List of technologies (optional)
    window_size = 56 # int | Size of time window in milliseconds (optional)
    to = 56 # int | Timestamp since Unix Epoch in milliseconds of the end of the time window (optional)
    page = 56 # int | Page number from results (optional)
    page_size = 56 # int | Number of items per page (optional)
    application_boundary_scope = 'application_boundary_scope_example' # str | Filter for application scope, i.e: INBOUND or ALL (optional)

    try:
        # Get endpoints
        api_response = api_instance.get_application_endpoints(name_filter=name_filter, types=types, technologies=technologies, window_size=window_size, to=to, page=page, page_size=page_size, application_boundary_scope=application_boundary_scope)
        print("The response of ApplicationResourcesApi->get_application_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_application_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_filter** | **str**| Name of service | [optional] 
 **types** | [**List[str]**](str.md)| Type of Endpoint | [optional] 
 **technologies** | [**List[str]**](str.md)| List of technologies | [optional] 
 **window_size** | **int**| Size of time window in milliseconds | [optional] 
 **to** | **int**| Timestamp since Unix Epoch in milliseconds of the end of the time window | [optional] 
 **page** | **int**| Page number from results | [optional] 
 **page_size** | **int**| Number of items per page | [optional] 
 **application_boundary_scope** | **str**| Filter for application scope, i.e: INBOUND or ALL | [optional] 

### Return type

[**EndpointResult**](EndpointResult.md)

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

# **get_application_services**
> ServiceResult get_application_services(name_filter=name_filter, window_size=window_size, to=to, page=page, page_size=page_size, application_boundary_scope=application_boundary_scope, include_snapshot_ids=include_snapshot_ids)

Get applications/services

Use this API endpoint if one wants to retrieve a list of services in an Application Perspective. A use case could be to retrieve all service ids present in an Application Perspective. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_result import ServiceResult
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
    api_instance = instana_client.ApplicationResourcesApi(api_client)
    name_filter = 'name_filter_example' # str | Name of application/service (optional)
    window_size = 56 # int | Size of time window in milliseconds (optional)
    to = 56 # int | Timestamp since Unix Epoch in milliseconds of the end of the time window (optional)
    page = 56 # int | Page number from results (optional)
    page_size = 56 # int | Number of items per page (optional)
    application_boundary_scope = 'application_boundary_scope_example' # str | Filter for application scope, i.e: INBOUND or ALL (optional)
    include_snapshot_ids = True # bool | Include snapshot ids in the results (optional)

    try:
        # Get applications/services
        api_response = api_instance.get_application_services(name_filter=name_filter, window_size=window_size, to=to, page=page, page_size=page_size, application_boundary_scope=application_boundary_scope, include_snapshot_ids=include_snapshot_ids)
        print("The response of ApplicationResourcesApi->get_application_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_application_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_filter** | **str**| Name of application/service | [optional] 
 **window_size** | **int**| Size of time window in milliseconds | [optional] 
 **to** | **int**| Timestamp since Unix Epoch in milliseconds of the end of the time window | [optional] 
 **page** | **int**| Page number from results | [optional] 
 **page_size** | **int**| Number of items per page | [optional] 
 **application_boundary_scope** | **str**| Filter for application scope, i.e: INBOUND or ALL | [optional] 
 **include_snapshot_ids** | **bool**| Include snapshot ids in the results | [optional] 

### Return type

[**ServiceResult**](ServiceResult.md)

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

# **get_applications**
> ApplicationResult get_applications(name_filter=name_filter, window_size=window_size, to=to, page=page, page_size=page_size, application_boundary_scope=application_boundary_scope)

Get applications

Use this API endpoint if one wants to retrieve a list of Application Perspectives. A use case could be to view the application id of an Application Perspective. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_result import ApplicationResult
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
    api_instance = instana_client.ApplicationResourcesApi(api_client)
    name_filter = 'name_filter_example' # str | Name of application (optional)
    window_size = 56 # int | Size of time window in milliseconds (optional)
    to = 56 # int | Timestamp since Unix Epoch in milliseconds of the end of the time window (optional)
    page = 56 # int | Page number from results (optional)
    page_size = 56 # int | Number of items per page (optional)
    application_boundary_scope = 'application_boundary_scope_example' # str | Filter for application scope, i.e: INBOUND or ALL (optional)

    try:
        # Get applications
        api_response = api_instance.get_applications(name_filter=name_filter, window_size=window_size, to=to, page=page, page_size=page_size, application_boundary_scope=application_boundary_scope)
        print("The response of ApplicationResourcesApi->get_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_filter** | **str**| Name of application | [optional] 
 **window_size** | **int**| Size of time window in milliseconds | [optional] 
 **to** | **int**| Timestamp since Unix Epoch in milliseconds of the end of the time window | [optional] 
 **page** | **int**| Page number from results | [optional] 
 **page_size** | **int**| Number of items per page | [optional] 
 **application_boundary_scope** | **str**| Filter for application scope, i.e: INBOUND or ALL | [optional] 

### Return type

[**ApplicationResult**](ApplicationResult.md)

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

# **get_services**
> ServiceResult get_services(name_filter=name_filter, window_size=window_size, to=to, page=page, page_size=page_size, include_snapshot_ids=include_snapshot_ids)

Get services

Use this API endpoint if one wants to retrieve a list of Services. A use case could be to view the service id of a Service. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_result import ServiceResult
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
    api_instance = instana_client.ApplicationResourcesApi(api_client)
    name_filter = 'name_filter_example' # str | Name of service (optional)
    window_size = 56 # int | Size of time window in milliseconds (optional)
    to = 56 # int | Timestamp since Unix Epoch in milliseconds of the end of the time window (optional)
    page = 56 # int | Page number from results (optional)
    page_size = 56 # int | Number of items per page (optional)
    include_snapshot_ids = True # bool | Include snapshot ids in the results (optional)

    try:
        # Get services
        api_response = api_instance.get_services(name_filter=name_filter, window_size=window_size, to=to, page=page, page_size=page_size, include_snapshot_ids=include_snapshot_ids)
        print("The response of ApplicationResourcesApi->get_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_filter** | **str**| Name of service | [optional] 
 **window_size** | **int**| Size of time window in milliseconds | [optional] 
 **to** | **int**| Timestamp since Unix Epoch in milliseconds of the end of the time window | [optional] 
 **page** | **int**| Page number from results | [optional] 
 **page_size** | **int**| Number of items per page | [optional] 
 **include_snapshot_ids** | **bool**| Include snapshot ids in the results | [optional] 

### Return type

[**ServiceResult**](ServiceResult.md)

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


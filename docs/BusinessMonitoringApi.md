# instana_client.BusinessMonitoringApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_perspective**](BusinessMonitoringApi.md#create_business_perspective) | **POST** /api/business-monitoring/business-perspectives | Create business perspective
[**delete_business_perspective**](BusinessMonitoringApi.md#delete_business_perspective) | **DELETE** /api/business-monitoring/business-perspectives/{id} | Delete business perspective
[**get_activities**](BusinessMonitoringApi.md#get_activities) | **POST** /api/business-monitoring/activities | Get Business Activities
[**get_activities_csv**](BusinessMonitoringApi.md#get_activities_csv) | **POST** /api/business-monitoring/activities/csv | Download Business Activities
[**get_business_perspective**](BusinessMonitoringApi.md#get_business_perspective) | **GET** /api/business-monitoring/business-perspectives/{id} | Get business perspective
[**get_business_perspectives**](BusinessMonitoringApi.md#get_business_perspectives) | **GET** /api/business-monitoring/business-perspectives | Get all business perspectives
[**get_business_tag_catalog**](BusinessMonitoringApi.md#get_business_tag_catalog) | **GET** /api/business-monitoring/catalog | Get business tag catalog
[**update_business_perspective**](BusinessMonitoringApi.md#update_business_perspective) | **PUT** /api/business-monitoring/business-perspectives/{id} | Update business perspective


# **create_business_perspective**
> BusinessPerspectiveConfig create_business_perspective(new_business_perspective_config)

Create business perspective

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.business_perspective_config import BusinessPerspectiveConfig
from instana_client.models.new_business_perspective_config import NewBusinessPerspectiveConfig
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    new_business_perspective_config = {"label":"biz-perspective","name":"biz-perspective","description":"This is an example business perspective","rbacTags":[{"id":"0xHKaxfaS161Al6Qc23g4w","displayName":"team 1"}],"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"EXPRESSION","logicalOperator":"OR","elements":[{"type":"TAG_FILTER","name":"service.id","stringValue":"my-service-1","numberValue":null,"booleanValue":null,"key":null,"value":"my-service-1","operator":"EQUALS","entity":"DESTINATION"},{"type":"TAG_FILTER","name":"service.id","stringValue":"my-service-2","numberValue":null,"booleanValue":null,"key":null,"value":"my-service-2","operator":"EQUALS","entity":"DESTINATION"}]}]}]}} # NewBusinessPerspectiveConfig | 

    try:
        # Create business perspective
        api_response = api_instance.create_business_perspective(new_business_perspective_config)
        print("The response of BusinessMonitoringApi->create_business_perspective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->create_business_perspective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_business_perspective_config** | [**NewBusinessPerspectiveConfig**](NewBusinessPerspectiveConfig.md)|  | 

### Return type

[**BusinessPerspectiveConfig**](BusinessPerspectiveConfig.md)

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

# **delete_business_perspective**
> delete_business_perspective(id)

Delete business perspective

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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete business perspective
        api_instance.delete_business_perspective(id)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->delete_business_perspective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_activities**
> CursorPaginatedBusinessActivityItem get_activities(get_activities=get_activities)

Get Business Activities

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.cursor_paginated_business_activity_item import CursorPaginatedBusinessActivityItem
from instana_client.models.get_activities import GetActivities
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    get_activities = instana_client.GetActivities() # GetActivities |  (optional)

    try:
        # Get Business Activities
        api_response = api_instance.get_activities(get_activities=get_activities)
        print("The response of BusinessMonitoringApi->get_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->get_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_activities** | [**GetActivities**](GetActivities.md)|  | [optional] 

### Return type

[**CursorPaginatedBusinessActivityItem**](CursorPaginatedBusinessActivityItem.md)

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

# **get_activities_csv**
> BusinessActivity get_activities_csv(get_activities=get_activities)

Download Business Activities

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.business_activity import BusinessActivity
from instana_client.models.get_activities import GetActivities
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    get_activities = instana_client.GetActivities() # GetActivities |  (optional)

    try:
        # Download Business Activities
        api_response = api_instance.get_activities_csv(get_activities=get_activities)
        print("The response of BusinessMonitoringApi->get_activities_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->get_activities_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_activities** | [**GetActivities**](GetActivities.md)|  | [optional] 

### Return type

[**BusinessActivity**](BusinessActivity.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_perspective**
> BusinessPerspectiveConfig get_business_perspective(id)

Get business perspective

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.business_perspective_config import BusinessPerspectiveConfig
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get business perspective
        api_response = api_instance.get_business_perspective(id)
        print("The response of BusinessMonitoringApi->get_business_perspective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->get_business_perspective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BusinessPerspectiveConfig**](BusinessPerspectiveConfig.md)

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

# **get_business_perspectives**
> BusinessPerspectiveConfig get_business_perspectives()

Get all business perspectives

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.business_perspective_config import BusinessPerspectiveConfig
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)

    try:
        # Get all business perspectives
        api_response = api_instance.get_business_perspectives()
        print("The response of BusinessMonitoringApi->get_business_perspectives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->get_business_perspectives: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BusinessPerspectiveConfig**](BusinessPerspectiveConfig.md)

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

# **get_business_tag_catalog**
> TagCatalog get_business_tag_catalog(var_from=var_from, use_case=use_case)

Get business tag catalog

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.tag_catalog import TagCatalog
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    var_from = 56 # int |  (optional)
    use_case = 'use_case_example' # str |  (optional)

    try:
        # Get business tag catalog
        api_response = api_instance.get_business_tag_catalog(var_from=var_from, use_case=use_case)
        print("The response of BusinessMonitoringApi->get_business_tag_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->get_business_tag_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **use_case** | **str**|  | [optional] 

### Return type

[**TagCatalog**](TagCatalog.md)

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

# **update_business_perspective**
> BusinessPerspectiveConfig update_business_perspective(id, updated_business_perspective_config)

Update business perspective

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.business_perspective_config import BusinessPerspectiveConfig
from instana_client.models.updated_business_perspective_config import UpdatedBusinessPerspectiveConfig
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
    api_instance = instana_client.BusinessMonitoringApi(api_client)
    id = 'id_example' # str | 
    updated_business_perspective_config = {"label":"biz-perspective","name":"biz-perspective","rbacTags":[{"id":"0xHKaxfaS161Al6Qc23g4w","displayName":"team 1"}],"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"EXPRESSION","logicalOperator":"OR","elements":[{"type":"TAG_FILTER","name":"service.id","stringValue":"my-service-1","numberValue":null,"booleanValue":null,"key":null,"value":"my-service-1","operator":"EQUALS","entity":"DESTINATION"},{"type":"TAG_FILTER","name":"service.id","stringValue":"my-service-2","numberValue":null,"booleanValue":null,"key":null,"value":"my-service-2","operator":"EQUALS","entity":"DESTINATION"}]}]}]}} # UpdatedBusinessPerspectiveConfig | 

    try:
        # Update business perspective
        api_response = api_instance.update_business_perspective(id, updated_business_perspective_config)
        print("The response of BusinessMonitoringApi->update_business_perspective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessMonitoringApi->update_business_perspective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **updated_business_perspective_config** | [**UpdatedBusinessPerspectiveConfig**](UpdatedBusinessPerspectiveConfig.md)|  | 

### Return type

[**BusinessPerspectiveConfig**](BusinessPerspectiveConfig.md)

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


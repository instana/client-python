# instana_client.MobileAppCatalogApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_mobile_app_catalog_tags**](MobileAppCatalogApi.md#get_all_mobile_app_catalog_tags) | **GET** /api/mobile-app-monitoring/catalog/tags | Get all existing mobile app tags
[**get_mobile_app_metric_catalog**](MobileAppCatalogApi.md#get_mobile_app_metric_catalog) | **GET** /api/mobile-app-monitoring/catalog/metrics | Metric catalog
[**get_mobile_app_tag_catalog**](MobileAppCatalogApi.md#get_mobile_app_tag_catalog) | **GET** /api/mobile-app-monitoring/catalog | Get mobile app tag catalog


# **get_all_mobile_app_catalog_tags**
> List[Tag] get_all_mobile_app_catalog_tags()

Get all existing mobile app tags

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.tag import Tag
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
    api_instance = instana_client.MobileAppCatalogApi(api_client)

    try:
        # Get all existing mobile app tags
        api_response = api_instance.get_all_mobile_app_catalog_tags()
        print("The response of MobileAppCatalogApi->get_all_mobile_app_catalog_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppCatalogApi->get_all_mobile_app_catalog_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Tag]**](Tag.md)

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

# **get_mobile_app_metric_catalog**
> List[MobileAppMonitoringMetricDescription] get_mobile_app_metric_catalog()

Metric catalog

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app_monitoring_metric_description import MobileAppMonitoringMetricDescription
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
    api_instance = instana_client.MobileAppCatalogApi(api_client)

    try:
        # Metric catalog
        api_response = api_instance.get_mobile_app_metric_catalog()
        print("The response of MobileAppCatalogApi->get_mobile_app_metric_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppCatalogApi->get_mobile_app_metric_catalog: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MobileAppMonitoringMetricDescription]**](MobileAppMonitoringMetricDescription.md)

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

# **get_mobile_app_tag_catalog**
> TagCatalog get_mobile_app_tag_catalog(beacon_type, use_case)

Get mobile app tag catalog

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
    api_instance = instana_client.MobileAppCatalogApi(api_client)
    beacon_type = 'beacon_type_example' # str | 
    use_case = 'use_case_example' # str | 

    try:
        # Get mobile app tag catalog
        api_response = api_instance.get_mobile_app_tag_catalog(beacon_type, use_case)
        print("The response of MobileAppCatalogApi->get_mobile_app_tag_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppCatalogApi->get_mobile_app_tag_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beacon_type** | **str**|  | 
 **use_case** | **str**|  | 

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
**400** | When the combination of beaconType and useCase is unsupported/unknown. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


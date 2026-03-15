# instana_client.MobileAppCatalogApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_mobile_app_catalog_tags**](MobileAppCatalogApi.md#get_all_mobile_app_catalog_tags) | **GET** /api/mobile-app-monitoring/catalog/tags | Get all existing mobile app tags
[**get_mobile_app_metric_catalog**](MobileAppCatalogApi.md#get_mobile_app_metric_catalog) | **GET** /api/mobile-app-monitoring/catalog/metrics | Metric catalog
[**get_mobile_app_tag_catalog**](MobileAppCatalogApi.md#get_mobile_app_tag_catalog) | **GET** /api/mobile-app-monitoring/catalog | Get mobile app tag catalog
[**get_session_replay_metadata**](MobileAppCatalogApi.md#get_session_replay_metadata) | **GET** /api/mobile-app-monitoring/mobile-apps/{mobileAppId}/sessions/{sessionId}/replay-metadata | Get session replay metadata
[**get_session_replay_timestamps**](MobileAppCatalogApi.md#get_session_replay_timestamps) | **GET** /api/mobile-app-monitoring/mobile-apps/{mobileAppId}/sessions/{sessionId}/replay-timestamps | Get session replay timestamps


# **get_all_mobile_app_catalog_tags**
> List[Tag] get_all_mobile_app_catalog_tags()

Get all existing mobile app tags

API request to get all mobile app tags.

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

API request to get mobile app metric catalog.

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

# **get_session_replay_metadata**
> GetSessionReplayMetadataResult get_session_replay_metadata(mobile_app_id, session_id, cursor=cursor, page_size=page_size)

Get session replay metadata

Retrieves detailed metadata for session replay captured during a mobile app session. Uses cursor-based pagination with timestamp cursors. Returns metadata within the time window from cursor to cursor + pageSize. The pageSize represents milliseconds (default 20000ms = 20 seconds). Includes all metadata fields such as event type, view components, orientation changes, etc.

### Example


```python
import instana_client
from instana_client.models.get_session_replay_metadata_result import GetSessionReplayMetadataResult
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)


# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.MobileAppCatalogApi(api_client)
    mobile_app_id = 'app-456' # str | Mobile app identifier
    session_id = 'session-123' # str | Session identifier
    cursor = 1234567890 # int | Timestamp cursor for pagination (epoch milliseconds). Retrieves metadata from this timestamp onwards. (optional)
    page_size = 20000 # int | Time window size in milliseconds (default: 20000ms = 20 seconds) (optional) (default to 20000)

    try:
        # Get session replay metadata
        api_response = api_instance.get_session_replay_metadata(mobile_app_id, session_id, cursor=cursor, page_size=page_size)
        print("The response of MobileAppCatalogApi->get_session_replay_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppCatalogApi->get_session_replay_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile app identifier | 
 **session_id** | **str**| Session identifier | 
 **cursor** | **int**| Timestamp cursor for pagination (epoch milliseconds). Retrieves metadata from this timestamp onwards. | [optional] 
 **page_size** | **int**| Time window size in milliseconds (default: 20000ms &#x3D; 20 seconds) | [optional] [default to 20000]

### Return type

[**GetSessionReplayMetadataResult**](GetSessionReplayMetadataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Invalid mobile app ID, session ID, or pagination parameters |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Forbidden - User doesn&#39;t have access to this mobile app |  -  |
**404** | Not Found - Mobile app or session not found |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_replay_timestamps**
> SessionReplayTimestamps get_session_replay_timestamps(mobile_app_id, session_id)

Get session replay timestamps

Retrieves the first and last image timestamps for a mobile app session. Returns null values if the session has no images.

### Example


```python
import instana_client
from instana_client.models.session_replay_timestamps import SessionReplayTimestamps
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)


# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.MobileAppCatalogApi(api_client)
    mobile_app_id = 'app-456' # str | Mobile app identifier
    session_id = 'session-123' # str | Session identifier

    try:
        # Get session replay timestamps
        api_response = api_instance.get_session_replay_timestamps(mobile_app_id, session_id)
        print("The response of MobileAppCatalogApi->get_session_replay_timestamps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppCatalogApi->get_session_replay_timestamps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile app identifier | 
 **session_id** | **str**| Session identifier | 

### Return type

[**SessionReplayTimestamps**](SessionReplayTimestamps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Invalid mobile app ID or session ID |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Forbidden - User doesn&#39;t have access to this mobile app |  -  |
**404** | Not Found - Mobile app or session not found |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


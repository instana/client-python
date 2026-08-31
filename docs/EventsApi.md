# instana_client.EventsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_monitoring_events**](EventsApi.md#agent_monitoring_events) | **GET** /api/events/agent-monitoring-events | Get Agent Monitoring Events
[**bulk_delete_cross_type_alert_configs**](EventsApi.md#bulk_delete_cross_type_alert_configs) | **PUT** /api/events/settings/alert-configs/bulk/delete | Bulk delete alert configurations across multiple types
[**bulk_disable_cross_type_alert_configs**](EventsApi.md#bulk_disable_cross_type_alert_configs) | **PUT** /api/events/settings/alert-configs/bulk/disable | Bulk disable alert configurations across multiple types
[**bulk_enable_cross_type_alert_configs**](EventsApi.md#bulk_enable_cross_type_alert_configs) | **PUT** /api/events/settings/alert-configs/bulk/enable | Bulk enable alert configurations across multiple types
[**get_event**](EventsApi.md#get_event) | **GET** /api/events/{eventId} | Get Event
[**get_events**](EventsApi.md#get_events) | **GET** /api/events | Get all Events
[**get_events_by_ids**](EventsApi.md#get_events_by_ids) | **POST** /api/events | Get Events by IDs
[**kubernetes_info_events**](EventsApi.md#kubernetes_info_events) | **GET** /api/events/kubernetes-info-events | Get Kubernetes Info Events


# **agent_monitoring_events**
> List[EventResult] agent_monitoring_events(to=to, window_size=window_size, var_from=var_from, filter_event_updates=filter_event_updates, exclude_triggered_before=exclude_triggered_before)

Get Agent Monitoring Events

Gets all Agent Monitoring Events within a timeframe. The timeframe is defined as `[from, to]` or `[to - windowSize, to]`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_result import EventResult
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
    api_instance = instana_client.EventsApi(api_client)
    to = 1704096000000 # int | A Unix timestamp representing the end of the requested timeframe. Defaults to the current system time (optional)
    window_size = 600000 # int | The size of the requested timeframe, in milliseconds, relative to the 'to' parameter. Defaults to 10 minutes (600000 milliseconds) if neither 'windowSize' nor 'from' are provided. Resulting timeframe range = [to - windowSize, to] (optional)
    var_from = 1672560000000 # int | A Unix timestamp representing the start of the requested timeframe. Can be used as an alternative to 'windowSize' to define the timeframe. If both 'from' and 'windowSize' are provided, 'from' takes precedence. Resulting timeframe range = [from, to] (optional)
    filter_event_updates = true # bool | Flag to filter the results to only show events with state changes within the timeframe. (optional)
    exclude_triggered_before = true # bool | Flag to filter the results to exclude events that have been triggered before the timeframe. This also filters out events with state changes within the timeframe if the events' start times begin before the timeframe. (optional)

    try:
        # Get Agent Monitoring Events
        api_response = api_instance.agent_monitoring_events(to=to, window_size=window_size, var_from=var_from, filter_event_updates=filter_event_updates, exclude_triggered_before=exclude_triggered_before)
        print("The response of EventsApi->agent_monitoring_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->agent_monitoring_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **int**| A Unix timestamp representing the end of the requested timeframe. Defaults to the current system time | [optional] 
 **window_size** | **int**| The size of the requested timeframe, in milliseconds, relative to the &#39;to&#39; parameter. Defaults to 10 minutes (600000 milliseconds) if neither &#39;windowSize&#39; nor &#39;from&#39; are provided. Resulting timeframe range &#x3D; [to - windowSize, to] | [optional] 
 **var_from** | **int**| A Unix timestamp representing the start of the requested timeframe. Can be used as an alternative to &#39;windowSize&#39; to define the timeframe. If both &#39;from&#39; and &#39;windowSize&#39; are provided, &#39;from&#39; takes precedence. Resulting timeframe range &#x3D; [from, to] | [optional] 
 **filter_event_updates** | **bool**| Flag to filter the results to only show events with state changes within the timeframe. | [optional] 
 **exclude_triggered_before** | **bool**| Flag to filter the results to exclude events that have been triggered before the timeframe. This also filters out events with state changes within the timeframe if the events&#39; start times begin before the timeframe. | [optional] 

### Return type

[**List[EventResult]**](EventResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The events do not exist in the timeframe. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_cross_type_alert_configs**
> bulk_delete_cross_type_alert_configs(bulk_alert_config_request)

Bulk delete alert configurations across multiple types

Atomically deletes alert configurations across multiple types. All operations succeed or all fail. Deletion is logical (creates new version with deleted=true) to maintain audit trail. Requires appropriate permissions for each alert config type in the request. For example, deleting WEBSITE and APPLICATION configs requires both CAN_CONFIGURE_WEBSITE_SMART_ALERTS and CAN_CONFIGURE_APPLICATION_SMART_ALERTS permissions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.bulk_alert_config_request import BulkAlertConfigRequest
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
    api_instance = instana_client.EventsApi(api_client)
    bulk_alert_config_request = {"configs":{"WEBSITE":["id1","id2"],"APPLICATION":["id3","id4"],"INFRA":["id5"]}} # BulkAlertConfigRequest | Map of alert config types to sets of IDs to delete

    try:
        # Bulk delete alert configurations across multiple types
        api_instance.bulk_delete_cross_type_alert_configs(bulk_alert_config_request)
    except Exception as e:
        print("Exception when calling EventsApi->bulk_delete_cross_type_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_alert_config_request** | [**BulkAlertConfigRequest**](BulkAlertConfigRequest.md)| Map of alert config types to sets of IDs to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized - No valid authentication provided |  -  |
**403** | Forbidden - Missing required permissions for one or more alert config types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_cross_type_alert_configs**
> bulk_disable_cross_type_alert_configs(bulk_alert_config_request)

Bulk disable alert configurations across multiple types

Atomically disables alert configurations across multiple types. All operations succeed or all fail. Requires appropriate permissions for each alert config type in the request. For example, disabling WEBSITE and APPLICATION configs requires both CAN_CONFIGURE_WEBSITE_SMART_ALERTS and CAN_CONFIGURE_APPLICATION_SMART_ALERTS permissions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.bulk_alert_config_request import BulkAlertConfigRequest
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
    api_instance = instana_client.EventsApi(api_client)
    bulk_alert_config_request = {"configs":{"WEBSITE":["id1","id2"],"APPLICATION":["id3","id4"],"INFRA":["id5"]}} # BulkAlertConfigRequest | Map of alert config types to sets of IDs to disable

    try:
        # Bulk disable alert configurations across multiple types
        api_instance.bulk_disable_cross_type_alert_configs(bulk_alert_config_request)
    except Exception as e:
        print("Exception when calling EventsApi->bulk_disable_cross_type_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_alert_config_request** | [**BulkAlertConfigRequest**](BulkAlertConfigRequest.md)| Map of alert config types to sets of IDs to disable | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized - No valid authentication provided |  -  |
**403** | Forbidden - Missing required permissions for one or more alert config types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_cross_type_alert_configs**
> bulk_enable_cross_type_alert_configs(bulk_alert_config_request)

Bulk enable alert configurations across multiple types

Atomically enables alert configurations across multiple types. All operations succeed or all fail. Requires appropriate permissions for each alert config type in the request. For example, enabling WEBSITE and APPLICATION configs requires both CAN_CONFIGURE_WEBSITE_SMART_ALERTS and CAN_CONFIGURE_APPLICATION_SMART_ALERTS permissions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.bulk_alert_config_request import BulkAlertConfigRequest
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
    api_instance = instana_client.EventsApi(api_client)
    bulk_alert_config_request = {"configs":{"WEBSITE":["id1","id2"],"APPLICATION":["id3","id4"],"INFRA":["id5"]}} # BulkAlertConfigRequest | Map of alert config types to sets of IDs to enable

    try:
        # Bulk enable alert configurations across multiple types
        api_instance.bulk_enable_cross_type_alert_configs(bulk_alert_config_request)
    except Exception as e:
        print("Exception when calling EventsApi->bulk_enable_cross_type_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_alert_config_request** | [**BulkAlertConfigRequest**](BulkAlertConfigRequest.md)| Map of alert config types to sets of IDs to enable | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized - No valid authentication provided |  -  |
**403** | Forbidden - Missing required permissions for one or more alert config types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> EventResult get_event(event_id, include_metadata=include_metadata)

Get Event

Gets a specific event.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_result import EventResult
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
    api_instance = instana_client.EventsApi(api_client)
    event_id = 'LZOGo1lXR4WeCB2ftgtGGQ' # str | ID of a specific Event to retrieve.
    include_metadata = true # bool | Option to include event metadata (optional)

    try:
        # Get Event
        api_response = api_instance.get_event(event_id, include_metadata=include_metadata)
        print("The response of EventsApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| ID of a specific Event to retrieve. | 
 **include_metadata** | **bool**| Option to include event metadata | [optional] 

### Return type

[**EventResult**](EventResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The requested event does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> List[EventResult] get_events(to=to, window_size=window_size, var_from=var_from, filter_event_updates=filter_event_updates, exclude_triggered_before=exclude_triggered_before, include_agent_monitoring_issues=include_agent_monitoring_issues, include_kubernetes_info_events=include_kubernetes_info_events, event_type_filters=event_type_filters, include_metadata=include_metadata)

Get all Events

Get all Events within a timeframe. The timeframe is defined as `[from, to]` or `[to - windowSize, to]`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_result import EventResult
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
    api_instance = instana_client.EventsApi(api_client)
    to = 1704096000000 # int | A Unix timestamp representing the end of the requested timeframe. Defaults to the current system time (optional)
    window_size = 600000 # int | The size of the requested timeframe, in milliseconds, relative to the 'to' parameter. Defaults to 10 minutes (600000 milliseconds) if neither 'windowSize' nor 'from' are provided. Resulting timeframe range = [to - windowSize, to] (optional)
    var_from = 1672560000000 # int | A Unix timestamp representing the start of the requested timeframe. Can be used as an alternative to 'windowSize' to define the timeframe. If both 'from' and 'windowSize' are provided, 'from' takes precedence. Resulting timeframe range = [from, to] (optional)
    filter_event_updates = true # bool | Flag to filter the results to only show events with state changes within the timeframe. (optional)
    exclude_triggered_before = true # bool | Flag to filter the results to exclude events that have been triggered before the timeframe. This also filters out events with state changes within the timeframe if the events' start times begin before the timeframe. (optional)
    include_agent_monitoring_issues = true # bool | Flag to filter the results to include Agent Monitoring Issues. (optional)
    include_kubernetes_info_events = true # bool | Flag to filter the results to include Kubernetes Info Events. (optional)
    event_type_filters = ['INCIDENT'] # List[str] | A string representing an event type - an INCIDENT, ISSUE, or CHANGE. This query can be repeated to use multiple filters. (optional)
    include_metadata = true # bool | Option to include event metadata (optional)

    try:
        # Get all Events
        api_response = api_instance.get_events(to=to, window_size=window_size, var_from=var_from, filter_event_updates=filter_event_updates, exclude_triggered_before=exclude_triggered_before, include_agent_monitoring_issues=include_agent_monitoring_issues, include_kubernetes_info_events=include_kubernetes_info_events, event_type_filters=event_type_filters, include_metadata=include_metadata)
        print("The response of EventsApi->get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **int**| A Unix timestamp representing the end of the requested timeframe. Defaults to the current system time | [optional] 
 **window_size** | **int**| The size of the requested timeframe, in milliseconds, relative to the &#39;to&#39; parameter. Defaults to 10 minutes (600000 milliseconds) if neither &#39;windowSize&#39; nor &#39;from&#39; are provided. Resulting timeframe range &#x3D; [to - windowSize, to] | [optional] 
 **var_from** | **int**| A Unix timestamp representing the start of the requested timeframe. Can be used as an alternative to &#39;windowSize&#39; to define the timeframe. If both &#39;from&#39; and &#39;windowSize&#39; are provided, &#39;from&#39; takes precedence. Resulting timeframe range &#x3D; [from, to] | [optional] 
 **filter_event_updates** | **bool**| Flag to filter the results to only show events with state changes within the timeframe. | [optional] 
 **exclude_triggered_before** | **bool**| Flag to filter the results to exclude events that have been triggered before the timeframe. This also filters out events with state changes within the timeframe if the events&#39; start times begin before the timeframe. | [optional] 
 **include_agent_monitoring_issues** | **bool**| Flag to filter the results to include Agent Monitoring Issues. | [optional] 
 **include_kubernetes_info_events** | **bool**| Flag to filter the results to include Kubernetes Info Events. | [optional] 
 **event_type_filters** | [**List[str]**](str.md)| A string representing an event type - an INCIDENT, ISSUE, or CHANGE. This query can be repeated to use multiple filters. | [optional] 
 **include_metadata** | **bool**| Option to include event metadata | [optional] 

### Return type

[**List[EventResult]**](EventResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_ids**
> List[EventResult] get_events_by_ids(request_body, include_metadata=include_metadata)

Get Events by IDs

Gets a set of events by their IDs. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_result import EventResult
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
    api_instance = instana_client.EventsApi(api_client)
    request_body = ["VOMNl0OgRv2HXlsR0iUYGg","h66yezD9Sfi5YNh_cmeG7Q"] # List[str] | 
    include_metadata = true # bool | Option to include event metadata (optional)

    try:
        # Get Events by IDs
        api_response = api_instance.get_events_by_ids(request_body, include_metadata=include_metadata)
        print("The response of EventsApi->get_events_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **include_metadata** | **bool**| Option to include event metadata | [optional] 

### Return type

[**List[EventResult]**](EventResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**206** | Some of the requested events do not exist. |  -  |
**422** | Unprocessable entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_info_events**
> List[EventResult] kubernetes_info_events(to=to, window_size=window_size, var_from=var_from, filter_event_updates=filter_event_updates, exclude_triggered_before=exclude_triggered_before)

Get Kubernetes Info Events

Gets all Kubernetes Info Events within a timeframe. The timeframe is defined as `[from, to]` or `[to - windowSize, to]`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_result import EventResult
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
    api_instance = instana_client.EventsApi(api_client)
    to = 1704096000000 # int | A Unix timestamp representing the end of the requested timeframe. Defaults to the current system time (optional)
    window_size = 600000 # int | The size of the requested timeframe, in milliseconds, relative to the 'to' parameter. Defaults to 10 minutes (600000 milliseconds) if neither 'windowSize' nor 'from' are provided. Resulting timeframe range = [to - windowSize, to] (optional)
    var_from = 1672560000000 # int | A Unix timestamp representing the start of the requested timeframe. Can be used as an alternative to 'windowSize' to define the timeframe. If both 'from' and 'windowSize' are provided, 'from' takes precedence. Resulting timeframe range = [from, to] (optional)
    filter_event_updates = true # bool | Flag to filter the results to only show events with state changes within the timeframe. (optional)
    exclude_triggered_before = true # bool | Flag to filter the results to exclude events that have been triggered before the timeframe. This also filters out events with state changes within the timeframe if the events' start times begin before the timeframe. (optional)

    try:
        # Get Kubernetes Info Events
        api_response = api_instance.kubernetes_info_events(to=to, window_size=window_size, var_from=var_from, filter_event_updates=filter_event_updates, exclude_triggered_before=exclude_triggered_before)
        print("The response of EventsApi->kubernetes_info_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->kubernetes_info_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **int**| A Unix timestamp representing the end of the requested timeframe. Defaults to the current system time | [optional] 
 **window_size** | **int**| The size of the requested timeframe, in milliseconds, relative to the &#39;to&#39; parameter. Defaults to 10 minutes (600000 milliseconds) if neither &#39;windowSize&#39; nor &#39;from&#39; are provided. Resulting timeframe range &#x3D; [to - windowSize, to] | [optional] 
 **var_from** | **int**| A Unix timestamp representing the start of the requested timeframe. Can be used as an alternative to &#39;windowSize&#39; to define the timeframe. If both &#39;from&#39; and &#39;windowSize&#39; are provided, &#39;from&#39; takes precedence. Resulting timeframe range &#x3D; [from, to] | [optional] 
 **filter_event_updates** | **bool**| Flag to filter the results to only show events with state changes within the timeframe. | [optional] 
 **exclude_triggered_before** | **bool**| Flag to filter the results to exclude events that have been triggered before the timeframe. This also filters out events with state changes within the timeframe if the events&#39; start times begin before the timeframe. | [optional] 

### Return type

[**List[EventResult]**](EventResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The events do not exist in the timeframe. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


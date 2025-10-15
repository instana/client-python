# instana_client.InfrastructureResourcesApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_monitoring_state**](InfrastructureResourcesApi.md#get_monitoring_state) | **GET** /api/infrastructure-monitoring/monitoring-state | Monitored host count
[**get_plugin_payload**](InfrastructureResourcesApi.md#get_plugin_payload) | **GET** /api/infrastructure-monitoring/payloads/{snapshotId}/{payloadKey} | Get a payload for a snapshot
[**get_snapshot**](InfrastructureResourcesApi.md#get_snapshot) | **GET** /api/infrastructure-monitoring/snapshots/{id} | Get snapshot details
[**get_snapshots**](InfrastructureResourcesApi.md#get_snapshots) | **GET** /api/infrastructure-monitoring/snapshots | Search snapshots
[**post_snapshots**](InfrastructureResourcesApi.md#post_snapshots) | **POST** /api/infrastructure-monitoring/snapshots | Get snapshot details for multiple snapshots
[**software_versions**](InfrastructureResourcesApi.md#software_versions) | **GET** /api/infrastructure-monitoring/software/versions | Get installed software


# **get_monitoring_state**
> MonitoringState get_monitoring_state()

Monitored host count

This API endpoint retrieves the current monitoring state of the system, providing details about the number of monitored hosts and serverless entities. It responds with a JSON object containing this information.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.monitoring_state import MonitoringState
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
    api_instance = instana_client.InfrastructureResourcesApi(api_client)

    try:
        # Monitored host count
        api_response = api_instance.get_monitoring_state()
        print("The response of InfrastructureResourcesApi->get_monitoring_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureResourcesApi->get_monitoring_state: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MonitoringState**](MonitoringState.md)

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

# **get_plugin_payload**
> get_plugin_payload(snapshot_id, payload_key, to=to, window_size=window_size)

Get a payload for a snapshot

This endpoint retrieves the payload for a snapshot. Please note that this endpoint is only available for instances of db2.

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
    api_instance = instana_client.InfrastructureResourcesApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | Snapshot id.
    payload_key = 'topqueries' # str | Payload key. Use [getAvailablePayloadKeysByPluginId](/openapi/#operation/getAvailablePayloadKeysByPluginId) to retrieve the list of possible keys.
    to = 1689018652000 # int | End of timeframe expressed as the Unix epoch time in milliseconds. (optional)
    window_size = 3600000 # int | Window size in milliseconds. (optional)

    try:
        # Get a payload for a snapshot
        api_instance.get_plugin_payload(snapshot_id, payload_key, to=to, window_size=window_size)
    except Exception as e:
        print("Exception when calling InfrastructureResourcesApi->get_plugin_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot id. | 
 **payload_key** | **str**| Payload key. Use [getAvailablePayloadKeysByPluginId](/openapi/#operation/getAvailablePayloadKeysByPluginId) to retrieve the list of possible keys. | 
 **to** | **int**| End of timeframe expressed as the Unix epoch time in milliseconds. | [optional] 
 **window_size** | **int**| Window size in milliseconds. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> SnapshotItem get_snapshot(id, to=to, window_size=window_size)

Get snapshot details

Get all snapshot information

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.snapshot_item import SnapshotItem
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
    api_instance = instana_client.InfrastructureResourcesApi(api_client)
    id = 'id_example' # str | snapshot id
    to = 1689018652000 # int | end of timeframe expressed as the Unix epoch time in milliseconds (optional)
    window_size = 3600000 # int | windowSize in milliseconds (optional)

    try:
        # Get snapshot details
        api_response = api_instance.get_snapshot(id, to=to, window_size=window_size)
        print("The response of InfrastructureResourcesApi->get_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureResourcesApi->get_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| snapshot id | 
 **to** | **int**| end of timeframe expressed as the Unix epoch time in milliseconds | [optional] 
 **window_size** | **int**| windowSize in milliseconds | [optional] 

### Return type

[**SnapshotItem**](SnapshotItem.md)

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

# **get_snapshots**
> SnapshotResult get_snapshots(query=query, to=to, window_size=window_size, size=size, plugin=plugin, offline=offline)

Search snapshots

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.snapshot_result import SnapshotResult
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
    api_instance = instana_client.InfrastructureResourcesApi(api_client)
    query = 'entity.zone:myZone*' # str | query to use to filter snapshot retrieval (optional)
    to = 1689018652000 # int | end of timeframe expressed as the Unix epoch time in milliseconds (optional)
    window_size = 3600000 # int | windowSize in milliseconds (optional)
    size = 100 # int | maximum number of snapshots to retrieve (optional)
    plugin = 'host' # str | entity type (optional)
    offline = false # bool | retrieve snapshots which were online during the timeframe, otherwise, return only snapshot which were online at the end of the timeframe (optional)

    try:
        # Search snapshots
        api_response = api_instance.get_snapshots(query=query, to=to, window_size=window_size, size=size, plugin=plugin, offline=offline)
        print("The response of InfrastructureResourcesApi->get_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureResourcesApi->get_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query to use to filter snapshot retrieval | [optional] 
 **to** | **int**| end of timeframe expressed as the Unix epoch time in milliseconds | [optional] 
 **window_size** | **int**| windowSize in milliseconds | [optional] 
 **size** | **int**| maximum number of snapshots to retrieve | [optional] 
 **plugin** | **str**| entity type | [optional] 
 **offline** | **bool**| retrieve snapshots which were online during the timeframe, otherwise, return only snapshot which were online at the end of the timeframe | [optional] 

### Return type

[**SnapshotResult**](SnapshotResult.md)

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

# **post_snapshots**
> PostSnapshotsResult post_snapshots(get_snapshots_query=get_snapshots_query)

Get snapshot details for multiple snapshots

This endpoint retrieves detail information for one or more snapshots. timeFrame defaults to the last 10 minutes if not specified.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_snapshots_query import GetSnapshotsQuery
from instana_client.models.post_snapshots_result import PostSnapshotsResult
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
    api_instance = instana_client.InfrastructureResourcesApi(api_client)
    get_snapshots_query = {"snapshotIds":["AB3DeFGHIJkLm9OpQrstUVwxY_z","ZY4XwVUTSRqPo8MlKjihGFedC_a"],"timeFrame":{"to":1689018652000,"windowSize":3600000}} # GetSnapshotsQuery |  (optional)

    try:
        # Get snapshot details for multiple snapshots
        api_response = api_instance.post_snapshots(get_snapshots_query=get_snapshots_query)
        print("The response of InfrastructureResourcesApi->post_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureResourcesApi->post_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_snapshots_query** | [**GetSnapshotsQuery**](GetSnapshotsQuery.md)|  | [optional] 

### Return type

[**PostSnapshotsResult**](PostSnapshotsResult.md)

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

# **software_versions**
> List[SoftwareVersion] software_versions(time=time, discovery_type=discovery_type, software_type=software_type, name=name, plugin=plugin, version=version, vendor=vendor)

Get installed software

Retrieve information about the software that are sensed by the agent remotely, natively, or both. This includes runtime and package manager information.

The `plugin`, `name`, `version`, `discoveryType`, `softwareType` and `vendor` parameters are optional filters that can be used to reduce the result data set.
The `snapshotId` in `usedBy` is either of host or container, if available

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.software_version import SoftwareVersion
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
    api_instance = instana_client.InfrastructureResourcesApi(api_client)
    time = 56 # int | Timeframe expressed as the Unix epoch time in milliseconds (optional)
    discovery_type = 'NATIVE_SENSOR' # str | Filter on discoveryType (optional)
    software_type = 'DEPENDENCY' # str | Filter on softwareType (optional)
    name = 'name_example' # str | Filter on this software name (optional)
    plugin = 'plugin_example' # str | Filter on this plugin (optional)
    version = 'version_example' # str | Filter on this version (optional)
    vendor = 'vendor_example' # str | Filter on this vendor (optional)

    try:
        # Get installed software
        api_response = api_instance.software_versions(time=time, discovery_type=discovery_type, software_type=software_type, name=name, plugin=plugin, version=version, vendor=vendor)
        print("The response of InfrastructureResourcesApi->software_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureResourcesApi->software_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **int**| Timeframe expressed as the Unix epoch time in milliseconds | [optional] 
 **discovery_type** | **str**| Filter on discoveryType | [optional] 
 **software_type** | **str**| Filter on softwareType | [optional] 
 **name** | **str**| Filter on this software name | [optional] 
 **plugin** | **str**| Filter on this plugin | [optional] 
 **version** | **str**| Filter on this version | [optional] 
 **vendor** | **str**| Filter on this vendor | [optional] 

### Return type

[**List[SoftwareVersion]**](SoftwareVersion.md)

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


# instana_client.InfrastructureTopologyApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_related_hosts**](InfrastructureTopologyApi.md#get_related_hosts) | **GET** /api/infrastructure-monitoring/graph/related-hosts/{snapshotId} | Related hosts
[**get_topology**](InfrastructureTopologyApi.md#get_topology) | **GET** /api/infrastructure-monitoring/topology | Gets the infrastructure topology


# **get_related_hosts**
> List[str] get_related_hosts(snapshot_id, window_size=window_size, to=to)

Related hosts

Gets the Related Hosts

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
    api_instance = instana_client.InfrastructureTopologyApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | Snapshot ID running on the host
    window_size = 56 # int | Size of time window in milliseconds (optional)
    to = 56 # int | Timestamp since Unix Epoch in milliseconds of the end of the time window (optional)

    try:
        # Related hosts
        api_response = api_instance.get_related_hosts(snapshot_id, window_size=window_size, to=to)
        print("The response of InfrastructureTopologyApi->get_related_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureTopologyApi->get_related_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID running on the host | 
 **window_size** | **int**| Size of time window in milliseconds | [optional] 
 **to** | **int**| Timestamp since Unix Epoch in milliseconds of the end of the time window | [optional] 

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
**200** | Returns the snapshot ID of the hosts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology**
> Topology get_topology(include_data=include_data)

Gets the infrastructure topology

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.topology import Topology
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
    api_instance = instana_client.InfrastructureTopologyApi(api_client)
    include_data = True # bool | Include snapshot data in nodes (optional)

    try:
        # Gets the infrastructure topology
        api_response = api_instance.get_topology(include_data=include_data)
        print("The response of InfrastructureTopologyApi->get_topology:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureTopologyApi->get_topology: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_data** | **bool**| Include snapshot data in nodes | [optional] 

### Return type

[**Topology**](Topology.md)

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


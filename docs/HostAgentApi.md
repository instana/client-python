# instana_client.HostAgentApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_clr_logs**](HostAgentApi.md#get_agent_clr_logs) | **GET** /api/host-agent/{hostId}/clr-logs | Agent CLR download logs
[**get_agent_logs**](HostAgentApi.md#get_agent_logs) | **GET** /api/host-agent/{hostId}/logs | Agent download logs
[**get_agent_snapshot**](HostAgentApi.md#get_agent_snapshot) | **GET** /api/host-agent/{id} | Get host agent snapshot details
[**get_agent_support_information**](HostAgentApi.md#get_agent_support_information) | **GET** /api/host-agent/{hostId}/support-info | Agent download support information
[**search_host_agents**](HostAgentApi.md#search_host_agents) | **GET** /api/host-agent | Query host agent snapshots
[**update_agent**](HostAgentApi.md#update_agent) | **POST** /api/host-agent/{hostId}/update | Agent update
[**update_configuration_by_host**](HostAgentApi.md#update_configuration_by_host) | **POST** /api/host-agent/{hostId}/configuration | Update agent configuration by host
[**update_configuration_by_query**](HostAgentApi.md#update_configuration_by_query) | **POST** /api/host-agent/configuration | Update agent configuration by query


# **get_agent_clr_logs**
> get_agent_clr_logs(host_id, download=download)

Agent CLR download logs

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
    api_instance = instana_client.HostAgentApi(api_client)
    host_id = 'host_id_example' # str | 
    download = True # bool |  (optional)

    try:
        # Agent CLR download logs
        api_instance.get_agent_clr_logs(host_id, download=download)
    except Exception as e:
        print("Exception when calling HostAgentApi->get_agent_clr_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
 **download** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_logs**
> get_agent_logs(host_id, file, download=download)

Agent download logs

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
    api_instance = instana_client.HostAgentApi(api_client)
    host_id = 'host_id_example' # str | 
    file = ['file_example'] # List[str] | 
    download = True # bool |  (optional)

    try:
        # Agent download logs
        api_instance.get_agent_logs(host_id, file, download=download)
    except Exception as e:
        print("Exception when calling HostAgentApi->get_agent_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
 **file** | [**List[str]**](str.md)|  | 
 **download** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_snapshot**
> SnapshotItem get_agent_snapshot(id, to=to, window_size=window_size)

Get host agent snapshot details

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
    api_instance = instana_client.HostAgentApi(api_client)
    id = 'id_example' # str | 
    to = 56 # int |  (optional)
    window_size = 56 # int |  (optional)

    try:
        # Get host agent snapshot details
        api_response = api_instance.get_agent_snapshot(id, to=to, window_size=window_size)
        print("The response of HostAgentApi->get_agent_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAgentApi->get_agent_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **to** | **int**|  | [optional] 
 **window_size** | **int**|  | [optional] 

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

# **get_agent_support_information**
> get_agent_support_information(host_id, support_info_id)

Agent download support information

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
    api_instance = instana_client.HostAgentApi(api_client)
    host_id = 'host_id_example' # str | 
    support_info_id = 'support_info_id_example' # str | 

    try:
        # Agent download support information
        api_instance.get_agent_support_information(host_id, support_info_id)
    except Exception as e:
        print("Exception when calling HostAgentApi->get_agent_support_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
 **support_info_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_host_agents**
> SnapshotResult search_host_agents(query=query, to=to, window_size=window_size, size=size, offline=offline)

Query host agent snapshots

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
    api_instance = instana_client.HostAgentApi(api_client)
    query = 'query_example' # str |  (optional)
    to = 56 # int |  (optional)
    window_size = 56 # int |  (optional)
    size = 56 # int |  (optional)
    offline = True # bool |  (optional)

    try:
        # Query host agent snapshots
        api_response = api_instance.search_host_agents(query=query, to=to, window_size=window_size, size=size, offline=offline)
        print("The response of HostAgentApi->search_host_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAgentApi->search_host_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **to** | **int**|  | [optional] 
 **window_size** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **offline** | **bool**|  | [optional] 

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

# **update_agent**
> update_agent(host_id)

Agent update

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
    api_instance = instana_client.HostAgentApi(api_client)
    host_id = 'host_id_example' # str | 

    try:
        # Agent update
        api_instance.update_agent(host_id)
    except Exception as e:
        print("Exception when calling HostAgentApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 

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

# **update_configuration_by_host**
> update_configuration_by_host(host_id, agent_configuration_update=agent_configuration_update)

Update agent configuration by host

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.agent_configuration_update import AgentConfigurationUpdate
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
    api_instance = instana_client.HostAgentApi(api_client)
    host_id = 'host_id_example' # str | 
    agent_configuration_update = instana_client.AgentConfigurationUpdate() # AgentConfigurationUpdate |  (optional)

    try:
        # Update agent configuration by host
        api_instance.update_configuration_by_host(host_id, agent_configuration_update=agent_configuration_update)
    except Exception as e:
        print("Exception when calling HostAgentApi->update_configuration_by_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
 **agent_configuration_update** | [**AgentConfigurationUpdate**](AgentConfigurationUpdate.md)|  | [optional] 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_by_query**
> update_configuration_by_query(query=query, to=to, window_size=window_size, size=size, offline=offline, agent_configuration_update=agent_configuration_update)

Update agent configuration by query

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.agent_configuration_update import AgentConfigurationUpdate
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
    api_instance = instana_client.HostAgentApi(api_client)
    query = 'query_example' # str |  (optional)
    to = 56 # int |  (optional)
    window_size = 56 # int |  (optional)
    size = 56 # int |  (optional)
    offline = True # bool |  (optional)
    agent_configuration_update = instana_client.AgentConfigurationUpdate() # AgentConfigurationUpdate |  (optional)

    try:
        # Update agent configuration by query
        api_instance.update_configuration_by_query(query=query, to=to, window_size=window_size, size=size, offline=offline, agent_configuration_update=agent_configuration_update)
    except Exception as e:
        print("Exception when calling HostAgentApi->update_configuration_by_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **to** | **int**|  | [optional] 
 **window_size** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **offline** | **bool**|  | [optional] 
 **agent_configuration_update** | [**AgentConfigurationUpdate**](AgentConfigurationUpdate.md)|  | [optional] 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


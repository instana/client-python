# instana_client.ActionHistoryApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_action_instance**](ActionHistoryApi.md#add_action_instance) | **POST** /api/automation/actioninstances | Run an automation action.
[**delete_action_instance**](ActionHistoryApi.md#delete_action_instance) | **DELETE** /api/automation/actioninstances/{actionInstanceId} | Deletes an automation action run result from the action run history by ID.
[**delete_action_instances**](ActionHistoryApi.md#delete_action_instances) | **DELETE** /api/automation/actioninstances | Delete automation action run results.
[**get_action_instance**](ActionHistoryApi.md#get_action_instance) | **GET** /api/automation/actioninstances/{actionInstanceId} | Get the details of an automation action run result by ID from action run history.
[**get_action_instances**](ActionHistoryApi.md#get_action_instances) | **GET** /api/automation/actioninstances | Get the details of automation action run results from action run history.


# **add_action_instance**
> ActionInstance add_action_instance(action_instance_request)

Run an automation action.

Submits the automation action for execution on an agent. The automation action to execute and the agent on which to execute the action must be specified as actionId and hostId. For more details on the request payload see the request sample. This call requires `Execution of automation actions`  permission.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.action_instance import ActionInstance
from instana_client.models.action_instance_request import ActionInstanceRequest
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
    api_instance = instana_client.ActionHistoryApi(api_client)
    action_instance_request = {"hostId":"aHostId","actionId":"d473c1b0-0740-4d08-95fe-31e5d0a9faff","policyId":"2nIOVtEW-iPbsEIi89-yDqJabc","inputParameters":[{"name":"name","type":"type","value":"value"}],"eventId":"M3wuBxuaSDyecZJ7ICioiw","async":"true","timeout":"600"} # ActionInstanceRequest | 

    try:
        # Run an automation action.
        api_response = api_instance.add_action_instance(action_instance_request)
        print("The response of ActionHistoryApi->add_action_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionHistoryApi->add_action_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_instance_request** | [**ActionInstanceRequest**](ActionInstanceRequest.md)|  | 

### Return type

[**ActionInstance**](ActionInstance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation action submitted for execution on the agent. |  -  |
**400** | The payload in the request body is not valid or the action ID (actionId) in the payload is invalid or the agent host ID (hostId) in the payload is invalid. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_action_instance**
> delete_action_instance(action_instance_id, var_from, to)

Deletes an automation action run result from the action run history by ID.

Deletes the automation action run result specified in the request path from the action run history. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` and `/api/automation/actioninstances/<{actionInstanceId}>` REST calls. This call requires `Deletion of automation action history` permission.

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
    api_instance = instana_client.ActionHistoryApi(api_client)
    action_instance_id = 'nCtEoR6NSPqG61QkIkwwCw' # str | Automation action run result ID to delete.
    var_from = 1706713140000 # int | From date filter in milliseconds (13-digit) to look up the action run result ID.
    to = 1706713190000 # int | To date filter in milliseconds (13-digit) to look up the action run result ID.

    try:
        # Deletes an automation action run result from the action run history by ID.
        api_instance.delete_action_instance(action_instance_id, var_from, to)
    except Exception as e:
        print("Exception when calling ActionHistoryApi->delete_action_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_instance_id** | **str**| Automation action run result ID to delete. | 
 **var_from** | **int**| From date filter in milliseconds (13-digit) to look up the action run result ID. | 
 **to** | **int**| To date filter in milliseconds (13-digit) to look up the action run result ID. | 

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
**200** | Automation action run result is deleted. |  -  |
**400** | Automation action run result ID is missing in the request path, or &#x60;from&#x60; date or &#x60;to&#x60; date is missing in the query parameters. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |
**500** | The request do not contain a valid user or API Token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_action_instances**
> delete_action_instances(var_from, to, target_snapshot_id=target_snapshot_id, event_id=event_id, event_specification_id=event_specification_id, search=search, types=types, action_statuses=action_statuses, action_ids=action_ids)

Delete automation action run results.

Deletes the automation action run results from the action run history. The results to delete is filtered by the filter values given in the query parameters. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. This call requires `Deletion of automation action history` permission and, `from` and `to` query parameters.

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
    api_instance = instana_client.ActionHistoryApi(api_client)
    var_from = 1706713140000 # int | From date filter in milliseconds (13-digit) to look up the action run results to delete
    to = 1706713140000 # int | To date filter in milliseconds (13-digit) to look up the action run results to delete
    target_snapshot_id = 'aCtEoR6NSPqG61QkIkwwCw' # str | Target snapshot ID to look up the action run results to delete (optional)
    event_id = 'bCtEoR6NSPqG61QkIkwwCw' # str | Event ID filter to look up the action run results to delete (optional)
    event_specification_id = '1706713140000' # str | Event specification ID filter to look up the action run results to delete (optional)
    search = '1706713140000' # str | Text in action run result name, description and event name to filter the action run results to delete (optional)
    types = ['One or more of the following types HTTP, SCRIPT, ANSIBLE, GITHUB, GITLAB, JIRA'] # List[str] | Action type filter to look up the action run results to delete (optional)
    action_statuses = ['One or more of the following status SUBMITTED, IN_PROGRESS, SUCCESS, FAILED, TIMEOUT'] # List[str] | Action status filter to look up the action run results to delete (optional)
    action_ids = ['cCtEoR6NSPqG61QkIkwwCw'] # List[str] | List of action IDs  to filter the action run results to delete (optional)

    try:
        # Delete automation action run results.
        api_instance.delete_action_instances(var_from, to, target_snapshot_id=target_snapshot_id, event_id=event_id, event_specification_id=event_specification_id, search=search, types=types, action_statuses=action_statuses, action_ids=action_ids)
    except Exception as e:
        print("Exception when calling ActionHistoryApi->delete_action_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**| From date filter in milliseconds (13-digit) to look up the action run results to delete | 
 **to** | **int**| To date filter in milliseconds (13-digit) to look up the action run results to delete | 
 **target_snapshot_id** | **str**| Target snapshot ID to look up the action run results to delete | [optional] 
 **event_id** | **str**| Event ID filter to look up the action run results to delete | [optional] 
 **event_specification_id** | **str**| Event specification ID filter to look up the action run results to delete | [optional] 
 **search** | **str**| Text in action run result name, description and event name to filter the action run results to delete | [optional] 
 **types** | [**List[str]**](str.md)| Action type filter to look up the action run results to delete | [optional] 
 **action_statuses** | [**List[str]**](str.md)| Action status filter to look up the action run results to delete | [optional] 
 **action_ids** | [**List[str]**](str.md)| List of action IDs  to filter the action run results to delete | [optional] 

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
**200** | Automation action run results are deleted. |  -  |
**400** | &#x60;from&#x60; date or &#x60;to&#x60; date query parameter is missing. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |
**500** | The request do not contain a valid user or API Token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_instance**
> ActionInstance get_action_instance(action_instance_id, window_size=window_size, to=to)

Get the details of an automation action run result by ID from action run history.

Get the details of automation action run result specified in the request path from action run history. The automation action run result will be fetched only if the action run result was created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` REST calls. When using personal access tokens, the user must have at least `Viewer` access for Automation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.action_instance import ActionInstance
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
    api_instance = instana_client.ActionHistoryApi(api_client)
    action_instance_id = 'nCtEoR6NSPqG61QkIkwwCw' # str | action run result ID to get action run result details
    window_size = 10000 # int | Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided. (optional)
    to = 1706713140000 # int | To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided. (optional)

    try:
        # Get the details of an automation action run result by ID from action run history.
        api_response = api_instance.get_action_instance(action_instance_id, window_size=window_size, to=to)
        print("The response of ActionHistoryApi->get_action_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionHistoryApi->get_action_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_instance_id** | **str**| action run result ID to get action run result details | 
 **window_size** | **int**| Window size in milliseconds. This value is used compute the from date &#x60;(from &#x3D; to - windowSize)&#x60; to get the action run result details. The default &#x60;windowSize&#x60; is set to 10 minutes if this value is not provided. | [optional] 
 **to** | **int**| To date filter in milliseconds (13-digit) to get the action run result details. The default &#x60;to&#x60; date is set to &#x60;System.currentTimeMillis()&#x60; if this value is not provided. | [optional] 

### Return type

[**ActionInstance**](ActionInstance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The automation action run result detail is returned. |  -  |
**400** | Missing automation action run result ID. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_instances**
> PaginatedResult get_action_instances(window_size=window_size, to=to, page=page, page_size=page_size, target_snapshot_id=target_snapshot_id, event_id=event_id, event_specification_id=event_specification_id, search=search, types=types, action_statuses=action_statuses, order_by=order_by, order_direction=order_direction)

Get the details of automation action run results from action run history.

Get the details of automation action run results from action run history. The results are filtered by the filters in the query parameters. The automation action run result will be fetched only if the action run results were created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. When using personal access tokens, the user must have at least `Viewer` access for Automation and the automation action run results returned are also filtered based on the access set in `Limited access` permission settings. This API returns paginated result as specified in query parameters `page` and `pageSize`. The response contains list of automation action run results whose contents corresponds to the `page` query parameter and whose size corresponds to the `pageSize` query parameter.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.paginated_result import PaginatedResult
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
    api_instance = instana_client.ActionHistoryApi(api_client)
    window_size = 10000 # int | Window size filter in milliseconds (to compute the from date) to get the action run result details (optional)
    to = 1706713140000 # int | To date filter in milliseconds (13-digit) to get the action run result details (optional)
    page = 2 # int | Page to fetch -- used for paging the action run result records (optional)
    page_size = 50 # int | Number of records to return in each page -- used for paging the action run result records (optional)
    target_snapshot_id = 'nCtEoR6NSPqG61QkIkwwCw' # str | Target snapshot ID filter to get the action run result details (optional)
    event_id = 'nCtEoR6NSPqG61QkIkwwCw' # str | Event ID filter to get the action run result details (optional)
    event_specification_id = '1706713140000' # str | Event specification ID filter to get the action run result details (optional)
    search = '1706713140000' # str | Text in action run result name, description and event name filter to get the action run result details (optional)
    types = ['One or more of the following types HTTP, SCRIPT, ANSIBLE, GITHUB, GITLAB, JIRA'] # List[str] | Action type filter to get the action run result details (optional)
    action_statuses = ['One or more of the following status SUBMITTED, IN_PROGRESS, SUCCESS, FAILED, TIMEOUT'] # List[str] | Action status filter to get the action run result details (optional)
    order_by = 'Name of the action run result column. Default is action run result start date.' # str | Action run result column to order the result set. (optional)
    order_direction = 'asc or desc' # str | Sort order direction. (optional)

    try:
        # Get the details of automation action run results from action run history.
        api_response = api_instance.get_action_instances(window_size=window_size, to=to, page=page, page_size=page_size, target_snapshot_id=target_snapshot_id, event_id=event_id, event_specification_id=event_specification_id, search=search, types=types, action_statuses=action_statuses, order_by=order_by, order_direction=order_direction)
        print("The response of ActionHistoryApi->get_action_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionHistoryApi->get_action_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_size** | **int**| Window size filter in milliseconds (to compute the from date) to get the action run result details | [optional] 
 **to** | **int**| To date filter in milliseconds (13-digit) to get the action run result details | [optional] 
 **page** | **int**| Page to fetch -- used for paging the action run result records | [optional] 
 **page_size** | **int**| Number of records to return in each page -- used for paging the action run result records | [optional] 
 **target_snapshot_id** | **str**| Target snapshot ID filter to get the action run result details | [optional] 
 **event_id** | **str**| Event ID filter to get the action run result details | [optional] 
 **event_specification_id** | **str**| Event specification ID filter to get the action run result details | [optional] 
 **search** | **str**| Text in action run result name, description and event name filter to get the action run result details | [optional] 
 **types** | [**List[str]**](str.md)| Action type filter to get the action run result details | [optional] 
 **action_statuses** | [**List[str]**](str.md)| Action status filter to get the action run result details | [optional] 
 **order_by** | **str**| Action run result column to order the result set. | [optional] 
 **order_direction** | **str**| Sort order direction. | [optional] 

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation action run result details are returned. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


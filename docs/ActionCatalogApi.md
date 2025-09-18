# instana_client.ActionCatalogApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_by_id**](ActionCatalogApi.md#get_action_by_id) | **GET** /api/automation/actions/{id} | Get an automation action by ID.
[**get_action_matches**](ActionCatalogApi.md#get_action_matches) | **POST** /api/automation/ai/action/match | Get automation actions that match the incidents or issues.
[**get_action_matches_by_id_and_time_window**](ActionCatalogApi.md#get_action_matches_by_id_and_time_window) | **GET** /api/automation/ai/action/match | Get action matches by application ID or snapshot ID.
[**get_actions**](ActionCatalogApi.md#get_actions) | **GET** /api/automation/actions | Get all automation actions.
[**get_dynamic_parameters_tag_catalog**](ActionCatalogApi.md#get_dynamic_parameters_tag_catalog) | **GET** /api/automation/parameters/dynamic/catalog | Get tag catalog for dynamic parameters
[**resolve**](ActionCatalogApi.md#resolve) | **PUT** /api/automation/parameters/dynamic | Resolve dynamic parameter values


# **get_action_by_id**
> Action get_action_by_id(id)

Get an automation action by ID.

Get an automation action by ID specified in the request path. When using personal access tokens, the user must have at least `Viewer` access for Automation and the actions returned are also filtered based on the access set in `Limited access` permission settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.action import Action
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
    api_instance = instana_client.ActionCatalogApi(api_client)
    id = 'd473c1b0-0740-4d08-95fe-31e5d0a9faff' # str | Automation action ID

    try:
        # Get an automation action by ID.
        api_response = api_instance.get_action_by_id(id)
        print("The response of ActionCatalogApi->get_action_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionCatalogApi->get_action_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Automation action ID | 

### Return type

[**Action**](Action.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation action is returned. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |
**404** | Automation action not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_matches**
> List[ActionMatch] get_action_matches(action_search_space, target_snapshot_id=target_snapshot_id)

Get automation actions that match the incidents or issues.

Get automation actions that match the incident or issue data in the request body.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.action_match import ActionMatch
from instana_client.models.action_search_space import ActionSearchSpace
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
    api_instance = instana_client.ActionCatalogApi(api_client)
    action_search_space = {"name":"CPU spends significant time waiting for input/output","description":"Checks whether the system spends significant time waiting for input/output."} # ActionSearchSpace | 
    target_snapshot_id = 'target_snapshot_id_example' # str |  (optional)

    try:
        # Get automation actions that match the incidents or issues.
        api_response = api_instance.get_action_matches(action_search_space, target_snapshot_id=target_snapshot_id)
        print("The response of ActionCatalogApi->get_action_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionCatalogApi->get_action_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_search_space** | [**ActionSearchSpace**](ActionSearchSpace.md)|  | 
 **target_snapshot_id** | **str**|  | [optional] 

### Return type

[**List[ActionMatch]**](ActionMatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The automation actions that match the incident are returned. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |
**500** | Failed to retrieve the matching automation actions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_matches_by_id_and_time_window**
> List[ActionMatch] get_action_matches_by_id_and_time_window(application_id=application_id, snapshot_id=snapshot_id, to=to, window_size=window_size)

Get action matches by application ID or snapshot ID.

Get automation actions that match based on application ID or snapshot ID within a specified time window.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.action_match import ActionMatch
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
    api_instance = instana_client.ActionCatalogApi(api_client)
    application_id = 'application_id_example' # str |  (optional)
    snapshot_id = 'snapshot_id_example' # str |  (optional)
    to = 56 # int |  (optional)
    window_size = 56 # int |  (optional)

    try:
        # Get action matches by application ID or snapshot ID.
        api_response = api_instance.get_action_matches_by_id_and_time_window(application_id=application_id, snapshot_id=snapshot_id, to=to, window_size=window_size)
        print("The response of ActionCatalogApi->get_action_matches_by_id_and_time_window:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionCatalogApi->get_action_matches_by_id_and_time_window: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | [optional] 
 **snapshot_id** | **str**|  | [optional] 
 **to** | **int**|  | [optional] 
 **window_size** | **int**|  | [optional] 

### Return type

[**List[ActionMatch]**](ActionMatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The automation actions that match are returned. |  -  |
**400** | Either applicationId or snapshotId must be provided, but not both. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |
**500** | Failed to retrieve the matching automation actions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions**
> List[Action] get_actions()

Get all automation actions.

Get all automation actions. When using personal access tokens, the user must have at least `Viewer` access for Automation and the actions returned are also filtered based on the access set in `Limited access` permission settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.action import Action
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
    api_instance = instana_client.ActionCatalogApi(api_client)

    try:
        # Get all automation actions.
        api_response = api_instance.get_actions()
        print("The response of ActionCatalogApi->get_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionCatalogApi->get_actions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Action]**](Action.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation actions are returned. |  -  |
**403** | Automation feature is not enabled or Insufficient permissions. |  -  |
**500** | Failed to retrieve the automation actions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_parameters_tag_catalog**
> TagCatalog get_dynamic_parameters_tag_catalog()

Get tag catalog for dynamic parameters

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
    api_instance = instana_client.ActionCatalogApi(api_client)

    try:
        # Get tag catalog for dynamic parameters
        api_response = api_instance.get_dynamic_parameters_tag_catalog()
        print("The response of ActionCatalogApi->get_dynamic_parameters_tag_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionCatalogApi->get_dynamic_parameters_tag_catalog: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve**
> GetDynamicParameterValues resolve(get_dynamic_parameter_values)

Resolve dynamic parameter values

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_dynamic_parameter_values import GetDynamicParameterValues
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
    api_instance = instana_client.ActionCatalogApi(api_client)
    get_dynamic_parameter_values = {"eventId":"7UPTIakhR3uVaMnSQuG3TA","timestamp":1710168530000,"parameters":[{"name":"Application name","tagName":"application.name"}]} # GetDynamicParameterValues | 

    try:
        # Resolve dynamic parameter values
        api_response = api_instance.resolve(get_dynamic_parameter_values)
        print("The response of ActionCatalogApi->resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionCatalogApi->resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_dynamic_parameter_values** | [**GetDynamicParameterValues**](GetDynamicParameterValues.md)|  | 

### Return type

[**GetDynamicParameterValues**](GetDynamicParameterValues.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# instana_client.PoliciesApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policies**](PoliciesApi.md#add_policies) | **POST** /api/automation/policies/bulk | Create automation policies.
[**add_policy**](PoliciesApi.md#add_policy) | **POST** /api/automation/policies | Create an automation policy.
[**delete_policy**](PoliciesApi.md#delete_policy) | **DELETE** /api/automation/policies/{id} | Deletes an automation policy by identifier.
[**get_policies**](PoliciesApi.md#get_policies) | **GET** /api/automation/policies | Get all automation policies.
[**get_policy_by_id**](PoliciesApi.md#get_policy_by_id) | **GET** /api/automation/policies/{id} | Get an automation policy by ID.
[**update_policy**](PoliciesApi.md#update_policy) | **PUT** /api/automation/policies/{id} | Updates an automation policy by identifier.


# **add_policies**
> List[Policy] add_policies(policy)

Create automation policies.

Creates a list of automation policies. Policy creation requires `Configuration of automation policies` permission.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.policy import Policy
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
    api_instance = instana_client.PoliciesApi(api_client)
    policy = [instana_client.Policy()] # List[Policy] | 

    try:
        # Create automation policies.
        api_response = api_instance.add_policies(policy)
        print("The response of PoliciesApi->add_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->add_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**List[Policy]**](Policy.md)|  | 

### Return type

[**List[Policy]**](Policy.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions. |  -  |
**412** | Invalid input value. |  -  |
**500** | Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_policy**
> Policy add_policy(policy)

Create an automation policy.

Creates a new automation policy. Policy creation requires `Configuration of automation policies` permission.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.policy import Policy
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
    api_instance = instana_client.PoliciesApi(api_client)
    policy = {"name":"builtin-action-custom-event","trigger":{"name":"test event","type":"customEvent","id":"2X5r-Un18MIE59rE"},"typeConfigurations":[{"name":"manual","runnable":{"type":"action","id":"c5ba4453-0bc2-3c3e-bdbe-b3ce68239145","runConfiguration":{"actions":[{"action":{"id":"c5ba4453-0bc2-3c3e-bdbe-b3ce68239145"}}]}}}]} # Policy | 

    try:
        # Create an automation policy.
        api_response = api_instance.add_policy(policy)
        print("The response of PoliciesApi->add_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->add_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policy**](Policy.md)|  | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New policy created. |  -  |
**403** | Insufficient permissions. |  -  |
**412** | Invalid input value. |  -  |
**500** | Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id)

Deletes an automation policy by identifier.

Deletes an automation policy by identifier. Policy deletion requires `Configuration of automation policies` permission. When using personal tokens the automation policies deleted are based on the access set in `Limited access` permission settings.

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
    api_instance = instana_client.PoliciesApi(api_client)
    id = 'a14700b0-401b-47eb-a751-deda0035fde3' # str | Automation policy ID to delete

    try:
        # Deletes an automation policy by identifier.
        api_instance.delete_policy(id)
    except Exception as e:
        print("Exception when calling PoliciesApi->delete_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Automation policy ID to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Automation policy successfully deleted |  -  |
**403** | Insufficient permissions. |  -  |
**412** | Automation policy does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> List[Policy] get_policies(trigger_type=trigger_type, trigger_id=trigger_id, execution_type=execution_type, action_id=action_id)

Get all automation policies.

Returns all the automation policies filtered by the values in optional query parameters. When using personal access tokens, the user must have at least `Viewer` access for Automation and the automation policies returned are also filtered based on the access set in `Limited access` permission settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.policy import Policy
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
    api_instance = instana_client.PoliciesApi(api_client)
    trigger_type = 'trigger_type_example' # str | Filter policies by the event or alert type that can trigger a policy. This is an optional parameter. Valid values are customEvent, builtinEvent, applicationSmartAlert, globalApplicationSmartAlert, websiteSmartAlert, infraSmartAlert, mobileAppSmartAlert, syntheticsSmartAlert, logSmartAlert, sloSmartAlert (optional)
    trigger_id = 'trigger_id_example' # str | Trigger identifier. This is an optional parameter. (optional)
    execution_type = 'execution_type_example' # str | Filter policies by policy execution type. This is an optional parameter.  Valid values are automatic or manual (optional)
    action_id = 'action_id_example' # str | Filter policies by action ID. This is an optional parameter. (optional)

    try:
        # Get all automation policies.
        api_response = api_instance.get_policies(trigger_type=trigger_type, trigger_id=trigger_id, execution_type=execution_type, action_id=action_id)
        print("The response of PoliciesApi->get_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->get_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_type** | **str**| Filter policies by the event or alert type that can trigger a policy. This is an optional parameter. Valid values are customEvent, builtinEvent, applicationSmartAlert, globalApplicationSmartAlert, websiteSmartAlert, infraSmartAlert, mobileAppSmartAlert, syntheticsSmartAlert, logSmartAlert, sloSmartAlert | [optional] 
 **trigger_id** | **str**| Trigger identifier. This is an optional parameter. | [optional] 
 **execution_type** | **str**| Filter policies by policy execution type. This is an optional parameter.  Valid values are automatic or manual | [optional] 
 **action_id** | **str**| Filter policies by action ID. This is an optional parameter. | [optional] 

### Return type

[**List[Policy]**](Policy.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation policies list filtered by the values in query parameters. |  -  |
**403** | Insufficient permissions. |  -  |
**412** | Invalid input value. |  -  |
**500** | Failed to retrieve the automation policies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_by_id**
> Policy get_policy_by_id(id)

Get an automation policy by ID.

Returns the automation policy filtered by the ID in request parameter. When using personal access tokens, the user must have at least `Viewer` access for Automation and the automation policies returned are also filtered based on the access set in `Limited access` permission settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.policy import Policy
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
    api_instance = instana_client.PoliciesApi(api_client)
    id = 'a14700b0-401b-47eb-a751-deda0035fde3' # str | Automation policy ID

    try:
        # Get an automation policy by ID.
        api_response = api_instance.get_policy_by_id(id)
        print("The response of PoliciesApi->get_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->get_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Automation policy ID | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation policy filtered by the ID in request parameter. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Automation policy not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(id, policy)

Updates an automation policy by identifier.

Updates an automation policy by identifier. Policy updates requires `Configuration of automation policies` permission. When using personal tokens the automation policies updated are based on the access set in `Limited access` permission settings.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.policy import Policy
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
    api_instance = instana_client.PoliciesApi(api_client)
    id = 'id_example' # str | 
    policy = {"name":"builtin-action-custom-event","trigger":{"name":"test event","type":"customEvent","id":"2X5r-Un18MIE59rE"},"typeConfigurations":[{"name":"manual","runnable":{"type":"action","id":"c5ba4453-0bc2-3c3e-bdbe-b3ce68239145","runConfiguration":{"actions":[{"action":{"id":"c5ba4453-0bc2-3c3e-bdbe-b3ce68239145"}}]}}}]} # Policy | 

    try:
        # Updates an automation policy by identifier.
        api_response = api_instance.update_policy(id, policy)
        print("The response of PoliciesApi->update_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->update_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **policy** | [**Policy**](Policy.md)|  | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation policy successfully updated. |  -  |
**403** | Insufficient permissions. |  -  |
**412** | Invalid input value. |  -  |
**500** | Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


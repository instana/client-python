# instana_client.GroupsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permissions_on_group**](GroupsApi.md#add_permissions_on_group) | **PUT** /api/settings/rbac/groups/{groupId}/permissions | Add permissions to group
[**add_users_to_group**](GroupsApi.md#add_users_to_group) | **PUT** /api/settings/rbac/groups/{groupId}/users | Add users to group
[**create_group**](GroupsApi.md#create_group) | **POST** /api/settings/rbac/groups | Create group
[**create_group_mapping**](GroupsApi.md#create_group_mapping) | **POST** /api/settings/rbac/mappings | Create group mapping
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /api/settings/rbac/groups/{id} | Delete group
[**delete_group_mapping**](GroupsApi.md#delete_group_mapping) | **DELETE** /api/settings/rbac/mappings/{id} | Delete group mapping
[**delete_group_mappings**](GroupsApi.md#delete_group_mappings) | **PUT** /api/settings/rbac/mappings/delete | Delete multiple group mappings
[**delete_groups**](GroupsApi.md#delete_groups) | **PUT** /api/settings/rbac/groups/delete | Delete groups
[**get_group**](GroupsApi.md#get_group) | **GET** /api/settings/rbac/groups/{id} | Get group
[**get_group_mapping**](GroupsApi.md#get_group_mapping) | **GET** /api/settings/rbac/mappings/{id} | Get group mapping
[**get_group_mappings**](GroupsApi.md#get_group_mappings) | **GET** /api/settings/rbac/mappings | Get all group mappings
[**get_group_mappings_overview**](GroupsApi.md#get_group_mappings_overview) | **GET** /api/settings/rbac/mappings/overview | Get all group mappings overview
[**get_groups**](GroupsApi.md#get_groups) | **GET** /api/settings/rbac/groups | Get groups
[**get_groups_by_user**](GroupsApi.md#get_groups_by_user) | **GET** /api/settings/rbac/groups/user/{email} | Get groups of a single user
[**get_identity_provider_patch**](GroupsApi.md#get_identity_provider_patch) | **GET** /api/settings/rbac/mappings/identityProvider/restrictEmptyIdpGroups | Check user restrictions for empty Idp group mapping
[**remove_user_from_group**](GroupsApi.md#remove_user_from_group) | **DELETE** /api/settings/rbac/groups/{id}/user/{userId} | Remove user from group
[**update_group**](GroupsApi.md#update_group) | **PUT** /api/settings/rbac/groups/{id} | Update group
[**update_group_mapping**](GroupsApi.md#update_group_mapping) | **PUT** /api/settings/rbac/mappings/{id} | Update group mapping
[**update_identity_provider**](GroupsApi.md#update_identity_provider) | **PUT** /api/settings/rbac/mappings/identityProvider/restrictEmptyIdpGroups | Allow/Restrict users with empty Idp group mapping


# **add_permissions_on_group**
> ApiGroup add_permissions_on_group(group_id, request_body)

Add permissions to group


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)
    group_id = 'groupId' # str | Id of the group to add permissions
    request_body = ["CAN_VIEW_SYNTHETIC_TESTS","CAN_VIEW_SYNTHETIC_LOCATIONS","CAN_CONFIGURE_AUTOMATION_ACTIONS"] # List[str] | 

    try:
        # Add permissions to group
        api_response = api_instance.add_permissions_on_group(group_id, request_body)
        print("The response of GroupsApi->add_permissions_on_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_permissions_on_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Id of the group to add permissions | 
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**ApiGroup**](ApiGroup.md)

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

# **add_users_to_group**
> ApiGroup add_users_to_group(group_id, request_body)

Add users to group


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)
    group_id = 'groupId' # str | Id of the group to add users
    request_body = ["userId1","userId3"] # List[str] | 

    try:
        # Add users to group
        api_response = api_instance.add_users_to_group(group_id, request_body)
        print("The response of GroupsApi->add_users_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_users_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Id of the group to add users | 
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**ApiGroup**](ApiGroup.md)

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

# **create_group**
> ApiGroup create_group(api_create_group)

Create group


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_create_group import ApiCreateGroup
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)
    api_create_group = {"name":"group name","members":[{"userId":"userId","email":"username@example.com"}],"permissionSet":{"permissions":["CAN_VIEW_LOGS"],"applicationIds":[{"scopeId":"scopeId1","scopeRoleId":"-102"}],"kubernetesClusterUUIDs":[],"kubernetesNamespaceUIDs":[],"websiteIds":[],"mobileAppIds":[],"syntheticTestIds":[{"scopeId":"scopeId10","scopeRoleId":"-1"}],"restrictedApplicationFilter":{"label":"group name","tagFilterExpression":{"type":"TAG_FILTER","name":"service.name","stringValue":"acceptor","numberValue":null,"booleanValue":null,"key":null,"value":"acceptor","operator":"EQUALS","entity":"DESTINATION"},"scope":"INCLUDE_NO_DOWNSTREAM"},"infraDfqFilter":{"scopeId":"","scopeRoleId":"-1"},"actionFilter":{"scopeId":"","scopeRoleId":"-1"}}} # ApiCreateGroup | 

    try:
        # Create group
        api_response = api_instance.create_group(api_create_group)
        print("The response of GroupsApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_create_group** | [**ApiCreateGroup**](ApiCreateGroup.md)|  | 

### Return type

[**ApiGroup**](ApiGroup.md)

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

# **create_group_mapping**
> GroupMapping create_group_mapping(group_mapping)

Create group mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.group_mapping import GroupMapping
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
    api_instance = instana_client.GroupsApi(api_client)
    group_mapping = {"key":"roles","value":"analyst","groupId":"-3"} # GroupMapping | 

    try:
        # Create group mapping
        api_response = api_instance.create_group_mapping(group_mapping)
        print("The response of GroupsApi->create_group_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_mapping** | [**GroupMapping**](GroupMapping.md)|  | 

### Return type

[**GroupMapping**](GroupMapping.md)

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

# **delete_group**
> delete_group(id)

Delete group

Delete the group data.
For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'groupId' # str | Id of the group to delete

    try:
        # Delete group
        api_instance.delete_group(id)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group to delete | 

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

# **delete_group_mapping**
> delete_group_mapping(id)

Delete group mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'mappingId' # str | Id of the group mapping to delete

    try:
        # Delete group mapping
        api_instance.delete_group_mapping(id)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group mapping to delete | 

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

# **delete_group_mappings**
> delete_group_mappings(body)

Delete multiple group mappings


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

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
    api_instance = instana_client.GroupsApi(api_client)
    body = ["firstid","secondid"] # str | 

    try:
        # Delete multiple group mappings
        api_instance.delete_group_mappings(body)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

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
**204** | OK |  -  |
**422** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groups**
> delete_groups(request_body)

Delete groups

Delete multiple groups
For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

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
    api_instance = instana_client.GroupsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete groups
        api_instance.delete_groups(request_body)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

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

# **get_group**
> ApiGroup get_group(id)

Get group


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'groupId' # str | Id of the group for retrieval

    try:
        # Get group
        api_response = api_instance.get_group(id)
        print("The response of GroupsApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group for retrieval | 

### Return type

[**ApiGroup**](ApiGroup.md)

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

# **get_group_mapping**
> GroupMapping get_group_mapping(id)

Get group mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.group_mapping import GroupMapping
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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get group mapping
        api_response = api_instance.get_group_mapping(id)
        print("The response of GroupsApi->get_group_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupMapping**](GroupMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No group mapping found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_mappings**
> List[GroupMapping] get_group_mappings()

Get all group mappings


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.group_mapping import GroupMapping
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
    api_instance = instana_client.GroupsApi(api_client)

    try:
        # Get all group mappings
        api_response = api_instance.get_group_mappings()
        print("The response of GroupsApi->get_group_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_mappings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GroupMapping]**](GroupMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No group mapping found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_mappings_overview**
> List[GroupMappingOverview] get_group_mappings_overview()

Get all group mappings overview


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.group_mapping_overview import GroupMappingOverview
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
    api_instance = instana_client.GroupsApi(api_client)

    try:
        # Get all group mappings overview
        api_response = api_instance.get_group_mappings_overview()
        print("The response of GroupsApi->get_group_mappings_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_mappings_overview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GroupMappingOverview]**](GroupMappingOverview.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No group mapping overviews found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> List[ApiGroup] get_groups()

Get groups


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)

    try:
        # Get groups
        api_response = api_instance.get_groups()
        print("The response of GroupsApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiGroup]**](ApiGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No groups found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_by_user**
> List[ApiGroup] get_groups_by_user(email)

Get groups of a single user


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)
    email = 'username@example.com' # str | Email of the user for retrieval

    try:
        # Get groups of a single user
        api_response = api_instance.get_groups_by_user(email)
        print("The response of GroupsApi->get_groups_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groups_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the user for retrieval | 

### Return type

[**List[ApiGroup]**](ApiGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No groups found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider_patch**
> IdentityProviderPatch get_identity_provider_patch()

Check user restrictions for empty Idp group mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.identity_provider_patch import IdentityProviderPatch
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
    api_instance = instana_client.GroupsApi(api_client)

    try:
        # Check user restrictions for empty Idp group mapping
        api_response = api_instance.get_identity_provider_patch()
        print("The response of GroupsApi->get_identity_provider_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_identity_provider_patch: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IdentityProviderPatch**](IdentityProviderPatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No group mapping restriction found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_group**
> remove_user_from_group(id, user_id)

Remove user from group

Remove the user from a group.
For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'groupId' # str | Id of the group to remove user from
    user_id = 'userId' # str | Id of the user to remove

    try:
        # Remove user from group
        api_instance.remove_user_from_group(id, user_id)
    except Exception as e:
        print("Exception when calling GroupsApi->remove_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group to remove user from | 
 **user_id** | **str**| Id of the user to remove | 

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

# **update_group**
> ApiGroup update_group(id, api_group)

Update group


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_group import ApiGroup
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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'groupId' # str | Id of the group to update
    api_group = {"name":"group name","members":[{"userId":"userId","email":"username@example.com"}],"permissionSet":{"permissions":["CAN_VIEW_LOGS"],"applicationIds":[{"scopeId":"scopeId1","scopeRoleId":"-102"}],"kubernetesClusterUUIDs":[],"kubernetesNamespaceUIDs":[],"websiteIds":[],"mobileAppIds":[],"syntheticTestIds":[{"scopeId":"scopeId10","scopeRoleId":"-1"}],"restrictedApplicationFilter":{"label":"group name","tagFilterExpression":{"type":"TAG_FILTER","name":"service.name","stringValue":"acceptor","numberValue":null,"booleanValue":null,"key":null,"value":"acceptor","operator":"EQUALS","entity":"DESTINATION"},"scope":"INCLUDE_NO_DOWNSTREAM"},"infraDfqFilter":{"scopeId":"","scopeRoleId":"-1"},"actionFilter":{"scopeId":"","scopeRoleId":"-1"}}} # ApiGroup | 

    try:
        # Update group
        api_response = api_instance.update_group(id, api_group)
        print("The response of GroupsApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group to update | 
 **api_group** | [**ApiGroup**](ApiGroup.md)|  | 

### Return type

[**ApiGroup**](ApiGroup.md)

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

# **update_group_mapping**
> GroupMapping update_group_mapping(id, group_mapping)

Update group mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.group_mapping import GroupMapping
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
    api_instance = instana_client.GroupsApi(api_client)
    id = 'mappingId' # str | Id of the group mapping to update
    group_mapping = {"id":"mappingId","key":"roles","value":"analyst","groupId":"-3"} # GroupMapping | 

    try:
        # Update group mapping
        api_response = api_instance.update_group_mapping(id, group_mapping)
        print("The response of GroupsApi->update_group_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_group_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group mapping to update | 
 **group_mapping** | [**GroupMapping**](GroupMapping.md)|  | 

### Return type

[**GroupMapping**](GroupMapping.md)

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

# **update_identity_provider**
> update_identity_provider(identity_provider_patch)

Allow/Restrict users with empty Idp group mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.identity_provider_patch import IdentityProviderPatch
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
    api_instance = instana_client.GroupsApi(api_client)
    identity_provider_patch = {"restrictEmptyIdpGroups":true} # IdentityProviderPatch | 

    try:
        # Allow/Restrict users with empty Idp group mapping
        api_instance.update_identity_provider(identity_provider_patch)
    except Exception as e:
        print("Exception when calling GroupsApi->update_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_patch** | [**IdentityProviderPatch**](IdentityProviderPatch.md)|  | 

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


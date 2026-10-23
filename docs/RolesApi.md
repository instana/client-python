# instana_client.RolesApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mapping**](RolesApi.md#create_mapping) | **POST** /api/settings/rbac/mappings | Create mapping
[**create_role**](RolesApi.md#create_role) | **POST** /api/settings/rbac/roles | Create role
[**delete_mapping**](RolesApi.md#delete_mapping) | **DELETE** /api/settings/rbac/mappings/{id} | Delete mapping
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/settings/rbac/roles/{id} | Delete role
[**get_identity_provider_patch**](RolesApi.md#get_identity_provider_patch) | **GET** /api/settings/rbac/mappings/identityProvider/restrictEmptyIdpGroups | Check user restrictions for empty Idp mapping
[**get_mapping**](RolesApi.md#get_mapping) | **GET** /api/settings/rbac/mappings/{id} | Get mapping
[**get_mappings**](RolesApi.md#get_mappings) | **GET** /api/settings/rbac/mappings | Get all mappings
[**get_mappings_overview**](RolesApi.md#get_mappings_overview) | **GET** /api/settings/rbac/mappings/overview | Get all mappings overview
[**get_role**](RolesApi.md#get_role) | **GET** /api/settings/rbac/roles/{id} | Get role by ID
[**get_role_mappings**](RolesApi.md#get_role_mappings) | **GET** /api/settings/rbac/roles/{roleId}/mappings | Get role mappings
[**get_roles**](RolesApi.md#get_roles) | **GET** /api/settings/rbac/roles | Get all roles
[**update_mapping**](RolesApi.md#update_mapping) | **PUT** /api/settings/rbac/mappings/{id} | Update mapping
[**update_role**](RolesApi.md#update_role) | **PUT** /api/settings/rbac/roles/{id} | Update role


# **create_mapping**
> Mapping create_mapping(mapping)

Create mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mapping import Mapping
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
    api_instance = instana_client.RolesApi(api_client)
    mapping = {"id":"mappingId","key":"roles","value":"analyst","groupId":"-3","teamId":null} # Mapping | 

    try:
        # Create mapping
        api_response = api_instance.create_mapping(mapping)
        print("The response of RolesApi->create_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping** | [**Mapping**](Mapping.md)|  | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**412** | Attempting to upsert a mapping containing a teamId - without teams being available |  -  |
**422** | invalid request body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> ApiRole create_role(api_create_role)

Create role

Create a new role.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_create_role import ApiCreateRole
from instana_client.models.api_role import ApiRole
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
    api_instance = instana_client.RolesApi(api_client)
    api_create_role = {"name":"New Role","description":"optional attribute","members":[{"userId":"user-5","email":"newuser@example.com","name":"New User"}],"permissions":["CAN_VIEW_APPLICATIONS","CAN_VIEW_EVENTS"]} # ApiCreateRole | Role to create

    try:
        # Create role
        api_response = api_instance.create_role(api_create_role)
        print("The response of RolesApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_create_role** | [**ApiCreateRole**](ApiCreateRole.md)| Role to create | 

### Return type

[**ApiRole**](ApiRole.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping**
> delete_mapping(id)

Delete mapping


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
    api_instance = instana_client.RolesApi(api_client)
    id = 'mappingId' # str | Id of the mapping to delete

    try:
        # Delete mapping
        api_instance.delete_mapping(id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the mapping to delete | 

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

# **delete_role**
> delete_role(id)

Delete role

Delete a role by ID.

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
    api_instance = instana_client.RolesApi(api_client)
    id = 'roleId' # str | Id of the role to delete

    try:
        # Delete role
        api_instance.delete_role(id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the role to delete | 

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
**204** | Role successfully deleted |  -  |
**404** | Role not found |  -  |
**412** | Pre-Condition Failed - Returned when attempting to delete protected system roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider_patch**
> IdentityProviderPatch get_identity_provider_patch()

Check user restrictions for empty Idp mapping


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
    api_instance = instana_client.RolesApi(api_client)

    try:
        # Check user restrictions for empty Idp mapping
        api_response = api_instance.get_identity_provider_patch()
        print("The response of RolesApi->get_identity_provider_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_identity_provider_patch: %s\n" % e)
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
**404** | No  mapping restriction found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping**
> Mapping get_mapping(id)

Get mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mapping import Mapping
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
    api_instance = instana_client.RolesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get mapping
        api_response = api_instance.get_mapping(id)
        print("The response of RolesApi->get_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No mapping found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappings**
> List[Mapping] get_mappings()

Get all mappings


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mapping import Mapping
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
    api_instance = instana_client.RolesApi(api_client)

    try:
        # Get all mappings
        api_response = api_instance.get_mappings()
        print("The response of RolesApi->get_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_mappings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Mapping]**](Mapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No mapping found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappings_overview**
> List[MappingOverview] get_mappings_overview()

Get all mappings overview


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mapping_overview import MappingOverview
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
    api_instance = instana_client.RolesApi(api_client)

    try:
        # Get all mappings overview
        api_response = api_instance.get_mappings_overview()
        print("The response of RolesApi->get_mappings_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_mappings_overview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MappingOverview]**](MappingOverview.md)

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

# **get_role**
> ApiRole get_role(id, include_team_usage=include_team_usage)

Get role by ID

Retrieve a specific role by its ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_role import ApiRole
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
    api_instance = instana_client.RolesApi(api_client)
    id = 'roleId' # str | Id of the role for retrieval
    include_team_usage = True # bool |  (optional)

    try:
        # Get role by ID
        api_response = api_instance.get_role(id, include_team_usage=include_team_usage)
        print("The response of RolesApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the role for retrieval | 
 **include_team_usage** | **bool**|  | [optional] 

### Return type

[**ApiRole**](ApiRole.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mappings**
> List[RoleMappingOverview] get_role_mappings(role_id)

Get role mappings

Retrieve IdP role mappings applicable to a specific role

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.role_mapping_overview import RoleMappingOverview
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
    api_instance = instana_client.RolesApi(api_client)
    role_id = 'role_id_example' # str | 

    try:
        # Get role mappings
        api_response = api_instance.get_role_mappings(role_id)
        print("The response of RolesApi->get_role_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  | 

### Return type

[**List[RoleMappingOverview]**](RoleMappingOverview.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | role mapping not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> List[ApiRole] get_roles()

Get all roles

Retrieve all roles for the current tenant unit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_role import ApiRole
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
    api_instance = instana_client.RolesApi(api_client)

    try:
        # Get all roles
        api_response = api_instance.get_roles()
        print("The response of RolesApi->get_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiRole]**](ApiRole.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No roles found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping**
> Mapping update_mapping(id, mapping)

Update mapping


For more information on groups please access the https://developer.ibm.com/apis/catalog/instana--instana-rest-api/Settings#groups.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mapping import Mapping
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
    api_instance = instana_client.RolesApi(api_client)
    id = 'mappingId' # str | Id of the mapping to update
    mapping = {"id":"mappingId","key":"roles","value":"analyst","groupId":"-3","teamId":null} # Mapping | 

    try:
        # Update mapping
        api_response = api_instance.update_mapping(id, mapping)
        print("The response of RolesApi->update_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the mapping to update | 
 **mapping** | [**Mapping**](Mapping.md)|  | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**412** | Attempting to upsert a mapping containing a teamId - without teams being available |  -  |
**422** | invalid request body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> ApiRole update_role(id, api_role)

Update role

Update an existing role by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_role import ApiRole
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
    api_instance = instana_client.RolesApi(api_client)
    id = 'roleId' # str | Id of the role to update
    api_role = {"id":"role-2","name":"Updated Developer Role","description":"optional attribute","members":[{"userId":"user-3","email":"dev1@example.com","name":"Developer One"},{"userId":"user-4","email":"dev2@example.com","name":"Developer Two"},{"userId":"user-6","email":"dev3@example.com","name":"Developer Three"}],"permissions":["CAN_VIEW_APPLICATIONS","CAN_VIEW_EVENTS","CAN_VIEW_INFRASTRUCTURE","CAN_CONFIGURE_APPLICATIONS"]} # ApiRole | Updated role data

    try:
        # Update role
        api_response = api_instance.update_role(id, api_role)
        print("The response of RolesApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the role to update | 
 **api_role** | [**ApiRole**](ApiRole.md)| Updated role data | 

### Return type

[**ApiRole**](ApiRole.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Role not found |  -  |
**412** | Pre-Condition Failed - Returned when attempting to modify protected roles in a forbidden way. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


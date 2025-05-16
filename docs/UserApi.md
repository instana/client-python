# instana_client.UserApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invitations**](UserApi.md#get_invitations) | **GET** /api/settings/invitations | All pending invitations
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /api/settings/users/{userId} | Get single user
[**get_users**](UserApi.md#get_users) | **GET** /api/settings/users | All users (without invitations)
[**get_users_including_invitations**](UserApi.md#get_users_including_invitations) | **GET** /api/settings/users/overview | All users (incl. invitations)
[**invite_users**](UserApi.md#invite_users) | **POST** /api/settings/invitations | Send user invitations
[**remove_user_from_tenant**](UserApi.md#remove_user_from_tenant) | **DELETE** /api/settings/users/{userId} | Remove user from tenant
[**revoke_pending_invitation**](UserApi.md#revoke_pending_invitation) | **DELETE** /api/settings/invitations | Revoke pending invitation
[**share_and_invite_users**](UserApi.md#share_and_invite_users) | **POST** /api/settings/invitation/share | Send user invitations
[**update_user**](UserApi.md#update_user) | **PUT** /api/settings/users/{email} | Change user name of single user


# **get_invitations**
> List[InvitationResult] get_invitations()

All pending invitations

This API endpoint retrieves the list of all pending invitations.   During the IdP configuration all pending invitations will be dismissed and whilst an IdP is configured invitations are prevented.  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.invitation_result import InvitationResult
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
    api_instance = instana_client.UserApi(api_client)

    try:
        # All pending invitations
        api_response = api_instance.get_invitations()
        print("The response of UserApi->get_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_invitations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[InvitationResult]**](InvitationResult.md)

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

# **get_user_by_id**
> List[UserResult] get_user_by_id(user_id)

Get single user

Retrieves the user with access to the tenant.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.user_result import UserResult
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
    api_instance = instana_client.UserApi(api_client)
    user_id = 'userId' # str | Id of the user for retrieval

    try:
        # Get single user
        api_response = api_instance.get_user_by_id(user_id)
        print("The response of UserApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user for retrieval | 

### Return type

[**List[UserResult]**](UserResult.md)

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

# **get_users**
> List[UserResult] get_users()

All users (without invitations)

Retrieves all users with access to the tenant. The result will not contain pending invitations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.user_result import UserResult
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
    api_instance = instana_client.UserApi(api_client)

    try:
        # All users (without invitations)
        api_response = api_instance.get_users()
        print("The response of UserApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserResult]**](UserResult.md)

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

# **get_users_including_invitations**
> UsersResult get_users_including_invitations()

All users (incl. invitations)

Retrieves all users with access to the tenant. The result will also contain pending invitations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.users_result import UsersResult
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
    api_instance = instana_client.UserApi(api_client)

    try:
        # All users (incl. invitations)
        api_response = api_instance.get_users_including_invitations()
        print("The response of UserApi->get_users_including_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users_including_invitations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersResult**](UsersResult.md)

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

# **invite_users**
> List[InvitationResponse] invite_users(invitation)

Send user invitations

This API endpoint allows to invite users to this tenant.   Each user requires the email address and the group to which the user will be added initially.    Inviting users whilst an IdP is configured will always result in failures, as in this case users will be provisioned during the login based on the IdP configuration.   During the IdP configurations all pending invitations are automatically revoked.  Inviting users who are already members of the tenant will also provide an error result.  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.invitation import Invitation
from instana_client.models.invitation_response import InvitationResponse
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
    api_instance = instana_client.UserApi(api_client)
    invitation = [{"email":"username@example.com","groupId":"-1"}] # List[Invitation] | 

    try:
        # Send user invitations
        api_response = api_instance.invite_users(invitation)
        print("The response of UserApi->invite_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->invite_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**List[Invitation]**](Invitation.md)|  | 

### Return type

[**List[InvitationResponse]**](InvitationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_tenant**
> remove_user_from_tenant(user_id)

Remove user from tenant

Remove the users access to the tenant. Removing a user from a tenant does not delete their user account.

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
    api_instance = instana_client.UserApi(api_client)
    user_id = 'userId' # str | Id of the user for removal

    try:
        # Remove user from tenant
        api_instance.remove_user_from_tenant(user_id)
    except Exception as e:
        print("Exception when calling UserApi->remove_user_from_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user for removal | 

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

# **revoke_pending_invitation**
> revoke_pending_invitation(email)

Revoke pending invitation

This API endpoint allows to delete an invitation, requires the users’ email as a Query parameter. 

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
    api_instance = instana_client.UserApi(api_client)
    email = 'username@example.com' # str | Email of the invite for removal

    try:
        # Revoke pending invitation
        api_instance.revoke_pending_invitation(email)
    except Exception as e:
        print("Exception when calling UserApi->revoke_pending_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the invite for removal | 

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

# **share_and_invite_users**
> List[InvitationResponse] share_and_invite_users(invitation)

Send user invitations

This API endpoint allows to invite users to this tenant.   Each user requires the email address and the group to which the user will be added initially.    Inviting users whilst an IdP is configured will always result in failures, as in this case users will be provisioned during the login based on the IdP configuration.   During the IdP configurations all pending invitations are automatically revoked.  Inviting users who are already members of the tenant will also provide an error result.  

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.invitation import Invitation
from instana_client.models.invitation_response import InvitationResponse
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
    api_instance = instana_client.UserApi(api_client)
    invitation = [{"email":"username@example.com","groupId":"-1","message":"hello message","path":"/testpath"}] # List[Invitation] | 

    try:
        # Send user invitations
        api_response = api_instance.share_and_invite_users(invitation)
        print("The response of UserApi->share_and_invite_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->share_and_invite_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**List[Invitation]**](Invitation.md)|  | 

### Return type

[**List[InvitationResponse]**](InvitationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(email, edit_user=edit_user)

Change user name of single user

Updates the full name of the user.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.edit_user import EditUser
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
    api_instance = instana_client.UserApi(api_client)
    email = 'email_example' # str | 
    edit_user = {"fullName":"Updated Name"} # EditUser |  (optional)

    try:
        # Change user name of single user
        api_instance.update_user(email, edit_user=edit_user)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **edit_user** | [**EditUser**](EditUser.md)|  | [optional] 

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


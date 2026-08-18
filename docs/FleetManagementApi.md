# instana_client.FleetManagementApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fleet_config_assignment**](FleetManagementApi.md#create_fleet_config_assignment) | **POST** /api/fleet/configuration-assignments | Create a configuration assignment
[**create_fleet_configuration**](FleetManagementApi.md#create_fleet_configuration) | **POST** /api/fleet/configurations | Creates a fleet configuration
[**delete_custom_collector_base**](FleetManagementApi.md#delete_custom_collector_base) | **DELETE** /api/fleet/configurations/{id} | Delete a custom collector base configuration
[**delete_fleet_config_assignment**](FleetManagementApi.md#delete_fleet_config_assignment) | **DELETE** /api/fleet/configuration-assignments/{id} | Delete a fleet configuration assignment
[**get_custom_collector_base**](FleetManagementApi.md#get_custom_collector_base) | **GET** /api/fleet/configurations/{id} | Get fleet configuration details
[**get_fleet_config_assignment**](FleetManagementApi.md#get_fleet_config_assignment) | **GET** /api/fleet/configuration-assignments/{id} | Get a fleet configuration assignment
[**list_custom_collector_base**](FleetManagementApi.md#list_custom_collector_base) | **GET** /api/fleet/configurations | List fleet configurations
[**list_fleet_config_assignments**](FleetManagementApi.md#list_fleet_config_assignments) | **GET** /api/fleet/configuration-assignments | List fleet configuration assignments
[**update_custom_collector_base**](FleetManagementApi.md#update_custom_collector_base) | **PUT** /api/fleet/configurations/{id} | Update a custom collector base configuration
[**update_fleet_config_assignment**](FleetManagementApi.md#update_fleet_config_assignment) | **PUT** /api/fleet/configuration-assignments/{id} | Update a fleet configuration assignment


# **create_fleet_config_assignment**
> FleetConfigurationAssignment create_fleet_config_assignment(fleet_configuration_assignment)

Create a configuration assignment

This end point creates a configuration assignment for a fleet management group.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_assignment import FleetConfigurationAssignment
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
    api_instance = instana_client.FleetManagementApi(api_client)
    fleet_configuration_assignment = instana_client.FleetConfigurationAssignment() # FleetConfigurationAssignment | 

    try:
        # Create a configuration assignment
        api_response = api_instance.create_fleet_config_assignment(fleet_configuration_assignment)
        print("The response of FleetManagementApi->create_fleet_config_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->create_fleet_config_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_configuration_assignment** | [**FleetConfigurationAssignment**](FleetConfigurationAssignment.md)|  | 

### Return type

[**FleetConfigurationAssignment**](FleetConfigurationAssignment.md)

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

# **create_fleet_configuration**
> FleetConfigurationResponse create_fleet_configuration(fleet_configuration)

Creates a fleet configuration

This end point creates a fleet configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration import FleetConfiguration
from instana_client.models.fleet_configuration_response import FleetConfigurationResponse
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
    api_instance = instana_client.FleetManagementApi(api_client)
    fleet_configuration = instana_client.FleetConfiguration() # FleetConfiguration | 

    try:
        # Creates a fleet configuration
        api_response = api_instance.create_fleet_configuration(fleet_configuration)
        print("The response of FleetManagementApi->create_fleet_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->create_fleet_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_configuration** | [**FleetConfiguration**](FleetConfiguration.md)|  | 

### Return type

[**FleetConfigurationResponse**](FleetConfigurationResponse.md)

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

# **delete_custom_collector_base**
> FleetConfigurationResponse delete_custom_collector_base(id)

Delete a custom collector base configuration

This end point deletes a custom collector base configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_response import FleetConfigurationResponse
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
    api_instance = instana_client.FleetManagementApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a custom collector base configuration
        api_response = api_instance.delete_custom_collector_base(id)
        print("The response of FleetManagementApi->delete_custom_collector_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->delete_custom_collector_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FleetConfigurationResponse**](FleetConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleet_config_assignment**
> FleetConfigurationAssignmentResponse delete_fleet_config_assignment(id)

Delete a fleet configuration assignment

This end point deletes a fleet configuration assignment

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_assignment_response import FleetConfigurationAssignmentResponse
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
    api_instance = instana_client.FleetManagementApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a fleet configuration assignment
        api_response = api_instance.delete_fleet_config_assignment(id)
        print("The response of FleetManagementApi->delete_fleet_config_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->delete_fleet_config_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FleetConfigurationAssignmentResponse**](FleetConfigurationAssignmentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_collector_base**
> FleetConfiguration get_custom_collector_base(id)

Get fleet configuration details

This endpoint gets a fleet configuration by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration import FleetConfiguration
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
    api_instance = instana_client.FleetManagementApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get fleet configuration details
        api_response = api_instance.get_custom_collector_base(id)
        print("The response of FleetManagementApi->get_custom_collector_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->get_custom_collector_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FleetConfiguration**](FleetConfiguration.md)

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

# **get_fleet_config_assignment**
> FleetConfigurationAssignment get_fleet_config_assignment(id)

Get a fleet configuration assignment

This endpoint gets a fleet configuration assignment by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_assignment import FleetConfigurationAssignment
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
    api_instance = instana_client.FleetManagementApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a fleet configuration assignment
        api_response = api_instance.get_fleet_config_assignment(id)
        print("The response of FleetManagementApi->get_fleet_config_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->get_fleet_config_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FleetConfigurationAssignment**](FleetConfigurationAssignment.md)

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

# **list_custom_collector_base**
> List[FleetConfiguration] list_custom_collector_base()

List fleet configurations

This end point lists fleet configurations by type

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration import FleetConfiguration
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
    api_instance = instana_client.FleetManagementApi(api_client)

    try:
        # List fleet configurations
        api_response = api_instance.list_custom_collector_base()
        print("The response of FleetManagementApi->list_custom_collector_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->list_custom_collector_base: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FleetConfiguration]**](FleetConfiguration.md)

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

# **list_fleet_config_assignments**
> List[FleetConfigurationAssignment] list_fleet_config_assignments()

List fleet configuration assignments

This end point lists all fleet configuration assignments

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_assignment import FleetConfigurationAssignment
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
    api_instance = instana_client.FleetManagementApi(api_client)

    try:
        # List fleet configuration assignments
        api_response = api_instance.list_fleet_config_assignments()
        print("The response of FleetManagementApi->list_fleet_config_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->list_fleet_config_assignments: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FleetConfigurationAssignment]**](FleetConfigurationAssignment.md)

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

# **update_custom_collector_base**
> FleetConfigurationResponse update_custom_collector_base(id, update_fleet_configuration_request)

Update a custom collector base configuration

This end points updates the details of a custom collector base configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_response import FleetConfigurationResponse
from instana_client.models.update_fleet_configuration_request import UpdateFleetConfigurationRequest
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
    api_instance = instana_client.FleetManagementApi(api_client)
    id = 'id_example' # str | 
    update_fleet_configuration_request = instana_client.UpdateFleetConfigurationRequest() # UpdateFleetConfigurationRequest | 

    try:
        # Update a custom collector base configuration
        api_response = api_instance.update_custom_collector_base(id, update_fleet_configuration_request)
        print("The response of FleetManagementApi->update_custom_collector_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->update_custom_collector_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_fleet_configuration_request** | [**UpdateFleetConfigurationRequest**](UpdateFleetConfigurationRequest.md)|  | 

### Return type

[**FleetConfigurationResponse**](FleetConfigurationResponse.md)

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

# **update_fleet_config_assignment**
> FleetConfigurationAssignmentResponse update_fleet_config_assignment(id, fleet_configuration_assignment)

Update a fleet configuration assignment

This end points updates the details of a fleet configuration assignment

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.fleet_configuration_assignment import FleetConfigurationAssignment
from instana_client.models.fleet_configuration_assignment_response import FleetConfigurationAssignmentResponse
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
    api_instance = instana_client.FleetManagementApi(api_client)
    id = 'id_example' # str | 
    fleet_configuration_assignment = instana_client.FleetConfigurationAssignment() # FleetConfigurationAssignment | 

    try:
        # Update a fleet configuration assignment
        api_response = api_instance.update_fleet_config_assignment(id, fleet_configuration_assignment)
        print("The response of FleetManagementApi->update_fleet_config_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetManagementApi->update_fleet_config_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fleet_configuration_assignment** | [**FleetConfigurationAssignment**](FleetConfigurationAssignment.md)|  | 

### Return type

[**FleetConfigurationAssignmentResponse**](FleetConfigurationAssignmentResponse.md)

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


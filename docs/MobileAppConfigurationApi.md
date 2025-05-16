# instana_client.MobileAppConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mobile_app_config**](MobileAppConfigurationApi.md#delete_mobile_app_config) | **DELETE** /api/mobile-app-monitoring/config/{mobileAppId} | Remove mobile app
[**get_mobile_app_config**](MobileAppConfigurationApi.md#get_mobile_app_config) | **GET** /api/mobile-app-monitoring/config | Get configured mobile apps
[**get_mobile_app_geo_location_configuration**](MobileAppConfigurationApi.md#get_mobile_app_geo_location_configuration) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/geo-location | Get geo location configuration for mobile app
[**get_mobile_app_geo_mapping_rules**](MobileAppConfigurationApi.md#get_mobile_app_geo_mapping_rules) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/geo-mapping-rules | Get custom geo mapping rules for mobile app
[**get_mobile_app_ip_masking_configuration**](MobileAppConfigurationApi.md#get_mobile_app_ip_masking_configuration) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/ip-masking | Get IP masking configuration for mobile app
[**post_mobile_app_config**](MobileAppConfigurationApi.md#post_mobile_app_config) | **POST** /api/mobile-app-monitoring/config | Configure new mobile app
[**rename_mobile_app_config**](MobileAppConfigurationApi.md#rename_mobile_app_config) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId} | Rename mobile app
[**set_mobile_app_geo_mapping_rules**](MobileAppConfigurationApi.md#set_mobile_app_geo_mapping_rules) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/geo-mapping-rules | Set custom geo mapping rules for mobile app
[**update_mobile_app_geo_location_configuration**](MobileAppConfigurationApi.md#update_mobile_app_geo_location_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/geo-location | Update geo location configuration for mobile app
[**update_mobile_app_ip_masking_configuration**](MobileAppConfigurationApi.md#update_mobile_app_ip_masking_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/ip-masking | Update IP masking configuration for mobile app


# **delete_mobile_app_config**
> delete_mobile_app_config(mobile_app_id)

Remove mobile app

API request to remove mobile app.

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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'K3bP-bmCRkyimNai9vvq8o' # str | Mobile App ID

    try:
        # Remove mobile app
        api_instance.delete_mobile_app_config(mobile_app_id)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->delete_mobile_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 

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
**204** | Mobile app successfully removed |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobile_app_config**
> List[MobileApp] get_mobile_app_config()

Get configured mobile apps

API request to get configured mobile apps.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app import MobileApp
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)

    try:
        # Get configured mobile apps
        api_response = api_instance.get_mobile_app_config()
        print("The response of MobileAppConfigurationApi->get_mobile_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MobileApp]**](MobileApp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobile_app_geo_location_configuration**
> GeoLocationConfiguration get_mobile_app_geo_location_configuration(mobile_app_id)

Get geo location configuration for mobile app

API request to get geo location configuration for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.geo_location_configuration import GeoLocationConfiguration
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Mobile App ID

    try:
        # Get geo location configuration for mobile app
        api_response = api_instance.get_mobile_app_geo_location_configuration(mobile_app_id)
        print("The response of MobileAppConfigurationApi->get_mobile_app_geo_location_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_geo_location_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 

### Return type

[**GeoLocationConfiguration**](GeoLocationConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobile_app_geo_mapping_rules**
> get_mobile_app_geo_mapping_rules(mobile_app_id)

Get custom geo mapping rules for mobile app

API request to get custom geo mapping rules for mobile app.

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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Mobile App ID

    try:
        # Get custom geo mapping rules for mobile app
        api_instance.get_mobile_app_geo_mapping_rules(mobile_app_id)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_geo_mapping_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobile_app_ip_masking_configuration**
> IpMaskingConfiguration get_mobile_app_ip_masking_configuration(mobile_app_id)

Get IP masking configuration for mobile app

API request to get IP masking configuration for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.ip_masking_configuration import IpMaskingConfiguration
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Mobile App ID

    try:
        # Get IP masking configuration for mobile app
        api_response = api_instance.get_mobile_app_ip_masking_configuration(mobile_app_id)
        print("The response of MobileAppConfigurationApi->get_mobile_app_ip_masking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_ip_masking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 

### Return type

[**IpMaskingConfiguration**](IpMaskingConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mobile_app_config**
> MobileApp post_mobile_app_config(name=name)

Configure new mobile app

API request to add new mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app import MobileApp
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    name = 'name_example' # str | Name of the mobile app (optional)

    try:
        # Configure new mobile app
        api_response = api_instance.post_mobile_app_config(name=name)
        print("The response of MobileAppConfigurationApi->post_mobile_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->post_mobile_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the mobile app | [optional] 

### Return type

[**MobileApp**](MobileApp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mobile App successfully configured |  -  |
**400** | Missing name query parameter or name already used for a configured mobile app. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_mobile_app_config**
> MobileApp rename_mobile_app_config(mobile_app_id, name=name)

Rename mobile app

API request to rename mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app import MobileApp
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'K3bP-bmCRkyimNai9vvq8o' # str | Mobile App ID
    name = 'name_example' # str | New name of the mobile app (optional)

    try:
        # Rename mobile app
        api_response = api_instance.rename_mobile_app_config(mobile_app_id, name=name)
        print("The response of MobileAppConfigurationApi->rename_mobile_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->rename_mobile_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **name** | **str**| New name of the mobile app | [optional] 

### Return type

[**MobileApp**](MobileApp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mobile app successfully renamed |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mobile_app_geo_mapping_rules**
> set_mobile_app_geo_mapping_rules(mobile_app_id, body=body)

Set custom geo mapping rules for mobile app

API request to set custom geo mapping rules for mobile app.

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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'K3bP-bmCRkyimNai9vvq8o' # str | Mobile App ID
    body = 'body_example' # str |  (optional)

    try:
        # Set custom geo mapping rules for mobile app
        api_instance.set_mobile_app_geo_mapping_rules(mobile_app_id, body=body)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->set_mobile_app_geo_mapping_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**415** | Unsupported Media Type. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mobile_app_geo_location_configuration**
> GeoLocationConfiguration update_mobile_app_geo_location_configuration(mobile_app_id, geo_location_configuration=geo_location_configuration)

Update geo location configuration for mobile app

API request to update geo location configuration for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.geo_location_configuration import GeoLocationConfiguration
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Mobile App ID
    geo_location_configuration = instana_client.GeoLocationConfiguration() # GeoLocationConfiguration |  (optional)

    try:
        # Update geo location configuration for mobile app
        api_response = api_instance.update_mobile_app_geo_location_configuration(mobile_app_id, geo_location_configuration=geo_location_configuration)
        print("The response of MobileAppConfigurationApi->update_mobile_app_geo_location_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->update_mobile_app_geo_location_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **geo_location_configuration** | [**GeoLocationConfiguration**](GeoLocationConfiguration.md)|  | [optional] 

### Return type

[**GeoLocationConfiguration**](GeoLocationConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mobile_app_ip_masking_configuration**
> IpMaskingConfiguration update_mobile_app_ip_masking_configuration(mobile_app_id, ip_masking_configuration=ip_masking_configuration)

Update IP masking configuration for mobile app

API request to update IP masking configuration for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.ip_masking_configuration import IpMaskingConfiguration
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
    api_instance = instana_client.MobileAppConfigurationApi(api_client)
    mobile_app_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Mobile App ID
    ip_masking_configuration = instana_client.IpMaskingConfiguration() # IpMaskingConfiguration |  (optional)

    try:
        # Update IP masking configuration for mobile app
        api_response = api_instance.update_mobile_app_ip_masking_configuration(mobile_app_id, ip_masking_configuration=ip_masking_configuration)
        print("The response of MobileAppConfigurationApi->update_mobile_app_ip_masking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->update_mobile_app_ip_masking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **ip_masking_configuration** | [**IpMaskingConfiguration**](IpMaskingConfiguration.md)|  | [optional] 

### Return type

[**IpMaskingConfiguration**](IpMaskingConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# instana_client.MobileAppConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_mobile_app_source_map_upload_configuration**](MobileAppConfigurationApi.md#clear_mobile_app_source_map_upload_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload/{sourceMapConfigId}/clear | Clear sourcemap files for sourcemap upload configuration
[**commit_mobile_app_source_map_file**](MobileAppConfigurationApi.md#commit_mobile_app_source_map_file) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload/{sourceMapConfigId}/commit | Commit sourcemap file upload for mobile app
[**delete_mobile_app_config**](MobileAppConfigurationApi.md#delete_mobile_app_config) | **DELETE** /api/mobile-app-monitoring/config/{mobileAppId} | Remove mobile app
[**delete_mobile_app_source_map_upload_configuration**](MobileAppConfigurationApi.md#delete_mobile_app_source_map_upload_configuration) | **DELETE** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload/{sourceMapConfigId} | Delete sourcemap configuration for mobile app
[**get_mobile_app_config**](MobileAppConfigurationApi.md#get_mobile_app_config) | **GET** /api/mobile-app-monitoring/config | Get configured mobile apps
[**get_mobile_app_geo_location_configuration**](MobileAppConfigurationApi.md#get_mobile_app_geo_location_configuration) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/geo-location | Get geo location configuration for mobile app
[**get_mobile_app_geo_mapping_rules**](MobileAppConfigurationApi.md#get_mobile_app_geo_mapping_rules) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/geo-mapping-rules | Get custom geo mapping rules for mobile app
[**get_mobile_app_ip_masking_configuration**](MobileAppConfigurationApi.md#get_mobile_app_ip_masking_configuration) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/ip-masking | Get IP masking configuration for mobile app
[**get_mobile_app_source_map_file**](MobileAppConfigurationApi.md#get_mobile_app_source_map_file) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload/{sourceMapConfigId} | Get sourcemap configuration for mobile app
[**get_mobile_app_source_map_files**](MobileAppConfigurationApi.md#get_mobile_app_source_map_files) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload | Get all sourcemap configurations for mobile app
[**get_single_mobile_app_config**](MobileAppConfigurationApi.md#get_single_mobile_app_config) | **GET** /api/mobile-app-monitoring/config/{mobileAppId} | Get mobile app configuration by ID
[**post_mobile_app_config**](MobileAppConfigurationApi.md#post_mobile_app_config) | **POST** /api/mobile-app-monitoring/config | Configure new mobile app
[**post_mobile_app_source_map_config**](MobileAppConfigurationApi.md#post_mobile_app_source_map_config) | **POST** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload | Add new sourcemap configuration for mobile app
[**rename_mobile_app_config**](MobileAppConfigurationApi.md#rename_mobile_app_config) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId} | Rename mobile app
[**set_mobile_app_geo_mapping_rules**](MobileAppConfigurationApi.md#set_mobile_app_geo_mapping_rules) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/geo-mapping-rules | Set custom geo mapping rules for mobile app
[**update_mobile_app_geo_location_configuration**](MobileAppConfigurationApi.md#update_mobile_app_geo_location_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/geo-location | Update geo location configuration for mobile app
[**update_mobile_app_ip_masking_configuration**](MobileAppConfigurationApi.md#update_mobile_app_ip_masking_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/ip-masking | Update IP masking configuration for mobile app
[**update_mobile_app_teams**](MobileAppConfigurationApi.md#update_mobile_app_teams) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/teams | Update teams assigned to the mobile app
[**upload_mobile_app_source_map_file**](MobileAppConfigurationApi.md#upload_mobile_app_source_map_file) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/sourcemap-upload/{sourceMapConfigId}/form | Upload sourcemap file for mobile app


# **clear_mobile_app_source_map_upload_configuration**
> clear_mobile_app_source_map_upload_configuration(mobile_app_id, source_map_config_id)

Clear sourcemap files for sourcemap upload configuration

API request to clear sourcemap files of a configuration for mobile app.

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
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID

    try:
        # Clear sourcemap files for sourcemap upload configuration
        api_instance.clear_mobile_app_source_map_upload_configuration(mobile_app_id, source_map_config_id)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->clear_mobile_app_source_map_upload_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **source_map_config_id** | **str**| Source Map Config ID | 

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
**204** | Sourcemap files in the sourcemap configuration successfully cleared |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_mobile_app_source_map_file**
> SourceMapUploadConfig commit_mobile_app_source_map_file(mobile_app_id, source_map_config_id, file_id=file_id, file_type=file_type)

Commit sourcemap file upload for mobile app

API request to commit sourcemap file upload for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.source_map_upload_config import SourceMapUploadConfig
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
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID
    file_id = 'file_id_example' # str |  (optional)
    file_type = 'file_type_example' # str |  (optional)

    try:
        # Commit sourcemap file upload for mobile app
        api_response = api_instance.commit_mobile_app_source_map_file(mobile_app_id, source_map_config_id, file_id=file_id, file_type=file_type)
        print("The response of MobileAppConfigurationApi->commit_mobile_app_source_map_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->commit_mobile_app_source_map_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **source_map_config_id** | **str**| Source Map Config ID | 
 **file_id** | **str**|  | [optional] 
 **file_type** | **str**|  | [optional] 

### Return type

[**SourceMapUploadConfig**](SourceMapUploadConfig.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully committed sourcemap file upload. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **delete_mobile_app_source_map_upload_configuration**
> delete_mobile_app_source_map_upload_configuration(mobile_app_id, source_map_config_id)

Delete sourcemap configuration for mobile app

API request to delete sourcemap configuration for mobile app.

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
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID

    try:
        # Delete sourcemap configuration for mobile app
        api_instance.delete_mobile_app_source_map_upload_configuration(mobile_app_id, source_map_config_id)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->delete_mobile_app_source_map_upload_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **source_map_config_id** | **str**| Source Map Config ID | 

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
**204** | Sourcemap configuration successfully deleted or sourcemap not found |  -  |
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
    mobile_app_id = 'mobile_app_id_example' # str | 

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
 **mobile_app_id** | **str**|  | 

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
    mobile_app_id = 'mobile_app_id_example' # str | 

    try:
        # Get custom geo mapping rules for mobile app
        api_instance.get_mobile_app_geo_mapping_rules(mobile_app_id)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_geo_mapping_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**|  | 

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
    mobile_app_id = 'mobile_app_id_example' # str | 

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
 **mobile_app_id** | **str**|  | 

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

# **get_mobile_app_source_map_file**
> SourceMapUploadConfig get_mobile_app_source_map_file(mobile_app_id, source_map_config_id)

Get sourcemap configuration for mobile app

API request to get sourcemap configuration for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.source_map_upload_config import SourceMapUploadConfig
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
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID

    try:
        # Get sourcemap configuration for mobile app
        api_response = api_instance.get_mobile_app_source_map_file(mobile_app_id, source_map_config_id)
        print("The response of MobileAppConfigurationApi->get_mobile_app_source_map_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_source_map_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **source_map_config_id** | **str**| Source Map Config ID | 

### Return type

[**SourceMapUploadConfig**](SourceMapUploadConfig.md)

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

# **get_mobile_app_source_map_files**
> SourceMapUploadConfigs get_mobile_app_source_map_files(mobile_app_id)

Get all sourcemap configurations for mobile app

API request to get all sourcemap configurations for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.source_map_upload_configs import SourceMapUploadConfigs
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
        # Get all sourcemap configurations for mobile app
        api_response = api_instance.get_mobile_app_source_map_files(mobile_app_id)
        print("The response of MobileAppConfigurationApi->get_mobile_app_source_map_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_mobile_app_source_map_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 

### Return type

[**SourceMapUploadConfigs**](SourceMapUploadConfigs.md)

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

# **get_single_mobile_app_config**
> MobileApp get_single_mobile_app_config(mobile_app_id)

Get mobile app configuration by ID

API request to get a specific mobile app configuration by ID.

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

    try:
        # Get mobile app configuration by ID
        api_response = api_instance.get_single_mobile_app_config(mobile_app_id)
        print("The response of MobileAppConfigurationApi->get_single_mobile_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->get_single_mobile_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 

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
**200** | OK |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mobile_app_config**
> MobileApp post_mobile_app_config(name=name, api_tag=api_tag)

Configure new mobile app

API request to add new mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_tag import ApiTag
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
    api_tag = [{"id":"test","displayName":"test"}] # List[ApiTag] |  (optional)

    try:
        # Configure new mobile app
        api_response = api_instance.post_mobile_app_config(name=name, api_tag=api_tag)
        print("The response of MobileAppConfigurationApi->post_mobile_app_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->post_mobile_app_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the mobile app | [optional] 
 **api_tag** | [**List[ApiTag]**](ApiTag.md)|  | [optional] 

### Return type

[**MobileApp**](MobileApp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **post_mobile_app_source_map_config**
> SourceMapUploadConfig post_mobile_app_source_map_config(mobile_app_id, post_mobile_app_source_map_config_request=post_mobile_app_source_map_config_request)

Add new sourcemap configuration for mobile app

API request to add sourcemap configuration for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.post_mobile_app_source_map_config_request import PostMobileAppSourceMapConfigRequest
from instana_client.models.source_map_upload_config import SourceMapUploadConfig
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
    post_mobile_app_source_map_config_request = {"description":"InstanaAgentExample_v2"} # PostMobileAppSourceMapConfigRequest |  (optional)

    try:
        # Add new sourcemap configuration for mobile app
        api_response = api_instance.post_mobile_app_source_map_config(mobile_app_id, post_mobile_app_source_map_config_request=post_mobile_app_source_map_config_request)
        print("The response of MobileAppConfigurationApi->post_mobile_app_source_map_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->post_mobile_app_source_map_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **post_mobile_app_source_map_config_request** | [**PostMobileAppSourceMapConfigRequest**](PostMobileAppSourceMapConfigRequest.md)|  | [optional] 

### Return type

[**SourceMapUploadConfig**](SourceMapUploadConfig.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mobile App sourcemap configuration added successfully |  -  |
**400** | Missing description or description already used for a configuration. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |
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
    mobile_app_id = 'mobile_app_id_example' # str | 
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
 **mobile_app_id** | **str**|  | 
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

# **update_mobile_app_teams**
> List[ApiTag] update_mobile_app_teams(mobile_app_id, api_tag=api_tag)

Update teams assigned to the mobile app

API request to update teams of a mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.api_tag import ApiTag
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
    mobile_app_id = 'mobile_app_id_example' # str | 
    api_tag = [{"id":"test","displayName":"test"}] # List[ApiTag] |  (optional)

    try:
        # Update teams assigned to the mobile app
        api_response = api_instance.update_mobile_app_teams(mobile_app_id, api_tag=api_tag)
        print("The response of MobileAppConfigurationApi->update_mobile_app_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->update_mobile_app_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**|  | 
 **api_tag** | [**List[ApiTag]**](ApiTag.md)|  | [optional] 

### Return type

[**List[ApiTag]**](ApiTag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mobile App successfully configured |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_mobile_app_source_map_file**
> SourceMapUploadConfig upload_mobile_app_source_map_file(mobile_app_id, source_map_config_id, blob_index, file_format, file_id, file_type, source_map)

Upload sourcemap file for mobile app

API request to upload sourcemap file for mobile app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.source_map_upload_config import SourceMapUploadConfig
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
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID
    blob_index = 56 # int | Blob index which starts from 1
    file_format = 'file_format_example' # str | File format. Example tgz
    file_id = 'file_id_example' # str | Identifier of your app. For example, com.instana.ios.InstanaExampleApp
    file_type = 'file_type_example' # str | dSYM stands for iOS symbol file, R8PG_MAP stands for Android java mapping file
    source_map = None # bytearray | Path to your local symbol file

    try:
        # Upload sourcemap file for mobile app
        api_response = api_instance.upload_mobile_app_source_map_file(mobile_app_id, source_map_config_id, blob_index, file_format, file_id, file_type, source_map)
        print("The response of MobileAppConfigurationApi->upload_mobile_app_source_map_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppConfigurationApi->upload_mobile_app_source_map_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| Mobile App ID | 
 **source_map_config_id** | **str**| Source Map Config ID | 
 **blob_index** | **int**| Blob index which starts from 1 | 
 **file_format** | **str**| File format. Example tgz | 
 **file_id** | **str**| Identifier of your app. For example, com.instana.ios.InstanaExampleApp | 
 **file_type** | **str**| dSYM stands for iOS symbol file, R8PG_MAP stands for Android java mapping file | 
 **source_map** | **bytearray**| Path to your local symbol file | 

### Return type

[**SourceMapUploadConfig**](SourceMapUploadConfig.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


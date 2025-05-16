# instana_client.WebsiteConfigurationApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_source_map_upload_configuration**](WebsiteConfigurationApi.md#clear_source_map_upload_configuration) | **PUT** /api/website-monitoring/config/{websiteId}/sourcemap-upload/{sourceMapConfigId}/clear | Clear source map files for source map upload configuration
[**create_website**](WebsiteConfigurationApi.md#create_website) | **POST** /api/website-monitoring/config | Configure new website
[**delete_website**](WebsiteConfigurationApi.md#delete_website) | **DELETE** /api/website-monitoring/config/{websiteId} | Remove website
[**get_website**](WebsiteConfigurationApi.md#get_website) | **GET** /api/website-monitoring/config/{websiteId} | Get configured website
[**get_website_geo_location_configuration**](WebsiteConfigurationApi.md#get_website_geo_location_configuration) | **GET** /api/website-monitoring/config/{websiteId}/geo-location | Get geo location configuration for website
[**get_website_geo_mapping_rules**](WebsiteConfigurationApi.md#get_website_geo_mapping_rules) | **GET** /api/website-monitoring/config/{websiteId}/geo-mapping-rules | Get custom geo mapping rules for website
[**get_website_ip_masking_configuration**](WebsiteConfigurationApi.md#get_website_ip_masking_configuration) | **GET** /api/website-monitoring/config/{websiteId}/ip-masking | Get IP masking configuration for website
[**get_websites**](WebsiteConfigurationApi.md#get_websites) | **GET** /api/website-monitoring/config | Get configured websites
[**rename_website**](WebsiteConfigurationApi.md#rename_website) | **PUT** /api/website-monitoring/config/{websiteId} | Rename website
[**set_website_geo_mapping_rules**](WebsiteConfigurationApi.md#set_website_geo_mapping_rules) | **PUT** /api/website-monitoring/config/{websiteId}/geo-mapping-rules | Set custom geo mapping rules for website
[**update_website_geo_location_configuration**](WebsiteConfigurationApi.md#update_website_geo_location_configuration) | **PUT** /api/website-monitoring/config/{websiteId}/geo-location | Update geo location configuration for website
[**update_website_ip_masking_configuration**](WebsiteConfigurationApi.md#update_website_ip_masking_configuration) | **PUT** /api/website-monitoring/config/{websiteId}/ip-masking | Update IP masking configuration for website
[**upload_source_map_file**](WebsiteConfigurationApi.md#upload_source_map_file) | **PUT** /api/website-monitoring/config/{websiteId}/sourcemap-upload/{sourceMapConfigId}/form | Upload source map file for website


# **clear_source_map_upload_configuration**
> clear_source_map_upload_configuration(website_id, source_map_config_id)

Clear source map files for source map upload configuration

API request to clear source map files for source map upload configuration.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'UhzF-fWORlyVLHDlvutYYQ' # str | Website ID
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID

    try:
        # Clear source map files for source map upload configuration
        api_instance.clear_source_map_upload_configuration(website_id, source_map_config_id)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->clear_source_map_upload_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website ID | 
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
**204** | Source map files in the source map upload configuration successfully cleared |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_website**
> Website create_website(name=name)

Configure new website

API request to add new website.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website import Website
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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        # Configure new website
        api_response = api_instance.create_website(name=name)
        print("The response of WebsiteConfigurationApi->create_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->create_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**Website**](Website.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website successfully configured |  -  |
**400** | Missing name query parameter or name already used for a configured website |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website**
> delete_website(website_id)

Remove website

API request to delete website.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'K3bP-bmCRkyimNai9vvq8o' # str | websiteId

    try:
        # Remove website
        api_instance.delete_website(website_id)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->delete_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| websiteId | 

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
**204** | Website successfully removed |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website**
> Website get_website(website_id)

Get configured website

API request to get configured website details for specified websiteId

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website import Website
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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = '1ELrNt-eQ9SlK4D_EgLMiA' # str | websiteId

    try:
        # Get configured website
        api_response = api_instance.get_website(website_id)
        print("The response of WebsiteConfigurationApi->get_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->get_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| websiteId | 

### Return type

[**Website**](Website.md)

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

# **get_website_geo_location_configuration**
> GeoLocationConfiguration get_website_geo_location_configuration(website_id)

Get geo location configuration for website

API request to get geo-location configuration of a website specified by its websiteId

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = '1ELrNt-eQ9SlK4D_EgLMiA' # str | websiteId

    try:
        # Get geo location configuration for website
        api_response = api_instance.get_website_geo_location_configuration(website_id)
        print("The response of WebsiteConfigurationApi->get_website_geo_location_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->get_website_geo_location_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| websiteId | 

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

# **get_website_geo_mapping_rules**
> get_website_geo_mapping_rules(website_id)

Get custom geo mapping rules for website

API request to get custom geo mapping rules for website.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Website ID

    try:
        # Get custom geo mapping rules for website
        api_instance.get_website_geo_mapping_rules(website_id)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->get_website_geo_mapping_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website ID | 

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

# **get_website_ip_masking_configuration**
> IpMaskingConfiguration get_website_ip_masking_configuration(website_id)

Get IP masking configuration for website

API request to get IP masking configuration of a website specified by its websiteId

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = '1ELrNt-eQ9SlK4D_EgLMiA' # str | websiteId

    try:
        # Get IP masking configuration for website
        api_response = api_instance.get_website_ip_masking_configuration(website_id)
        print("The response of WebsiteConfigurationApi->get_website_ip_masking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->get_website_ip_masking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| websiteId | 

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

# **get_websites**
> List[Website] get_websites()

Get configured websites

API request to get all configured websites details.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website import Website
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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)

    try:
        # Get configured websites
        api_response = api_instance.get_websites()
        print("The response of WebsiteConfigurationApi->get_websites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->get_websites: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Website]**](Website.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_website**
> Website rename_website(website_id, name=name)

Rename website

API request to rename website.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website import Website
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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'K3bP-bmCRkyimNai9vvq8o' # str | websiteId
    name = 'name_example' # str |  (optional)

    try:
        # Rename website
        api_response = api_instance.rename_website(website_id, name=name)
        print("The response of WebsiteConfigurationApi->rename_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->rename_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| websiteId | 
 **name** | **str**|  | [optional] 

### Return type

[**Website**](Website.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website successfully renamed |  -  |
**400** | Missing name query parameter or name already used for a configured website |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_website_geo_mapping_rules**
> set_website_geo_mapping_rules(website_id, body=body)

Set custom geo mapping rules for website

API request to set custom geo mapping rules for website.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'K3bP-bmCRkyimNai9vvq8o' # str | Website ID
    body = 'body_example' # str |  (optional)

    try:
        # Set custom geo mapping rules for website
        api_instance.set_website_geo_mapping_rules(website_id, body=body)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->set_website_geo_mapping_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website ID | 
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

# **update_website_geo_location_configuration**
> GeoLocationConfiguration update_website_geo_location_configuration(website_id, geo_location_configuration=geo_location_configuration)

Update geo location configuration for website

API request to update geo location configuration for website.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Website ID
    geo_location_configuration = instana_client.GeoLocationConfiguration() # GeoLocationConfiguration |  (optional)

    try:
        # Update geo location configuration for website
        api_response = api_instance.update_website_geo_location_configuration(website_id, geo_location_configuration=geo_location_configuration)
        print("The response of WebsiteConfigurationApi->update_website_geo_location_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->update_website_geo_location_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website ID | 
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

# **update_website_ip_masking_configuration**
> IpMaskingConfiguration update_website_ip_masking_configuration(website_id, ip_masking_configuration=ip_masking_configuration)

Update IP masking configuration for website

API request to update IP masking configuration for website.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'iiLxP1zaTuCS7fyk9m4W0W' # str | Website ID
    ip_masking_configuration = instana_client.IpMaskingConfiguration() # IpMaskingConfiguration |  (optional)

    try:
        # Update IP masking configuration for website
        api_response = api_instance.update_website_ip_masking_configuration(website_id, ip_masking_configuration=ip_masking_configuration)
        print("The response of WebsiteConfigurationApi->update_website_ip_masking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->update_website_ip_masking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website ID | 
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

# **upload_source_map_file**
> SourceMapUploadConfig upload_source_map_file(website_id, source_map_config_id, file_format=file_format, source_map=source_map, url=url)

Upload source map file for website

API request to upload source map file for a website.

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
    api_instance = instana_client.WebsiteConfigurationApi(api_client)
    website_id = 'UhzF-fWORlyVLHDlvutYYQ' # str | Website ID
    source_map_config_id = '97e0ad312110d3ad' # str | Source Map Config ID
    file_format = 'file_format_example' # str |  (optional)
    source_map = None # bytearray |  (optional)
    url = 'url_example' # str |  (optional)

    try:
        # Upload source map file for website
        api_response = api_instance.upload_source_map_file(website_id, source_map_config_id, file_format=file_format, source_map=source_map, url=url)
        print("The response of WebsiteConfigurationApi->upload_source_map_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteConfigurationApi->upload_source_map_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website ID | 
 **source_map_config_id** | **str**| Source Map Config ID | 
 **file_format** | **str**|  | [optional] 
 **source_map** | **bytearray**|  | [optional] 
 **url** | **str**|  | [optional] 

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
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


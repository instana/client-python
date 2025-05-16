# instana_client.ApplicationSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_application_config**](ApplicationSettingsApi.md#add_application_config) | **POST** /api/application-monitoring/settings/application | Add application configuration
[**add_manual_service_config**](ApplicationSettingsApi.md#add_manual_service_config) | **POST** /api/application-monitoring/settings/manual-service | Add manual service configuration
[**add_service_config**](ApplicationSettingsApi.md#add_service_config) | **POST** /api/application-monitoring/settings/service | Add service configuration
[**create_endpoint_config**](ApplicationSettingsApi.md#create_endpoint_config) | **POST** /api/application-monitoring/settings/endpoint | Create endpoint configuration
[**create_http_endpoint_config**](ApplicationSettingsApi.md#create_http_endpoint_config) | **POST** /api/application-monitoring/settings/http-endpoint | Create HTTP endpoint configuration
[**delete_application_config**](ApplicationSettingsApi.md#delete_application_config) | **DELETE** /api/application-monitoring/settings/application/{id} | Delete application configuration
[**delete_endpoint_config**](ApplicationSettingsApi.md#delete_endpoint_config) | **DELETE** /api/application-monitoring/settings/endpoint/{id} | Delete endpoint configuration
[**delete_http_endpoint_config**](ApplicationSettingsApi.md#delete_http_endpoint_config) | **DELETE** /api/application-monitoring/settings/http-endpoint/{id} | Delete HTTP endpoint configuration
[**delete_manual_service_config**](ApplicationSettingsApi.md#delete_manual_service_config) | **DELETE** /api/application-monitoring/settings/manual-service/{id} | Delete manual service configuration
[**delete_service_config**](ApplicationSettingsApi.md#delete_service_config) | **DELETE** /api/application-monitoring/settings/service/{id} | Delete service configuration
[**get_all_manual_service_configs**](ApplicationSettingsApi.md#get_all_manual_service_configs) | **GET** /api/application-monitoring/settings/manual-service | All manual service configurations
[**get_application_config**](ApplicationSettingsApi.md#get_application_config) | **GET** /api/application-monitoring/settings/application/{id} | Application configuration
[**get_application_configs**](ApplicationSettingsApi.md#get_application_configs) | **GET** /api/application-monitoring/settings/application | All Application configurations
[**get_endpoint_config**](ApplicationSettingsApi.md#get_endpoint_config) | **GET** /api/application-monitoring/settings/endpoint/{id} | Endpoint configuration
[**get_endpoint_configs**](ApplicationSettingsApi.md#get_endpoint_configs) | **GET** /api/application-monitoring/settings/endpoint | All Endpoint configurations
[**get_http_endpoint_config**](ApplicationSettingsApi.md#get_http_endpoint_config) | **GET** /api/application-monitoring/settings/http-endpoint/{id} | HTTP Endpoint configuration
[**get_http_endpoint_configs**](ApplicationSettingsApi.md#get_http_endpoint_configs) | **GET** /api/application-monitoring/settings/http-endpoint | All HTTP endpoint configurations
[**get_service_config**](ApplicationSettingsApi.md#get_service_config) | **GET** /api/application-monitoring/settings/service/{id} | Service configuration
[**get_service_configs**](ApplicationSettingsApi.md#get_service_configs) | **GET** /api/application-monitoring/settings/service | All service configurations
[**order_service_config**](ApplicationSettingsApi.md#order_service_config) | **PUT** /api/application-monitoring/settings/service/order | Order of service configuration
[**put_application_config**](ApplicationSettingsApi.md#put_application_config) | **PUT** /api/application-monitoring/settings/application/{id} | Update application configuration
[**put_service_config**](ApplicationSettingsApi.md#put_service_config) | **PUT** /api/application-monitoring/settings/service/{id} | Update service configuration
[**replace_all**](ApplicationSettingsApi.md#replace_all) | **PUT** /api/application-monitoring/settings/service | Replace all service configurations
[**replace_all_manual_service_configs**](ApplicationSettingsApi.md#replace_all_manual_service_configs) | **PUT** /api/application-monitoring/settings/manual-service | Replace all manual service configurations
[**update_endpoint_config**](ApplicationSettingsApi.md#update_endpoint_config) | **PUT** /api/application-monitoring/settings/endpoint/{id} | Update endpoint configuration
[**update_http_endpoint_config**](ApplicationSettingsApi.md#update_http_endpoint_config) | **PUT** /api/application-monitoring/settings/http-endpoint/{id} | Update HTTP endpoint configuration
[**update_manual_service_config**](ApplicationSettingsApi.md#update_manual_service_config) | **PUT** /api/application-monitoring/settings/manual-service/{id} | Update manual service configuration


# **add_application_config**
> ApplicationConfig add_application_config(new_application_config)

Add application configuration

Use this API endpoint if one wants to create a new Application Perspective. This endpoint requires `canConfigureApplications` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureApplications` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Configuration of applications` to `true`.   ## Deprecated Parameters **matchSpecification:** A binary tree sturcture of match expression connected with binary operator AND or OR. It is replaced by **tagFilterExpression** which is also used in Application Analyze API endpoints.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_config import ApplicationConfig
from instana_client.models.new_application_config import NewApplicationConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    new_application_config = {"accessRules":[{"accessType":"READ_WRITE","relationType":"GLOBAL","relatedId":null}],"boundaryScope":"INBOUND","label":"Discount Build 6987","scope":"INCLUDE_IMMEDIATE_DOWNSTREAM_DATABASE_AND_MESSAGING","tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"kubernetes.label","stringValue":"stage=canary","numberValue":null,"booleanValue":null,"key":"stage","value":"canary","operator":"EQUALS","entity":"DESTINATION"},{"type":"TAG_FILTER","name":"kubernetes.label","stringValue":"build=6987","numberValue":null,"booleanValue":null,"key":"build","value":"6987","operator":"EQUALS","entity":"DESTINATION"},{"type":"TAG_FILTER","name":"kubernetes.label","stringValue":"app=discount","numberValue":null,"booleanValue":null,"key":"app","value":"discount","operator":"EQUALS","entity":"DESTINATION"}]}} # NewApplicationConfig | 

    try:
        # Add application configuration
        api_response = api_instance.add_application_config(new_application_config)
        print("The response of ApplicationSettingsApi->add_application_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->add_application_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_application_config** | [**NewApplicationConfig**](NewApplicationConfig.md)|  | 

### Return type

[**ApplicationConfig**](ApplicationConfig.md)

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

# **add_manual_service_config**
> ManualServiceConfig add_manual_service_config(new_manual_service_config)

Add manual service configuration

Use this API endpoint if one wants to add a manual service configuration. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.  **This is an experimental endpoint to workaround service mapping issues.**  ### Use cases  The manual service configuration APIs enables mapping calls to services using tag filter expressions based on call tags.  There are two use cases on the usage of these APIs:  1. Map to an Unmonitored Service with a Custom Name. For example, Map HTTP calls to different Google domains (`www.ibm.com`, `www.ibm.fr`) into a single service named `IBM` using the `call.http.host tag`. 2. Link Calls to an Existing Monitored Service. For example, Link database calls (`jdbc:mysql://10.128.0.1:3306`) to an existing service like `MySQL@3306` on demo-host by referencing its service ID.  ### Important Note  1. Use `tagfilterExpression` to match calls on which the manual service configuration will be applied. **Only call tags are allowed** in the tag filter expression.  2.  Either `unmonitoredServiceName` or `existingServiceId` should be specified in a configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.manual_service_config import ManualServiceConfig
from instana_client.models.new_manual_service_config import NewManualServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    new_manual_service_config = {"description":"Map source service example","enabled":true,"existingServiceId":"c467ca0fa21477fee3cde75a140b2963307388a7","tagFilterExpression":{"type":"TAG_FILTER","name":"service.name","stringValue":"front","numberValue":null,"booleanValue":null,"key":null,"value":"front","operator":"EQUALS","entity":"SOURCE"},"unmonitoredServiceName":null} # NewManualServiceConfig | 

    try:
        # Add manual service configuration
        api_response = api_instance.add_manual_service_config(new_manual_service_config)
        print("The response of ApplicationSettingsApi->add_manual_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->add_manual_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_manual_service_config** | [**NewManualServiceConfig**](NewManualServiceConfig.md)|  | 

### Return type

[**ManualServiceConfig**](ManualServiceConfig.md)

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

# **add_service_config**
> ServiceConfig add_service_config(service_config)

Add service configuration

Use this API endpoint if one wants to create a custom service rule. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.    ## Errata:    The following field is documented in the request schema: - The `id` field is not mandatory and one can't have a service configuration id before creating one configuration. Instana creates it automatically. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_config import ServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    service_config = {"comment":null,"enabled":true,"label":"{gce.zone}-{jvm.args.abc}","matchSpecification":[{"key":"gce.zone","value":".*"},{"key":"jvm.args.abc","value":".*"}],"name":"ABC is good"} # ServiceConfig | 

    try:
        # Add service configuration
        api_response = api_instance.add_service_config(service_config)
        print("The response of ApplicationSettingsApi->add_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->add_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_config** | [**ServiceConfig**](ServiceConfig.md)|  | 

### Return type

[**ServiceConfig**](ServiceConfig.md)

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

# **create_endpoint_config**
> EndpointConfig create_endpoint_config(endpoint_config)

Create endpoint configuration

Use this API endpoint if one wants to create an endpoint configuration of a service. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.endpoint_config import EndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    endpoint_config = {"serviceId":"d0cedae516f2182ede16f57f67476dd4c7dab9cd","endpointCase":"LOWER","endpointNameByFirstPathSegmentRuleEnabled":false,"endpointNameByCollectedPathTemplateRuleEnabled":false,"rules":null} # EndpointConfig | 

    try:
        # Create endpoint configuration
        api_response = api_instance.create_endpoint_config(endpoint_config)
        print("The response of ApplicationSettingsApi->create_endpoint_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->create_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_config** | [**EndpointConfig**](EndpointConfig.md)|  | 

### Return type

[**EndpointConfig**](EndpointConfig.md)

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

# **create_http_endpoint_config**
> HttpEndpointConfig create_http_endpoint_config(http_endpoint_config)

Create HTTP endpoint configuration

This is a deprecated endpoint. Use `Create endpoint configuration` instead. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.http_endpoint_config import HttpEndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    http_endpoint_config = {"endpointNameByCollectedPathTemplateRuleEnabled":true,"endpointNameByFirstPathSegmentRuleEnabled":true,"rules":[{"enabled":true,"pathSegments":[{"type":"MATCH_ALL"}],"testCases":["/api/v2/users"]}],"serviceId":"20ba31821b079e7d845a08096124880db3eeeb40"} # HttpEndpointConfig | 

    try:
        # Create HTTP endpoint configuration
        api_response = api_instance.create_http_endpoint_config(http_endpoint_config)
        print("The response of ApplicationSettingsApi->create_http_endpoint_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->create_http_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_endpoint_config** | [**HttpEndpointConfig**](HttpEndpointConfig.md)|  | 

### Return type

[**HttpEndpointConfig**](HttpEndpointConfig.md)

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

# **delete_application_config**
> delete_application_config(id)

Delete application configuration

Use this API endpoint if one wants to delete an Application Perspective. This endpoint requires `canConfigureApplications` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureApplications` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token.  ## Deprecated Parameters **matchSpecification:** A binary tree structure of match expression connected with binary operator AND or OR. It is replaced by **tagFilterExpression** which is also used in Application Analyze API endpoints. 

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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete application configuration
        api_instance.delete_application_config(id)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->delete_application_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **delete_endpoint_config**
> delete_endpoint_config(id)

Delete endpoint configuration

Use this API endpoint if one wants to delete an endpoint configuration of a service. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete endpoint configuration
        api_instance.delete_endpoint_config(id)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->delete_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **delete_http_endpoint_config**
> delete_http_endpoint_config(id)

Delete HTTP endpoint configuration

This is a deprecated endpoint. Use `Delete endpoint configuration` instead. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete HTTP endpoint configuration
        api_instance.delete_http_endpoint_config(id)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->delete_http_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **delete_manual_service_config**
> delete_manual_service_config(id)

Delete manual service configuration

Use this API endpoint if one wants to delete a manual service configuration. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.  **This is an experimental endpoint to workaround service mapping issues.**  ### Use cases  The manual service configuration APIs enables mapping calls to services using tag filter expressions based on call tags.  There are two use cases on the usage of these APIs:  1. Map to an Unmonitored Service with a Custom Name. For example, Map HTTP calls to different Google domains (`www.ibm.com`, `www.ibm.fr`) into a single service named `IBM` using the `call.http.host tag`. 2. Link Calls to an Existing Monitored Service. For example, Link database calls (`jdbc:mysql://10.128.0.1:3306`) to an existing service like `MySQL@3306` on demo-host by referencing its service ID.

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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete manual service configuration
        api_instance.delete_manual_service_config(id)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->delete_manual_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **delete_service_config**
> delete_service_config(id)

Delete service configuration

Use this API endpoint if one wants to delete a service configuration. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete service configuration
        api_instance.delete_service_config(id)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->delete_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_all_manual_service_configs**
> List[ManualServiceConfig] get_all_manual_service_configs()

All manual service configurations

Use this API Endpoint if one wants to retrieve a list of all manual service configurations. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.  **This is an experimental endpoint to workaround service mapping issues.**  ### Use cases  The manual service configuration APIs enables mapping calls to services using tag filter expressions based on call tags.  There are two use cases on the usage of these APIs:  1. Map to an Unmonitored Service with a Custom Name. For example, Map HTTP calls to different Google domains (`www.ibm.com`, `www.ibm.fr`) into a single service named `IBM` using the `call.http.host tag`. 2. Link Calls to an Existing Monitored Service. For example, Link database calls (`jdbc:mysql://10.128.0.1:3306`) to an existing service like `MySQL@3306` on demo-host by referencing its service ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.manual_service_config import ManualServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)

    try:
        # All manual service configurations
        api_response = api_instance.get_all_manual_service_configs()
        print("The response of ApplicationSettingsApi->get_all_manual_service_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_all_manual_service_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ManualServiceConfig]**](ManualServiceConfig.md)

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

# **get_application_config**
> ApplicationConfig get_application_config(id)

Application configuration

Use this API endpoint if one wants to retrieve an Application Perspective with its configuration setting. This endpoint requires `canConfigureApplications` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureApplications` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Configuration of applications` to `true`.  ## Deprecated Parameters **matchSpecification:** A binary tree structure of match expression connected with binary operator AND or OR. It is replaced by **tagFilterExpression** which is also used in Application Analyze API endpoints. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_config import ApplicationConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Application configuration
        api_response = api_instance.get_application_config(id)
        print("The response of ApplicationSettingsApi->get_application_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_application_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApplicationConfig**](ApplicationConfig.md)

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

# **get_application_configs**
> List[ApplicationConfig] get_application_configs()

All Application configurations

Use this API endpoint if one wants to retrieve a list of all Application Perspectives with their configuration settings. This endpoint requires `canConfigureApplications` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureApplications` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Configuration of applications` to `true`.  ## Deprecated Parameters **matchSpecification:** A binary tree sturcture of match expression connected with binary operator AND or OR. It is replaced by **tagFilterExpression** which is also used in Application Analyze API endpoints. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_config import ApplicationConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)

    try:
        # All Application configurations
        api_response = api_instance.get_application_configs()
        print("The response of ApplicationSettingsApi->get_application_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_application_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApplicationConfig]**](ApplicationConfig.md)

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

# **get_endpoint_config**
> EndpointConfig get_endpoint_config(id)

Endpoint configuration

Use this API endpoint if one wants to retrieve the endpoint configuration of a service. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.endpoint_config import EndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Endpoint configuration
        api_response = api_instance.get_endpoint_config(id)
        print("The response of ApplicationSettingsApi->get_endpoint_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EndpointConfig**](EndpointConfig.md)

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

# **get_endpoint_configs**
> List[EndpointConfig] get_endpoint_configs()

All Endpoint configurations

Use this API endpoint if one wants to retrieve a list of all endpoint configurations. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.endpoint_config import EndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)

    try:
        # All Endpoint configurations
        api_response = api_instance.get_endpoint_configs()
        print("The response of ApplicationSettingsApi->get_endpoint_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_endpoint_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EndpointConfig]**](EndpointConfig.md)

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

# **get_http_endpoint_config**
> HttpEndpointConfig get_http_endpoint_config(id)

HTTP Endpoint configuration

This is a deprecated endpoint. Use `Endpoint configuration` instead. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.http_endpoint_config import HttpEndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # HTTP Endpoint configuration
        api_response = api_instance.get_http_endpoint_config(id)
        print("The response of ApplicationSettingsApi->get_http_endpoint_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_http_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HttpEndpointConfig**](HttpEndpointConfig.md)

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

# **get_http_endpoint_configs**
> List[HttpEndpointConfig] get_http_endpoint_configs()

All HTTP endpoint configurations

This is a deprecated endpoint. Use `All Endpoint configurations` instead. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.http_endpoint_config import HttpEndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)

    try:
        # All HTTP endpoint configurations
        api_response = api_instance.get_http_endpoint_configs()
        print("The response of ApplicationSettingsApi->get_http_endpoint_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_http_endpoint_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[HttpEndpointConfig]**](HttpEndpointConfig.md)

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

# **get_service_config**
> ServiceConfig get_service_config(id)

Service configuration

Use this API endpoint if one wants to retrieve a particular custom service rule. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_config import ServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Service configuration
        api_response = api_instance.get_service_config(id)
        print("The response of ApplicationSettingsApi->get_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ServiceConfig**](ServiceConfig.md)

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

# **get_service_configs**
> List[ServiceConfig] get_service_configs()

All service configurations

Use this API endpoint if one wants to retrive a list of all service configurations. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_config import ServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)

    try:
        # All service configurations
        api_response = api_instance.get_service_configs()
        print("The response of ApplicationSettingsApi->get_service_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->get_service_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ServiceConfig]**](ServiceConfig.md)

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

# **order_service_config**
> order_service_config(request_body)

Order of service configuration

Use this API endpoint if one wants to change the order of service configurations aka custom service rules. Note that all service configuration IDs have to be passed in the request to re-order the configurations. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    request_body = ["9uma4MhnTTSyBzwu_FKBJA","oMsVfR0fSCuTKF2TFdYRmQ"] # List[str] | 

    try:
        # Order of service configuration
        api_instance.order_service_config(request_body)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->order_service_config: %s\n" % e)
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

# **put_application_config**
> ApplicationConfig put_application_config(id, application_config)

Update application configuration

Use this API endpoint if one wants to update an existing Application Perspective. This endpoint requires `canConfigureApplications` permission. One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureApplications` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Configuration of applications` to `true`.  ## Deprecated Parameters **matchSpecification:** A binary tree sturcture of match expression connected with binary operator AND or OR. It is replaced by **tagFilterExpression** which is also used in Application Analyze API endpoints.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.application_config import ApplicationConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 
    application_config = {"accessRules":[{"accessType":"READ","relationType":"ROLE"}],"boundaryScope":"INBOUND","id":"CxJ55sRbQwqBIfw5DzpRmQ","label":"Discount Build 1","scope":"INCLUDE_NO_DOWNSTREAM","tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"kubernetes.label","stringValue":"stage=canary","numberValue":null,"booleanValue":null,"key":"stage","value":"canary","operator":"EQUALS","entity":"DESTINATION"},{"type":"TAG_FILTER","name":"kubernetes.label","stringValue":"build=6987","numberValue":null,"booleanValue":null,"key":"build","value":"6987","operator":"EQUALS","entity":"DESTINATION"},{"type":"TAG_FILTER","name":"kubernetes.label","stringValue":"app=discount","numberValue":null,"booleanValue":null,"key":"app","value":"discount","operator":"EQUALS","entity":"DESTINATION"}]}} # ApplicationConfig | 

    try:
        # Update application configuration
        api_response = api_instance.put_application_config(id, application_config)
        print("The response of ApplicationSettingsApi->put_application_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->put_application_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **application_config** | [**ApplicationConfig**](ApplicationConfig.md)|  | 

### Return type

[**ApplicationConfig**](ApplicationConfig.md)

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

# **put_service_config**
> ServiceConfig put_service_config(id, service_config)

Update service configuration

Use this API endpoint if one wants to update a particular custom service rule. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_config import ServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 
    service_config = {"comment":null,"enabled":true,"id":"9uma4MhnTTSyBzwu_FKBJA","label":"{gce.zone}-{jvm.args.abc}","matchSpecification":[{"key":"gce.zone","value":".*"},{"key":"jvm.args.abc","value":".*"}],"name":"DEF is good"} # ServiceConfig | 

    try:
        # Update service configuration
        api_response = api_instance.put_service_config(id, service_config)
        print("The response of ApplicationSettingsApi->put_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->put_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **service_config** | [**ServiceConfig**](ServiceConfig.md)|  | 

### Return type

[**ServiceConfig**](ServiceConfig.md)

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

# **replace_all**
> List[ServiceConfig] replace_all(service_config)

Replace all service configurations

Use this API endpoint if one wants to modify 1 or more existing service configuration. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_config import ServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    service_config = [{"comment":null,"enabled":true,"id":"8C-jGYx8Rsue854tzkh8KQ","label":"{docker.container.name}","matchSpecification":[{"key":"docker.container.name","value":".*"}],"name":"Rule"}] # List[ServiceConfig] | 

    try:
        # Replace all service configurations
        api_response = api_instance.replace_all(service_config)
        print("The response of ApplicationSettingsApi->replace_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->replace_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_config** | [**List[ServiceConfig]**](ServiceConfig.md)|  | 

### Return type

[**List[ServiceConfig]**](ServiceConfig.md)

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

# **replace_all_manual_service_configs**
> List[ManualServiceConfig] replace_all_manual_service_configs(new_manual_service_config)

Replace all manual service configurations

Use this API endpoint if one wants to update more than 1 manual service configurations. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`.  **This is an experimental endpoint to workaround service mapping issues.**  ### Use cases  The manual service configuration APIs enables mapping calls to services using tag filter expressions based on call tags.  There are two use cases on the usage of these APIs:  1. Map to an Unmonitored Service with a Custom Name. For example, Map HTTP calls to different Google domains (`www.ibm.com`, `www.ibm.fr`) into a single service named `IBM` using the `call.http.host tag`. 2. Link Calls to an Existing Monitored Service. For example, Link database calls (`jdbc:mysql://10.128.0.1:3306`) to an existing service like `MySQL@3306` on demo-host by referencing its service ID.  ### Important Note  1. Use `tagfilterExpression` to match calls on which the manual service configuration will be applied. **Only call tags are allowed** in the tag filter expression.  2.  Either `unmonitoredServiceName` or `existingServiceId` should be specified in a configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.manual_service_config import ManualServiceConfig
from instana_client.models.new_manual_service_config import NewManualServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    new_manual_service_config = [{"description":"Map source service","enabled":true,"existingServiceId":"c467ca0fa21477fee3cde75a140b2963307388a7","tagFilterExpression":{"type":"TAG_FILTER","name":"service.name","stringValue":"front","numberValue":null,"booleanValue":null,"key":null,"value":"front","operator":"EQUALS","entity":"SOURCE"},"unmonitoredServiceName":null}] # List[NewManualServiceConfig] | 

    try:
        # Replace all manual service configurations
        api_response = api_instance.replace_all_manual_service_configs(new_manual_service_config)
        print("The response of ApplicationSettingsApi->replace_all_manual_service_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->replace_all_manual_service_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_manual_service_config** | [**List[NewManualServiceConfig]**](NewManualServiceConfig.md)|  | 

### Return type

[**List[ManualServiceConfig]**](ManualServiceConfig.md)

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

# **update_endpoint_config**
> EndpointConfig update_endpoint_config(id, endpoint_config)

Update endpoint configuration

Use this API endpoint if one wants to update an existing endpoint configuration of a service. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.endpoint_config import EndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 
    endpoint_config = {"serviceId":"20ba31821b079e7d845a08096124880db3eeeb40","endpointNameByCollectedPathTemplateRuleEnabled":true,"endpointNameByFirstPathSegmentRuleEnabled":true,"rules":[{"enabled":true,"pathSegments":[{"name":"api","type":"FIXED"},{"name":"version","type":"PARAMETER"}],"testCases":["/api/v2/users"]}],"endpointCase":"UPPER"} # EndpointConfig | 

    try:
        # Update endpoint configuration
        api_response = api_instance.update_endpoint_config(id, endpoint_config)
        print("The response of ApplicationSettingsApi->update_endpoint_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->update_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **endpoint_config** | [**EndpointConfig**](EndpointConfig.md)|  | 

### Return type

[**EndpointConfig**](EndpointConfig.md)

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

# **update_http_endpoint_config**
> HttpEndpointConfig update_http_endpoint_config(id, http_endpoint_config)

Update HTTP endpoint configuration

This is a deprecated endpoint. Use `Update endpoint configuration` instead. This endpoint requires `CanConfigureServiceMapping` permission.   One can use `Create or update an API token` endpoint to update the permission by setting `canConfigureServiceMapping` to `true`. If one wants to enable the permission from Instana UI, go to Settings -> Security & Access -> Access Control -> API Token. There one can update the existing token or create a new token and set `Customize service rules and endpoint mapping` to `true`. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.http_endpoint_config import HttpEndpointConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 
    http_endpoint_config = {"endpointNameByCollectedPathTemplateRuleEnabled":true,"endpointNameByFirstPathSegmentRuleEnabled":true,"rules":[{"enabled":true,"pathSegments":[{"name":"api","type":"FIXED"},{"name":"version","type":"PARAMETER"},{"type":"MATCH_ALL"}],"testCases":["/api/v2/users"]}],"serviceId":"20ba31821b079e7d845a08096124880db3eeeb40"} # HttpEndpointConfig | 

    try:
        # Update HTTP endpoint configuration
        api_response = api_instance.update_http_endpoint_config(id, http_endpoint_config)
        print("The response of ApplicationSettingsApi->update_http_endpoint_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->update_http_endpoint_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **http_endpoint_config** | [**HttpEndpointConfig**](HttpEndpointConfig.md)|  | 

### Return type

[**HttpEndpointConfig**](HttpEndpointConfig.md)

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

# **update_manual_service_config**
> ManualServiceConfig update_manual_service_config(id, manual_service_config)

Update manual service configuration

Use this API endpoint if one wants to update a manual service configuration.  **This is an experimental endpoint to workaround service mapping issues.**  ### Use cases  The manual service configuration APIs enables mapping calls to services using tag filter expressions based on call tags.  There are two use cases on the usage of these APIs:  1. Map to an Unmonitored Service with a Custom Name. For example, Map HTTP calls to different Google domains (`www.ibm.com`, `www.ibm.fr`) into a single service named `IBM` using the `call.http.host tag`. 2. Link Calls to an Existing Monitored Service. For example, Link database calls (`jdbc:mysql://10.128.0.1:3306`) to an existing service like `MySQL@3306` on demo-host by referencing its service ID.  ### Important Note  1. Use `tagfilterExpression` to match calls on which the manual service configuration will be applied. **Only call tags are allowed** in the tag filter expression.  2.  Either `unmonitoredServiceName` or `existingServiceId` should be specified in a configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.manual_service_config import ManualServiceConfig
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
    api_instance = instana_client.ApplicationSettingsApi(api_client)
    id = 'id_example' # str | 
    manual_service_config = {"description":"Map source service example","enabled":true,"existingServiceId":"c467ca0fa21477fee3cde75a140b2963307388a7","id":"BDGeDcG4TRSzRkJ1mGOk-Q","tagFilterExpression":{"type":"TAG_FILTER","name":"service.name","stringValue":"front","numberValue":null,"booleanValue":null,"key":null,"value":"front","operator":"EQUALS","entity":"SOURCE"},"unmonitoredServiceName":null} # ManualServiceConfig | 

    try:
        # Update manual service configuration
        api_response = api_instance.update_manual_service_config(id, manual_service_config)
        print("The response of ApplicationSettingsApi->update_manual_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSettingsApi->update_manual_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **manual_service_config** | [**ManualServiceConfig**](ManualServiceConfig.md)|  | 

### Return type

[**ManualServiceConfig**](ManualServiceConfig.md)

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


# instana_client.EventSettingsApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_mobile_app_alert_configs**](EventSettingsApi.md#bulk_delete_mobile_app_alert_configs) | **PUT** /api/events/settings/mobile-app-alert-configs/bulk/delete | Bulk delete Mobile Smart Alert Configs
[**bulk_delete_website_alert_configs**](EventSettingsApi.md#bulk_delete_website_alert_configs) | **PUT** /api/events/settings/website-alert-configs/bulk/delete | Bulk Delete Website Smart Alert Configs
[**bulk_disable_mobile_app_alert_configs**](EventSettingsApi.md#bulk_disable_mobile_app_alert_configs) | **PUT** /api/events/settings/mobile-app-alert-configs/bulk/disable | Bulk disable Mobile Smart Alert Configs
[**bulk_disable_website_alert_configs**](EventSettingsApi.md#bulk_disable_website_alert_configs) | **PUT** /api/events/settings/website-alert-configs/bulk/disable | Bulk Disable Website Smart Alert Configs
[**bulk_enable_mobile_app_alert_configs**](EventSettingsApi.md#bulk_enable_mobile_app_alert_configs) | **PUT** /api/events/settings/mobile-app-alert-configs/bulk/enable | Bulk enable Mobile Smart Alert Configs
[**bulk_enable_website_alert_configs**](EventSettingsApi.md#bulk_enable_website_alert_configs) | **PUT** /api/events/settings/website-alert-configs/bulk/enable | Bulk Enable Website Smart Alert Configs
[**create_mobile_app_alert_config**](EventSettingsApi.md#create_mobile_app_alert_config) | **POST** /api/events/settings/mobile-app-alert-configs | Create Mobile Smart Alert Config
[**create_website_alert_config**](EventSettingsApi.md#create_website_alert_config) | **POST** /api/events/settings/website-alert-configs | Create Website Smart Alert Config
[**delete_alert**](EventSettingsApi.md#delete_alert) | **DELETE** /api/events/settings/alerts/{id} | Delete Alert Configuration
[**delete_alerting_channel**](EventSettingsApi.md#delete_alerting_channel) | **DELETE** /api/events/settings/alertingChannels/{id} | Delete Alerting Channel
[**delete_built_in_event_specification**](EventSettingsApi.md#delete_built_in_event_specification) | **DELETE** /api/events/settings/event-specifications/built-in/{eventSpecificationId} | Delete built-in event specification
[**delete_custom_event_specification**](EventSettingsApi.md#delete_custom_event_specification) | **DELETE** /api/events/settings/event-specifications/custom/{eventSpecificationId} | Delete custom event specification
[**delete_custom_payload_configuration**](EventSettingsApi.md#delete_custom_payload_configuration) | **DELETE** /api/events/settings/custom-payload-configurations | Delete Custom Payload Configuration
[**delete_mobile_app_alert_config**](EventSettingsApi.md#delete_mobile_app_alert_config) | **DELETE** /api/events/settings/mobile-app-alert-configs/{id} | Delete Mobile Smart Alert Config
[**delete_website_alert_config**](EventSettingsApi.md#delete_website_alert_config) | **DELETE** /api/events/settings/website-alert-configs/{id} | Delete Website Smart Alert Config
[**disable_built_in_event_specification**](EventSettingsApi.md#disable_built_in_event_specification) | **POST** /api/events/settings/event-specifications/built-in/{eventSpecificationId}/disable | Disable built-in event specification
[**disable_custom_event_specification**](EventSettingsApi.md#disable_custom_event_specification) | **POST** /api/events/settings/event-specifications/custom/{eventSpecificationId}/disable | Disable custom event specification
[**disable_mobile_app_alert_config**](EventSettingsApi.md#disable_mobile_app_alert_config) | **PUT** /api/events/settings/mobile-app-alert-configs/{id}/disable | Disable Mobile Smart Alert Config
[**disable_website_alert_config**](EventSettingsApi.md#disable_website_alert_config) | **PUT** /api/events/settings/website-alert-configs/{id}/disable | Disable Website Smart Alert Config
[**enable_built_in_event_specification**](EventSettingsApi.md#enable_built_in_event_specification) | **POST** /api/events/settings/event-specifications/built-in/{eventSpecificationId}/enable | Enable built-in event specification
[**enable_custom_event_specification**](EventSettingsApi.md#enable_custom_event_specification) | **POST** /api/events/settings/event-specifications/custom/{eventSpecificationId}/enable | Enable custom event specification
[**enable_mobile_app_alert_config**](EventSettingsApi.md#enable_mobile_app_alert_config) | **PUT** /api/events/settings/mobile-app-alert-configs/{id}/enable | Enable Mobile Smart Alert Config
[**enable_website_alert_config**](EventSettingsApi.md#enable_website_alert_config) | **PUT** /api/events/settings/website-alert-configs/{id}/enable | Enable Website Smart Alert Config
[**find_active_mobile_app_alert_configs**](EventSettingsApi.md#find_active_mobile_app_alert_configs) | **GET** /api/events/settings/mobile-app-alert-configs | Get all Mobile Smart Alert Configs
[**find_active_website_alert_configs**](EventSettingsApi.md#find_active_website_alert_configs) | **GET** /api/events/settings/website-alert-configs | Get all Website Smart Alert Configs
[**find_mobile_app_alert_config**](EventSettingsApi.md#find_mobile_app_alert_config) | **GET** /api/events/settings/mobile-app-alert-configs/{id} | Get Mobile Smart Alert Config
[**find_mobile_app_alert_config_versions**](EventSettingsApi.md#find_mobile_app_alert_config_versions) | **GET** /api/events/settings/mobile-app-alert-configs/{id}/versions | Get Mobile Smart Alert Config Versions
[**find_website_alert_config**](EventSettingsApi.md#find_website_alert_config) | **GET** /api/events/settings/website-alert-configs/{id} | Get Website Smart Alert Config
[**find_website_alert_config_versions**](EventSettingsApi.md#find_website_alert_config_versions) | **GET** /api/events/settings/website-alert-configs/{id}/versions | Get Website Smart Alert Config Versions. 
[**get_alert**](EventSettingsApi.md#get_alert) | **GET** /api/events/settings/alerts/{id} | Get Alert Configuration
[**get_alerting_channel**](EventSettingsApi.md#get_alerting_channel) | **GET** /api/events/settings/alertingChannels/{id} | Get Alerting Channel
[**get_alerting_channels**](EventSettingsApi.md#get_alerting_channels) | **GET** /api/events/settings/alertingChannels | Get all Alerting Channels
[**get_alerting_channels_overview**](EventSettingsApi.md#get_alerting_channels_overview) | **GET** /api/events/settings/alertingChannels/infos | Get Overview of Alerting Channels
[**get_alerting_configuration_infos**](EventSettingsApi.md#get_alerting_configuration_infos) | **GET** /api/events/settings/alerts/infos | All alerting configuration info
[**get_alerts**](EventSettingsApi.md#get_alerts) | **GET** /api/events/settings/alerts | Get all Alert Configurations
[**get_built_in_event_specification**](EventSettingsApi.md#get_built_in_event_specification) | **GET** /api/events/settings/event-specifications/built-in/{eventSpecificationId} | Built-in event specifications
[**get_built_in_event_specifications**](EventSettingsApi.md#get_built_in_event_specifications) | **GET** /api/events/settings/event-specifications/built-in | All built-in event specification
[**get_current_prefix**](EventSettingsApi.md#get_current_prefix) | **GET** /api/events/settings/shortcode/current-prefix | Get current shortcode prefix.
[**get_custom_event_specification**](EventSettingsApi.md#get_custom_event_specification) | **GET** /api/events/settings/event-specifications/custom/{eventSpecificationId} | Custom event specification
[**get_custom_event_specifications**](EventSettingsApi.md#get_custom_event_specifications) | **GET** /api/events/settings/event-specifications/custom | All custom event specifications
[**get_custom_payload_configurations**](EventSettingsApi.md#get_custom_payload_configurations) | **GET** /api/events/settings/custom-payload-configurations | Get All Global Custom Payload Configurations
[**get_custom_payload_tag_catalog**](EventSettingsApi.md#get_custom_payload_tag_catalog) | **GET** /api/events/settings/custom-payload-configurations/catalog | Get Tag Catalog for Custom Payload
[**get_event_specification_infos**](EventSettingsApi.md#get_event_specification_infos) | **GET** /api/events/settings/event-specifications/infos | Summary of all built-in and custom event specifications
[**get_event_specification_infos_by_ids**](EventSettingsApi.md#get_event_specification_infos_by_ids) | **POST** /api/events/settings/event-specifications/infos | All built-in and custom event specifications
[**get_system_rules**](EventSettingsApi.md#get_system_rules) | **GET** /api/events/settings/event-specifications/custom/systemRules | All system rules for custom event specifications
[**manually_close_event**](EventSettingsApi.md#manually_close_event) | **POST** /api/events/settings/manual-close/{eventId} | Manually close an event.
[**multi_close_event**](EventSettingsApi.md#multi_close_event) | **POST** /api/events/settings/manual-close | Manually closing multiple events
[**post_alerting_channel**](EventSettingsApi.md#post_alerting_channel) | **POST** /api/events/settings/alertingChannels | Create Alert Channel
[**post_custom_event_specification**](EventSettingsApi.md#post_custom_event_specification) | **POST** /api/events/settings/event-specifications/custom | Create new custom event specification
[**put_alert**](EventSettingsApi.md#put_alert) | **PUT** /api/events/settings/alerts/{id} | Create or update Alert Configuration
[**put_alerting_channel**](EventSettingsApi.md#put_alerting_channel) | **PUT** /api/events/settings/alertingChannels/{id} | Update Alert Channel
[**put_custom_event_specification**](EventSettingsApi.md#put_custom_event_specification) | **PUT** /api/events/settings/event-specifications/custom/{eventSpecificationId} | Create or update custom event specification
[**restore_mobile_app_alert_config**](EventSettingsApi.md#restore_mobile_app_alert_config) | **PUT** /api/events/settings/mobile-app-alert-configs/{id}/restore/{created} | Restore Mobile Smart Alert Config
[**restore_website_alert_config**](EventSettingsApi.md#restore_website_alert_config) | **PUT** /api/events/settings/website-alert-configs/{id}/restore/{created} | Restore Website Smart Alert Config
[**send_test_alerting**](EventSettingsApi.md#send_test_alerting) | **PUT** /api/events/settings/alertingChannels/test | Test Alerting Channel
[**send_test_alerting_by_id**](EventSettingsApi.md#send_test_alerting_by_id) | **POST** /api/events/settings/alertingChannels/notify/{id} | Notify manually to Alerting Channel. Requires the permission called CanConfigureIntegrations.
[**update_mobile_app_alert_config**](EventSettingsApi.md#update_mobile_app_alert_config) | **POST** /api/events/settings/mobile-app-alert-configs/{id} | Update Mobile Smart Alert Config
[**update_mobile_app_historic_baseline**](EventSettingsApi.md#update_mobile_app_historic_baseline) | **POST** /api/events/settings/mobile-app-alert-configs/{id}/update-baseline | Recalculate Mobile Smart Alert Config Baseline
[**update_prefix**](EventSettingsApi.md#update_prefix) | **PUT** /api/events/settings/shortcode/current-prefix | Update shortcode prefix.
[**update_website_alert_config**](EventSettingsApi.md#update_website_alert_config) | **POST** /api/events/settings/website-alert-configs/{id} | Update Website Smart Alert Config
[**update_website_historic_baseline**](EventSettingsApi.md#update_website_historic_baseline) | **POST** /api/events/settings/website-alert-configs/{id}/update-baseline | Recalculate Website Smart Alert Config Baseline
[**upsert_custom_payload_configuration**](EventSettingsApi.md#upsert_custom_payload_configuration) | **PUT** /api/events/settings/custom-payload-configurations | Create/Update Global Custom Payload Configuration
[**upsert_custom_payload_configuration_v2**](EventSettingsApi.md#upsert_custom_payload_configuration_v2) | **PUT** /api/events/settings/custom-payload-configurations/v2 | Create/Update Global Custom Payload Configuration


# **bulk_delete_mobile_app_alert_configs**
> bulk_delete_mobile_app_alert_configs(request_body)

Bulk delete Mobile Smart Alert Configs

Deletes multiple Mobile Smart Alert Configurations in a single request.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Bulk delete Mobile Smart Alert Configs
        api_instance.bulk_delete_mobile_app_alert_configs(request_body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->bulk_delete_mobile_app_alert_configs: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_website_alert_configs**
> bulk_delete_website_alert_configs(body)

Bulk Delete Website Smart Alert Configs

Deletes multiple website alert configurations. Creates new revisions for all specified alerts with deleted=true. All revisions share the same timestamp. Maximum 1000 IDs per request.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    body = ["alert-id-1","alert-id-2","alert-id-3"] # str | 

    try:
        # Bulk Delete Website Smart Alert Configs
        api_instance.bulk_delete_website_alert_configs(body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->bulk_delete_website_alert_configs: %s\n" % e)
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
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_mobile_app_alert_configs**
> bulk_disable_mobile_app_alert_configs(request_body)

Bulk disable Mobile Smart Alert Configs

Disables multiple Mobile Smart Alert Configurations in a single request.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Bulk disable Mobile Smart Alert Configs
        api_instance.bulk_disable_mobile_app_alert_configs(request_body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->bulk_disable_mobile_app_alert_configs: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_website_alert_configs**
> bulk_disable_website_alert_configs(body)

Bulk Disable Website Smart Alert Configs

Disables multiple website alert configurations. Creates new revisions for all specified alerts with enabled=false. All revisions share the same timestamp. Maximum 1000 IDs per request.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    body = ["alert-id-1","alert-id-2","alert-id-3"] # str | 

    try:
        # Bulk Disable Website Smart Alert Configs
        api_instance.bulk_disable_website_alert_configs(body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->bulk_disable_website_alert_configs: %s\n" % e)
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
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_mobile_app_alert_configs**
> bulk_enable_mobile_app_alert_configs(request_body)

Bulk enable Mobile Smart Alert Configs

Enables multiple Mobile Smart Alert Configurations in a single request.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Bulk enable Mobile Smart Alert Configs
        api_instance.bulk_enable_mobile_app_alert_configs(request_body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->bulk_enable_mobile_app_alert_configs: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_website_alert_configs**
> bulk_enable_website_alert_configs(body)

Bulk Enable Website Smart Alert Configs

Enables multiple website alert configurations. Creates new revisions for all specified alerts with enabled=true. All revisions share the same timestamp. Maximum 1000 IDs per request.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    body = ["alert-id-1","alert-id-2","alert-id-3"] # str | 

    try:
        # Bulk Enable Website Smart Alert Configs
        api_instance.bulk_enable_website_alert_configs(body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->bulk_enable_website_alert_configs: %s\n" % e)
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
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mobile_app_alert_config**
> WithMetaData create_mobile_app_alert_config(mobile_app_alert_config)

Create Mobile Smart Alert Config

Creates a new Mobile Smart Alert Configuration. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app_alert_config import MobileAppAlertConfig
from instana_client.models.with_meta_data import WithMetaData
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
    api_instance = instana_client.EventSettingsApi(api_client)
    mobile_app_alert_config = {"name":"HTTP Status Code(s): 5XX","description":"Occurrences of HTTP Status Code 5XX (Server Error) is above the expectation.","mobileAppId":"tk2OLeusR3aQJD5h-rBh2A","severity":5,"triggering":false,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"rule":{"alertType":"statusCode","metricName":"httpxxx","operator":"STARTS_WITH","value":"5","aggregation":"SUM"},"threshold":{"type":"staticThreshold","operator":">=","value":5.0,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"customPayloadFields":[]} # MobileAppAlertConfig | 

    try:
        # Create Mobile Smart Alert Config
        api_response = api_instance.create_mobile_app_alert_config(mobile_app_alert_config)
        print("The response of EventSettingsApi->create_mobile_app_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->create_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_alert_config** | [**MobileAppAlertConfig**](MobileAppAlertConfig.md)|  | 

### Return type

[**WithMetaData**](WithMetaData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_website_alert_config**
> WebsiteAlertConfigWithMetadata create_website_alert_config(website_alert_config)

Create Website Smart Alert Config

Creates a new Website Smart Alert Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website_alert_config import WebsiteAlertConfig
from instana_client.models.website_alert_config_with_metadata import WebsiteAlertConfigWithMetadata
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
    api_instance = instana_client.EventSettingsApi(api_client)
    website_alert_config = {"name":"onLoad Time (90th) is too high","description":"The onLoad Time (90th) is above the expectation.","websiteId":"XIZGGVT1TX2O-0OFeT2Yig","severity":5,"triggering":false,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"rule":{"alertType":"slowness","metricName":"onLoadTime","aggregation":"P90"},"threshold":{"type":"historicBaseline","operator":">=","seasonality":"DAILY","baseline":[[0,239.164,6.1026],[600000,240.0013,7.4109],[85200000,241.3653,3],[85800000,239.4759,3.9012]],"deviationFactor":3.0,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"customPayloadFields":[{"type":"staticString","key":"1","value":"2"},{"type":"dynamic","key":"2","value":{"tagName":"beacon.website.name","key":null}}]} # WebsiteAlertConfig | 

    try:
        # Create Website Smart Alert Config
        api_response = api_instance.create_website_alert_config(website_alert_config)
        print("The response of EventSettingsApi->create_website_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->create_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_alert_config** | [**WebsiteAlertConfig**](WebsiteAlertConfig.md)|  | 

### Return type

[**WebsiteAlertConfigWithMetadata**](WebsiteAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |
**428** | Baseline calculation failed due to insufficient data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> delete_alert(id)

Delete Alert Configuration

Delete a specific Alert Configuration by ID

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'hu6ynJbwgB4X1rjkkw' # str | ID of a specific Alert Configuration to delete.

    try:
        # Delete Alert Configuration
        api_instance.delete_alert(id)
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Alert Configuration to delete. | 

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alerting_channel**
> delete_alerting_channel(id)

Delete Alerting Channel

Deletes an alert channel. Requires the permission called CanConfigureIntegrations.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'YbcFlaG8k5oIkxD0' # str | ID of the Alerting Channel to delete.

    try:
        # Delete Alerting Channel
        api_instance.delete_alerting_channel(id)
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_alerting_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Alerting Channel to delete. | 

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
**204** | Successful - no content to return. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_built_in_event_specification**
> delete_built_in_event_specification(event_specification_id)

Delete built-in event specification

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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 

    try:
        # Delete built-in event specification
        api_instance.delete_built_in_event_specification(event_specification_id)
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_built_in_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_event_specification**
> delete_custom_event_specification(event_specification_id)

Delete custom event specification

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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 

    try:
        # Delete custom event specification
        api_instance.delete_custom_event_specification(event_specification_id)
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_custom_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_payload_configuration**
> delete_custom_payload_configuration()

Delete Custom Payload Configuration

Deletes a Global Custom Payload Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # Delete Custom Payload Configuration
        api_instance.delete_custom_payload_configuration()
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_custom_payload_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Successful - no content to return. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mobile_app_alert_config**
> delete_mobile_app_alert_config(id)

Delete Mobile Smart Alert Config

Deletes a Mobile Smart Alert Configuration

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to delete.

    try:
        # Delete Mobile Smart Alert Config
        api_instance.delete_mobile_app_alert_config(id)
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to delete. | 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_alert_config**
> delete_website_alert_config(id)

Delete Website Smart Alert Config

Deletes a Website Smart Alert Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to delete.

    try:
        # Delete Website Smart Alert Config
        api_instance.delete_website_alert_config(id)
    except Exception as e:
        print("Exception when calling EventSettingsApi->delete_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to delete. | 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_built_in_event_specification**
> BuiltInEventSpecificationWithLastUpdated disable_built_in_event_specification(event_specification_id, body=body)

Disable built-in event specification

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.built_in_event_specification_with_last_updated import BuiltInEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Disable built-in event specification
        api_response = api_instance.disable_built_in_event_specification(event_specification_id, body=body)
        print("The response of EventSettingsApi->disable_built_in_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->disable_built_in_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**BuiltInEventSpecificationWithLastUpdated**](BuiltInEventSpecificationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Built-in event specification not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_custom_event_specification**
> CustomEventSpecificationWithLastUpdated disable_custom_event_specification(event_specification_id, body=body)

Disable custom event specification

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Disable custom event specification
        api_response = api_instance.disable_custom_event_specification(event_specification_id, body=body)
        print("The response of EventSettingsApi->disable_custom_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->disable_custom_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**CustomEventSpecificationWithLastUpdated**](CustomEventSpecificationWithLastUpdated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The event configuration was already migrated |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Custom Event does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mobile_app_alert_config**
> disable_mobile_app_alert_config(id, body=body)

Disable Mobile Smart Alert Config

Disables a Mobile Smart Alert Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to disable.
    body = 'body_example' # str |  (optional)

    try:
        # Disable Mobile Smart Alert Config
        api_instance.disable_mobile_app_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->disable_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to disable. | 
 **body** | **str**|  | [optional] 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_website_alert_config**
> disable_website_alert_config(id, body=body)

Disable Website Smart Alert Config

Disables a Website Smart Alert Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to disable.
    body = 'body_example' # str |  (optional)

    try:
        # Disable Website Smart Alert Config
        api_instance.disable_website_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->disable_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to disable. | 
 **body** | **str**|  | [optional] 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_built_in_event_specification**
> BuiltInEventSpecificationWithLastUpdated enable_built_in_event_specification(event_specification_id, body=body)

Enable built-in event specification

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.built_in_event_specification_with_last_updated import BuiltInEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Enable built-in event specification
        api_response = api_instance.enable_built_in_event_specification(event_specification_id, body=body)
        print("The response of EventSettingsApi->enable_built_in_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->enable_built_in_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**BuiltInEventSpecificationWithLastUpdated**](BuiltInEventSpecificationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Built-in event specification not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_custom_event_specification**
> CustomEventSpecificationWithLastUpdated enable_custom_event_specification(event_specification_id, body=body)

Enable custom event specification

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Enable custom event specification
        api_response = api_instance.enable_custom_event_specification(event_specification_id, body=body)
        print("The response of EventSettingsApi->enable_custom_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->enable_custom_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**CustomEventSpecificationWithLastUpdated**](CustomEventSpecificationWithLastUpdated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The event configuration was already migrated |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Custom Event does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_mobile_app_alert_config**
> enable_mobile_app_alert_config(id, body=body)

Enable Mobile Smart Alert Config

Enables a Mobile Smart Alert Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to enable.
    body = 'body_example' # str |  (optional)

    try:
        # Enable Mobile Smart Alert Config
        api_instance.enable_mobile_app_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->enable_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to enable. | 
 **body** | **str**|  | [optional] 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_website_alert_config**
> enable_website_alert_config(id, body=body)

Enable Website Smart Alert Config

Enables a website alert configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to enable.
    body = 'body_example' # str |  (optional)

    try:
        # Enable Website Smart Alert Config
        api_instance.enable_website_alert_config(id, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->enable_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to enable. | 
 **body** | **str**|  | [optional] 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_active_mobile_app_alert_configs**
> List[MobileAppAlertConfigWithRBACTag] find_active_mobile_app_alert_configs(mobile_app_id, alert_ids=alert_ids)

Get all Mobile Smart Alert Configs

Gets all the Mobile Smart Alert Configuration pertaining to a specific mobile app.Configurations are sorted by creation date in descending order.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app_alert_config_with_rbac_tag import MobileAppAlertConfigWithRBACTag
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
    api_instance = instana_client.EventSettingsApi(api_client)
    mobile_app_id = 'tk2OLeusR3aQJD5h-rBh2A' # str | The ID of a specific Mobile Application.
    alert_ids = ['smRTFp08juKWtn8I'] # List[str] | A list of Smart Alert Configuration IDs. This allows Mobile Application Smart Alert Configuration of a specific set of Configurations. This query can be repeated to use multiple IDs. (optional)

    try:
        # Get all Mobile Smart Alert Configs
        api_response = api_instance.find_active_mobile_app_alert_configs(mobile_app_id, alert_ids=alert_ids)
        print("The response of EventSettingsApi->find_active_mobile_app_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->find_active_mobile_app_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_app_id** | **str**| The ID of a specific Mobile Application. | 
 **alert_ids** | [**List[str]**](str.md)| A list of Smart Alert Configuration IDs. This allows Mobile Application Smart Alert Configuration of a specific set of Configurations. This query can be repeated to use multiple IDs. | [optional] 

### Return type

[**List[MobileAppAlertConfigWithRBACTag]**](MobileAppAlertConfigWithRBACTag.md)

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

# **find_active_website_alert_configs**
> List[WebsiteAlertConfigWithRBACTag] find_active_website_alert_configs(website_id, alert_ids=alert_ids)

Get all Website Smart Alert Configs

Gets all the Website Smart Alert Configuration pertaining to a specific website. Configurations are sorted by creation date in descending order.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website_alert_config_with_rbac_tag import WebsiteAlertConfigWithRBACTag
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
    api_instance = instana_client.EventSettingsApi(api_client)
    website_id = 'XIZGGVT1TX2O-0OFeT2Yig' # str | The ID of a specific Website
    alert_ids = ['smRTFp08juKWtn8I'] # List[str] | A list of Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. (optional)

    try:
        # Get all Website Smart Alert Configs
        api_response = api_instance.find_active_website_alert_configs(website_id, alert_ids=alert_ids)
        print("The response of EventSettingsApi->find_active_website_alert_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->find_active_website_alert_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The ID of a specific Website | 
 **alert_ids** | [**List[str]**](str.md)| A list of Smart Alert Configuration IDs. This allows fetching of a specific set of Configurations. This query can be repeated to use multiple IDs. | [optional] 

### Return type

[**List[WebsiteAlertConfigWithRBACTag]**](WebsiteAlertConfigWithRBACTag.md)

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

# **find_mobile_app_alert_config**
> MobileAppAlertConfigWithRBACTag find_mobile_app_alert_config(id, valid_on=valid_on)

Get Mobile Smart Alert Config

Gets a specific Mobile Smart Alert Configuration. This may return a deleted Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app_alert_config_with_rbac_tag import MobileAppAlertConfigWithRBACTag
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to retrieve
    valid_on = 1722877985000 # int | A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  (optional)

    try:
        # Get Mobile Smart Alert Config
        api_response = api_instance.find_mobile_app_alert_config(id, valid_on=valid_on)
        print("The response of EventSettingsApi->find_mobile_app_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->find_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to retrieve | 
 **valid_on** | **int**| A Unix timestamp representing a specific time the Configuration was active. If no timestamp is provided, the latest active version will be retrieved.  | [optional] 

### Return type

[**MobileAppAlertConfigWithRBACTag**](MobileAppAlertConfigWithRBACTag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_mobile_app_alert_config_versions**
> List[ConfigVersion] find_mobile_app_alert_config_versions(id)

Get Mobile Smart Alert Config Versions

Gets all versions of a Mobile Smart Alert Configuration. This may return deleted Configurations. Configurations are sorted by creation date in descending order.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.config_version import ConfigVersion
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to retrieve.

    try:
        # Get Mobile Smart Alert Config Versions
        api_response = api_instance.find_mobile_app_alert_config_versions(id)
        print("The response of EventSettingsApi->find_mobile_app_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->find_mobile_app_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to retrieve. | 

### Return type

[**List[ConfigVersion]**](ConfigVersion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_website_alert_config**
> WebsiteAlertConfigWithRBACTag find_website_alert_config(id, valid_on=valid_on)

Get Website Smart Alert Config

Gets a specific Website Smart Alert Configuration. This may return a deleted Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website_alert_config_with_rbac_tag import WebsiteAlertConfigWithRBACTag
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to retrieve.
    valid_on = 1722877985000 # int | A Unix timestamp representing a specific time the config was active. If no timestamp is provided, the latest active version will be retrieved.  (optional)

    try:
        # Get Website Smart Alert Config
        api_response = api_instance.find_website_alert_config(id, valid_on=valid_on)
        print("The response of EventSettingsApi->find_website_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->find_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to retrieve. | 
 **valid_on** | **int**| A Unix timestamp representing a specific time the config was active. If no timestamp is provided, the latest active version will be retrieved.  | [optional] 

### Return type

[**WebsiteAlertConfigWithRBACTag**](WebsiteAlertConfigWithRBACTag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_website_alert_config_versions**
> List[ConfigVersion] find_website_alert_config_versions(id)

Get Website Smart Alert Config Versions. 

Gets all versions of a Website Smart Alert Configuration. This may return deleted Configurations. Configurations are sorted by creation date in descending order.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.config_version import ConfigVersion
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to retrieve.

    try:
        # Get Website Smart Alert Config Versions. 
        api_response = api_instance.find_website_alert_config_versions(id)
        print("The response of EventSettingsApi->find_website_alert_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->find_website_alert_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to retrieve. | 

### Return type

[**List[ConfigVersion]**](ConfigVersion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> AlertingConfigurationWithLastUpdated get_alert(id)

Get Alert Configuration

Get a specific Alert Configuration by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.alerting_configuration_with_last_updated import AlertingConfigurationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'iSjG7UWK3Dy6bDUc' # str | ID of a specific Alert Configuration to retrieve.

    try:
        # Get Alert Configuration
        api_response = api_instance.get_alert(id)
        print("The response of EventSettingsApi->get_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Alert Configuration to retrieve. | 

### Return type

[**AlertingConfigurationWithLastUpdated**](AlertingConfigurationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerting_channel**
> AbstractIntegration get_alerting_channel(id)

Get Alerting Channel

Gets an alerting channel. Requires the permission called CanConfigureIntegrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.abstract_integration import AbstractIntegration
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'YbcFlaG8k5oIkxD0' # str | ID of the Alerting Channel to get.

    try:
        # Get Alerting Channel
        api_response = api_instance.get_alerting_channel(id)
        print("The response of EventSettingsApi->get_alerting_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_alerting_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Alerting Channel to get. | 

### Return type

[**AbstractIntegration**](AbstractIntegration.md)

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

# **get_alerting_channels**
> List[AbstractIntegration] get_alerting_channels(ids=ids)

Get all Alerting Channels

Gets all the alerting channels. Requires the permission called CanConfigureIntegrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.abstract_integration import AbstractIntegration
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
    api_instance = instana_client.EventSettingsApi(api_client)
    ids = ['[\"YbcFlaG8k5oIkxD0\",\"OYcbU9gdP6OTBThJ\",\"qbhfsL9vTtlaBOAt\"]'] # List[str] | List of IDs of alert channels defined in Instana. Can be left empty. (optional)

    try:
        # Get all Alerting Channels
        api_response = api_instance.get_alerting_channels(ids=ids)
        print("The response of EventSettingsApi->get_alerting_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_alerting_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| List of IDs of alert channels defined in Instana. Can be left empty. | [optional] 

### Return type

[**List[AbstractIntegration]**](AbstractIntegration.md)

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

# **get_alerting_channels_overview**
> List[IntegrationOverview] get_alerting_channels_overview(ids=ids)

Get Overview of Alerting Channels

Gets the overview information of all alerting channels. Requires the permission called CanConfigureIntegrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.integration_overview import IntegrationOverview
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
    api_instance = instana_client.EventSettingsApi(api_client)
    ids = ['[\"YbcFlaG8k5oIkxD0\",\"OYcbU9gdP6OTBThJ\",\"qbhfsL9vTtlaBOAt\"]'] # List[str] | List of IDs of alert channels defined in Instana. Can be left empty. (optional)

    try:
        # Get Overview of Alerting Channels
        api_response = api_instance.get_alerting_channels_overview(ids=ids)
        print("The response of EventSettingsApi->get_alerting_channels_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_alerting_channels_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| List of IDs of alert channels defined in Instana. Can be left empty. | [optional] 

### Return type

[**List[IntegrationOverview]**](IntegrationOverview.md)

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

# **get_alerting_configuration_infos**
> List[ValidatedAlertingChannelInputInfo] get_alerting_configuration_infos(integration_id)

All alerting configuration info

Gets all alert configurations that relate to the given alert channel.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.validated_alerting_channel_input_info import ValidatedAlertingChannelInputInfo
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
    api_instance = instana_client.EventSettingsApi(api_client)
    integration_id = 'hu6ynJbwgB4X1rjk' # str | ID of a specific alert channel configuration.

    try:
        # All alerting configuration info
        api_response = api_instance.get_alerting_configuration_infos(integration_id)
        print("The response of EventSettingsApi->get_alerting_configuration_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_alerting_configuration_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| ID of a specific alert channel configuration. | 

### Return type

[**List[ValidatedAlertingChannelInputInfo]**](ValidatedAlertingChannelInputInfo.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> List[ValidatedAlertingConfiguration] get_alerts()

Get all Alert Configurations

Gets all Alert Configurations

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.validated_alerting_configuration import ValidatedAlertingConfiguration
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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # Get all Alert Configurations
        api_response = api_instance.get_alerts()
        print("The response of EventSettingsApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_alerts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ValidatedAlertingConfiguration]**](ValidatedAlertingConfiguration.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_built_in_event_specification**
> BuiltInEventSpecification get_built_in_event_specification(event_specification_id)

Built-in event specifications

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.built_in_event_specification import BuiltInEventSpecification
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 

    try:
        # Built-in event specifications
        api_response = api_instance.get_built_in_event_specification(event_specification_id)
        print("The response of EventSettingsApi->get_built_in_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_built_in_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 

### Return type

[**BuiltInEventSpecification**](BuiltInEventSpecification.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Built-in event specification not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_built_in_event_specifications**
> List[BuiltInEventSpecificationWithLastUpdated] get_built_in_event_specifications(ids=ids)

All built-in event specification

Get all built-in event specifications

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.built_in_event_specification_with_last_updated import BuiltInEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    ids = ['ids_example'] # List[str] |  (optional)

    try:
        # All built-in event specification
        api_response = api_instance.get_built_in_event_specifications(ids=ids)
        print("The response of EventSettingsApi->get_built_in_event_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_built_in_event_specifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[BuiltInEventSpecificationWithLastUpdated]**](BuiltInEventSpecificationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_prefix**
> get_current_prefix()

Get current shortcode prefix.

Returns the current shortcode prefix used for events.

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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # Get current shortcode prefix.
        api_instance.get_current_prefix()
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_current_prefix: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | The current shortcode prefix. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_event_specification**
> CustomEventSpecificationWithLastUpdated get_custom_event_specification(event_specification_id)

Custom event specification

This API helps to get the Custom Event specification for the given ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'Yojfl6Yn9SXaFhJG' # str | eventSpecificationId

    try:
        # Custom event specification
        api_response = api_instance.get_custom_event_specification(event_specification_id)
        print("The response of EventSettingsApi->get_custom_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_custom_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**| eventSpecificationId | 

### Return type

[**CustomEventSpecificationWithLastUpdated**](CustomEventSpecificationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Custom Event does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_event_specifications**
> List[CustomEventSpecificationWithLastUpdated] get_custom_event_specifications()

All custom event specifications

 This API helps in getting all the custom event specifications.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # All custom event specifications
        api_response = api_instance.get_custom_event_specifications()
        print("The response of EventSettingsApi->get_custom_event_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_custom_event_specifications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CustomEventSpecificationWithLastUpdated]**](CustomEventSpecificationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_payload_configurations**
> CustomPayloadWithVersion get_custom_payload_configurations(context=context, owner_type=owner_type)

Get All Global Custom Payload Configurations

Gets All Global Custom Payload Configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_payload_with_version import CustomPayloadWithVersion
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
    api_instance = instana_client.EventSettingsApi(api_client)
    context = ALL # str |  (optional) (default to ALL)
    owner_type = 'owner_type_example' # str |  (optional)

    try:
        # Get All Global Custom Payload Configurations
        api_response = api_instance.get_custom_payload_configurations(context=context, owner_type=owner_type)
        print("The response of EventSettingsApi->get_custom_payload_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_custom_payload_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  | [optional] [default to ALL]
 **owner_type** | **str**|  | [optional] 

### Return type

[**CustomPayloadWithVersion**](CustomPayloadWithVersion.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_payload_tag_catalog**
> TagCatalog get_custom_payload_tag_catalog()

Get Tag Catalog for Custom Payload

Custom payload tags used to filter, extract and aggregate specific data like AP calls for alert notifications. The catalog defines available tags like application.name and their types, and other attributes.

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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # Get Tag Catalog for Custom Payload
        api_response = api_instance.get_custom_payload_tag_catalog()
        print("The response of EventSettingsApi->get_custom_payload_tag_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_custom_payload_tag_catalog: %s\n" % e)
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
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_specification_infos**
> List[EventSpecificationInfo] get_event_specification_infos()

Summary of all built-in and custom event specifications

This API helps to get the summary of all build-in and custom event specifications

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_specification_info import EventSpecificationInfo
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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # Summary of all built-in and custom event specifications
        api_response = api_instance.get_event_specification_infos()
        print("The response of EventSettingsApi->get_event_specification_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_event_specification_infos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EventSpecificationInfo]**](EventSpecificationInfo.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_specification_infos_by_ids**
> List[EventSpecificationInfo] get_event_specification_infos_by_ids(request_body)

All built-in and custom event specifications

Summary of all built-in and custom event specifications by IDs

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event_specification_info import EventSpecificationInfo
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
    api_instance = instana_client.EventSettingsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # All built-in and custom event specifications
        api_response = api_instance.get_event_specification_infos_by_ids(request_body)
        print("The response of EventSettingsApi->get_event_specification_infos_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_event_specification_infos_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**List[EventSpecificationInfo]**](EventSpecificationInfo.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_rules**
> List[SystemRuleLabel] get_system_rules()

All system rules for custom event specifications

This API helps to get all the system rules for custom event specifications.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.system_rule_label import SystemRuleLabel
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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # All system rules for custom event specifications
        api_response = api_instance.get_system_rules()
        print("The response of EventSettingsApi->get_system_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->get_system_rules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SystemRuleLabel]**](SystemRuleLabel.md)

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
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manually_close_event**
> Event manually_close_event(event_id, manual_close_info)

Manually close an event.

Manually close an event (issue or incident). A close notification will be sent out and the event state will be updated accordingly.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.event import Event
from instana_client.models.manual_close_info import ManualCloseInfo
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_id = 'exampleEventId' # str | 
    manual_close_info = {"username":"user123","reasonForClosing":"Routine maintenance completed","closeTimestamp":1691505637000,"muteAlerts":true} # ManualCloseInfo | 

    try:
        # Manually close an event.
        api_response = api_instance.manually_close_event(event_id, manual_close_info)
        print("The response of EventSettingsApi->manually_close_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->manually_close_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **manual_close_info** | [**ManualCloseInfo**](ManualCloseInfo.md)|  | 

### Return type

[**Event**](Event.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The event associated with that event id was successfully closed. |  -  |
**400** | The manual close information is required. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | The event id refers to an event that is not open. |  -  |
**422** | Validation failed. The request body contains invalid or missing required fields (e.g., blank username or reasonForClosing). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multi_close_event**
> object multi_close_event(manual_close_info)

Manually closing multiple events

Manually close a set of events. A close notification will be sent out and the event state will be updated accordingly for each event

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.manual_close_info import ManualCloseInfo
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
    api_instance = instana_client.EventSettingsApi(api_client)
    manual_close_info = {"eventIds":["DPmhOKanQ3KmQCCElqOBeg","PRYfcm_7QRid9IRRhW3Y4w"],"username":"user123","reasonForClosing":"Routine maintenance completed","closeTimestamp":1691505637000,"muteAlerts":true} # ManualCloseInfo | 

    try:
        # Manually closing multiple events
        api_response = api_instance.multi_close_event(manual_close_info)
        print("The response of EventSettingsApi->multi_close_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->multi_close_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_close_info** | [**ManualCloseInfo**](ManualCloseInfo.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The multi close operation was successful |  -  |
**207** | At least one of the manual close operations failed |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**501** | The multi close feature is not enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alerting_channel**
> AbstractIntegration post_alerting_channel(abstract_integration)

Create Alert Channel

Creates an alerting channel. Requires the permission called CanConfigureIntegrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.abstract_integration import AbstractIntegration
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
    api_instance = instana_client.EventSettingsApi(api_client)
    abstract_integration = instana_client.AbstractIntegration() # AbstractIntegration | 

    try:
        # Create Alert Channel
        api_response = api_instance.post_alerting_channel(abstract_integration)
        print("The response of EventSettingsApi->post_alerting_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->post_alerting_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abstract_integration** | [**AbstractIntegration**](AbstractIntegration.md)|  | 

### Return type

[**AbstractIntegration**](AbstractIntegration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | created the alert channel setting |  -  |
**302** | Redirect to the integration service for continuing the configuration with the 3rd party system  |  -  |
**400** | Failed creating the alert channel setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_custom_event_specification**
> CustomEventSpecificationWithLastUpdated post_custom_event_specification(custom_event_specification)

Create new custom event specification

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_event_specification import CustomEventSpecification
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    custom_event_specification = instana_client.CustomEventSpecification() # CustomEventSpecification | 

    try:
        # Create new custom event specification
        api_response = api_instance.post_custom_event_specification(custom_event_specification)
        print("The response of EventSettingsApi->post_custom_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->post_custom_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_event_specification** | [**CustomEventSpecification**](CustomEventSpecification.md)|  | 

### Return type

[**CustomEventSpecificationWithLastUpdated**](CustomEventSpecificationWithLastUpdated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request: unsupported entity type or incorrect query. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alert**
> AlertingConfigurationWithLastUpdated put_alert(id, alerting_configuration)

Create or update Alert Configuration

Create or update a specific Alert configuration by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.alerting_configuration import AlertingConfiguration
from instana_client.models.alerting_configuration_with_last_updated import AlertingConfigurationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'hu6ynJbwgB4X1rjk' # str | ID of a specific Alert Configuration to create or update.
    alerting_configuration = {"id":"hu6ynJbwgB4X1rjk","alertName":"Alerts Test","muteUntil":9007199254740991,"integrationIds":["ctCR9Q373YAY27H_","wyAPFbP_xZCeEUn6","M01h5MDfb7YVQPAz","BH4nVcoPdSpJH_4U","ldF14o6dCKmQFJxP","IbQkmZ46_oUGV-L7","wpWi9SYL7cJOu_UZ","ds1Lpvix2WVoWTKg"],"eventFilteringConfiguration":{"query":null,"ruleIds":[],"eventTypes":["incident","critical"],"applicationAlertConfigIds":[],"validVersion":1},"customPayloadFields":[{"type":"staticString","key":"assignment_group","value":"ITSM App-Dev"},{"type":"staticString","key":"category","value":"Software"},{"type":"staticString","key":"change_test","value":"test kevin"},{"type":"staticString","key":"assigned_to","value":"Antony Alldis"}]} # AlertingConfiguration | 

    try:
        # Create or update Alert Configuration
        api_response = api_instance.put_alert(id, alerting_configuration)
        print("The response of EventSettingsApi->put_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->put_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Alert Configuration to create or update. | 
 **alerting_configuration** | [**AlertingConfiguration**](AlertingConfiguration.md)|  | 

### Return type

[**AlertingConfigurationWithLastUpdated**](AlertingConfigurationWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alerting_channel**
> AbstractIntegration put_alerting_channel(id, abstract_integration)

Update Alert Channel

Updates an alerting channel. Requires the permission called CanConfigureIntegrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.abstract_integration import AbstractIntegration
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'YbcFlaG8k5oIkxD0' # str | ID of the Alerting Channel to update.
    abstract_integration = instana_client.AbstractIntegration() # AbstractIntegration | 

    try:
        # Update Alert Channel
        api_response = api_instance.put_alerting_channel(id, abstract_integration)
        print("The response of EventSettingsApi->put_alerting_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->put_alerting_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Alerting Channel to update. | 
 **abstract_integration** | [**AbstractIntegration**](AbstractIntegration.md)|  | 

### Return type

[**AbstractIntegration**](AbstractIntegration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated the alert channel setting |  -  |
**302** | Redirect to the integration service for continuing the configuration with the 3rd party system  |  -  |
**400** | Failed updating the alert channel setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_custom_event_specification**
> CustomEventSpecificationWithLastUpdated put_custom_event_specification(event_specification_id, custom_event_specification, allow_restore=allow_restore)

Create or update custom event specification

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_event_specification import CustomEventSpecification
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    event_specification_id = 'event_specification_id_example' # str | 
    custom_event_specification = instana_client.CustomEventSpecification() # CustomEventSpecification | 
    allow_restore = True # bool |  (optional)

    try:
        # Create or update custom event specification
        api_response = api_instance.put_custom_event_specification(event_specification_id, custom_event_specification, allow_restore=allow_restore)
        print("The response of EventSettingsApi->put_custom_event_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->put_custom_event_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_specification_id** | **str**|  | 
 **custom_event_specification** | [**CustomEventSpecification**](CustomEventSpecification.md)|  | 
 **allow_restore** | **bool**|  | [optional] 

### Return type

[**CustomEventSpecificationWithLastUpdated**](CustomEventSpecificationWithLastUpdated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request: unsupported entity type, incorrect query, or event is deleted or migrated. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**500** | Custom event cannot be updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_mobile_app_alert_config**
> restore_mobile_app_alert_config(id, created, body=body)

Restore Mobile Smart Alert Config

Restores a Mobile Smart Alert Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to restore.
    created = 1707726529124 # int | Unix timestamp representing the creation time of a specific Mobile Smart Alert Configuration.
    body = 'body_example' # str |  (optional)

    try:
        # Restore Mobile Smart Alert Config
        api_instance.restore_mobile_app_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->restore_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to restore. | 
 **created** | **int**| Unix timestamp representing the creation time of a specific Mobile Smart Alert Configuration. | 
 **body** | **str**|  | [optional] 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_website_alert_config**
> restore_website_alert_config(id, created, body=body)

Restore Website Smart Alert Config

Restores a deleted Website Smart Alert Configuration.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to restore.
    created = 1707726529124 # int | Unix timestamp representing the creation time of a specific Website Smart Alert Configuration.
    body = 'body_example' # str |  (optional)

    try:
        # Restore Website Smart Alert Config
        api_instance.restore_website_alert_config(id, created, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->restore_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to restore. | 
 **created** | **int**| Unix timestamp representing the creation time of a specific Website Smart Alert Configuration. | 
 **body** | **str**|  | [optional] 

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
**204** | Successful - no content to return. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_alerting**
> send_test_alerting(abstract_integration)

Test Alerting Channel

Sends a test alert to an alert channel. This is for testing if an potential alert channel is able to receive alerts from Instana. Requires the permission called CanConfigureIntegrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.abstract_integration import AbstractIntegration
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
    api_instance = instana_client.EventSettingsApi(api_client)
    abstract_integration = instana_client.AbstractIntegration() # AbstractIntegration | 

    try:
        # Test Alerting Channel
        api_instance.send_test_alerting(abstract_integration)
    except Exception as e:
        print("Exception when calling EventSettingsApi->send_test_alerting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abstract_integration** | [**AbstractIntegration**](AbstractIntegration.md)|  | 

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
**200** | Test alerting channel response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_alerting_by_id**
> send_test_alerting_by_id(id, manual_alerting_channel_configuration)

Notify manually to Alerting Channel. Requires the permission called CanConfigureIntegrations.

Sends alert for a specific event to an alerting channel.  Provided the event Id, an alert could be sent to the alerting channel. This endpoint requires `canInvokeAlertChannel` permission.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.manual_alerting_channel_configuration import ManualAlertingChannelConfiguration
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'YbcFlaG8k5oIkxD0' # str | ID of the alerting channel to be notified on.
    manual_alerting_channel_configuration = instana_client.ManualAlertingChannelConfiguration() # ManualAlertingChannelConfiguration | 

    try:
        # Notify manually to Alerting Channel. Requires the permission called CanConfigureIntegrations.
        api_instance.send_test_alerting_by_id(id, manual_alerting_channel_configuration)
    except Exception as e:
        print("Exception when calling EventSettingsApi->send_test_alerting_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alerting channel to be notified on. | 
 **manual_alerting_channel_configuration** | [**ManualAlertingChannelConfiguration**](ManualAlertingChannelConfiguration.md)|  | 

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

# **update_mobile_app_alert_config**
> WithMetaData update_mobile_app_alert_config(id, mobile_app_alert_config)

Update Mobile Smart Alert Config

Updates an existing Mobile Smart Alert Configuration. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.mobile_app_alert_config import MobileAppAlertConfig
from instana_client.models.with_meta_data import WithMetaData
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to update.
    mobile_app_alert_config = {"name":"HTTP Status Code(s): 5XX","description":"Occurrences of HTTP Status Code 5XX (Server Error) is above the expectation.","mobileAppId":"tk2OLeusR3aQJD5h-rBh2A","severity":5,"triggering":false,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"rule":{"alertType":"statusCode","metricName":"httpxxx","operator":"STARTS_WITH","value":"5","aggregation":"SUM"},"threshold":{"type":"staticThreshold","operator":">=","value":5.0,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"customPayloadFields":[]} # MobileAppAlertConfig | 

    try:
        # Update Mobile Smart Alert Config
        api_response = api_instance.update_mobile_app_alert_config(id, mobile_app_alert_config)
        print("The response of EventSettingsApi->update_mobile_app_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->update_mobile_app_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to update. | 
 **mobile_app_alert_config** | [**MobileAppAlertConfig**](MobileAppAlertConfig.md)|  | 

### Return type

[**WithMetaData**](WithMetaData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | Mobile Smart Alert Configuration did not change. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mobile_app_historic_baseline**
> update_mobile_app_historic_baseline(id, body=body)

Recalculate Mobile Smart Alert Config Baseline

Recalculates and updates the historic baseline (static seasonal threshold) of a Configuration. The `LastUpdated` field of the Configuration is changed to the current time.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'qOW5jlR5TQafXKWDIceRkA' # str | ID of a specific Mobile Smart Alert Configuration to recalculate.
    body = 'body_example' # str |  (optional)

    try:
        # Recalculate Mobile Smart Alert Config Baseline
        api_instance.update_mobile_app_historic_baseline(id, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->update_mobile_app_historic_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Mobile Smart Alert Configuration to recalculate. | 
 **body** | **str**|  | [optional] 

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
**200** | Mobile Smart Alert Configuration baseline successfully recalculated and updated. |  -  |
**204** | Baseline recalculation completed with no changes needed. |  -  |
**400** | Invalid configuration type or configuration is read-only. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**428** | Baseline calculation failed due to insufficient data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prefix**
> update_prefix()

Update shortcode prefix.

Updates the shortcode prefix used for events.

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
    api_instance = instana_client.EventSettingsApi(api_client)

    try:
        # Update shortcode prefix.
        api_instance.update_prefix()
    except Exception as e:
        print("Exception when calling EventSettingsApi->update_prefix: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | The result of the update operation. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_alert_config**
> WebsiteAlertConfigWithMetadata update_website_alert_config(id, website_alert_config)

Update Website Smart Alert Config

Updates an existing Website Smart Alert Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.website_alert_config import WebsiteAlertConfig
from instana_client.models.website_alert_config_with_metadata import WebsiteAlertConfigWithMetadata
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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to update.
    website_alert_config = {"name":"onLoad Time (90th) is too high","description":"The onLoad Time (90th) is above the expectation.","websiteId":"XIZGGVT1TX2O-0OFeT2Yig","severity":5,"triggering":false,"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[]},"rule":{"alertType":"slowness","metricName":"onLoadTime","aggregation":"P90"},"threshold":{"type":"historicBaseline","operator":">=","seasonality":"DAILY","baseline":[[0,239.164,6.1026],[600000,240.0013,7.4109],[85200000,241.3653,3],[85800000,239.4759,3.9012]],"deviationFactor":3.0,"lastUpdated":0},"alertChannelIds":[],"granularity":600000,"timeThreshold":{"type":"violationsInSequence","timeWindow":600000},"customPayloadFields":[{"type":"staticString","key":"1","value":"2"},{"type":"dynamic","key":"2","value":{"tagName":"beacon.website.name","key":null}}]} # WebsiteAlertConfig | 

    try:
        # Update Website Smart Alert Config
        api_response = api_instance.update_website_alert_config(id, website_alert_config)
        print("The response of EventSettingsApi->update_website_alert_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->update_website_alert_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to update. | 
 **website_alert_config** | [**WebsiteAlertConfig**](WebsiteAlertConfig.md)|  | 

### Return type

[**WebsiteAlertConfigWithMetadata**](WebsiteAlertConfigWithMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | Successful - no content to return. |  -  |
**400** | Bad request. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**422** | Unprocessable request - missing/invalid data. |  -  |
**428** | Baseline calculation failed due to insufficient data. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_historic_baseline**
> update_website_historic_baseline(id, body=body)

Recalculate Website Smart Alert Config Baseline

Recalculates and updates the historic baseline (static seasonal threshold) of a Configuration. The `LastUpdated` field of the Configuration is changed to the current time.

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
    api_instance = instana_client.EventSettingsApi(api_client)
    id = 'G-h5p0znTHan2m2U3c-Z1Q' # str | ID of a specific Website Smart Alert Configuration to recalculate.
    body = 'body_example' # str |  (optional)

    try:
        # Recalculate Website Smart Alert Config Baseline
        api_instance.update_website_historic_baseline(id, body=body)
    except Exception as e:
        print("Exception when calling EventSettingsApi->update_website_historic_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a specific Website Smart Alert Configuration to recalculate. | 
 **body** | **str**|  | [optional] 

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
**200** | Website Smart Alert Configuration baseline successfully recalculated and updated. |  -  |
**204** | Baseline recalculation completed with no changes needed. |  -  |
**400** | Invalid configuration type or configuration is read-only. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**404** | Resource not found. |  -  |
**428** | Baseline calculation failed due to insufficient data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custom_payload_configuration**
> List[CustomPayloadWithLastUpdated] upsert_custom_payload_configuration(custom_payload_configuration)

Create/Update Global Custom Payload Configuration

Creates or Updates Global Custom Payload Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_payload_configuration import CustomPayloadConfiguration
from instana_client.models.custom_payload_with_last_updated import CustomPayloadWithLastUpdated
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
    api_instance = instana_client.EventSettingsApi(api_client)
    custom_payload_configuration = {"fields":[{"type":"staticString","key":"string","value":"customValue"},{"type":"dynamic","key":"string","value":{"tagName":"agent.zone","key":"string"}}]} # CustomPayloadConfiguration | 

    try:
        # Create/Update Global Custom Payload Configuration
        api_response = api_instance.upsert_custom_payload_configuration(custom_payload_configuration)
        print("The response of EventSettingsApi->upsert_custom_payload_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->upsert_custom_payload_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_payload_configuration** | [**CustomPayloadConfiguration**](CustomPayloadConfiguration.md)|  | 

### Return type

[**List[CustomPayloadWithLastUpdated]**](CustomPayloadWithLastUpdated.md)

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
**403** | Insufficient permissions or limited in access. |  -  |
**422** | Unable to process request, request data is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custom_payload_configuration_v2**
> List[CustomPayloadWithVersion] upsert_custom_payload_configuration_v2(custom_payload_with_version)

Create/Update Global Custom Payload Configuration

Creates or Updates Global Custom Payload Configuration.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.custom_payload_with_version import CustomPayloadWithVersion
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
    api_instance = instana_client.EventSettingsApi(api_client)
    custom_payload_with_version =       "fields":
      [
        {
            "type": "staticString",
            "key": "string",
            "value": "customValue"
        },
        {
            "type": "dynamic",
            "key": "string",
            "value": {
                "tagName": "agent.zone",
                "key": "string"
            }
        }
      ],
      "version": 1
 # CustomPayloadWithVersion | 

    try:
        # Create/Update Global Custom Payload Configuration
        api_response = api_instance.upsert_custom_payload_configuration_v2(custom_payload_with_version)
        print("The response of EventSettingsApi->upsert_custom_payload_configuration_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventSettingsApi->upsert_custom_payload_configuration_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_payload_with_version** | [**CustomPayloadWithVersion**](CustomPayloadWithVersion.md)|  | 

### Return type

[**List[CustomPayloadWithVersion]**](CustomPayloadWithVersion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized access - requires user authentication. |  -  |
**403** | Insufficient permissions or limited in access. |  -  |
**409** | Version conflict. |  -  |
**422** | Unable to process request, request data is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


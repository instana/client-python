# instana_client.AuditLogApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_logs**](AuditLogApi.md#get_access_logs) | **GET** /api/settings/accesslog | Access log
[**get_audit_logs**](AuditLogApi.md#get_audit_logs) | **GET** /api/settings/auditlog | Audit log


# **get_access_logs**
> AccessLogResponse get_access_logs(offset=offset, query=query, page_size=page_size)

Access log

Retrieve all access logs using defined query.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.access_log_response import AccessLogResponse
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
    api_instance = instana_client.AuditLogApi(api_client)
    offset = 0 # int | The offset within the result set (optional)
    query = 'username@example' # str | The query to filter the results (optional)
    page_size = 10 # int | The size of returned page (optional)

    try:
        # Access log
        api_response = api_instance.get_access_logs(offset=offset, query=query, page_size=page_size)
        print("The response of AuditLogApi->get_access_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_access_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset within the result set | [optional] 
 **query** | **str**| The query to filter the results | [optional] 
 **page_size** | **int**| The size of returned page | [optional] 

### Return type

[**AccessLogResponse**](AccessLogResponse.md)

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

# **get_audit_logs**
> AuditLogUiResponse get_audit_logs(offset=offset, query=query, page_size=page_size)

Audit log

Retrieve all audit logs using defined query.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.audit_log_ui_response import AuditLogUiResponse
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
    api_instance = instana_client.AuditLogApi(api_client)
    offset = 0 # int | The offset within the result set (optional)
    query = 'username@example.com' # str | The query to filter the results (optional)
    page_size = 10 # int | The size of returned page (optional)

    try:
        # Audit log
        api_response = api_instance.get_audit_logs(offset=offset, query=query, page_size=page_size)
        print("The response of AuditLogApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset within the result set | [optional] 
 **query** | **str**| The query to filter the results | [optional] 
 **page_size** | **int**| The size of returned page | [optional] 

### Return type

[**AuditLogUiResponse**](AuditLogUiResponse.md)

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


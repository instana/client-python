# instana_client.ApplicationTopologyApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services_map**](ApplicationTopologyApi.md#get_services_map) | **GET** /api/application-monitoring/topology/services | Gets the service topology


# **get_services_map**
> ServiceMap get_services_map(window_size=window_size, to=to, application_id=application_id, application_boundary_scope=application_boundary_scope)

Gets the service topology

Use this API endpoint if one wants to retrieve services and connections (call paths) between them for calls in the scope given by the parameters.  ## Errata:  The following fields are unsupported but documented in the schema for the result `services`: - The `applications` field is always missing and the `snapshotIds` field is always empty, despite being declared as required in the result schema. - The `maxSeverity` and `numberOfOpenIssues` fields are always missing. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.service_map import ServiceMap
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
    api_instance = instana_client.ApplicationTopologyApi(api_client)
    window_size = 56 # int | Size of time window in milliseconds (optional)
    to = 56 # int | Timestamp since Unix Epoch in milliseconds of the end of the time window (optional)
    application_id = 'application_id_example' # str | Filter by application ID (optional)
    application_boundary_scope = 'application_boundary_scope_example' # str | Filter by application scope, i.e., INBOUND or ALL. The default value is INBOUND. Applies only if application ID filter is specified. (optional)

    try:
        # Gets the service topology
        api_response = api_instance.get_services_map(window_size=window_size, to=to, application_id=application_id, application_boundary_scope=application_boundary_scope)
        print("The response of ApplicationTopologyApi->get_services_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTopologyApi->get_services_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_size** | **int**| Size of time window in milliseconds | [optional] 
 **to** | **int**| Timestamp since Unix Epoch in milliseconds of the end of the time window | [optional] 
 **application_id** | **str**| Filter by application ID | [optional] 
 **application_boundary_scope** | **str**| Filter by application scope, i.e., INBOUND or ALL. The default value is INBOUND. Applies only if application ID filter is specified. | [optional] 

### Return type

[**ServiceMap**](ServiceMap.md)

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


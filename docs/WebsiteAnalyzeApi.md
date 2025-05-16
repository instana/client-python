# instana_client.WebsiteAnalyzeApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_beacon_groups**](WebsiteAnalyzeApi.md#get_beacon_groups) | **POST** /api/website-monitoring/analyze/beacon-groups | Get grouped beacon metrics
[**get_beacons**](WebsiteAnalyzeApi.md#get_beacons) | **POST** /api/website-monitoring/analyze/beacons | Get all beacons


# **get_beacon_groups**
> WebsiteBeaconGroupsResult get_beacon_groups(fill_time_series=fill_time_series, get_website_beacon_groups=get_website_beacon_groups)

Get grouped beacon metrics

API request to get grouped website monitoring beacon metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_website_beacon_groups import GetWebsiteBeaconGroups
from instana_client.models.website_beacon_groups_result import WebsiteBeaconGroupsResult
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
    api_instance = instana_client.WebsiteAnalyzeApi(api_client)
    fill_time_series = True # bool |  (optional)
    get_website_beacon_groups = {"metrics":[{"metric":"beaconCount","aggregation":"SUM","granularity":60}],"group":{"groupByTag":"beacon.page.name"},"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"beacon.website.name","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"robot-shop"},{"type":"TAG_FILTER","name":"beacon.location.path","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"/checkout"}]},"timeFrame":{"to":null,"windowSize":3600000},"type":"PAGELOAD"} # GetWebsiteBeaconGroups |  (optional)

    try:
        # Get grouped beacon metrics
        api_response = api_instance.get_beacon_groups(fill_time_series=fill_time_series, get_website_beacon_groups=get_website_beacon_groups)
        print("The response of WebsiteAnalyzeApi->get_beacon_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteAnalyzeApi->get_beacon_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**|  | [optional] 
 **get_website_beacon_groups** | [**GetWebsiteBeaconGroups**](GetWebsiteBeaconGroups.md)|  | [optional] 

### Return type

[**WebsiteBeaconGroupsResult**](WebsiteBeaconGroupsResult.md)

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
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beacons**
> WebsiteBeaconResult get_beacons(get_website_beacons=get_website_beacons)

Get all beacons

API request to get all website monitoring beacons with matching type.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_website_beacons import GetWebsiteBeacons
from instana_client.models.website_beacon_result import WebsiteBeaconResult
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
    api_instance = instana_client.WebsiteAnalyzeApi(api_client)
    get_website_beacons = {"tagFilterExpression":{"type":"TAG_FILTER","name":"beacon.website.name","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"robot-shop"},"timeFrame":{"to":null,"windowSize":3600000},"type":"PAGELOAD"} # GetWebsiteBeacons |  (optional)

    try:
        # Get all beacons
        api_response = api_instance.get_beacons(get_website_beacons=get_website_beacons)
        print("The response of WebsiteAnalyzeApi->get_beacons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteAnalyzeApi->get_beacons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_website_beacons** | [**GetWebsiteBeacons**](GetWebsiteBeacons.md)|  | [optional] 

### Return type

[**WebsiteBeaconResult**](WebsiteBeaconResult.md)

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
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


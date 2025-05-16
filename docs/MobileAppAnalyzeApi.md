# instana_client.MobileAppAnalyzeApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mobile_app_beacon_groups**](MobileAppAnalyzeApi.md#get_mobile_app_beacon_groups) | **POST** /api/mobile-app-monitoring/analyze/beacon-groups | Get grouped beacon metrics
[**get_mobile_app_beacons**](MobileAppAnalyzeApi.md#get_mobile_app_beacons) | **POST** /api/mobile-app-monitoring/analyze/beacons | Get all beacons


# **get_mobile_app_beacon_groups**
> MobileAppBeaconGroupsResult get_mobile_app_beacon_groups(fill_time_series=fill_time_series, get_mobile_app_beacon_groups=get_mobile_app_beacon_groups)

Get grouped beacon metrics

API request to get grouped mobile app beacon metrics.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_mobile_app_beacon_groups import GetMobileAppBeaconGroups
from instana_client.models.mobile_app_beacon_groups_result import MobileAppBeaconGroupsResult
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
    api_instance = instana_client.MobileAppAnalyzeApi(api_client)
    fill_time_series = True # bool |  (optional)
    get_mobile_app_beacon_groups = {"metrics":[{"metric":"beaconCount","aggregation":"SUM","granularity":60}],"group":{"groupbyTag":"mobileBeacon.view.name"},"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"mobileBeacon.mobileApp.name","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"robot-warehouse"},{"type":"TAG_FILTER","name":"mobileBeacon.platform","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"iOS"}]},"timeFrame":{"to":null,"windowSize":3600000},"type":"SESSION_START"} # GetMobileAppBeaconGroups |  (optional)

    try:
        # Get grouped beacon metrics
        api_response = api_instance.get_mobile_app_beacon_groups(fill_time_series=fill_time_series, get_mobile_app_beacon_groups=get_mobile_app_beacon_groups)
        print("The response of MobileAppAnalyzeApi->get_mobile_app_beacon_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppAnalyzeApi->get_mobile_app_beacon_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_time_series** | **bool**|  | [optional] 
 **get_mobile_app_beacon_groups** | [**GetMobileAppBeaconGroups**](GetMobileAppBeaconGroups.md)|  | [optional] 

### Return type

[**MobileAppBeaconGroupsResult**](MobileAppBeaconGroupsResult.md)

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

# **get_mobile_app_beacons**
> MobileAppBeaconResult get_mobile_app_beacons(get_mobile_app_beacons=get_mobile_app_beacons)

Get all beacons

API request to get all mobile app beacons with matching type.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.get_mobile_app_beacons import GetMobileAppBeacons
from instana_client.models.mobile_app_beacon_result import MobileAppBeaconResult
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
    api_instance = instana_client.MobileAppAnalyzeApi(api_client)
    get_mobile_app_beacons = {"tagFilterExpression":{"entity":"NOT_APPLICABLE","name":"mobileBeacon.mobileApp.name","operator":"EQUALS","value":"robot-warehouse"},"timeFrame":{"to":null,"windowSize":60000},"type":"SESSION_START"} # GetMobileAppBeacons |  (optional)

    try:
        # Get all beacons
        api_response = api_instance.get_mobile_app_beacons(get_mobile_app_beacons=get_mobile_app_beacons)
        print("The response of MobileAppAnalyzeApi->get_mobile_app_beacons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileAppAnalyzeApi->get_mobile_app_beacons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_mobile_app_beacons** | [**GetMobileAppBeacons**](GetMobileAppBeacons.md)|  | [optional] 

### Return type

[**MobileAppBeaconResult**](MobileAppBeaconResult.md)

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


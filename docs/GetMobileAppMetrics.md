# GetMobileAppMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[MobileAppMonitoringMetricsConfiguration]**](MobileAppMonitoringMetricsConfiguration.md) |  | 
**tag_filters** | [**List[DeprecatedTagFilter]**](DeprecatedTagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.get_mobile_app_metrics import GetMobileAppMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetMobileAppMetrics from a JSON string
get_mobile_app_metrics_instance = GetMobileAppMetrics.from_json(json)
# print the JSON string representation of the object
print(GetMobileAppMetrics.to_json())

# convert the object into a dict
get_mobile_app_metrics_dict = get_mobile_app_metrics_instance.to_dict()
# create an instance of GetMobileAppMetrics from a dict
get_mobile_app_metrics_from_dict = GetMobileAppMetrics.from_dict(get_mobile_app_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



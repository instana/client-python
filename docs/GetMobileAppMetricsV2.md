# GetMobileAppMetricsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[MobileAppMonitoringMetricsConfiguration]**](MobileAppMonitoringMetricsConfiguration.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.get_mobile_app_metrics_v2 import GetMobileAppMetricsV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetMobileAppMetricsV2 from a JSON string
get_mobile_app_metrics_v2_instance = GetMobileAppMetricsV2.from_json(json)
# print the JSON string representation of the object
print(GetMobileAppMetricsV2.to_json())

# convert the object into a dict
get_mobile_app_metrics_v2_dict = get_mobile_app_metrics_v2_instance.to_dict()
# create an instance of GetMobileAppMetricsV2 from a dict
get_mobile_app_metrics_v2_from_dict = GetMobileAppMetricsV2.from_dict(get_mobile_app_metrics_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



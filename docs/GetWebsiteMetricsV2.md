# GetWebsiteMetricsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[WebsiteMonitoringMetricsConfiguration]**](WebsiteMonitoringMetricsConfiguration.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.get_website_metrics_v2 import GetWebsiteMetricsV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebsiteMetricsV2 from a JSON string
get_website_metrics_v2_instance = GetWebsiteMetricsV2.from_json(json)
# print the JSON string representation of the object
print(GetWebsiteMetricsV2.to_json())

# convert the object into a dict
get_website_metrics_v2_dict = get_website_metrics_v2_instance.to_dict()
# create an instance of GetWebsiteMetricsV2 from a dict
get_website_metrics_v2_from_dict = GetWebsiteMetricsV2.from_dict(get_website_metrics_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



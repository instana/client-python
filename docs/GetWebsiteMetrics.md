# GetWebsiteMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[WebsiteMonitoringMetricsConfiguration]**](WebsiteMonitoringMetricsConfiguration.md) |  | 
**tag_filters** | [**List[DeprecatedTagFilter]**](DeprecatedTagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.get_website_metrics import GetWebsiteMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebsiteMetrics from a JSON string
get_website_metrics_instance = GetWebsiteMetrics.from_json(json)
# print the JSON string representation of the object
print(GetWebsiteMetrics.to_json())

# convert the object into a dict
get_website_metrics_dict = get_website_metrics_instance.to_dict()
# create an instance of GetWebsiteMetrics from a dict
get_website_metrics_from_dict = GetWebsiteMetrics.from_dict(get_website_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



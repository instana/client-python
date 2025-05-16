# WebsiteMonitoringMetricsConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Set aggregation that can be applied to a series of values. Eg: &#x60;MEAN&#x60;. | 
**granularity** | **int** | If the granularity is set you will get data points with the specified granularity in seconds. Default: &#x60;1000&#x60; milliseconds | [optional] 
**metric** | **str** | Set a particular metric, eg: &#x60;latency&#x60;. | 

## Example

```python
from instana_client.models.website_monitoring_metrics_configuration import WebsiteMonitoringMetricsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteMonitoringMetricsConfiguration from a JSON string
website_monitoring_metrics_configuration_instance = WebsiteMonitoringMetricsConfiguration.from_json(json)
# print the JSON string representation of the object
print(WebsiteMonitoringMetricsConfiguration.to_json())

# convert the object into a dict
website_monitoring_metrics_configuration_dict = website_monitoring_metrics_configuration_instance.to_dict()
# create an instance of WebsiteMonitoringMetricsConfiguration from a dict
website_monitoring_metrics_configuration_from_dict = WebsiteMonitoringMetricsConfiguration.from_dict(website_monitoring_metrics_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



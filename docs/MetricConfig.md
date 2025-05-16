# MetricConfig

A list of objects each of which defines a metric and the (statistical) aggregation -- MEAN, SUM, MAX, etc -- that should be used to summarize it for the defined time frame. Eg: `[{ 'metric': 'latency', 'aggregation': 'MEAN'}]`. To know more about supported metrics and its aggregation, See `Get Metric catalog`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Set aggregation that can be applied to a series of values. Eg: &#x60;MEAN&#x60;. | 
**granularity** | **int** | If the granularity is set you will get data points with the specified granularity in seconds. Default: &#x60;1000&#x60; milliseconds | [optional] 
**metric** | **str** | Set a particular metric, eg: &#x60;latency&#x60;. | 

## Example

```python
from instana_client.models.metric_config import MetricConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MetricConfig from a JSON string
metric_config_instance = MetricConfig.from_json(json)
# print the JSON string representation of the object
print(MetricConfig.to_json())

# convert the object into a dict
metric_config_dict = metric_config_instance.to_dict()
# create an instance of MetricConfig from a dict
metric_config_from_dict = MetricConfig.from_dict(metric_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



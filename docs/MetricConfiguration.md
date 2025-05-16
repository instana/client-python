# MetricConfiguration

Details regarding the metric to be configured, including the metric name, threshold, and aggregation method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_aggregation** | **str** | Specifies the types of aggregations that can be applied to a series of values. For example, &#x60;P25&#x60; refers to the 25th percentile. Note that not all aggregation methods are available for every metric. For instance, the &#x60;Call count&#x60; metric supports only the &#x60;SUM&#x60; aggregation, whereas the &#x60;Error rate&#x60; metric only supports the &#x60;MEAN&#x60; aggregation.  | [optional] 
**metric_name** | **str** | Defines the name of the metric to be monitored. Examples include &#x60;calls&#x60; and &#x60;latency&#x60; | 
**threshold** | **float** | Specifies the threshold value for the metric being monitored | [optional] 

## Example

```python
from instana_client.models.metric_configuration import MetricConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MetricConfiguration from a JSON string
metric_configuration_instance = MetricConfiguration.from_json(json)
# print the JSON string representation of the object
print(MetricConfiguration.to_json())

# convert the object into a dict
metric_configuration_dict = metric_configuration_instance.to_dict()
# create an instance of MetricConfiguration from a dict
metric_configuration_from_dict = MetricConfiguration.from_dict(metric_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



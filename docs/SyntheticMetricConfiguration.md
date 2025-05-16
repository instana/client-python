# SyntheticMetricConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Set aggregation that can be applied to a series of values. Eg: &#x60;MEAN&#x60;. | 
**granularity** | **int** | If the granularity is set you will get data points with the specified granularity in seconds. Default: &#x60;1000&#x60; milliseconds | [optional] 
**metric** | **str** | Set a particular metric, eg: &#x60;latency&#x60;. | 

## Example

```python
from instana_client.models.synthetic_metric_configuration import SyntheticMetricConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticMetricConfiguration from a JSON string
synthetic_metric_configuration_instance = SyntheticMetricConfiguration.from_json(json)
# print the JSON string representation of the object
print(SyntheticMetricConfiguration.to_json())

# convert the object into a dict
synthetic_metric_configuration_dict = synthetic_metric_configuration_instance.to_dict()
# create an instance of SyntheticMetricConfiguration from a dict
synthetic_metric_configuration_from_dict = SyntheticMetricConfiguration.from_dict(synthetic_metric_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CustomMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Aggregation to apply on the metric for every member. | [optional] 
**category** | **str** | Category of the metric in the catalog | [optional] 
**description** | **str** | Description to be used in the catalog | [optional] 
**formatter** | **str** | | * NUMBER: Generic number * BYTES: Number of bytes * KILO_BYTES: Number of kilobytes * MEGA_BYTES: Number of megabytes * PERCENTAGE: Percentage in scale [0,1] * PERCENTAGE_100: Percentage in scale [0,100] * PERCENTAGE_NO_CAPPING: Percentage in scale [0,1] but value could exceed 1 for example when metric is aggregated * PERCENTAGE_100_NO_CAPPING: Percentage in scale [0,100] but value could exceed 100 for example when metric is aggregated * LATENCY: Time in milliseconds, with value of 0 should not be considered a a strict 0, but considered as &lt; 1ms * NANOS: Time in nanoseconds * MILLIS: Time in milliseconds * MICROS: Time in microseconds * SECONDS: Time in seconds * RATE: Number of occurrences per second * BYTE_RATE: Number of bytes per second * UNDEFINED: Metric value unit is not known  | [optional] 
**label** | **str** | Label to be used in the catalog | [optional] 
**name** | **str** | Name of the metric | [optional] 
**section** | **str** | Section of the metric in the catalog | [optional] 
**source** | **str** | Name of the source metric | [optional] 
**type** | **str** | Type of entity for the source metric | [optional] 

## Example

```python
from instana_client.models.custom_metric import CustomMetric

# TODO update the JSON string below
json = "{}"
# create an instance of CustomMetric from a JSON string
custom_metric_instance = CustomMetric.from_json(json)
# print the JSON string representation of the object
print(CustomMetric.to_json())

# convert the object into a dict
custom_metric_dict = custom_metric_instance.to_dict()
# create an instance of CustomMetric from a dict
custom_metric_from_dict = CustomMetric.from_dict(custom_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



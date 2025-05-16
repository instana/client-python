# MetricMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category of the metric | [optional] 
**cross_series_aggregations** | **List[str]** | Possible cross series aggregation the metric supports | [optional] 
**description** | **str** | Description of the metric | [optional] 
**format** | **str** | | * NUMBER: Generic number * BYTES: Number of bytes * KILO_BYTES: Number of kilobytes * MEGA_BYTES: Number of megabytes * PERCENTAGE: Percentage in scale [0,1] * PERCENTAGE_100: Percentage in scale [0,100] * PERCENTAGE_NO_CAPPING: Percentage in scale [0,1] but value could exceed 1 for example when metric is aggregated * PERCENTAGE_100_NO_CAPPING: Percentage in scale [0,100] but value could exceed 100 for example when metric is aggregated * LATENCY: Time in milliseconds, with value of 0 should not be considered a a strict 0, but considered as &lt; 1ms * NANOS: Time in nanoseconds * MILLIS: Time in milliseconds * MICROS: Time in microseconds * SECONDS: Time in seconds * RATE: Number of occurrences per second * BYTE_RATE: Number of bytes per second * UNDEFINED: Metric value unit is not known  | [optional] 
**id** | **str** | Identifier for the metric | 
**infra_tag_category** | **str** | Category of the entity | 
**label** | **str** | Label for the metric | 
**owner_type** | **str** | Type of the entity associated with the metric | 
**tags** | **List[str]** | Metric tags | [optional] 

## Example

```python
from instana_client.models.metric_metadata import MetricMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MetricMetadata from a JSON string
metric_metadata_instance = MetricMetadata.from_json(json)
# print the JSON string representation of the object
print(MetricMetadata.to_json())

# convert the object into a dict
metric_metadata_dict = metric_metadata_instance.to_dict()
# create an instance of MetricMetadata from a dict
metric_metadata_from_dict = MetricMetadata.from_dict(metric_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



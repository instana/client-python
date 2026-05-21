# MetricFieldValue

Configuration for a metric-based custom payload field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | The aggregation type to apply to the metric | 
**entity_type** | **str** | The entity type for the metric query | [optional] 
**metric_id** | **str** | The metric ID to retrieve | 
**time_window** | **object** | The time window in milliseconds for metric aggregation | [optional] 

## Example

```python
from instana_client.models.metric_field_value import MetricFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetricFieldValue from a JSON string
metric_field_value_instance = MetricFieldValue.from_json(json)
# print the JSON string representation of the object
print(MetricFieldValue.to_json())

# convert the object into a dict
metric_field_value_dict = metric_field_value_instance.to_dict()
# create an instance of MetricFieldValue from a dict
metric_field_value_from_dict = MetricFieldValue.from_dict(metric_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



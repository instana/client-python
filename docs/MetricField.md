# MetricField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**metric_id** | **str** |  | [optional] 
**time_window** | **object** |  | [optional] 
**value** | [**MetricFieldValue**](MetricFieldValue.md) |  | [optional] 

## Example

```python
from instana_client.models.metric_field import MetricField

# TODO update the JSON string below
json = "{}"
# create an instance of MetricField from a JSON string
metric_field_instance = MetricField.from_json(json)
# print the JSON string representation of the object
print(MetricField.to_json())

# convert the object into a dict
metric_field_dict = metric_field_instance.to_dict()
# create an instance of MetricField from a dict
metric_field_from_dict = MetricField.from_dict(metric_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



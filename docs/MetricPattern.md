# MetricPattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**postfix** | **str** |  | [optional] 
**prefix** | **str** |  | 

## Example

```python
from instana_client.models.metric_pattern import MetricPattern

# TODO update the JSON string below
json = "{}"
# create an instance of MetricPattern from a JSON string
metric_pattern_instance = MetricPattern.from_json(json)
# print the JSON string representation of the object
print(MetricPattern.to_json())

# convert the object into a dict
metric_pattern_dict = metric_pattern_instance.to_dict()
# create an instance of MetricPattern from a dict
metric_pattern_from_dict = MetricPattern.from_dict(metric_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



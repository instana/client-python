# ThresholdRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**condition_operator** | **str** |  | 
**condition_value** | **float** |  | [optional] 
**metric_name** | **str** |  | [optional] 
**metric_pattern** | [**MetricPattern**](MetricPattern.md) |  | [optional] 
**rollup** | **int** |  | [optional] 
**window** | **int** |  | [optional] 

## Example

```python
from instana_client.models.threshold_rule import ThresholdRule

# TODO update the JSON string below
json = "{}"
# create an instance of ThresholdRule from a JSON string
threshold_rule_instance = ThresholdRule.from_json(json)
# print the JSON string representation of the object
print(ThresholdRule.to_json())

# convert the object into a dict
threshold_rule_dict = threshold_rule_instance.to_dict()
# create an instance of ThresholdRule from a dict
threshold_rule_from_dict = ThresholdRule.from_dict(threshold_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



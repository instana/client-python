# StaticBaselineThresholdRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | **List[List[float]]** |  | [optional] 
**deviation_factor** | **float** |  | [optional] 
**seasonality** | **str** |  | 

## Example

```python
from instana_client.models.static_baseline_threshold_rule import StaticBaselineThresholdRule

# TODO update the JSON string below
json = "{}"
# create an instance of StaticBaselineThresholdRule from a JSON string
static_baseline_threshold_rule_instance = StaticBaselineThresholdRule.from_json(json)
# print the JSON string representation of the object
print(StaticBaselineThresholdRule.to_json())

# convert the object into a dict
static_baseline_threshold_rule_dict = static_baseline_threshold_rule_instance.to_dict()
# create an instance of StaticBaselineThresholdRule from a dict
static_baseline_threshold_rule_from_dict = StaticBaselineThresholdRule.from_dict(static_baseline_threshold_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



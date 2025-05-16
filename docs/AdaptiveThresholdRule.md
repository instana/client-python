# AdaptiveThresholdRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviation_factor** | **float** |  | [optional] 

## Example

```python
from instana_client.models.adaptive_threshold_rule import AdaptiveThresholdRule

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptiveThresholdRule from a JSON string
adaptive_threshold_rule_instance = AdaptiveThresholdRule.from_json(json)
# print the JSON string representation of the object
print(AdaptiveThresholdRule.to_json())

# convert the object into a dict
adaptive_threshold_rule_dict = adaptive_threshold_rule_instance.to_dict()
# create an instance of AdaptiveThresholdRule from a dict
adaptive_threshold_rule_from_dict = AdaptiveThresholdRule.from_dict(adaptive_threshold_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



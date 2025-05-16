# ThresholdConfigRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from instana_client.models.threshold_config_rule import ThresholdConfigRule

# TODO update the JSON string below
json = "{}"
# create an instance of ThresholdConfigRule from a JSON string
threshold_config_rule_instance = ThresholdConfigRule.from_json(json)
# print the JSON string representation of the object
print(ThresholdConfigRule.to_json())

# convert the object into a dict
threshold_config_rule_dict = threshold_config_rule_instance.to_dict()
# create an instance of ThresholdConfigRule from a dict
threshold_config_rule_from_dict = ThresholdConfigRule.from_dict(threshold_config_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



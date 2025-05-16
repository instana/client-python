# SyntheticCallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**match_specification** | [**MatchExpressionDTO**](MatchExpressionDTO.md) |  | 
**name** | **str** |  | 

## Example

```python
from instana_client.models.synthetic_call_rule import SyntheticCallRule

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticCallRule from a JSON string
synthetic_call_rule_instance = SyntheticCallRule.from_json(json)
# print the JSON string representation of the object
print(SyntheticCallRule.to_json())

# convert the object into a dict
synthetic_call_rule_dict = synthetic_call_rule_instance.to_dict()
# create an instance of SyntheticCallRule from a dict
synthetic_call_rule_from_dict = SyntheticCallRule.from_dict(synthetic_call_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



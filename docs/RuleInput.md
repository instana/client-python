# RuleInput

List of input rules of the Built-in Event Specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_kind** | **str** |  | 
**input_name** | **str** |  | 

## Example

```python
from instana_client.models.rule_input import RuleInput

# TODO update the JSON string below
json = "{}"
# create an instance of RuleInput from a JSON string
rule_input_instance = RuleInput.from_json(json)
# print the JSON string representation of the object
print(RuleInput.to_json())

# convert the object into a dict
rule_input_dict = rule_input_instance.to_dict()
# create an instance of RuleInput from a dict
rule_input_from_dict = RuleInput.from_dict(rule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



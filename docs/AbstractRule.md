# AbstractRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** |  | 
**severity** | **int** |  | [optional] 

## Example

```python
from instana_client.models.abstract_rule import AbstractRule

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractRule from a JSON string
abstract_rule_instance = AbstractRule.from_json(json)
# print the JSON string representation of the object
print(AbstractRule.to_json())

# convert the object into a dict
abstract_rule_dict = abstract_rule_instance.to_dict()
# create an instance of AbstractRule from a dict
abstract_rule_from_dict = AbstractRule.from_dict(abstract_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



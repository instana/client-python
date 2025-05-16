# EntityCountRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_operator** | **str** |  | 
**condition_value** | **float** |  | [optional] 

## Example

```python
from instana_client.models.entity_count_rule import EntityCountRule

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCountRule from a JSON string
entity_count_rule_instance = EntityCountRule.from_json(json)
# print the JSON string representation of the object
print(EntityCountRule.to_json())

# convert the object into a dict
entity_count_rule_dict = entity_count_rule_instance.to_dict()
# create an instance of EntityCountRule from a dict
entity_count_rule_from_dict = EntityCountRule.from_dict(entity_count_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



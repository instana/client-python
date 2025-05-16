# EntityCountVerificationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_operator** | **str** |  | 
**condition_value** | **float** |  | [optional] 
**matching_entity_label** | **str** |  | 
**matching_entity_type** | **str** |  | 
**matching_operator** | **str** |  | 

## Example

```python
from instana_client.models.entity_count_verification_rule import EntityCountVerificationRule

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCountVerificationRule from a JSON string
entity_count_verification_rule_instance = EntityCountVerificationRule.from_json(json)
# print the JSON string representation of the object
print(EntityCountVerificationRule.to_json())

# convert the object into a dict
entity_count_verification_rule_dict = entity_count_verification_rule_instance.to_dict()
# create an instance of EntityCountVerificationRule from a dict
entity_count_verification_rule_from_dict = EntityCountVerificationRule.from_dict(entity_count_verification_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EntityVerificationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matching_entity_label** | **str** |  | 
**matching_entity_type** | **str** |  | 
**matching_operator** | **str** |  | 
**offline_duration** | **int** |  | [optional] 

## Example

```python
from instana_client.models.entity_verification_rule import EntityVerificationRule

# TODO update the JSON string below
json = "{}"
# create an instance of EntityVerificationRule from a JSON string
entity_verification_rule_instance = EntityVerificationRule.from_json(json)
# print the JSON string representation of the object
print(EntityVerificationRule.to_json())

# convert the object into a dict
entity_verification_rule_dict = entity_verification_rule_instance.to_dict()
# create an instance of EntityVerificationRule from a dict
entity_verification_rule_from_dict = EntityVerificationRule.from_dict(entity_verification_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



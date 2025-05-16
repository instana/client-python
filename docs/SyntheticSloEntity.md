# SyntheticSloEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**synthetic_test_ids** | **List[str]** | List of Unique Synthetic Tests IDs  | 

## Example

```python
from instana_client.models.synthetic_slo_entity import SyntheticSloEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticSloEntity from a JSON string
synthetic_slo_entity_instance = SyntheticSloEntity.from_json(json)
# print the JSON string representation of the object
print(SyntheticSloEntity.to_json())

# convert the object into a dict
synthetic_slo_entity_dict = synthetic_slo_entity_instance.to_dict()
# create an instance of SyntheticSloEntity from a dict
synthetic_slo_entity_from_dict = SyntheticSloEntity.from_dict(synthetic_slo_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InfraSloEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infra_type** | **str** | Infrastructure Type | 

## Example

```python
from instana_client.models.infra_slo_entity import InfraSloEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InfraSloEntity from a JSON string
infra_slo_entity_instance = InfraSloEntity.from_json(json)
# print the JSON string representation of the object
print(InfraSloEntity.to_json())

# convert the object into a dict
infra_slo_entity_dict = infra_slo_entity_instance.to_dict()
# create an instance of InfraSloEntity from a dict
infra_slo_entity_from_dict = InfraSloEntity.from_dict(infra_slo_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



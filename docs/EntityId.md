# EntityId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**plugin_id** | **str** | Plugin name | 
**steady_id** | **str** | Steady identifier for the entity. | 

## Example

```python
from instana_client.models.entity_id import EntityId

# TODO update the JSON string below
json = "{}"
# create an instance of EntityId from a JSON string
entity_id_instance = EntityId.from_json(json)
# print the JSON string representation of the object
print(EntityId.to_json())

# convert the object into a dict
entity_id_dict = entity_id_instance.to_dict()
# create an instance of EntityId from a dict
entity_id_from_dict = EntityId.from_dict(entity_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



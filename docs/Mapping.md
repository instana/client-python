# Mapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | ID of role or group to be assigned if the mapping is matched. | 
**id** | **str** | ID of the current mapping. | [optional] 
**key** | **str** | Key (in the IdPs \&quot;user-profile\&quot; to be checked for mapping. | 
**team_id** | **str** | Optional, ID of team, to which the role assignment is scoped. If absent mapping is unit scoped. | [optional] 
**value** | **str** | Value (of the key in the IdPs \&quot;user-profile\&quot; to be compared for mapping. | 

## Example

```python
from instana_client.models.mapping import Mapping

# TODO update the JSON string below
json = "{}"
# create an instance of Mapping from a JSON string
mapping_instance = Mapping.from_json(json)
# print the JSON string representation of the object
print(Mapping.to_json())

# convert the object into a dict
mapping_dict = mapping_instance.to_dict()
# create an instance of Mapping from a dict
mapping_from_dict = Mapping.from_dict(mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GroupMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**id** | **str** |  | [optional] 
**key** | **str** |  | 
**team_id** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from instana_client.models.group_mapping import GroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMapping from a JSON string
group_mapping_instance = GroupMapping.from_json(json)
# print the JSON string representation of the object
print(GroupMapping.to_json())

# convert the object into a dict
group_mapping_dict = group_mapping_instance.to_dict()
# create an instance of GroupMapping from a dict
group_mapping_from_dict = GroupMapping.from_dict(group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GroupMappingOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**team** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from instana_client.models.group_mapping_overview import GroupMappingOverview

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMappingOverview from a JSON string
group_mapping_overview_instance = GroupMappingOverview.from_json(json)
# print the JSON string representation of the object
print(GroupMappingOverview.to_json())

# convert the object into a dict
group_mapping_overview_dict = group_mapping_overview_instance.to_dict()
# create an instance of GroupMappingOverview from a dict
group_mapping_overview_from_dict = GroupMappingOverview.from_dict(group_mapping_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MappingOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the current mapping. | [optional] 
**key** | **str** | Key (in the IdPs \&quot;user-profile\&quot; to be checked for mapping. | [optional] 
**role** | **str** | Name of role or group to be assigned if the mapping is matched. | [optional] 
**team** | **str** | Optional, Name of team, to which the role assignment is scoped. If absent mapping is unit scoped. | [optional] 
**value** | **str** | Value (of the key in the IdPs \&quot;user-profile\&quot; to be compared for mapping. | [optional] 

## Example

```python
from instana_client.models.mapping_overview import MappingOverview

# TODO update the JSON string below
json = "{}"
# create an instance of MappingOverview from a JSON string
mapping_overview_instance = MappingOverview.from_json(json)
# print the JSON string representation of the object
print(MappingOverview.to_json())

# convert the object into a dict
mapping_overview_dict = mapping_overview_instance.to_dict()
# create an instance of MappingOverview from a dict
mapping_overview_from_dict = MappingOverview.from_dict(mapping_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



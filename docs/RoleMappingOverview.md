# RoleMappingOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**role** | **str** |  | 
**role_id** | **str** |  | 
**team** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from instana_client.models.role_mapping_overview import RoleMappingOverview

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMappingOverview from a JSON string
role_mapping_overview_instance = RoleMappingOverview.from_json(json)
# print the JSON string representation of the object
print(RoleMappingOverview.to_json())

# convert the object into a dict
role_mapping_overview_dict = role_mapping_overview_instance.to_dict()
# create an instance of RoleMappingOverview from a dict
role_mapping_overview_from_dict = RoleMappingOverview.from_dict(role_mapping_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



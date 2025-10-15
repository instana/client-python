# SLOConfigWithRBACTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Created date of Service Levels Objective Configuration | [optional] 
**entity** | [**SloEntity**](SloEntity.md) |  | 
**id** | **str** | Service Levels Objective Configuration ID | [optional] 
**indicator** | [**ServiceLevelIndicator**](ServiceLevelIndicator.md) |  | 
**last_updated** | **datetime** | Last updated date of Service Levels Objective Configuration | [optional] 
**name** | **str** | Name of the Service Levels Objective Configuration | 
**rbac_tags** | [**List[ApiTag]**](ApiTag.md) |  | [optional] 
**tags** | **List[str]** | List of tags associated with Service Levels Objective Configuration | 
**target** | **float** | Service Levels Objective Configuration Target | 
**time_window** | [**TimeWindow**](TimeWindow.md) |  | 

## Example

```python
from instana_client.models.slo_config_with_rbac_tag import SLOConfigWithRBACTag

# TODO update the JSON string below
json = "{}"
# create an instance of SLOConfigWithRBACTag from a JSON string
slo_config_with_rbac_tag_instance = SLOConfigWithRBACTag.from_json(json)
# print the JSON string representation of the object
print(SLOConfigWithRBACTag.to_json())

# convert the object into a dict
slo_config_with_rbac_tag_dict = slo_config_with_rbac_tag_instance.to_dict()
# create an instance of SLOConfigWithRBACTag from a dict
slo_config_with_rbac_tag_from_dict = SLOConfigWithRBACTag.from_dict(slo_config_with_rbac_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



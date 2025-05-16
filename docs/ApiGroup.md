# ApiGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**members** | [**List[ApiMember]**](ApiMember.md) |  | 
**name** | **str** |  | 
**permission_set** | [**ApiPermissionSet**](ApiPermissionSet.md) |  | 

## Example

```python
from instana_client.models.api_group import ApiGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ApiGroup from a JSON string
api_group_instance = ApiGroup.from_json(json)
# print the JSON string representation of the object
print(ApiGroup.to_json())

# convert the object into a dict
api_group_dict = api_group_instance.to_dict()
# create an instance of ApiGroup from a dict
api_group_from_dict = ApiGroup.from_dict(api_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



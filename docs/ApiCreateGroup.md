# ApiCreateGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ApiMember]**](ApiMember.md) |  | 
**name** | **str** |  | 
**permission_set** | [**ApiPermissionSet**](ApiPermissionSet.md) |  | 

## Example

```python
from instana_client.models.api_create_group import ApiCreateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateGroup from a JSON string
api_create_group_instance = ApiCreateGroup.from_json(json)
# print the JSON string representation of the object
print(ApiCreateGroup.to_json())

# convert the object into a dict
api_create_group_dict = api_create_group_instance.to_dict()
# create an instance of ApiCreateGroup from a dict
api_create_group_from_dict = ApiCreateGroup.from_dict(api_create_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiCreateRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ApiMember]**](ApiMember.md) |  | [optional] 
**name** | **str** |  | 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.api_create_role import ApiCreateRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateRole from a JSON string
api_create_role_instance = ApiCreateRole.from_json(json)
# print the JSON string representation of the object
print(ApiCreateRole.to_json())

# convert the object into a dict
api_create_role_dict = api_create_role_instance.to_dict()
# create an instance of ApiCreateRole from a dict
api_create_role_from_dict = ApiCreateRole.from_dict(api_create_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



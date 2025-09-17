# ApiRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**members** | [**List[ApiMember]**](ApiMember.md) |  | 
**name** | **str** |  | 
**permissions** | **List[str]** |  | 

## Example

```python
from instana_client.models.api_role import ApiRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRole from a JSON string
api_role_instance = ApiRole.from_json(json)
# print the JSON string representation of the object
print(ApiRole.to_json())

# convert the object into a dict
api_role_dict = api_role_instance.to_dict()
# create an instance of ApiRole from a dict
api_role_from_dict = ApiRole.from_dict(api_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



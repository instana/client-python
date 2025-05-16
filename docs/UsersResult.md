# UsersResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[InvitationResult]**](InvitationResult.md) |  | [optional] 
**users** | [**List[UserResult]**](UserResult.md) |  | [optional] 

## Example

```python
from instana_client.models.users_result import UsersResult

# TODO update the JSON string below
json = "{}"
# create an instance of UsersResult from a JSON string
users_result_instance = UsersResult.from_json(json)
# print the JSON string representation of the object
print(UsersResult.to_json())

# convert the object into a dict
users_result_dict = users_result_instance.to_dict()
# create an instance of UsersResult from a dict
users_result_from_dict = UsersResult.from_dict(users_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



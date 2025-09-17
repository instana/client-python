# ApiTeamMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**roles** | [**List[ApiTeamRole]**](ApiTeamRole.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from instana_client.models.api_team_member import ApiTeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTeamMember from a JSON string
api_team_member_instance = ApiTeamMember.from_json(json)
# print the JSON string representation of the object
print(ApiTeamMember.to_json())

# convert the object into a dict
api_team_member_dict = api_team_member_instance.to_dict()
# create an instance of ApiTeamMember from a dict
api_team_member_from_dict = ApiTeamMember.from_dict(api_team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



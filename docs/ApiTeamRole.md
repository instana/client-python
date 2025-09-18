# ApiTeamRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** |  | 
**role_name** | **str** |  | [optional] 
**via_id_p** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.api_team_role import ApiTeamRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTeamRole from a JSON string
api_team_role_instance = ApiTeamRole.from_json(json)
# print the JSON string representation of the object
print(ApiTeamRole.to_json())

# convert the object into a dict
api_team_role_dict = api_team_role_instance.to_dict()
# create an instance of ApiTeamRole from a dict
api_team_role_from_dict = ApiTeamRole.from_dict(api_team_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



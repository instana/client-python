# ApiTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**info** | [**ApiTeamInfo**](ApiTeamInfo.md) |  | [optional] 
**members** | [**List[ApiTeamMember]**](ApiTeamMember.md) |  | [optional] 
**scope** | [**ApiTeamScope**](ApiTeamScope.md) |  | [optional] 
**tag** | **str** |  | 

## Example

```python
from instana_client.models.api_team import ApiTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTeam from a JSON string
api_team_instance = ApiTeam.from_json(json)
# print the JSON string representation of the object
print(ApiTeam.to_json())

# convert the object into a dict
api_team_dict = api_team_instance.to_dict()
# create an instance of ApiTeam from a dict
api_team_from_dict = ApiTeam.from_dict(api_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



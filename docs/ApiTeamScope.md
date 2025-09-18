# ApiTeamScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_permissions** | **List[str]** |  | [optional] 
**action_filter** | **str** |  | [optional] 
**applications** | **List[str]** |  | [optional] 
**business_perspectives** | **List[str]** |  | [optional] 
**infra_dfq_filter** | **str** |  | [optional] 
**kubernetes_clusters** | **List[str]** |  | [optional] 
**kubernetes_namespaces** | **List[str]** |  | [optional] 
**log_filter** | **str** |  | [optional] 
**mobile_apps** | **List[str]** |  | [optional] 
**restricted_application_filter** | [**ApiRestrictedApplicationFilter**](ApiRestrictedApplicationFilter.md) |  | [optional] 
**synthetic_credentials** | **List[str]** |  | [optional] 
**synthetic_tests** | **List[str]** |  | [optional] 
**tag_ids** | **List[str]** |  | [optional] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.api_team_scope import ApiTeamScope

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTeamScope from a JSON string
api_team_scope_instance = ApiTeamScope.from_json(json)
# print the JSON string representation of the object
print(ApiTeamScope.to_json())

# convert the object into a dict
api_team_scope_dict = api_team_scope_instance.to_dict()
# create an instance of ApiTeamScope from a dict
api_team_scope_from_dict = ApiTeamScope.from_dict(api_team_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



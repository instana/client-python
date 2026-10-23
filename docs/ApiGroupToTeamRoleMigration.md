# ApiGroupToTeamRoleMigration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_role_id** | **str** | The ID of the pre-existing role to assign to all migrated team members | 

## Example

```python
from instana_client.models.api_group_to_team_role_migration import ApiGroupToTeamRoleMigration

# TODO update the JSON string below
json = "{}"
# create an instance of ApiGroupToTeamRoleMigration from a JSON string
api_group_to_team_role_migration_instance = ApiGroupToTeamRoleMigration.from_json(json)
# print the JSON string representation of the object
print(ApiGroupToTeamRoleMigration.to_json())

# convert the object into a dict
api_group_to_team_role_migration_dict = api_group_to_team_role_migration_instance.to_dict()
# create an instance of ApiGroupToTeamRoleMigration from a dict
api_group_to_team_role_migration_from_dict = ApiGroupToTeamRoleMigration.from_dict(api_group_to_team_role_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



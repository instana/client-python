# ActionInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_description** | **str** | Action description of the action to run. | [optional] 
**action_id** | **str** | Action identifier of the action to run. | 
**action_instance_id** | **str** | Action run identifier. | [optional] [readonly] 
**action_name** | **str** | Action name of the action to run. | 
**action_snapshot** | **str** | Snapshot of the action definition. | [optional] [readonly] 
**actor_id** | **str** | User identifier, API token or the policy identifier that started the action run. | [optional] 
**actor_name** | **str** | Name of the user, API token or the policy that started the action run. | [optional] 
**actor_type** | **str** | Type of Actor. Valid values are listed in the enum definition. | [optional] 
**created_date** | **int** | Action run created timestamp. The timestamp at which the action run got submitted. | [optional] 
**end_date** | **int** | Action run end timestamp. The timestamp at which the action run ended on the agent host. | [optional] 
**error_message** | **str** | Error message, if any, of action run on the agent host. | [optional] 
**event_entity_type** | **str** | Event entity type set in the event that triggered this action run. | [optional] 
**event_id** | **str** | Event identifier of the event that triggered this action run. | [optional] 
**event_specification_id** | **str** | Event specification identifier of the event that triggered this action run. | [optional] 
**external_source_type** | **str** | If the action type is external this field contains the name of the external source. | [optional] 
**host_snapshot_id** | **str** | Host snapshot identifier of the agent on which the action ran. | [optional] 
**input_parameters** | [**List[ActionInstanceParameter]**](ActionInstanceParameter.md) | List of input parameters to this action run. | [optional] 
**metadata** | [**List[ActionInstanceMetadataEntry]**](ActionInstanceMetadataEntry.md) | List of metadata parameters set to this action run by sensors. | [optional] 
**output** | **str** | Action run output. | [optional] 
**policy_id** | **str** | Identifier of the policy that triggered this action run. | [optional] 
**problem_text** | **str** | Event problem text of the event that triggered this action run. | [optional] 
**return_code** | **int** | Return code of action run on the agent host. | [optional] 
**start_date** | **int** | Action run start timestamp. The timestamp at which the action run started on the agent host. | [optional] 
**status** | **str** | Action run status. Valid values are listed in the enum definition. | [optional] 
**target_snapshot_id** | **str** | Action target entity identifier set in the event that triggered this action run. This is the identifier of the entity on which an incident or issue was raised. | [optional] 
**type** | **str** | Action type. Valid values are listed in the enum definition. | 

## Example

```python
from instana_client.models.action_instance import ActionInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInstance from a JSON string
action_instance_instance = ActionInstance.from_json(json)
# print the JSON string representation of the object
print(ActionInstance.to_json())

# convert the object into a dict
action_instance_dict = action_instance_instance.to_dict()
# create an instance of ActionInstance from a dict
action_instance_from_dict = ActionInstance.from_dict(action_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



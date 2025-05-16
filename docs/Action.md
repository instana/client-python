# Action

Automation action definition. When this is used in policy creation request, only `id` should be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Action created time. | 
**description** | **str** | Action description. | [optional] 
**fields** | [**List[ModelField]**](ModelField.md) | List of fields that describe an action. | [optional] 
**id** | **str** | Action identifier. | 
**input_parameters** | [**List[Parameter]**](Parameter.md) | List of inputs to the action. | [optional] 
**metadata** | [**MetaData**](MetaData.md) |  | [optional] 
**modified_at** | **datetime** | Action modified time. | 
**name** | **str** | Action name. | 
**tags** | **List[str]** | List of tags added to the action. | [optional] 
**type** | **str** | Action type can be one of the following values:  SCRIPT, HTTP, ANSIBLE, EXTERNAL, GITHUB, GITLAB, JIRA, MANUAL, DOC_LINK | 

## Example

```python
from instana_client.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



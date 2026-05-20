# AgentModeUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_mode** | **str** |  | 
**mode_as_integer** | **int** |  | [optional] 

## Example

```python
from instana_client.models.agent_mode_update import AgentModeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentModeUpdate from a JSON string
agent_mode_update_instance = AgentModeUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentModeUpdate.to_json())

# convert the object into a dict
agent_mode_update_dict = agent_mode_update_instance.to_dict()
# create an instance of AgentModeUpdate from a dict
agent_mode_update_from_dict = AgentModeUpdate.from_dict(agent_mode_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



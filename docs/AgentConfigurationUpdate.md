# AgentConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_branch** | **str** |  | [optional] 
**remote_name** | **str** |  | [optional] 
**remote_uri** | **str** |  | [optional] 

## Example

```python
from instana_client.models.agent_configuration_update import AgentConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConfigurationUpdate from a JSON string
agent_configuration_update_instance = AgentConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentConfigurationUpdate.to_json())

# convert the object into a dict
agent_configuration_update_dict = agent_configuration_update_instance.to_dict()
# create an instance of AgentConfigurationUpdate from a dict
agent_configuration_update_from_dict = AgentConfigurationUpdate.from_dict(agent_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



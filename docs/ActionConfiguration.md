# ActionConfiguration

List of action configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | 
**agent_id** | **str** | Identifier of the agent host on which to run the action. | [optional] 
**input_parameter_values** | [**List[ParameterValue]**](ParameterValue.md) | List of action input parameters. | [optional] 

## Example

```python
from instana_client.models.action_configuration import ActionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ActionConfiguration from a JSON string
action_configuration_instance = ActionConfiguration.from_json(json)
# print the JSON string representation of the object
print(ActionConfiguration.to_json())

# convert the object into a dict
action_configuration_dict = action_configuration_instance.to_dict()
# create an instance of ActionConfiguration from a dict
action_configuration_from_dict = ActionConfiguration.from_dict(action_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



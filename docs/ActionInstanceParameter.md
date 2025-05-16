# ActionInstanceParameter

List of input parameters to this action run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Parameter display name. | 
**name** | **str** | Parameter name. | 
**type** | **str** | Parameter type. Valid values are &#x60;static&#x60;, &#x60;dynamic&#x60; or &#x60;vault&#x60; | [optional] 
**value** | **str** | Parameter value. | [optional] 

## Example

```python
from instana_client.models.action_instance_parameter import ActionInstanceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInstanceParameter from a JSON string
action_instance_parameter_instance = ActionInstanceParameter.from_json(json)
# print the JSON string representation of the object
print(ActionInstanceParameter.to_json())

# convert the object into a dict
action_instance_parameter_dict = action_instance_parameter_instance.to_dict()
# create an instance of ActionInstanceParameter from a dict
action_instance_parameter_from_dict = ActionInstanceParameter.from_dict(action_instance_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



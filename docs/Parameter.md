# Parameter

List of inputs to the action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Parameter description. | [optional] 
**hidden** | **bool** | Is parameter hidden or not. | [optional] 
**label** | **str** | Parameter label. | 
**name** | **str** | Parameter name. | 
**required** | **bool** | Is parameter required or not. | [optional] 
**secured** | **bool** | Is parameter secured or not. | [optional] 
**type** | **str** | Parameter type. Valid values are &#x60;static&#x60;, &#x60;dynamic&#x60;, or &#x60;vault&#x60;. Default value is &#x60;static&#x60; | 
**value** | **str** | Parameter value. | [optional] 

## Example

```python
from instana_client.models.parameter import Parameter

# TODO update the JSON string below
json = "{}"
# create an instance of Parameter from a JSON string
parameter_instance = Parameter.from_json(json)
# print the JSON string representation of the object
print(Parameter.to_json())

# convert the object into a dict
parameter_dict = parameter_instance.to_dict()
# create an instance of Parameter from a dict
parameter_from_dict = Parameter.from_dict(parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



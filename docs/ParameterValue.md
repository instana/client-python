# ParameterValue

List of action input parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name. | 
**value** | **str** | Parameter value. | 

## Example

```python
from instana_client.models.parameter_value import ParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterValue from a JSON string
parameter_value_instance = ParameterValue.from_json(json)
# print the JSON string representation of the object
print(ParameterValue.to_json())

# convert the object into a dict
parameter_value_dict = parameter_value_instance.to_dict()
# create an instance of ParameterValue from a dict
parameter_value_from_dict = ParameterValue.from_dict(parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



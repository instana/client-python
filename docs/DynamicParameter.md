# DynamicParameter

List of dynamic parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Parameter key | [optional] 
**name** | **str** | Parameter name | [optional] 
**resolved_value** | **str** | Parameter value after resolution | [optional] 
**tag_name** | **str** | The name of the tag. Eg: &#x60;call.name&#x60; | [optional] 

## Example

```python
from instana_client.models.dynamic_parameter import DynamicParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicParameter from a JSON string
dynamic_parameter_instance = DynamicParameter.from_json(json)
# print the JSON string representation of the object
print(DynamicParameter.to_json())

# convert the object into a dict
dynamic_parameter_dict = dynamic_parameter_instance.to_dict()
# create an instance of DynamicParameter from a dict
dynamic_parameter_from_dict = DynamicParameter.from_dict(dynamic_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



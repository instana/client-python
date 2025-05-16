# GetDynamicParameterValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event identifier | 
**parameters** | [**List[DynamicParameter]**](DynamicParameter.md) | List of dynamic parameters | 
**timestamp** | **int** | The start of the timestamp expressed in Unix epoch time in milliseconds. | 

## Example

```python
from instana_client.models.get_dynamic_parameter_values import GetDynamicParameterValues

# TODO update the JSON string below
json = "{}"
# create an instance of GetDynamicParameterValues from a JSON string
get_dynamic_parameter_values_instance = GetDynamicParameterValues.from_json(json)
# print the JSON string representation of the object
print(GetDynamicParameterValues.to_json())

# convert the object into a dict
get_dynamic_parameter_values_dict = get_dynamic_parameter_values_instance.to_dict()
# create an instance of GetDynamicParameterValues from a dict
get_dynamic_parameter_values_from_dict = GetDynamicParameterValues.from_dict(get_dynamic_parameter_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DynamicField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DynamicFieldValue**](DynamicFieldValue.md) |  | 

## Example

```python
from instana_client.models.dynamic_field import DynamicField

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicField from a JSON string
dynamic_field_instance = DynamicField.from_json(json)
# print the JSON string representation of the object
print(DynamicField.to_json())

# convert the object into a dict
dynamic_field_dict = dynamic_field_instance.to_dict()
# create an instance of DynamicField from a dict
dynamic_field_from_dict = DynamicField.from_dict(dynamic_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



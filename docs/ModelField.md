# ModelField

List of fields that describe an action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**encoding** | **str** |  | 
**name** | **str** |  | 
**secured** | **bool** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from instana_client.models.model_field import ModelField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelField from a JSON string
model_field_instance = ModelField.from_json(json)
# print the JSON string representation of the object
print(ModelField.to_json())

# convert the object into a dict
model_field_dict = model_field_instance.to_dict()
# create an instance of ModelField from a dict
model_field_from_dict = ModelField.from_dict(model_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



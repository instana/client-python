# DynamicFieldValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key for selected dynamic tag: specifies which dictionary style value user is interested in. | [optional] 
**tag_name** | **str** | Each dynamic payload entry is associated with tag from Instana&#39;s tag catalog | 

## Example

```python
from instana_client.models.dynamic_field_value import DynamicFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicFieldValue from a JSON string
dynamic_field_value_instance = DynamicFieldValue.from_json(json)
# print the JSON string representation of the object
print(DynamicFieldValue.to_json())

# convert the object into a dict
dynamic_field_value_dict = dynamic_field_value_instance.to_dict()
# create an instance of DynamicFieldValue from a dict
dynamic_field_value_from_dict = DynamicFieldValue.from_dict(dynamic_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



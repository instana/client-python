# StaticStringField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Custom value for static type custom payload | 

## Example

```python
from instana_client.models.static_string_field import StaticStringField

# TODO update the JSON string below
json = "{}"
# create an instance of StaticStringField from a JSON string
static_string_field_instance = StaticStringField.from_json(json)
# print the JSON string representation of the object
print(StaticStringField.to_json())

# convert the object into a dict
static_string_field_dict = static_string_field_instance.to_dict()
# create an instance of StaticStringField from a dict
static_string_field_from_dict = StaticStringField.from_dict(static_string_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CustomPayloadField

Custom payload fields to send additional information in the alert notifications. Can be left empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A user-specified unique identifier or name for a custom payload entry. | 
**type** | **str** |  | 

## Example

```python
from instana_client.models.custom_payload_field import CustomPayloadField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPayloadField from a JSON string
custom_payload_field_instance = CustomPayloadField.from_json(json)
# print the JSON string representation of the object
print(CustomPayloadField.to_json())

# convert the object into a dict
custom_payload_field_dict = custom_payload_field_instance.to_dict()
# create an instance of CustomPayloadField from a dict
custom_payload_field_from_dict = CustomPayloadField.from_dict(custom_payload_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



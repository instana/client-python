# CustomPayloadConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Required parameters for custom payload configuration. | 

## Example

```python
from instana_client.models.custom_payload_configuration import CustomPayloadConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPayloadConfiguration from a JSON string
custom_payload_configuration_instance = CustomPayloadConfiguration.from_json(json)
# print the JSON string representation of the object
print(CustomPayloadConfiguration.to_json())

# convert the object into a dict
custom_payload_configuration_dict = custom_payload_configuration_instance.to_dict()
# create an instance of CustomPayloadConfiguration from a dict
custom_payload_configuration_from_dict = CustomPayloadConfiguration.from_dict(custom_payload_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



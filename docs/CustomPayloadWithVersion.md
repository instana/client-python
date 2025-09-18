# CustomPayloadWithVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Required parameters for custom payload configuration. | 
**last_updated** | **int** | Unix timestamp representing the time (in milliseconds) the configuration was last updated. | [optional] 
**version** | **int** | Global custom payloads version. | 

## Example

```python
from instana_client.models.custom_payload_with_version import CustomPayloadWithVersion

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPayloadWithVersion from a JSON string
custom_payload_with_version_instance = CustomPayloadWithVersion.from_json(json)
# print the JSON string representation of the object
print(CustomPayloadWithVersion.to_json())

# convert the object into a dict
custom_payload_with_version_dict = custom_payload_with_version_instance.to_dict()
# create an instance of CustomPayloadWithVersion from a dict
custom_payload_with_version_from_dict = CustomPayloadWithVersion.from_dict(custom_payload_with_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



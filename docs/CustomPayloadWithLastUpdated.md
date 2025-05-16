# CustomPayloadWithLastUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Required parameters for custom payload configuration. | 
**last_updated** | **int** | Unix timestamp representing the time (in milliseconds) the configuration was last updated. | [optional] 

## Example

```python
from instana_client.models.custom_payload_with_last_updated import CustomPayloadWithLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPayloadWithLastUpdated from a JSON string
custom_payload_with_last_updated_instance = CustomPayloadWithLastUpdated.from_json(json)
# print the JSON string representation of the object
print(CustomPayloadWithLastUpdated.to_json())

# convert the object into a dict
custom_payload_with_last_updated_dict = custom_payload_with_last_updated_instance.to_dict()
# create an instance of CustomPayloadWithLastUpdated from a dict
custom_payload_with_last_updated_from_dict = CustomPayloadWithLastUpdated.from_dict(custom_payload_with_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



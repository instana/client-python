# GetPayloadKeysResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_keys** | **List[str]** | Keys that can be used to retrieve plugin payloads. | [optional] 

## Example

```python
from instana_client.models.get_payload_keys_result import GetPayloadKeysResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayloadKeysResult from a JSON string
get_payload_keys_result_instance = GetPayloadKeysResult.from_json(json)
# print the JSON string representation of the object
print(GetPayloadKeysResult.to_json())

# convert the object into a dict
get_payload_keys_result_dict = get_payload_keys_result_instance.to_dict()
# create an instance of GetPayloadKeysResult from a dict
get_payload_keys_result_from_dict = GetPayloadKeysResult.from_dict(get_payload_keys_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



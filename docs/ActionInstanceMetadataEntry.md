# ActionInstanceMetadataEntry

List of metadata parameters set to this action run by sensors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Metadata name. | 
**value** | **str** | Metadata value. | [optional] 

## Example

```python
from instana_client.models.action_instance_metadata_entry import ActionInstanceMetadataEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInstanceMetadataEntry from a JSON string
action_instance_metadata_entry_instance = ActionInstanceMetadataEntry.from_json(json)
# print the JSON string representation of the object
print(ActionInstanceMetadataEntry.to_json())

# convert the object into a dict
action_instance_metadata_entry_dict = action_instance_metadata_entry_instance.to_dict()
# create an instance of ActionInstanceMetadataEntry from a dict
action_instance_metadata_entry_from_dict = ActionInstanceMetadataEntry.from_dict(action_instance_metadata_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



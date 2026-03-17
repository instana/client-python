# SessionReplayMetadata

List of session replay metadata records

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_ingested_image** | **int** | Size of the image in bytes | 
**id** | **str** | Unique identifier for the metadata record | 
**image_data** | **str** | Base64-encoded image data loaded from external storage | [optional] 
**image_format** | **str** | Image format | 
**session_id** | **str** | Session identifier | 
**timestamp** | **int** | Timestamp when the record was captured (epoch milliseconds) | 
**type** | **str** | Type of record | 

## Example

```python
from instana_client.models.session_replay_metadata import SessionReplayMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SessionReplayMetadata from a JSON string
session_replay_metadata_instance = SessionReplayMetadata.from_json(json)
# print the JSON string representation of the object
print(SessionReplayMetadata.to_json())

# convert the object into a dict
session_replay_metadata_dict = session_replay_metadata_instance.to_dict()
# create an instance of SessionReplayMetadata from a dict
session_replay_metadata_from_dict = SessionReplayMetadata.from_dict(session_replay_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



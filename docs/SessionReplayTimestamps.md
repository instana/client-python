# SessionReplayTimestamps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_image_timestamp** | **int** | Timestamp of the first image in the session (epoch milliseconds). Null if no images exist. | [optional] 
**last_image_timestamp** | **int** | Timestamp of the last image in the session (epoch milliseconds). Null if no images exist. | [optional] 

## Example

```python
from instana_client.models.session_replay_timestamps import SessionReplayTimestamps

# TODO update the JSON string below
json = "{}"
# create an instance of SessionReplayTimestamps from a JSON string
session_replay_timestamps_instance = SessionReplayTimestamps.from_json(json)
# print the JSON string representation of the object
print(SessionReplayTimestamps.to_json())

# convert the object into a dict
session_replay_timestamps_dict = session_replay_timestamps_instance.to_dict()
# create an instance of SessionReplayTimestamps from a dict
session_replay_timestamps_from_dict = SessionReplayTimestamps.from_dict(session_replay_timestamps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



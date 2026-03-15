# GetSessionReplayMetadataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Whether there are more records to fetch beyond this page | 
**metadata** | [**List[SessionReplayMetadata]**](SessionReplayMetadata.md) | List of session replay metadata records | 
**next_cursor** | **int** | Cursor for the next page (timestamp of last record) | [optional] 

## Example

```python
from instana_client.models.get_session_replay_metadata_result import GetSessionReplayMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetSessionReplayMetadataResult from a JSON string
get_session_replay_metadata_result_instance = GetSessionReplayMetadataResult.from_json(json)
# print the JSON string representation of the object
print(GetSessionReplayMetadataResult.to_json())

# convert the object into a dict
get_session_replay_metadata_result_dict = get_session_replay_metadata_result_instance.to_dict()
# create an instance of GetSessionReplayMetadataResult from a dict
get_session_replay_metadata_result_from_dict = GetSessionReplayMetadataResult.from_dict(get_session_replay_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



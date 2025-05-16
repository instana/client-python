# PostSnapshotsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SnapshotItem]**](SnapshotItem.md) | Detail information for requested snapshots. | [optional] 
**not_found_snapshots_ids** | **List[str]** | Snapshot ids for snapshots that could not be retrieved. | [optional] 

## Example

```python
from instana_client.models.post_snapshots_result import PostSnapshotsResult

# TODO update the JSON string below
json = "{}"
# create an instance of PostSnapshotsResult from a JSON string
post_snapshots_result_instance = PostSnapshotsResult.from_json(json)
# print the JSON string representation of the object
print(PostSnapshotsResult.to_json())

# convert the object into a dict
post_snapshots_result_dict = post_snapshots_result_instance.to_dict()
# create an instance of PostSnapshotsResult from a dict
post_snapshots_result_from_dict = PostSnapshotsResult.from_dict(post_snapshots_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



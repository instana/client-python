# GetSnapshotsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_ids** | **List[str]** | List of one or more snapshot ids. | 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_snapshots_query import GetSnapshotsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetSnapshotsQuery from a JSON string
get_snapshots_query_instance = GetSnapshotsQuery.from_json(json)
# print the JSON string representation of the object
print(GetSnapshotsQuery.to_json())

# convert the object into a dict
get_snapshots_query_dict = get_snapshots_query_instance.to_dict()
# create an instance of GetSnapshotsQuery from a dict
get_snapshots_query_from_dict = GetSnapshotsQuery.from_dict(get_snapshots_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



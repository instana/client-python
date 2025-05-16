# SnapshotResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SnapshotItem]**](SnapshotItem.md) |  | [optional] 

## Example

```python
from instana_client.models.snapshot_result import SnapshotResult

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResult from a JSON string
snapshot_result_instance = SnapshotResult.from_json(json)
# print the JSON string representation of the object
print(SnapshotResult.to_json())

# convert the object into a dict
snapshot_result_dict = snapshot_result_instance.to_dict()
# create an instance of SnapshotResult from a dict
snapshot_result_from_dict = SnapshotResult.from_dict(snapshot_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



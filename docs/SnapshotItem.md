# SnapshotItem

Detail information for requested snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**var_from** | **int** | Start of timeframe expressed as the Unix epoch time in milliseconds | [optional] 
**host** | **str** | Host name | [optional] 
**label** | **str** | Friendly label for the entity | [optional] 
**plugin** | **str** | Plugin name | [optional] 
**snapshot_id** | **str** | Snapshot ID | [optional] 
**tags** | **List[str]** | Tags which can be used to search for this entity | [optional] 
**to** | **int** | End of timeframe expressed as the Unix epoch time in milliseconds | [optional] 

## Example

```python
from instana_client.models.snapshot_item import SnapshotItem

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotItem from a JSON string
snapshot_item_instance = SnapshotItem.from_json(json)
# print the JSON string representation of the object
print(SnapshotItem.to_json())

# convert the object into a dict
snapshot_item_dict = snapshot_item_instance.to_dict()
# create an instance of SnapshotItem from a dict
snapshot_item_from_dict = SnapshotItem.from_dict(snapshot_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SloHealthSnapshotItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprint** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**health_score** | **int** |  | [optional] 
**health_state** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**primary_reason** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**target** | **float** |  | [optional] 
**trend** | **str** |  | [optional] 
**window_duration** | **int** |  | [optional] 
**window_duration_unit** | **str** |  | [optional] 
**window_type** | **str** |  | [optional] 

## Example

```python
from instana_client.models.slo_health_snapshot_item import SloHealthSnapshotItem

# TODO update the JSON string below
json = "{}"
# create an instance of SloHealthSnapshotItem from a JSON string
slo_health_snapshot_item_instance = SloHealthSnapshotItem.from_json(json)
# print the JSON string representation of the object
print(SloHealthSnapshotItem.to_json())

# convert the object into a dict
slo_health_snapshot_item_dict = slo_health_snapshot_item_instance.to_dict()
# create an instance of SloHealthSnapshotItem from a dict
slo_health_snapshot_item_from_dict = SloHealthSnapshotItem.from_dict(slo_health_snapshot_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



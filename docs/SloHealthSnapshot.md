# SloHealthSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SloHealthSnapshotItem]**](SloHealthSnapshotItem.md) |  | [optional] 
**state_counts** | **Dict[str, int]** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from instana_client.models.slo_health_snapshot import SloHealthSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of SloHealthSnapshot from a JSON string
slo_health_snapshot_instance = SloHealthSnapshot.from_json(json)
# print the JSON string representation of the object
print(SloHealthSnapshot.to_json())

# convert the object into a dict
slo_health_snapshot_dict = slo_health_snapshot_instance.to_dict()
# create an instance of SloHealthSnapshot from a dict
slo_health_snapshot_from_dict = SloHealthSnapshot.from_dict(slo_health_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



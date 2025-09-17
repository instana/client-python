# SnapshotPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Subset of the data section of the plugin. In most cases this field will be null. | [optional] 
**id** | **str** | This is a snapshot ID. A unique identifier the metrics are assigned to. | 
**label** | **str** | Name of the entity. | [optional] 
**plugin** | **str** | A short plugin ID. For example, &#x60;containerd&#x60;, &#x60;nginx&#x60; etc. | [optional] 
**time** | **int** | Specifies the exact point at which the id, label and plugin are valid. | [optional] 

## Example

```python
from instana_client.models.snapshot_preview import SnapshotPreview

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotPreview from a JSON string
snapshot_preview_instance = SnapshotPreview.from_json(json)
# print the JSON string representation of the object
print(SnapshotPreview.to_json())

# convert the object into a dict
snapshot_preview_dict = snapshot_preview_instance.to_dict()
# create an instance of SnapshotPreview from a dict
snapshot_preview_from_dict = SnapshotPreview.from_dict(snapshot_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



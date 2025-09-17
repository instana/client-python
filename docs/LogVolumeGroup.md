# LogVolumeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**log_volume** | **int** |  | 

## Example

```python
from instana_client.models.log_volume_group import LogVolumeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LogVolumeGroup from a JSON string
log_volume_group_instance = LogVolumeGroup.from_json(json)
# print the JSON string representation of the object
print(LogVolumeGroup.to_json())

# convert the object into a dict
log_volume_group_dict = log_volume_group_instance.to_dict()
# create an instance of LogVolumeGroup from a dict
log_volume_group_from_dict = LogVolumeGroup.from_dict(log_volume_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



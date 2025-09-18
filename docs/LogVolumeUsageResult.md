# LogVolumeUsageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_volume_usage_items** | [**List[LogVolumeUsageItem]**](LogVolumeUsageItem.md) |  | 

## Example

```python
from instana_client.models.log_volume_usage_result import LogVolumeUsageResult

# TODO update the JSON string below
json = "{}"
# create an instance of LogVolumeUsageResult from a JSON string
log_volume_usage_result_instance = LogVolumeUsageResult.from_json(json)
# print the JSON string representation of the object
print(LogVolumeUsageResult.to_json())

# convert the object into a dict
log_volume_usage_result_dict = log_volume_usage_result_instance.to_dict()
# create an instance of LogVolumeUsageResult from a dict
log_volume_usage_result_from_dict = LogVolumeUsageResult.from_dict(log_volume_usage_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



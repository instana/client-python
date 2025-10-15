# LogVolumeUsageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_volume** | **int** |  | 
**number_of_month** | **int** |  | [optional] 
**retention_periods** | [**List[RetentionPeriod]**](RetentionPeriod.md) |  | 

## Example

```python
from instana_client.models.log_volume_usage_item import LogVolumeUsageItem

# TODO update the JSON string below
json = "{}"
# create an instance of LogVolumeUsageItem from a JSON string
log_volume_usage_item_instance = LogVolumeUsageItem.from_json(json)
# print the JSON string representation of the object
print(LogVolumeUsageItem.to_json())

# convert the object into a dict
log_volume_usage_item_dict = log_volume_usage_item_instance.to_dict()
# create an instance of LogVolumeUsageItem from a dict
log_volume_usage_item_from_dict = LogVolumeUsageItem.from_dict(log_volume_usage_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



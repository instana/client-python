# RetentionPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_volume** | **int** |  | 
**log_volume_groups** | [**List[LogVolumeGroup]**](LogVolumeGroup.md) |  | [optional] 
**retention_days** | **int** |  | [optional] 

## Example

```python
from instana_client.models.retention_period import RetentionPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of RetentionPeriod from a JSON string
retention_period_instance = RetentionPeriod.from_json(json)
# print the JSON string representation of the object
print(RetentionPeriod.to_json())

# convert the object into a dict
retention_period_dict = retention_period_instance.to_dict()
# create an instance of RetentionPeriod from a dict
retention_period_from_dict = RetentionPeriod.from_dict(retention_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LogTimeThreshold

The type of threshold to define the criteria when the event and alert triggers and resolves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.log_time_threshold import LogTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of LogTimeThreshold from a JSON string
log_time_threshold_instance = LogTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(LogTimeThreshold.to_json())

# convert the object into a dict
log_time_threshold_dict = log_time_threshold_instance.to_dict()
# create an instance of LogTimeThreshold from a dict
log_time_threshold_from_dict = LogTimeThreshold.from_dict(log_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



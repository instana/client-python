# LogEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | ID of the snapshot. | [optional] 

## Example

```python
from instana_client.models.log_event_result import LogEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of LogEventResult from a JSON string
log_event_result_instance = LogEventResult.from_json(json)
# print the JSON string representation of the object
print(LogEventResult.to_json())

# convert the object into a dict
log_event_result_dict = log_event_result_instance.to_dict()
# create an instance of LogEventResult from a dict
log_event_result_from_dict = LogEventResult.from_dict(log_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AlertingTimeWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** |  | 
**duration_type** | **str** |  | 
**duration_unit** | **str** |  | [optional] 

## Example

```python
from instana_client.models.alerting_time_window import AlertingTimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingTimeWindow from a JSON string
alerting_time_window_instance = AlertingTimeWindow.from_json(json)
# print the JSON string representation of the object
print(AlertingTimeWindow.to_json())

# convert the object into a dict
alerting_time_window_dict = alerting_time_window_instance.to_dict()
# create an instance of AlertingTimeWindow from a dict
alerting_time_window_from_dict = AlertingTimeWindow.from_dict(alerting_time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



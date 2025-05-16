# FixedTimeWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_timestamp** | **datetime** | The timestamp at which the fixed time window of the SLO starts | 

## Example

```python
from instana_client.models.fixed_time_window import FixedTimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of FixedTimeWindow from a JSON string
fixed_time_window_instance = FixedTimeWindow.from_json(json)
# print the JSON string representation of the object
print(FixedTimeWindow.to_json())

# convert the object into a dict
fixed_time_window_dict = fixed_time_window_instance.to_dict()
# create an instance of FixedTimeWindow from a dict
fixed_time_window_from_dict = FixedTimeWindow.from_dict(fixed_time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



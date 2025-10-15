# TimeWindow

Time Window type of the SLO, it could be Fixed or Rolling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Duration of the Time Window | 
**duration_unit** | **str** | Unit of the Time Window Duration | 
**timezone** | **str** | Timezone string | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.time_window import TimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindow from a JSON string
time_window_instance = TimeWindow.from_json(json)
# print the JSON string representation of the object
print(TimeWindow.to_json())

# convert the object into a dict
time_window_dict = time_window_instance.to_dict()
# create an instance of TimeWindow from a dict
time_window_from_dict = TimeWindow.from_dict(time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



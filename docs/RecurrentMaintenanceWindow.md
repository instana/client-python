# RecurrentMaintenanceWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rrule** | **str** |  | 
**timezone_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.recurrent_maintenance_window import RecurrentMaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrentMaintenanceWindow from a JSON string
recurrent_maintenance_window_instance = RecurrentMaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(RecurrentMaintenanceWindow.to_json())

# convert the object into a dict
recurrent_maintenance_window_dict = recurrent_maintenance_window_instance.to_dict()
# create an instance of RecurrentMaintenanceWindow from a dict
recurrent_maintenance_window_from_dict = RecurrentMaintenanceWindow.from_dict(recurrent_maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MaintenanceConfigScheduling

Time scheduling of the Maintenance Window configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**Duration**](Duration.md) |  | 
**start** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from instana_client.models.maintenance_config_scheduling import MaintenanceConfigScheduling

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceConfigScheduling from a JSON string
maintenance_config_scheduling_instance = MaintenanceConfigScheduling.from_json(json)
# print the JSON string representation of the object
print(MaintenanceConfigScheduling.to_json())

# convert the object into a dict
maintenance_config_scheduling_dict = maintenance_config_scheduling_instance.to_dict()
# create an instance of MaintenanceConfigScheduling from a dict
maintenance_config_scheduling_from_dict = MaintenanceConfigScheduling.from_dict(maintenance_config_scheduling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



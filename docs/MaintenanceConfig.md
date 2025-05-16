# MaintenanceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Maintenance Window Configuration. | 
**name** | **str** | Name of the Maintenance Window Configuration. | 
**query** | **str** | Dynamic Focus Query that determines the scope of the Maintenance Window configuration. | 
**windows** | [**List[MaintenanceWindow]**](MaintenanceWindow.md) | A set of time periods when the Maintenance Window Configuration is active. | [optional] 

## Example

```python
from instana_client.models.maintenance_config import MaintenanceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceConfig from a JSON string
maintenance_config_instance = MaintenanceConfig.from_json(json)
# print the JSON string representation of the object
print(MaintenanceConfig.to_json())

# convert the object into a dict
maintenance_config_dict = maintenance_config_instance.to_dict()
# create an instance of MaintenanceConfig from a dict
maintenance_config_from_dict = MaintenanceConfig.from_dict(maintenance_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



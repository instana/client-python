# MaintenanceConfigWithLastUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Maintenance Window Configuration. | 
**last_updated** | **int** |  | [optional] 
**name** | **str** | Name of the Maintenance Window Configuration. | 
**query** | **str** | Dynamic Focus Query that determines the scope of the Maintenance Window configuration. | 
**windows** | [**List[MaintenanceWindow]**](MaintenanceWindow.md) | A set of time periods when the Maintenance Window Configuration is active. | [optional] 

## Example

```python
from instana_client.models.maintenance_config_with_last_updated import MaintenanceConfigWithLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceConfigWithLastUpdated from a JSON string
maintenance_config_with_last_updated_instance = MaintenanceConfigWithLastUpdated.from_json(json)
# print the JSON string representation of the object
print(MaintenanceConfigWithLastUpdated.to_json())

# convert the object into a dict
maintenance_config_with_last_updated_dict = maintenance_config_with_last_updated_instance.to_dict()
# create an instance of MaintenanceConfigWithLastUpdated from a dict
maintenance_config_with_last_updated_from_dict = MaintenanceConfigWithLastUpdated.from_dict(maintenance_config_with_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



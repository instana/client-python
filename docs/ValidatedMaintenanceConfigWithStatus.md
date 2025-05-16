# ValidatedMaintenanceConfigWithStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Maintenance Window Configuration. | 
**invalid** | **bool** | Boolean flag that tells if the Dynamic Focus Query(DFQ) is invalid. | [optional] 
**last_updated** | **int** |  | [optional] 
**name** | **str** | Name of the Maintenance Window Configuration. | 
**query** | **str** | Dynamic Focus Query that determines the scope of the Maintenance Window configuration. | 
**status** | **str** | Status of the Maintenance Window Configuration. It can be one of: UNSCHEDULED, SCHEDULED, ACTIVE, FINISHED, PAUSED. | 
**windows** | [**List[MaintenanceWindow]**](MaintenanceWindow.md) | A set of time periods when the Maintenance Window Configuration is active. | [optional] 

## Example

```python
from instana_client.models.validated_maintenance_config_with_status import ValidatedMaintenanceConfigWithStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedMaintenanceConfigWithStatus from a JSON string
validated_maintenance_config_with_status_instance = ValidatedMaintenanceConfigWithStatus.from_json(json)
# print the JSON string representation of the object
print(ValidatedMaintenanceConfigWithStatus.to_json())

# convert the object into a dict
validated_maintenance_config_with_status_dict = validated_maintenance_config_with_status_instance.to_dict()
# create an instance of ValidatedMaintenanceConfigWithStatus from a dict
validated_maintenance_config_with_status_from_dict = ValidatedMaintenanceConfigWithStatus.from_dict(validated_maintenance_config_with_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



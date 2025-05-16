# MaintenanceConfigV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Maintenance Window configuration. | 
**name** | **str** | Name of the Maintenance Window configuration. | 
**paused** | **bool** | Boolean flag to determine if the Maintenance Window configuration is paused or still live. | [optional] 
**query** | **str** | Dynamic Focus Query that determines the scope of the Maintenance Window configuration. | 
**retrigger_open_alerts_enabled** | **bool** | Boolean flag to determine if we should retrigger open alerts to be sent out for any events that opened during this maintenance window, and continues to remain open after the window expires | [optional] 
**scheduling** | [**MaintenanceConfigScheduling**](MaintenanceConfigScheduling.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filter_expression_enabled** | **bool** | Boolean flag to determine if the tagFilterExpression is enabled. | [optional] 

## Example

```python
from instana_client.models.maintenance_config_v2 import MaintenanceConfigV2

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceConfigV2 from a JSON string
maintenance_config_v2_instance = MaintenanceConfigV2.from_json(json)
# print the JSON string representation of the object
print(MaintenanceConfigV2.to_json())

# convert the object into a dict
maintenance_config_v2_dict = maintenance_config_v2_instance.to_dict()
# create an instance of MaintenanceConfigV2 from a dict
maintenance_config_v2_from_dict = MaintenanceConfigV2.from_dict(maintenance_config_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



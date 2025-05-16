# MaintenanceConfigV2WithStateAndOccurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Maintenance Window configuration. | 
**last_updated** | **int** |  | [optional] 
**name** | **str** | Name of the Maintenance Window configuration. | 
**occurrence** | [**Occurrence**](Occurrence.md) |  | 
**paused** | **bool** | Boolean flag to determine if the Maintenance Window configuration is paused or still live. | [optional] 
**query** | **str** | Dynamic Focus Query that determines the scope of the Maintenance Window configuration. | 
**retrigger_open_alerts_enabled** | **bool** | Boolean flag to determine if we should retrigger open alerts to be sent out for any events that opened during this maintenance window, and continues to remain open after the window expires | [optional] 
**scheduling** | [**MaintenanceConfigScheduling**](MaintenanceConfigScheduling.md) |  | 
**state** | **str** | State of the Maintenance Window, it can be: UNSCHEDULED, SCHEDULED, ACTIVE, PAUSED, EXPIRED. | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filter_expression_enabled** | **bool** | Boolean flag to determine if the tagFilterExpression is enabled. | [optional] 

## Example

```python
from instana_client.models.maintenance_config_v2_with_state_and_occurrence import MaintenanceConfigV2WithStateAndOccurrence

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceConfigV2WithStateAndOccurrence from a JSON string
maintenance_config_v2_with_state_and_occurrence_instance = MaintenanceConfigV2WithStateAndOccurrence.from_json(json)
# print the JSON string representation of the object
print(MaintenanceConfigV2WithStateAndOccurrence.to_json())

# convert the object into a dict
maintenance_config_v2_with_state_and_occurrence_dict = maintenance_config_v2_with_state_and_occurrence_instance.to_dict()
# create an instance of MaintenanceConfigV2WithStateAndOccurrence from a dict
maintenance_config_v2_with_state_and_occurrence_from_dict = MaintenanceConfigV2WithStateAndOccurrence.from_dict(maintenance_config_v2_with_state_and_occurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



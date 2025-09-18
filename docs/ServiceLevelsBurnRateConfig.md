# ServiceLevelsBurnRateConfig

This is the burn rate alert configuration which defines alerting windows and corresponding thresholds. This configuration must to specified for BURN_RATE_V2 Alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_window_type** | **str** | Specifies the Burn Rate Alerting Window type: SINGLE for single window/threshold alerts, or LONG and SHORT for multi-window/threshold alerts. | [optional] 
**duration** | **int** | Duration of the Burn Rate Alerting Window. | 
**duration_unit_type** | **str** | Duration Unit Type of the Burn Rate Alerting Window. | 
**threshold** | [**ServiceLevelsStaticThresholdConfig**](ServiceLevelsStaticThresholdConfig.md) |  | 

## Example

```python
from instana_client.models.service_levels_burn_rate_config import ServiceLevelsBurnRateConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelsBurnRateConfig from a JSON string
service_levels_burn_rate_config_instance = ServiceLevelsBurnRateConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelsBurnRateConfig.to_json())

# convert the object into a dict
service_levels_burn_rate_config_dict = service_levels_burn_rate_config_instance.to_dict()
# create an instance of ServiceLevelsBurnRateConfig from a dict
service_levels_burn_rate_config_from_dict = ServiceLevelsBurnRateConfig.from_dict(service_levels_burn_rate_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



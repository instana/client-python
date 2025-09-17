# ServiceLevelseAlertConfigWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | This is the list of channel IDs when alert triggered and sent to. | 
**burn_rate_config** | [**List[ServiceLevelsBurnRateConfig]**](ServiceLevelsBurnRateConfig.md) | This is the burn rate alert configuration which defines alerting windows and corresponding thresholds. This configuration must to specified for BURN_RATE_V2 Alerts. | [optional] 
**burn_rate_time_windows** | [**ServiceLevelsBurnRateTimeWindows**](ServiceLevelsBurnRateTimeWindows.md) |  | [optional] 
**created** | **int** | Created Date of the version of Service Levels Smart Alerts Configuration. | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | This is the custom name and value pairs to be sent along with the alert to the alert channels. | 
**description** | **str** | The description of the alert. It is also the alert message content. | 
**enabled** | **bool** | Boolean Parameter specifying the enabled state of Service Levels Smart Alerts Configuration. | [optional] 
**id** | **str** | Unique ID of the Service Levels Smart Alerts Configuration. | 
**initial_created** | **int** | Created Date of the Initial version of Service Levels Smart Alerts Configuration. | [optional] 
**name** | **str** | Name of the Service Levels Smart Alerts Configuration. | 
**read_only** | **bool** | Boolean Parameter specifying the readonly access to Service Levels Smart Alerts Configuration. | [optional] 
**rule** | [**ServiceLevelsAlertRule**](ServiceLevelsAlertRule.md) |  | 
**severity** | **int** | This is the severity of the alert. The value can be: &lt;b&gt;5&lt;/b&gt;: warning, &lt;b&gt;10&lt;/b&gt;: critical. | 
**slo_ids** | **List[str]** | This is the list of SLO configurations related to this alert. | 
**threshold** | [**StaticThreshold**](StaticThreshold.md) |  | [optional] 
**time_threshold** | [**ServiceLevelsTimeThreshold**](ServiceLevelsTimeThreshold.md) |  | 
**triggering** | **bool** | Incident flag. If value is true, this alert will become an accident. | [optional] 

## Example

```python
from instana_client.models.service_levelse_alert_config_with_metadata import ServiceLevelseAlertConfigWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelseAlertConfigWithMetadata from a JSON string
service_levelse_alert_config_with_metadata_instance = ServiceLevelseAlertConfigWithMetadata.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelseAlertConfigWithMetadata.to_json())

# convert the object into a dict
service_levelse_alert_config_with_metadata_dict = service_levelse_alert_config_with_metadata_instance.to_dict()
# create an instance of ServiceLevelseAlertConfigWithMetadata from a dict
service_levelse_alert_config_with_metadata_from_dict = ServiceLevelseAlertConfigWithMetadata.from_dict(service_levelse_alert_config_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



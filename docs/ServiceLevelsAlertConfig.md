# ServiceLevelsAlertConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | This is the list of channel IDs when alert triggered and sent to. | 
**burn_rate_time_windows** | [**ServiceLevelsBurnRateTimeWindows**](ServiceLevelsBurnRateTimeWindows.md) |  | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | This is the custom name and value pairs to be sent along with the alert to the alert channels. | 
**description** | **str** | The description of the alert. It is also the alert message content. | 
**name** | **str** | Name of the Service Levels Smart Alerts Configuration. | 
**rule** | [**ServiceLevelsAlertRule**](ServiceLevelsAlertRule.md) |  | 
**severity** | **int** | This is the severity of the alert. The value can be: &lt;b&gt;5&lt;/b&gt;: warning, &lt;b&gt;10&lt;/b&gt;: critical. | [optional] 
**slo_ids** | **List[str]** | This is the list of SLO configurations related to this alert. | 
**threshold** | [**StaticThreshold**](StaticThreshold.md) |  | 
**time_threshold** | [**ServiceLevelsTimeThreshold**](ServiceLevelsTimeThreshold.md) |  | 
**triggering** | **bool** | Incident flag. If value is true, this alert will become an accident. | [optional] 

## Example

```python
from instana_client.models.service_levels_alert_config import ServiceLevelsAlertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelsAlertConfig from a JSON string
service_levels_alert_config_instance = ServiceLevelsAlertConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelsAlertConfig.to_json())

# convert the object into a dict
service_levels_alert_config_dict = service_levels_alert_config_instance.to_dict()
# create an instance of ServiceLevelsAlertConfig from a dict
service_levels_alert_config_from_dict = ServiceLevelsAlertConfig.from_dict(service_levels_alert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



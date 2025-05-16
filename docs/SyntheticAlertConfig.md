# SyntheticAlertConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**description** | **str** | Description of the synthetic alert configuration. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**name** | **str** | Name of the synthetic alert configuration. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**rule** | [**SyntheticAlertRule**](SyntheticAlertRule.md) |  | 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**synthetic_test_ids** | **List[str]** | IDs of the synthetic tests that this Smart Alert configuration is applied to. | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**time_threshold** | [**SyntheticTimeThreshold**](SyntheticTimeThreshold.md) |  | 

## Example

```python
from instana_client.models.synthetic_alert_config import SyntheticAlertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticAlertConfig from a JSON string
synthetic_alert_config_instance = SyntheticAlertConfig.from_json(json)
# print the JSON string representation of the object
print(SyntheticAlertConfig.to_json())

# convert the object into a dict
synthetic_alert_config_dict = synthetic_alert_config_instance.to_dict()
# create an instance of SyntheticAlertConfig from a dict
synthetic_alert_config_from_dict = SyntheticAlertConfig.from_dict(synthetic_alert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



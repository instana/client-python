# InfraAlertConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | [optional] 
**alert_channels** | **Dict[str, List[str]]** | Set of alert channel IDs associated with the severity. | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**description** | **str** | Description of the Infrastructure Smart Alert. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**evaluation_type** | **str** | Determines whether we evaluate each infra entity independently or group of entities will be evaluated together. | [optional] 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**granularity** | **int** | The evaluation granularity used for detection of violations of the defined threshold. Defines the size of the tumbling window used. | [default to 600000]
**group_by** | **List[str]** | The grouping tags used to group the metric results. | 
**name** | **str** | Name of the Infrastructure Smart Alert. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**rule** | [**InfraAlertRule**](InfraAlertRule.md) |  | [optional] 
**rules** | [**List[RuleWithThresholdInfraAlertRule]**](RuleWithThresholdInfraAlertRule.md) | A list of rules where each rule is associated with multiple thresholds and their corresponding severity levels. This enables more complex alert configurations with validations to ensure consistent and logical threshold-severity combinations. | [optional] 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**time_threshold** | [**InfraTimeThreshold**](InfraTimeThreshold.md) |  | 

## Example

```python
from instana_client.models.infra_alert_config import InfraAlertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InfraAlertConfig from a JSON string
infra_alert_config_instance = InfraAlertConfig.from_json(json)
# print the JSON string representation of the object
print(InfraAlertConfig.to_json())

# convert the object into a dict
infra_alert_config_dict = infra_alert_config_instance.to_dict()
# create an instance of InfraAlertConfig from a dict
infra_alert_config_from_dict = InfraAlertConfig.from_dict(infra_alert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



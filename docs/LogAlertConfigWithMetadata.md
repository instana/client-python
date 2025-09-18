# LogAlertConfigWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | [optional] 
**alert_channels** | **Dict[str, List[str]]** | Set of alert channel IDs associated with the severity. | [optional] 
**created** | **int** |  | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | [optional] 
**description** | **str** | Description of the Log Smart Alert. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**enabled** | **bool** |  | [optional] 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**granularity** | **int** | The evaluation granularity used for detection of violations of the defined threshold. Defines the size of the tumbling window used. | [default to 600000]
**group_by** | [**List[GroupByTag]**](GroupByTag.md) | The grouping tags used to group the metric results. | [optional] 
**id** | **str** |  | 
**initial_created** | **int** |  | [optional] 
**name** | **str** | Name of the Log Smart Alert. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**read_only** | **bool** |  | [optional] 
**rules** | [**List[RuleWithThresholdLogAlertRule]**](RuleWithThresholdLogAlertRule.md) | A list of rules where each rule is associated with multiple thresholds and their corresponding severity levels. This enables more complex alert configurations with validations to ensure consistent and logical threshold-severity combinations. | [optional] 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**time_threshold** | [**LogTimeThreshold**](LogTimeThreshold.md) |  | 

## Example

```python
from instana_client.models.log_alert_config_with_metadata import LogAlertConfigWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LogAlertConfigWithMetadata from a JSON string
log_alert_config_with_metadata_instance = LogAlertConfigWithMetadata.from_json(json)
# print the JSON string representation of the object
print(LogAlertConfigWithMetadata.to_json())

# convert the object into a dict
log_alert_config_with_metadata_dict = log_alert_config_with_metadata_instance.to_dict()
# create an instance of LogAlertConfigWithMetadata from a dict
log_alert_config_with_metadata_from_dict = LogAlertConfigWithMetadata.from_dict(log_alert_config_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



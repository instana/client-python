# WebsiteAlertConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | [optional] 
**alert_channels** | **Dict[str, List[str]]** | Set of alert channel IDs associated with the severity. | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**description** | **str** | Description of the website alert configuration. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**granularity** | **int** | The evaluation granularity used for detection of violations of the defined threshold. Defines the size of the tumbling window used. | [default to 600000]
**name** | **str** | Name of the website alert configuration. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**rule** | [**WebsiteAlertRule**](WebsiteAlertRule.md) |  | [optional] 
**rules** | [**List[RuleWithThresholdWebsiteAlertRule]**](RuleWithThresholdWebsiteAlertRule.md) | A list of rules where each rule is associated with multiple thresholds and their corresponding severity levels. This enables more complex alert configurations with validations to ensure consistent and logical threshold-severity combinations. | [optional] 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**tag_filters** | [**List[TagFilter]**](TagFilter.md) |  | [optional] 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**time_threshold** | [**WebsiteTimeThreshold**](WebsiteTimeThreshold.md) |  | 
**triggering** | **bool** | Optional flag to indicate whether an Incident is also triggered or not. | [optional] 
**website_id** | **str** | ID of the website that this Smart Alert configuration is applied to. | 

## Example

```python
from instana_client.models.website_alert_config import WebsiteAlertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteAlertConfig from a JSON string
website_alert_config_instance = WebsiteAlertConfig.from_json(json)
# print the JSON string representation of the object
print(WebsiteAlertConfig.to_json())

# convert the object into a dict
website_alert_config_dict = website_alert_config_instance.to_dict()
# create an instance of WebsiteAlertConfig from a dict
website_alert_config_from_dict = WebsiteAlertConfig.from_dict(website_alert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



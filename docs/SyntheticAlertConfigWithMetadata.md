# SyntheticAlertConfigWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | 
**created** | **int** | Unix timestamp representing the creation time of this revision. | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**description** | **str** | Description of the synthetic alert configuration. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**enabled** | **bool** | Flag to indicate whether or not the configuration is enabled. | [optional] 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**id** | **str** | ID of this Synthetic Alert Config.  | 
**initial_created** | **int** | Unix timestamp representing the time of the initial revision. | [optional] 
**name** | **str** | Name of the synthetic alert configuration. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**read_only** | **bool** | Flag to indicate whether or not the configuration is read-only. Read-only access restricts modification of the config. | [optional] 
**rule** | [**SyntheticAlertRule**](SyntheticAlertRule.md) |  | 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**synthetic_test_ids** | **List[str]** | IDs of the synthetic tests that this Smart Alert configuration is applied to. | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**time_threshold** | [**SyntheticTimeThreshold**](SyntheticTimeThreshold.md) |  | 

## Example

```python
from instana_client.models.synthetic_alert_config_with_metadata import SyntheticAlertConfigWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticAlertConfigWithMetadata from a JSON string
synthetic_alert_config_with_metadata_instance = SyntheticAlertConfigWithMetadata.from_json(json)
# print the JSON string representation of the object
print(SyntheticAlertConfigWithMetadata.to_json())

# convert the object into a dict
synthetic_alert_config_with_metadata_dict = synthetic_alert_config_with_metadata_instance.to_dict()
# create an instance of SyntheticAlertConfigWithMetadata from a dict
synthetic_alert_config_with_metadata_from_dict = SyntheticAlertConfigWithMetadata.from_dict(synthetic_alert_config_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



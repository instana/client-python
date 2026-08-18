# SyntheticAlertConfigWithRBACTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_locations_count** | **int** | Number of locations encounters failure | [optional] 
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | 
**created** | **int** | Unix timestamp representing the creation time of this revision. | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**description** | **str** | Description of the synthetic alert configuration. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**enabled** | **bool** | Flag to indicate whether or not the configuration is enabled. | [optional] 
**evaluation_type** | **str** | Determines whether synthetic test results are evaluated per location independently or grouped across all locations. | [optional] 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**id** | **str** | ID of this Synthetic Alert Config.  | 
**include_on_demand** | **bool** | Controls whether on-demand synthetic test runs should be included in alert evaluation. When true, both scheduled and on-demand test runs are evaluated. When false, only scheduled test runs are evaluated. Default behavior when not provided: (1) If tagFilterExpression contains RUN_TYPE filter that is NOT &#39;Scheduled&#39; → defaults to true; (2) If tagFilterExpression contains RUN_TYPE EQUALS &#39;Scheduled&#39; → defaults to false; (3) If no RUN_TYPE filter exists → defaults to false. | [optional] 
**initial_created** | **int** | Unix timestamp representing the time of the initial revision. | [optional] 
**name** | **str** | Name of the synthetic alert configuration. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**rbac_tags** | [**List[ApiTag]**](ApiTag.md) | RBAC tags associated with the synthetic test | [optional] 
**read_only** | **bool** | Flag to indicate whether or not the configuration is read-only. Read-only access restricts modification of the config. | [optional] 
**rule** | [**SyntheticAlertRule**](SyntheticAlertRule.md) |  | 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**synthetic_test_ids** | **List[str]** | IDs of the synthetic tests that this Smart Alert configuration is applied to. | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**time_threshold** | [**SyntheticTimeThreshold**](SyntheticTimeThreshold.md) |  | 

## Example

```python
from instana_client.models.synthetic_alert_config_with_rbac_tag import SyntheticAlertConfigWithRBACTag

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticAlertConfigWithRBACTag from a JSON string
synthetic_alert_config_with_rbac_tag_instance = SyntheticAlertConfigWithRBACTag.from_json(json)
# print the JSON string representation of the object
print(SyntheticAlertConfigWithRBACTag.to_json())

# convert the object into a dict
synthetic_alert_config_with_rbac_tag_dict = synthetic_alert_config_with_rbac_tag_instance.to_dict()
# create an instance of SyntheticAlertConfigWithRBACTag from a dict
synthetic_alert_config_with_rbac_tag_from_dict = SyntheticAlertConfigWithRBACTag.from_dict(synthetic_alert_config_with_rbac_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GlobalApplicationAlertConfigWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of IDs of alert channels defined in Instana. Can be left empty. | 
**alert_channels** | **Dict[str, List[str]]** | Set of alert channel IDs associated with the severity. | [optional] 
**application_ids** | **List[str]** | IDs of the applications that this Smart Alert is applied to. | [optional] 
**applications** | [**Dict[str, ApplicationNode]**](ApplicationNode.md) | Selection of applications, services, and endpoints that this Smart Alert configuration is associated with. This selection is connected to the defined &#x60;tagFilterExpression&#x60; by the logical &#x60;AND&#x60; operator. | 
**boundary_scope** | **str** | Determines the source of the application alert configuration. An &#x60;INBOUND&#x60; scope refers to consumer-made calls. An &#x60;ALL&#x60; scope refers to both consumer and internally made calls. | 
**built_in** | **bool** | Flag that indicates whether this configuration is a built-in Smart Alert.  | [optional] 
**created** | **int** | Unix timestamp representing the creation time of this revision. | [optional] 
**custom_payload_fields** | [**List[CustomPayloadField]**](CustomPayloadField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**description** | **str** | Description of the application alert configuration. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration. | 
**enabled** | **bool** | Flag to indicate whether or not the configuration is enabled. | [optional] 
**evaluation_type** | **str** | Determines whether calls of the aggregated metrics are grouped by the application, the service, or the endpoint. This also determines whether the resulting events are categorized as an issue on the respective entity of that group. | 
**grace_period** | **int** | The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires. | [optional] 
**granularity** | **int** | The evaluation granularity used for detection of violations of the defined threshold. Defines the size of the tumbling window used. | [default to 600000]
**id** | **str** | ID of this Global Application Alert Configuration. | 
**include_internal** | **bool** | Flag to include Internal Calls. These calls are work done inside a service and correspond to intermediate spans in custom tracing. | [optional] 
**include_synthetic** | **bool** | Flag to include Synthetic Calls. These calls have a synthetic endpoint as their destination, such as calls to health-check endpoints.  | [optional] 
**initial_created** | **int** | Unix timestamp representing the time of the initial revision. | [optional] 
**name** | **str** | Name of the application alert configuration. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration. | 
**read_only** | **bool** | Flag to indicate whether or not the configuration is read-only. Read-only access restricts modification of the config. | [optional] 
**rule** | [**ApplicationAlertRule**](ApplicationAlertRule.md) |  | [optional] 
**rules** | [**List[RuleWithThresholdApplicationAlertRule]**](RuleWithThresholdApplicationAlertRule.md) | A list of rules where each rule is associated with multiple thresholds and their corresponding severity levels. This enables more complex alert configurations with validations to ensure consistent and logical threshold-severity combinations. | [optional] 
**severity** | **int** | The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical). | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**threshold** | [**Threshold**](Threshold.md) |  | [optional] 
**time_threshold** | [**ApplicationTimeThreshold**](ApplicationTimeThreshold.md) |  | 
**triggering** | **bool** | Optional flag to indicate whether an Incident is also triggered or not. | [optional] 

## Example

```python
from instana_client.models.global_application_alert_config_with_metadata import GlobalApplicationAlertConfigWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalApplicationAlertConfigWithMetadata from a JSON string
global_application_alert_config_with_metadata_instance = GlobalApplicationAlertConfigWithMetadata.from_json(json)
# print the JSON string representation of the object
print(GlobalApplicationAlertConfigWithMetadata.to_json())

# convert the object into a dict
global_application_alert_config_with_metadata_dict = global_application_alert_config_with_metadata_instance.to_dict()
# create an instance of GlobalApplicationAlertConfigWithMetadata from a dict
global_application_alert_config_with_metadata_from_dict = GlobalApplicationAlertConfigWithMetadata.from_dict(global_application_alert_config_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



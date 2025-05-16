# ValidatedAlertingConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_names** | **List[str]** | Set of Alert Channel names added in the Alert Configuration. | [optional] 
**alert_name** | **str** | Name of the Alert Configuration. | 
**application_names** | **List[str]** | Set of Application Perspective names added in the Alert Configuration. | [optional] 
**custom_payload_fields** | [**List[StaticStringField]**](StaticStringField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**event_filtering_configuration** | [**EventFilteringConfiguration**](EventFilteringConfiguration.md) |  | 
**id** | **str** | ID of the Alert Configuration. | 
**include_entity_name_in_legacy_alerts** | **bool** | To include the entity name in a legacy alert based on built-in/custom events. | [optional] 
**integration_ids** | **List[str]** | List of Alert Channel IDs added in this Alert Configuration. | 
**invalid** | **bool** | Flag to show whether the Alert Configuration is valid. | [optional] 
**last_updated** | **int** | Unix timestamp representing the time the configuration was last updated. | [optional] 
**mute_until** | **int** | Timer dictating how long the Alert Configuration will stay muted. A value of &#x60;0&#x60; means the Alert Configuration is currently enabled. Otherwise, the Alert Configuration is currently disabled (muted). | [optional] 

## Example

```python
from instana_client.models.validated_alerting_configuration import ValidatedAlertingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedAlertingConfiguration from a JSON string
validated_alerting_configuration_instance = ValidatedAlertingConfiguration.from_json(json)
# print the JSON string representation of the object
print(ValidatedAlertingConfiguration.to_json())

# convert the object into a dict
validated_alerting_configuration_dict = validated_alerting_configuration_instance.to_dict()
# create an instance of ValidatedAlertingConfiguration from a dict
validated_alerting_configuration_from_dict = ValidatedAlertingConfiguration.from_dict(validated_alerting_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



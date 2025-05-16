# AlertingConfigurationWithLastUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_name** | **str** | Name of the Alert Configuration. | 
**custom_payload_fields** | [**List[StaticStringField]**](StaticStringField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**event_filtering_configuration** | [**EventFilteringConfiguration**](EventFilteringConfiguration.md) |  | 
**id** | **str** | ID of the Alert Configuration. | 
**include_entity_name_in_legacy_alerts** | **bool** | To include the entity name in a legacy alert based on built-in/custom events. | [optional] 
**integration_ids** | **List[str]** | List of Alert Channel IDs added in this Alert Configuration. | 
**last_updated** | **int** | Unix timestamp representing the time the configuration was last updated. | [optional] 
**mute_until** | **int** | Timer dictating how long the Alert Configuration will stay muted. A value of &#x60;0&#x60; means the Alert Configuration is currently enabled. Otherwise, the Alert Configuration is currently disabled (muted). | [optional] 

## Example

```python
from instana_client.models.alerting_configuration_with_last_updated import AlertingConfigurationWithLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingConfigurationWithLastUpdated from a JSON string
alerting_configuration_with_last_updated_instance = AlertingConfigurationWithLastUpdated.from_json(json)
# print the JSON string representation of the object
print(AlertingConfigurationWithLastUpdated.to_json())

# convert the object into a dict
alerting_configuration_with_last_updated_dict = alerting_configuration_with_last_updated_instance.to_dict()
# create an instance of AlertingConfigurationWithLastUpdated from a dict
alerting_configuration_with_last_updated_from_dict = AlertingConfigurationWithLastUpdated.from_dict(alerting_configuration_with_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



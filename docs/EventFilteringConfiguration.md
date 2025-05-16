# EventFilteringConfiguration

Event Filter Configuration for supporting the scope of the Alert Configuration. Applies a filter based on the application perspective or selected entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_alert_config_ids** | **List[str]** |  | [optional] 
**event_types** | **List[str]** |  | [optional] 
**query** | **str** |  | [optional] 
**rule_ids** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.event_filtering_configuration import EventFilteringConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilteringConfiguration from a JSON string
event_filtering_configuration_instance = EventFilteringConfiguration.from_json(json)
# print the JSON string representation of the object
print(EventFilteringConfiguration.to_json())

# convert the object into a dict
event_filtering_configuration_dict = event_filtering_configuration_instance.to_dict()
# create an instance of EventFilteringConfiguration from a dict
event_filtering_configuration_from_dict = EventFilteringConfiguration.from_dict(event_filtering_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



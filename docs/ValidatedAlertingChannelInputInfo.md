# ValidatedAlertingChannelInputInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag to indicate whether or not the configuration is enabled. | [optional] 
**entity_id** | **str** | The entity ID in case of Smart Alerts, such as for the application, website or mobile app. | [optional] 
**event_types** | **List[str]** | The selected event types, if applicable. | [optional] 
**id** | **str** | ID of the alert configuration. | 
**invalid** | **bool** | Flag to indicate whether the specified query is invalid. | [optional] 
**label** | **str** | The name of the alert configuration. | 
**query** | **str** | The DFQ used in the alert configuration, if applicable. | [optional] 
**selected_events** | **int** | The number of selected events, if applicable. | [optional] 
**type** | **str** | The alert type. | 

## Example

```python
from instana_client.models.validated_alerting_channel_input_info import ValidatedAlertingChannelInputInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedAlertingChannelInputInfo from a JSON string
validated_alerting_channel_input_info_instance = ValidatedAlertingChannelInputInfo.from_json(json)
# print the JSON string representation of the object
print(ValidatedAlertingChannelInputInfo.to_json())

# convert the object into a dict
validated_alerting_channel_input_info_dict = validated_alerting_channel_input_info_instance.to_dict()
# create an instance of ValidatedAlertingChannelInputInfo from a dict
validated_alerting_channel_input_info_from_dict = ValidatedAlertingChannelInputInfo.from_dict(validated_alerting_channel_input_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



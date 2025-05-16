# ManualAlertingChannelConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_payload_fields** | [**List[StaticStringField]**](StaticStringField.md) | Custom payload fields to send additional information in the alert notifications. Can be left empty. | 
**event_id** | **str** | Id of the event to be notified about. | 

## Example

```python
from instana_client.models.manual_alerting_channel_configuration import ManualAlertingChannelConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ManualAlertingChannelConfiguration from a JSON string
manual_alerting_channel_configuration_instance = ManualAlertingChannelConfiguration.from_json(json)
# print the JSON string representation of the object
print(ManualAlertingChannelConfiguration.to_json())

# convert the object into a dict
manual_alerting_channel_configuration_dict = manual_alerting_channel_configuration_instance.to_dict()
# create an instance of ManualAlertingChannelConfiguration from a dict
manual_alerting_channel_configuration_from_dict = ManualAlertingChannelConfiguration.from_dict(manual_alerting_channel_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



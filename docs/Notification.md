# Notification

Optional notifications configuration for action execution events. Each notification specifies a condition (started, fail, success) and associated alert channels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_channel_ids** | **List[str]** | List of alert channel identifiers to send notifications to for this condition. | 
**condition** | **str** | Notification condition. Determines when the notification is sent. Each notification object represents a single condition with its associated alert channels. | 

## Example

```python
from instana_client.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



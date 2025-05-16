# CustomEventWebsiteAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_event_name** | **str** |  | 

## Example

```python
from instana_client.models.custom_event_website_alert_rule import CustomEventWebsiteAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEventWebsiteAlertRule from a JSON string
custom_event_website_alert_rule_instance = CustomEventWebsiteAlertRule.from_json(json)
# print the JSON string representation of the object
print(CustomEventWebsiteAlertRule.to_json())

# convert the object into a dict
custom_event_website_alert_rule_dict = custom_event_website_alert_rule_instance.to_dict()
# create an instance of CustomEventWebsiteAlertRule from a dict
custom_event_website_alert_rule_from_dict = CustomEventWebsiteAlertRule.from_dict(custom_event_website_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



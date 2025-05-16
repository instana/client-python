# StatusCodeMobileAppAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from instana_client.models.status_code_mobile_app_alert_rule import StatusCodeMobileAppAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodeMobileAppAlertRule from a JSON string
status_code_mobile_app_alert_rule_instance = StatusCodeMobileAppAlertRule.from_json(json)
# print the JSON string representation of the object
print(StatusCodeMobileAppAlertRule.to_json())

# convert the object into a dict
status_code_mobile_app_alert_rule_dict = status_code_mobile_app_alert_rule_instance.to_dict()
# create an instance of StatusCodeMobileAppAlertRule from a dict
status_code_mobile_app_alert_rule_from_dict = StatusCodeMobileAppAlertRule.from_dict(status_code_mobile_app_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MobileAppAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**alert_type** | **str** |  | 
**metric_name** | **str** |  | 

## Example

```python
from instana_client.models.mobile_app_alert_rule import MobileAppAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppAlertRule from a JSON string
mobile_app_alert_rule_instance = MobileAppAlertRule.from_json(json)
# print the JSON string representation of the object
print(MobileAppAlertRule.to_json())

# convert the object into a dict
mobile_app_alert_rule_dict = mobile_app_alert_rule_instance.to_dict()
# create an instance of MobileAppAlertRule from a dict
mobile_app_alert_rule_from_dict = MobileAppAlertRule.from_dict(mobile_app_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



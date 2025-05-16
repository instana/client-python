# SpecificJsErrorsWebsiteAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from instana_client.models.specific_js_errors_website_alert_rule import SpecificJsErrorsWebsiteAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificJsErrorsWebsiteAlertRule from a JSON string
specific_js_errors_website_alert_rule_instance = SpecificJsErrorsWebsiteAlertRule.from_json(json)
# print the JSON string representation of the object
print(SpecificJsErrorsWebsiteAlertRule.to_json())

# convert the object into a dict
specific_js_errors_website_alert_rule_dict = specific_js_errors_website_alert_rule_instance.to_dict()
# create an instance of SpecificJsErrorsWebsiteAlertRule from a dict
specific_js_errors_website_alert_rule_from_dict = SpecificJsErrorsWebsiteAlertRule.from_dict(specific_js_errors_website_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



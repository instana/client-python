# WebsiteAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**alert_type** | **str** |  | 
**metric_name** | **str** |  | 

## Example

```python
from instana_client.models.website_alert_rule import WebsiteAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteAlertRule from a JSON string
website_alert_rule_instance = WebsiteAlertRule.from_json(json)
# print the JSON string representation of the object
print(WebsiteAlertRule.to_json())

# convert the object into a dict
website_alert_rule_dict = website_alert_rule_instance.to_dict()
# create an instance of WebsiteAlertRule from a dict
website_alert_rule_from_dict = WebsiteAlertRule.from_dict(website_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



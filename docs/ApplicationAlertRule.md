# ApplicationAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**alert_type** | **str** |  | 
**metric_name** | **str** |  | 

## Example

```python
from instana_client.models.application_alert_rule import ApplicationAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationAlertRule from a JSON string
application_alert_rule_instance = ApplicationAlertRule.from_json(json)
# print the JSON string representation of the object
print(ApplicationAlertRule.to_json())

# convert the object into a dict
application_alert_rule_dict = application_alert_rule_instance.to_dict()
# create an instance of ApplicationAlertRule from a dict
application_alert_rule_from_dict = ApplicationAlertRule.from_dict(application_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



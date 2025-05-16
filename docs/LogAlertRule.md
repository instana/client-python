# LogAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**alert_type** | **str** |  | 
**metric_name** | **str** |  | 

## Example

```python
from instana_client.models.log_alert_rule import LogAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of LogAlertRule from a JSON string
log_alert_rule_instance = LogAlertRule.from_json(json)
# print the JSON string representation of the object
print(LogAlertRule.to_json())

# convert the object into a dict
log_alert_rule_dict = log_alert_rule_instance.to_dict()
# create an instance of LogAlertRule from a dict
log_alert_rule_from_dict = LogAlertRule.from_dict(log_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



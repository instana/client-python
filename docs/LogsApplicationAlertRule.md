# LogsApplicationAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | 
**loglevel** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**operator** | **str** |  | 

## Example

```python
from instana_client.models.logs_application_alert_rule import LogsApplicationAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of LogsApplicationAlertRule from a JSON string
logs_application_alert_rule_instance = LogsApplicationAlertRule.from_json(json)
# print the JSON string representation of the object
print(LogsApplicationAlertRule.to_json())

# convert the object into a dict
logs_application_alert_rule_dict = logs_application_alert_rule_instance.to_dict()
# create an instance of LogsApplicationAlertRule from a dict
logs_application_alert_rule_from_dict = LogsApplicationAlertRule.from_dict(logs_application_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StatusCodeApplicationAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code_end** | **int** |  | [optional] 
**status_code_start** | **int** |  | [optional] 

## Example

```python
from instana_client.models.status_code_application_alert_rule import StatusCodeApplicationAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodeApplicationAlertRule from a JSON string
status_code_application_alert_rule_instance = StatusCodeApplicationAlertRule.from_json(json)
# print the JSON string representation of the object
print(StatusCodeApplicationAlertRule.to_json())

# convert the object into a dict
status_code_application_alert_rule_dict = status_code_application_alert_rule_instance.to_dict()
# create an instance of StatusCodeApplicationAlertRule from a dict
status_code_application_alert_rule_from_dict = StatusCodeApplicationAlertRule.from_dict(status_code_application_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



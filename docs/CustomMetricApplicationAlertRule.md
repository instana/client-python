# CustomMetricApplicationAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_key** | **str** |  | 

## Example

```python
from instana_client.models.custom_metric_application_alert_rule import CustomMetricApplicationAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of CustomMetricApplicationAlertRule from a JSON string
custom_metric_application_alert_rule_instance = CustomMetricApplicationAlertRule.from_json(json)
# print the JSON string representation of the object
print(CustomMetricApplicationAlertRule.to_json())

# convert the object into a dict
custom_metric_application_alert_rule_dict = custom_metric_application_alert_rule_instance.to_dict()
# create an instance of CustomMetricApplicationAlertRule from a dict
custom_metric_application_alert_rule_from_dict = CustomMetricApplicationAlertRule.from_dict(custom_metric_application_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



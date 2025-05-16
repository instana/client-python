# SyntheticAlertRule

Indicates the type of rule this alert configuration is about.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**alert_type** | **str** |  | 
**metric_name** | **str** |  | 

## Example

```python
from instana_client.models.synthetic_alert_rule import SyntheticAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticAlertRule from a JSON string
synthetic_alert_rule_instance = SyntheticAlertRule.from_json(json)
# print the JSON string representation of the object
print(SyntheticAlertRule.to_json())

# convert the object into a dict
synthetic_alert_rule_dict = synthetic_alert_rule_instance.to_dict()
# create an instance of SyntheticAlertRule from a dict
synthetic_alert_rule_from_dict = SyntheticAlertRule.from_dict(synthetic_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RuleWithThresholdInfraAlertRule

A list of rules where each rule is associated with multiple thresholds and their corresponding severity levels. This enables more complex alert configurations with validations to ensure consistent and logical threshold-severity combinations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**InfraAlertRule**](InfraAlertRule.md) |  | 
**threshold_operator** | **str** |  | 
**thresholds** | [**Dict[str, ThresholdConfigRule]**](ThresholdConfigRule.md) |  | 

## Example

```python
from instana_client.models.rule_with_threshold_infra_alert_rule import RuleWithThresholdInfraAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of RuleWithThresholdInfraAlertRule from a JSON string
rule_with_threshold_infra_alert_rule_instance = RuleWithThresholdInfraAlertRule.from_json(json)
# print the JSON string representation of the object
print(RuleWithThresholdInfraAlertRule.to_json())

# convert the object into a dict
rule_with_threshold_infra_alert_rule_dict = rule_with_threshold_infra_alert_rule_instance.to_dict()
# create an instance of RuleWithThresholdInfraAlertRule from a dict
rule_with_threshold_infra_alert_rule_from_dict = RuleWithThresholdInfraAlertRule.from_dict(rule_with_threshold_infra_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



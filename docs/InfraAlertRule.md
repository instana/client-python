# InfraAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**alert_type** | **str** |  | 
**cross_series_aggregation** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**metric_name** | **str** |  | 
**regex** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.infra_alert_rule import InfraAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of InfraAlertRule from a JSON string
infra_alert_rule_instance = InfraAlertRule.from_json(json)
# print the JSON string representation of the object
print(InfraAlertRule.to_json())

# convert the object into a dict
infra_alert_rule_dict = infra_alert_rule_instance.to_dict()
# create an instance of InfraAlertRule from a dict
infra_alert_rule_from_dict = InfraAlertRule.from_dict(infra_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



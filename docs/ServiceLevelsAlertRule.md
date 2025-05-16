# ServiceLevelsAlertRule

This is the service levels alert type. It could be error budget alert or service levels object alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_type** | **str** |  | 

## Example

```python
from instana_client.models.service_levels_alert_rule import ServiceLevelsAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelsAlertRule from a JSON string
service_levels_alert_rule_instance = ServiceLevelsAlertRule.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelsAlertRule.to_json())

# convert the object into a dict
service_levels_alert_rule_dict = service_levels_alert_rule_instance.to_dict()
# create an instance of ServiceLevelsAlertRule from a dict
service_levels_alert_rule_from_dict = ServiceLevelsAlertRule.from_dict(service_levels_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceLevelObjectiveAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | This is the service levels metric type. Service levels objective alerts using &lt;b&gt;status&lt;/b&gt; metric. | [optional] 

## Example

```python
from instana_client.models.service_level_objective_alert_rule import ServiceLevelObjectiveAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelObjectiveAlertRule from a JSON string
service_level_objective_alert_rule_instance = ServiceLevelObjectiveAlertRule.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelObjectiveAlertRule.to_json())

# convert the object into a dict
service_level_objective_alert_rule_dict = service_level_objective_alert_rule_instance.to_dict()
# create an instance of ServiceLevelObjectiveAlertRule from a dict
service_level_objective_alert_rule_from_dict = ServiceLevelObjectiveAlertRule.from_dict(service_level_objective_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApdexAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | This is the Apdex metric type. Apdex alert uses &lt;b&gt;SCORE&lt;/b&gt; metric. | 

## Example

```python
from instana_client.models.apdex_alert_rule import ApdexAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexAlertRule from a JSON string
apdex_alert_rule_instance = ApdexAlertRule.from_json(json)
# print the JSON string representation of the object
print(ApdexAlertRule.to_json())

# convert the object into a dict
apdex_alert_rule_dict = apdex_alert_rule_instance.to_dict()
# create an instance of ApdexAlertRule from a dict
apdex_alert_rule_from_dict = ApdexAlertRule.from_dict(apdex_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



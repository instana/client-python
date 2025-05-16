# ErrorBudgetAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | This is the service levels metric type. Error budget alert uses &lt;b&gt;spent&lt;/b&gt; or &lt;b&gt;burn rate&lt;/b&gt; metric. | 

## Example

```python
from instana_client.models.error_budget_alert_rule import ErrorBudgetAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorBudgetAlertRule from a JSON string
error_budget_alert_rule_instance = ErrorBudgetAlertRule.from_json(json)
# print the JSON string representation of the object
print(ErrorBudgetAlertRule.to_json())

# convert the object into a dict
error_budget_alert_rule_dict = error_budget_alert_rule_instance.to_dict()
# create an instance of ErrorBudgetAlertRule from a dict
error_budget_alert_rule_from_dict = ErrorBudgetAlertRule.from_dict(error_budget_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



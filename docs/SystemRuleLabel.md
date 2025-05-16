# SystemRuleLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from instana_client.models.system_rule_label import SystemRuleLabel

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRuleLabel from a JSON string
system_rule_label_instance = SystemRuleLabel.from_json(json)
# print the JSON string representation of the object
print(SystemRuleLabel.to_json())

# convert the object into a dict
system_rule_label_dict = system_rule_label_instance.to_dict()
# create an instance of SystemRuleLabel from a dict
system_rule_label_from_dict = SystemRuleLabel.from_dict(system_rule_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



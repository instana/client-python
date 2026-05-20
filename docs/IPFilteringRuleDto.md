# IPFilteringRuleDto

Actual traffic rules. Enforcing allow / block based on incoming IP address. Are evaluated in given order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | **bool** | If the traffic should be blocked or denied. | 
**target** | **str** | Target of this rule, can be either a IP address or a IP address range. | 

## Example

```python
from instana_client.models.ip_filtering_rule_dto import IPFilteringRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of IPFilteringRuleDto from a JSON string
ip_filtering_rule_dto_instance = IPFilteringRuleDto.from_json(json)
# print the JSON string representation of the object
print(IPFilteringRuleDto.to_json())

# convert the object into a dict
ip_filtering_rule_dto_dict = ip_filtering_rule_dto_instance.to_dict()
# create an instance of IPFilteringRuleDto from a dict
ip_filtering_rule_dto_from_dict = IPFilteringRuleDto.from_dict(ip_filtering_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



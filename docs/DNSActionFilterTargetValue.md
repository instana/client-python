# DNSActionFilterTargetValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from instana_client.models.dns_action_filter_target_value import DNSActionFilterTargetValue

# TODO update the JSON string below
json = "{}"
# create an instance of DNSActionFilterTargetValue from a JSON string
dns_action_filter_target_value_instance = DNSActionFilterTargetValue.from_json(json)
# print the JSON string representation of the object
print(DNSActionFilterTargetValue.to_json())

# convert the object into a dict
dns_action_filter_target_value_dict = dns_action_filter_target_value_instance.to_dict()
# create an instance of DNSActionFilterTargetValue from a dict
dns_action_filter_target_value_from_dict = DNSActionFilterTargetValue.from_dict(dns_action_filter_target_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



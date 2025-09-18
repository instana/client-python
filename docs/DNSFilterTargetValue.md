# DNSFilterTargetValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from instana_client.models.dns_filter_target_value import DNSFilterTargetValue

# TODO update the JSON string below
json = "{}"
# create an instance of DNSFilterTargetValue from a JSON string
dns_filter_target_value_instance = DNSFilterTargetValue.from_json(json)
# print the JSON string representation of the object
print(DNSFilterTargetValue.to_json())

# convert the object into a dict
dns_filter_target_value_dict = dns_filter_target_value_instance.to_dict()
# create an instance of DNSFilterTargetValue from a dict
dns_filter_target_value_from_dict = DNSFilterTargetValue.from_dict(dns_filter_target_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



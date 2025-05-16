# HostAvailabilityRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_after** | **int** |  | [optional] 
**offline_duration** | **int** |  | [optional] 
**tag_filter** | [**TagFilter**](TagFilter.md) |  | [optional] 

## Example

```python
from instana_client.models.host_availability_rule import HostAvailabilityRule

# TODO update the JSON string below
json = "{}"
# create an instance of HostAvailabilityRule from a JSON string
host_availability_rule_instance = HostAvailabilityRule.from_json(json)
# print the JSON string representation of the object
print(HostAvailabilityRule.to_json())

# convert the object into a dict
host_availability_rule_dict = host_availability_rule_instance.to_dict()
# create an instance of HostAvailabilityRule from a dict
host_availability_rule_from_dict = HostAvailabilityRule.from_dict(host_availability_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



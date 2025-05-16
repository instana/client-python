# DNSActionFilterQueryTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from instana_client.models.dns_action_filter_query_time import DNSActionFilterQueryTime

# TODO update the JSON string below
json = "{}"
# create an instance of DNSActionFilterQueryTime from a JSON string
dns_action_filter_query_time_instance = DNSActionFilterQueryTime.from_json(json)
# print the JSON string representation of the object
print(DNSActionFilterQueryTime.to_json())

# convert the object into a dict
dns_action_filter_query_time_dict = dns_action_filter_query_time_instance.to_dict()
# create an instance of DNSActionFilterQueryTime from a dict
dns_action_filter_query_time_from_dict = DNSActionFilterQueryTime.from_dict(dns_action_filter_query_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



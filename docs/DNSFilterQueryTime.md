# DNSFilterQueryTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from instana_client.models.dns_filter_query_time import DNSFilterQueryTime

# TODO update the JSON string below
json = "{}"
# create an instance of DNSFilterQueryTime from a JSON string
dns_filter_query_time_instance = DNSFilterQueryTime.from_json(json)
# print the JSON string representation of the object
print(DNSFilterQueryTime.to_json())

# convert the object into a dict
dns_filter_query_time_dict = dns_filter_query_time_instance.to_dict()
# create an instance of DNSFilterQueryTime from a dict
dns_filter_query_time_from_dict = DNSFilterQueryTime.from_dict(dns_filter_query_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



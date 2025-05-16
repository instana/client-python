# DNSActionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_cname** | **bool** |  | [optional] 
**lookup** | **str** |  | 
**lookup_server_name** | **bool** |  | [optional] 
**port** | **int** |  | [optional] 
**query_time** | [**DNSActionFilterQueryTime**](DNSActionFilterQueryTime.md) |  | [optional] 
**query_type** | **str** |  | [optional] 
**recursive_lookups** | **bool** |  | [optional] 
**server** | **str** |  | 
**server_retries** | **int** |  | [optional] 
**target_values** | [**List[DNSActionFilterTargetValue]**](DNSActionFilterTargetValue.md) |  | [optional] 

## Example

```python
from instana_client.models.dns_action_configuration import DNSActionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DNSActionConfiguration from a JSON string
dns_action_configuration_instance = DNSActionConfiguration.from_json(json)
# print the JSON string representation of the object
print(DNSActionConfiguration.to_json())

# convert the object into a dict
dns_action_configuration_dict = dns_action_configuration_instance.to_dict()
# create an instance of DNSActionConfiguration from a dict
dns_action_configuration_from_dict = DNSActionConfiguration.from_dict(dns_action_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



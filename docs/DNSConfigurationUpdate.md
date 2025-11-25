# DNSConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_cname** | **bool** |  | [optional] 
**lookup** | **str** |  | [optional] 
**lookup_server_name** | **bool** |  | [optional] 
**port** | **int** |  | [optional] 
**query_time** | [**DNSFilterQueryTime**](DNSFilterQueryTime.md) |  | [optional] 
**query_type** | **str** |  | [optional] 
**recursive_lookups** | **bool** |  | [optional] 
**server** | **str** |  | [optional] 
**server_retries** | **int** |  | [optional] 
**target_values** | [**SyntheticResourceUpdateListDNSFilterTargetValueListDNSFilterTargetValue**](SyntheticResourceUpdateListDNSFilterTargetValueListDNSFilterTargetValue.md) |  | [optional] 
**transport** | **str** |  | [optional] 

## Example

```python
from instana_client.models.dns_configuration_update import DNSConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DNSConfigurationUpdate from a JSON string
dns_configuration_update_instance = DNSConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(DNSConfigurationUpdate.to_json())

# convert the object into a dict
dns_configuration_update_dict = dns_configuration_update_instance.to_dict()
# create an instance of DNSConfigurationUpdate from a dict
dns_configuration_update_from_dict = DNSConfigurationUpdate.from_dict(dns_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



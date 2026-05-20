# ICMPConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_count** | **int** |  | [optional] 
**packet_interval** | **str** |  | [optional] 
**packet_size** | **int** |  | [optional] 
**packet_timeout** | **str** |  | [optional] 
**target_host** | **str** |  | [optional] 
**use_dns** | **bool** |  | [optional] 
**use_ipv6** | **bool** |  | [optional] 
**validation_rules** | [**SyntheticResourceUpdateListICMPValidationListICMPValidation**](SyntheticResourceUpdateListICMPValidationListICMPValidation.md) |  | [optional] 

## Example

```python
from instana_client.models.icmp_configuration_update import ICMPConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ICMPConfigurationUpdate from a JSON string
icmp_configuration_update_instance = ICMPConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(ICMPConfigurationUpdate.to_json())

# convert the object into a dict
icmp_configuration_update_dict = icmp_configuration_update_instance.to_dict()
# create an instance of ICMPConfigurationUpdate from a dict
icmp_configuration_update_from_dict = ICMPConfigurationUpdate.from_dict(icmp_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



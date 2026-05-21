# ICMPConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packet_count** | **int** |  | [optional] 
**packet_interval** | **str** |  | [optional] 
**packet_size** | **int** |  | [optional] 
**packet_timeout** | **str** |  | [optional] 
**target_host** | **str** |  | 
**use_dns** | **bool** |  | [optional] 
**use_ipv6** | **bool** |  | [optional] 
**validation_rules** | [**List[ICMPValidation]**](ICMPValidation.md) |  | [optional] 

## Example

```python
from instana_client.models.icmp_configuration import ICMPConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ICMPConfiguration from a JSON string
icmp_configuration_instance = ICMPConfiguration.from_json(json)
# print the JSON string representation of the object
print(ICMPConfiguration.to_json())

# convert the object into a dict
icmp_configuration_dict = icmp_configuration_instance.to_dict()
# create an instance of ICMPConfiguration from a dict
icmp_configuration_from_dict = ICMPConfiguration.from_dict(icmp_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



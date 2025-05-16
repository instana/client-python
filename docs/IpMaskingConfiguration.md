# IpMaskingConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_masking** | **str** |  | 

## Example

```python
from instana_client.models.ip_masking_configuration import IpMaskingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of IpMaskingConfiguration from a JSON string
ip_masking_configuration_instance = IpMaskingConfiguration.from_json(json)
# print the JSON string representation of the object
print(IpMaskingConfiguration.to_json())

# convert the object into a dict
ip_masking_configuration_dict = ip_masking_configuration_instance.to_dict()
# create an instance of IpMaskingConfiguration from a dict
ip_masking_configuration_from_dict = IpMaskingConfiguration.from_dict(ip_masking_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



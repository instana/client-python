# SyntheticDatacenterConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addresses** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_datacenter_configuration import SyntheticDatacenterConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticDatacenterConfiguration from a JSON string
synthetic_datacenter_configuration_instance = SyntheticDatacenterConfiguration.from_json(json)
# print the JSON string representation of the object
print(SyntheticDatacenterConfiguration.to_json())

# convert the object into a dict
synthetic_datacenter_configuration_dict = synthetic_datacenter_configuration_instance.to_dict()
# create an instance of SyntheticDatacenterConfiguration from a dict
synthetic_datacenter_configuration_from_dict = SyntheticDatacenterConfiguration.from_dict(synthetic_datacenter_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



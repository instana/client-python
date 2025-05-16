# SyntheticLocationConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**tenant_type** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_location_configuration import SyntheticLocationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticLocationConfiguration from a JSON string
synthetic_location_configuration_instance = SyntheticLocationConfiguration.from_json(json)
# print the JSON string representation of the object
print(SyntheticLocationConfiguration.to_json())

# convert the object into a dict
synthetic_location_configuration_dict = synthetic_location_configuration_instance.to_dict()
# create an instance of SyntheticLocationConfiguration from a dict
synthetic_location_configuration_from_dict = SyntheticLocationConfiguration.from_dict(synthetic_location_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SyntheticConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_synthetic_call** | **bool** |  | [optional] 
**retries** | **int** |  | [optional] 
**retry_interval** | **int** |  | [optional] 
**timeout** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_configuration_update import SyntheticConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticConfigurationUpdate from a JSON string
synthetic_configuration_update_instance = SyntheticConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(SyntheticConfigurationUpdate.to_json())

# convert the object into a dict
synthetic_configuration_update_dict = synthetic_configuration_update_instance.to_dict()
# create an instance of SyntheticConfigurationUpdate from a dict
synthetic_configuration_update_from_dict = SyntheticConfigurationUpdate.from_dict(synthetic_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



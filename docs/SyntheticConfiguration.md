# SyntheticConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retries** | **int** |  | [optional] 
**retry_interval** | **int** |  | [optional] 
**timeout** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_configuration import SyntheticConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticConfiguration from a JSON string
synthetic_configuration_instance = SyntheticConfiguration.from_json(json)
# print the JSON string representation of the object
print(SyntheticConfiguration.to_json())

# convert the object into a dict
synthetic_configuration_dict = synthetic_configuration_instance.to_dict()
# create an instance of SyntheticConfiguration from a dict
synthetic_configuration_from_dict = SyntheticConfiguration.from_dict(synthetic_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



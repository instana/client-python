# SyntheticTestShallowUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**SyntheticConfigurationUpdate**](SyntheticConfigurationUpdate.md) |  | [optional] 

## Example

```python
from instana_client.models.synthetic_test_shallow_update import SyntheticTestShallowUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTestShallowUpdate from a JSON string
synthetic_test_shallow_update_instance = SyntheticTestShallowUpdate.from_json(json)
# print the JSON string representation of the object
print(SyntheticTestShallowUpdate.to_json())

# convert the object into a dict
synthetic_test_shallow_update_dict = synthetic_test_shallow_update_instance.to_dict()
# create an instance of SyntheticTestShallowUpdate from a dict
synthetic_test_shallow_update_from_dict = SyntheticTestShallowUpdate.from_dict(synthetic_test_shallow_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SyntheticTestCICD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customization** | [**SyntheticTestCICDCustomization**](SyntheticTestCICDCustomization.md) |  | 
**run_type** | **str** |  | [optional] 
**test_id** | **str** |  | 

## Example

```python
from instana_client.models.synthetic_test_cicd import SyntheticTestCICD

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTestCICD from a JSON string
synthetic_test_cicd_instance = SyntheticTestCICD.from_json(json)
# print the JSON string representation of the object
print(SyntheticTestCICD.to_json())

# convert the object into a dict
synthetic_test_cicd_dict = synthetic_test_cicd_instance.to_dict()
# create an instance of SyntheticTestCICD from a dict
synthetic_test_cicd_from_dict = SyntheticTestCICD.from_dict(synthetic_test_cicd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



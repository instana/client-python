# SyntheticTestCICDCustomization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**SyntheticConfiguration**](SyntheticConfiguration.md) |  | 
**custom_properties** | **Dict[str, str]** |  | [optional] 
**locations** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_test_cicd_customization import SyntheticTestCICDCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTestCICDCustomization from a JSON string
synthetic_test_cicd_customization_instance = SyntheticTestCICDCustomization.from_json(json)
# print the JSON string representation of the object
print(SyntheticTestCICDCustomization.to_json())

# convert the object into a dict
synthetic_test_cicd_customization_dict = synthetic_test_cicd_customization_instance.to_dict()
# create an instance of SyntheticTestCICDCustomization from a dict
synthetic_test_cicd_customization_from_dict = SyntheticTestCICDCustomization.from_dict(synthetic_test_cicd_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



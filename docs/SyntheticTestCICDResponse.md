# SyntheticTestCICDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | 
**test_id** | **str** |  | 
**test_result_id** | **str** |  | 

## Example

```python
from instana_client.models.synthetic_test_cicd_response import SyntheticTestCICDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTestCICDResponse from a JSON string
synthetic_test_cicd_response_instance = SyntheticTestCICDResponse.from_json(json)
# print the JSON string representation of the object
print(SyntheticTestCICDResponse.to_json())

# convert the object into a dict
synthetic_test_cicd_response_dict = synthetic_test_cicd_response_instance.to_dict()
# create an instance of SyntheticTestCICDResponse from a dict
synthetic_test_cicd_response_from_dict = SyntheticTestCICDResponse.from_dict(synthetic_test_cicd_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



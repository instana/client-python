# TestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_result** | [**List[TestResultItem]**](TestResultItem.md) |  | [optional] 
**test_result_items** | [**List[TestResultItem]**](TestResultItem.md) |  | [optional] 

## Example

```python
from instana_client.models.test_result import TestResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResult from a JSON string
test_result_instance = TestResult.from_json(json)
# print the JSON string representation of the object
print(TestResult.to_json())

# convert the object into a dict
test_result_dict = test_result_instance.to_dict()
# create an instance of TestResult from a dict
test_result_from_dict = TestResult.from_dict(test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



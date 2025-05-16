# TestResultListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TestResultListItem]**](TestResultListItem.md) |  | 
**page** | **int** | Page Number | [optional] 
**page_size** | **int** |  | [optional] 
**total_hits** | **int** |  | [optional] 

## Example

```python
from instana_client.models.test_result_list_result import TestResultListResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultListResult from a JSON string
test_result_list_result_instance = TestResultListResult.from_json(json)
# print the JSON string representation of the object
print(TestResultListResult.to_json())

# convert the object into a dict
test_result_list_result_dict = test_result_list_result_instance.to_dict()
# create an instance of TestResultListResult from a dict
test_result_list_result_from_dict = TestResultListResult.from_dict(test_result_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



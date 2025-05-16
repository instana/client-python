# GetTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**location_id** | **List[str]** |  | [optional] 
**metrics** | [**List[SyntheticMetricConfiguration]**](SyntheticMetricConfiguration.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**service_id** | **str** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[TagFilter]**](TagFilter.md) |  | [optional] 
**test_id** | **List[str]** |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_test_result import GetTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResult from a JSON string
get_test_result_instance = GetTestResult.from_json(json)
# print the JSON string representation of the object
print(GetTestResult.to_json())

# convert the object into a dict
get_test_result_dict = get_test_result_instance.to_dict()
# create an instance of GetTestResult from a dict
get_test_result_from_dict = GetTestResult.from_dict(get_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetTestSummaryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[SyntheticMetricConfiguration]**](SyntheticMetricConfiguration.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[TagFilter]**](TagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_test_summary_result import GetTestSummaryResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestSummaryResult from a JSON string
get_test_summary_result_instance = GetTestSummaryResult.from_json(json)
# print the JSON string representation of the object
print(GetTestSummaryResult.to_json())

# convert the object into a dict
get_test_summary_result_dict = get_test_summary_result_instance.to_dict()
# create an instance of GetTestSummaryResult from a dict
get_test_summary_result_from_dict = GetTestSummaryResult.from_dict(get_test_summary_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



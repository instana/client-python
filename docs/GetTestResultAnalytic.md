# GetTestResultAnalytic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_function** | **str** |  | 
**include_location_id_grouping** | **bool** |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**synthetic_metrics** | **List[str]** |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[TagFilter]**](TagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_test_result_analytic import GetTestResultAnalytic

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultAnalytic from a JSON string
get_test_result_analytic_instance = GetTestResultAnalytic.from_json(json)
# print the JSON string representation of the object
print(GetTestResultAnalytic.to_json())

# convert the object into a dict
get_test_result_analytic_dict = get_test_result_analytic_instance.to_dict()
# create an instance of GetTestResultAnalytic from a dict
get_test_result_analytic_from_dict = GetTestResultAnalytic.from_dict(get_test_result_analytic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



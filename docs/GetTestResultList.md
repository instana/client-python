# GetTestResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**synthetic_metrics** | **List[str]** |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[TagFilter]**](TagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_test_result_list import GetTestResultList

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultList from a JSON string
get_test_result_list_instance = GetTestResultList.from_json(json)
# print the JSON string representation of the object
print(GetTestResultList.to_json())

# convert the object into a dict
get_test_result_list_dict = get_test_result_list_instance.to_dict()
# create an instance of GetTestResultList from a dict
get_test_result_list_from_dict = GetTestResultList.from_dict(get_test_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



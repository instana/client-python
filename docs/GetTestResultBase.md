# GetTestResultBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[TagFilter]**](TagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_test_result_base import GetTestResultBase

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultBase from a JSON string
get_test_result_base_instance = GetTestResultBase.from_json(json)
# print the JSON string representation of the object
print(GetTestResultBase.to_json())

# convert the object into a dict
get_test_result_base_dict = get_test_result_base_instance.to_dict()
# create an instance of GetTestResultBase from a dict
get_test_result_base_from_dict = GetTestResultBase.from_dict(get_test_result_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



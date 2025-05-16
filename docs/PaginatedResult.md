# PaginatedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[object]** |  | 
**page** | **int** | Page Number | [optional] 
**page_size** | **int** |  | [optional] 
**total_hits** | **int** |  | [optional] 

## Example

```python
from instana_client.models.paginated_result import PaginatedResult

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResult from a JSON string
paginated_result_instance = PaginatedResult.from_json(json)
# print the JSON string representation of the object
print(PaginatedResult.to_json())

# convert the object into a dict
paginated_result_dict = paginated_result_instance.to_dict()
# create an instance of PaginatedResult from a dict
paginated_result_from_dict = PaginatedResult.from_dict(paginated_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



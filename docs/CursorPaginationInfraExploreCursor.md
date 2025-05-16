# CursorPaginationInfraExploreCursor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **object** | cursor to use between successive queries | [optional] 
**retrieval_size** | **int** | number of values to return | 

## Example

```python
from instana_client.models.cursor_pagination_infra_explore_cursor import CursorPaginationInfraExploreCursor

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaginationInfraExploreCursor from a JSON string
cursor_pagination_infra_explore_cursor_instance = CursorPaginationInfraExploreCursor.from_json(json)
# print the JSON string representation of the object
print(CursorPaginationInfraExploreCursor.to_json())

# convert the object into a dict
cursor_pagination_infra_explore_cursor_dict = cursor_pagination_infra_explore_cursor_instance.to_dict()
# create an instance of CursorPaginationInfraExploreCursor from a dict
cursor_pagination_infra_explore_cursor_from_dict = CursorPaginationInfraExploreCursor.from_dict(cursor_pagination_infra_explore_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



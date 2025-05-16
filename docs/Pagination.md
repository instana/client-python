# Pagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page number for a specific page in the results. For example, if you&#39;d like to retrieve the 5th page out of 10 pages, the value would be 5. | [optional] 
**page_size** | **int** | Set the number of items you want to return with one query. Eg: if you want to retrieve 10 items, the value would be 10. | [optional] 

## Example

```python
from instana_client.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



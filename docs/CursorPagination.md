# CursorPagination

Details for controlling the pagination of the API response. This object allows you to define the starting point for retrieving records, how many records to skip, and the size of the result set. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingestion_time** | **int** | The timestamp indicating the starting point from which data was ingested. The format of the timestamp is in Unix epoch Time. For example, &#x60;Thursday, 5 September 2024 07:03:13 GMT&#x60; can be represented as &#x60;1725519793&#x60;.  | [optional] 
**offset** | **int** | The number of records to be skipped from the &#x60;ingestionTime&#x60;. For example: when &#x60;offset&#x60; is 20 and &#x60;ingestionTime&#x60; is 1725519793, the API response should have records starting from the 21st record after the specified &#x60;ingestionTime&#x60;. Note that if &#x60;offset&#x60; value is not empty, &#x60;ingestionTime&#x60; can&#39;t be empty.  | [optional] 
**retrieval_size** | **int** | The number of records to retrieve in a single request. For example, when retrievalSize is set to 30, offset is 20, and ingestionTime is 1725519793, the API request will fetch 30 records starting from the 21st record after the specified &#x60;ingestionTime&#x60;. Minimum value is 1 and maximum value is 200.  | [optional] 

## Example

```python
from instana_client.models.cursor_pagination import CursorPagination

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPagination from a JSON string
cursor_pagination_instance = CursorPagination.from_json(json)
# print the JSON string representation of the object
print(CursorPagination.to_json())

# convert the object into a dict
cursor_pagination_dict = cursor_pagination_instance.to_dict()
# create an instance of CursorPagination from a dict
cursor_pagination_from_dict = CursorPagination.from_dict(cursor_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



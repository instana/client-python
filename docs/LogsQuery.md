# LogsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**FilterInterface**](FilterInterface.md) |  | [optional] 
**offset** | **int** |  | [optional] 
**order_direction** | **str** |  | [optional] 
**requested_tags** | **List[str]** |  | [optional] 
**retrieval_size** | **int** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**time_config** | [**TimeConfig**](TimeConfig.md) |  | [optional] 

## Example

```python
from instana_client.models.logs_query import LogsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LogsQuery from a JSON string
logs_query_instance = LogsQuery.from_json(json)
# print the JSON string representation of the object
print(LogsQuery.to_json())

# convert the object into a dict
logs_query_dict = logs_query_instance.to_dict()
# create an instance of LogsQuery from a dict
logs_query_from_dict = LogsQuery.from_dict(logs_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



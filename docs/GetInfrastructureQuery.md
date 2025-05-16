# GetInfrastructureQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[InfraMetricConfiguration]**](InfraMetricConfiguration.md) |  | [optional] 
**missing_placeholder** | **str** |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**CursorPaginationInfraExploreCursor**](CursorPaginationInfraExploreCursor.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**tags** | **List[str]** |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | 
**type** | **str** | Type of entities | [optional] 

## Example

```python
from instana_client.models.get_infrastructure_query import GetInfrastructureQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfrastructureQuery from a JSON string
get_infrastructure_query_instance = GetInfrastructureQuery.from_json(json)
# print the JSON string representation of the object
print(GetInfrastructureQuery.to_json())

# convert the object into a dict
get_infrastructure_query_dict = get_infrastructure_query_instance.to_dict()
# create an instance of GetInfrastructureQuery from a dict
get_infrastructure_query_from_dict = GetInfrastructureQuery.from_dict(get_infrastructure_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



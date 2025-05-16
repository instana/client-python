# GetInfrastructureGroupsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **List[str]** | Entity grouping tag. Use the Instana Analyze Infrastructure dashboard to determine the entity grouping tag name. | 
**metrics** | [**List[InfraMetricConfiguration]**](InfraMetricConfiguration.md) |  | [optional] 
**missing_placeholder** | **str** |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**CursorPaginationInfraExploreCursor**](CursorPaginationInfraExploreCursor.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | 
**type** | **str** | Type of entities | [optional] 

## Example

```python
from instana_client.models.get_infrastructure_groups_query import GetInfrastructureGroupsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfrastructureGroupsQuery from a JSON string
get_infrastructure_groups_query_instance = GetInfrastructureGroupsQuery.from_json(json)
# print the JSON string representation of the object
print(GetInfrastructureGroupsQuery.to_json())

# convert the object into a dict
get_infrastructure_groups_query_dict = get_infrastructure_groups_query_instance.to_dict()
# create an instance of GetInfrastructureGroupsQuery from a dict
get_infrastructure_groups_query_from_dict = GetInfrastructureGroupsQuery.from_dict(get_infrastructure_groups_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetCallGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Group**](Group.md) |  | 
**include_internal** | **bool** | Flag to include Internal Calls. These calls are work done inside a service and correspond to intermediate spans in custom tracing. | [optional] 
**include_synthetic** | **bool** | Flag to include Synthetic Calls. These calls have a synthetic endpoint as their destination, such as calls to health-check endpoints. | [optional] 
**metrics** | [**List[MetricConfig]**](MetricConfig.md) | A list of objects each of which defines a metric and the (statistical) aggregation -- MEAN, SUM, MAX, etc -- that should be used to summarize it for the defined time frame. Eg: &#x60;[{ &#39;metric&#39;: &#39;latency&#39;, &#39;aggregation&#39;: &#39;MEAN&#39;}]&#x60;. To know more about supported metrics and its aggregation, See &#x60;Get Metric catalog&#x60;. | 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[DeprecatedTagFilter]**](DeprecatedTagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_call_groups import GetCallGroups

# TODO update the JSON string below
json = "{}"
# create an instance of GetCallGroups from a JSON string
get_call_groups_instance = GetCallGroups.from_json(json)
# print the JSON string representation of the object
print(GetCallGroups.to_json())

# convert the object into a dict
get_call_groups_dict = get_call_groups_instance.to_dict()
# create an instance of GetCallGroups from a dict
get_call_groups_from_dict = GetCallGroups.from_dict(get_call_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



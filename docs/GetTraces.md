# GetTraces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_internal** | **bool** | Flag to include Internal Calls. These calls are work done inside a service and correspond to intermediate spans in custom tracing. | [optional] 
**include_synthetic** | **bool** | Flag to include Synthetic Calls. These calls have a synthetic endpoint as their destination, such as calls to health-check endpoints. | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[DeprecatedTagFilter]**](DeprecatedTagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_traces import GetTraces

# TODO update the JSON string below
json = "{}"
# create an instance of GetTraces from a JSON string
get_traces_instance = GetTraces.from_json(json)
# print the JSON string representation of the object
print(GetTraces.to_json())

# convert the object into a dict
get_traces_dict = get_traces_instance.to_dict()
# create an instance of GetTraces from a dict
get_traces_from_dict = GetTraces.from_dict(get_traces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



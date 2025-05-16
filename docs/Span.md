# Span


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_self_time** | **int** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**calculated_self_time** | **int** |  | [optional] 
**call_id** | **str** |  | 
**child_spans** | [**List[Span]**](Span.md) |  | 
**data** | **Dict[str, object]** |  | 
**destination** | [**SpanRelation**](SpanRelation.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**foreign_parent_id** | **str** |  | [optional] 
**id** | **str** |  | 
**is_synthetic** | **bool** |  | [optional] 
**kind** | **str** |  | 
**label** | **str** |  | 
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**source** | [**SpanRelation**](SpanRelation.md) |  | [optional] 
**stack_trace** | [**List[StackTraceItem]**](StackTraceItem.md) |  | 
**start** | **int** |  | [optional] 

## Example

```python
from instana_client.models.span import Span

# TODO update the JSON string below
json = "{}"
# create an instance of Span from a JSON string
span_instance = Span.from_json(json)
# print the JSON string representation of the object
print(Span.to_json())

# convert the object into a dict
span_dict = span_instance.to_dict()
# create an instance of Span from a dict
span_from_dict = Span.from_dict(span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



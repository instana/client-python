# SpanExcerpt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 
**database_integrations** | [**List[DatabaseIntegration]**](DatabaseIntegration.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**foreign_parent_id** | **str** |  | [optional] 
**id** | **str** |  | 
**kind** | **str** |  | 
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**stack_trace** | [**List[StackTraceItem]**](StackTraceItem.md) |  | 
**start** | **int** |  | [optional] 

## Example

```python
from instana_client.models.span_excerpt import SpanExcerpt

# TODO update the JSON string below
json = "{}"
# create an instance of SpanExcerpt from a JSON string
span_excerpt_instance = SpanExcerpt.from_json(json)
# print the JSON string representation of the object
print(SpanExcerpt.to_json())

# convert the object into a dict
span_excerpt_dict = span_excerpt_instance.to_dict()
# create an instance of SpanExcerpt from a dict
span_excerpt_from_dict = SpanExcerpt.from_dict(span_excerpt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SpanExcerpt

Information about the logs attached to the call, if available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Some information about the span, like service name, if it is an http call, then some information about it like, path, method, host, errors etc. | 
**database_integrations** | [**List[DatabaseIntegration]**](DatabaseIntegration.md) |  | [optional] 
**duration** | **int** | The total time taken for the entire operation of a call, from the moment the request was initiated to when the response was received. The time measured is in milliseconds. This is also known as latency of a call. | [optional] 
**error_count** | **int** | Represents whether the span is erroneous or not. 0 is not erroneous and 1 is erroneous. | [optional] 
**foreign_parent_id** | **str** |  | [optional] 
**id** | **str** | The call ID. A unique identifier for an individual call. For example: &#x60;1bcad5c82338deaf&#x60;. | 
**kind** | **str** | There are 4 types of span kind: 1. &#x60;ENTRY&#x60;: An entry span represents an incoming request into a traced service. 2. &#x60;EXIT&#x60;: An exit span represents an outgoing request that a service makes to some other service. 3. &#x60;INTERMEDIATE&#x60;: An intermediate span represents anything that happens inside a traced service where the flow of control neither enters nor leaves that service, but stays inside it. 4. &#x60;UNKNOWN&#x60;: Instana can&#39;t determine the span kind.  | 
**name** | **str** | The technical type of the span. For example, &#x60;node.http.client&#x60; or &#x60;jdbc&#x60;. | 
**parent_id** | **str** | The parent call id, referring to another call in the same trace which triggered the processing associated with this call. | [optional] 
**stack_trace** | [**List[StackTraceItem]**](StackTraceItem.md) | For an erroneous call, if stack trace is available it will show a list of items containing file, method and line number of the code. | 
**start** | **int** | The timestamp when the call or request was initiated. For example, Unix epoch time in milliseconds &#x60;1735532879870&#x60; is &#x60;Monday, 30 December 2024 04:27:59.870 GMT&#x60; | [optional] 

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



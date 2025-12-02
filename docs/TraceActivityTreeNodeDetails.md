# TraceActivityTreeNodeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_self_time** | **int** | Sum of all self times in a batch of calls. For example, if 5 calls are in a batch and its self times are : &#x60;[1,2,3,4,5]&#x60; in milliseconds, then the batch self time would be sum of the self times, in this case, it will be 15 milliseconds.  | [optional] 
**batch_size** | **int** | Number of calls in a batch. | [optional] 
**destination** | [**SpanRelation**](SpanRelation.md) |  | [optional] 
**duration** | **int** | The total time taken for the entire operation of a call, from the moment the request was initiated to when the response was received. The time measured is in milliseconds. This is also known as latency of a call. | [optional] 
**error_count** | **int** | Represents whether the call is erroneous or not. 0 is not erroneous and 1 is erroneous. | [optional] 
**id** | **str** | The call ID. A unique identifier for an individual call. For example: &#x60;1bcad5c82338deaf&#x60;. | 
**is_synthetic** | **bool** |  | [optional] 
**label** | **str** | Name of the call. For example: &#x60;GET /articles/:id&#x60;. | 
**logs** | [**List[SpanExcerpt]**](SpanExcerpt.md) | Information about the logs attached to the call, if available. | 
**min_self_time** | **int** | The smallest self time in the batch. May be null to indicate that &#x60;minSelfTime&#x60; is unknown when this node has only an exit span and no children. The time measured is in milliseconds. | [optional] 
**network_time** | **int** | The time difference between the Exit Span Time of the caller and the Entry Span Time of the call. This value is measured in milliseconds and may be null if network time is not applicable. | [optional] 
**raw_span_load_error** | **str** | Whether an error occurred loading raw spans from external storage. | [optional] 
**source** | [**SpanRelation**](SpanRelation.md) |  | [optional] 
**spans** | [**List[SpanExcerpt]**](SpanExcerpt.md) | Information about the spans from which the call is composed. | 
**start** | **int** | The timestamp when the call or request was initiated. For example, Unix epoch time in milliseconds &#x60;1735532879870&#x60; is &#x60;Monday, 30 December 2024 04:27:59.870 GMT&#x60; | [optional] 
**synthetic** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.trace_activity_tree_node_details import TraceActivityTreeNodeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TraceActivityTreeNodeDetails from a JSON string
trace_activity_tree_node_details_instance = TraceActivityTreeNodeDetails.from_json(json)
# print the JSON string representation of the object
print(TraceActivityTreeNodeDetails.to_json())

# convert the object into a dict
trace_activity_tree_node_details_dict = trace_activity_tree_node_details_instance.to_dict()
# create an instance of TraceActivityTreeNodeDetails from a dict
trace_activity_tree_node_details_from_dict = TraceActivityTreeNodeDetails.from_dict(trace_activity_tree_node_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



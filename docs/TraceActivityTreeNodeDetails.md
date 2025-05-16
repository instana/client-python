# TraceActivityTreeNodeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_self_time** | **int** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**destination** | [**SpanRelation**](SpanRelation.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**id** | **str** |  | 
**is_synthetic** | **bool** |  | [optional] 
**label** | **str** |  | 
**logs** | [**List[SpanExcerpt]**](SpanExcerpt.md) |  | 
**min_self_time** | **int** |  | [optional] 
**network_time** | **int** |  | [optional] 
**source** | [**SpanRelation**](SpanRelation.md) |  | [optional] 
**spans** | [**List[SpanExcerpt]**](SpanExcerpt.md) |  | 
**start** | **int** |  | [optional] 
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



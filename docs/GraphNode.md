# GraphNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**entity_id** | [**EntityId**](EntityId.md) |  | [optional] 
**id** | **str** | GraphNode ID. | [optional] 
**label** | **str** | Label of the entity | [optional] 
**plugin** | **str** | Name of the plugin | [optional] 

## Example

```python
from instana_client.models.graph_node import GraphNode

# TODO update the JSON string below
json = "{}"
# create an instance of GraphNode from a JSON string
graph_node_instance = GraphNode.from_json(json)
# print the JSON string representation of the object
print(GraphNode.to_json())

# convert the object into a dict
graph_node_dict = graph_node_instance.to_dict()
# create an instance of GraphNode from a dict
graph_node_from_dict = GraphNode.from_dict(graph_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



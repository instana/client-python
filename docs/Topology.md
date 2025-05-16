# Topology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[GraphEdge]**](GraphEdge.md) |  | [optional] 
**nodes** | [**List[GraphNode]**](GraphNode.md) |  | [optional] 

## Example

```python
from instana_client.models.topology import Topology

# TODO update the JSON string below
json = "{}"
# create an instance of Topology from a JSON string
topology_instance = Topology.from_json(json)
# print the JSON string representation of the object
print(Topology.to_json())

# convert the object into a dict
topology_dict = topology_instance.to_dict()
# create an instance of Topology from a dict
topology_from_dict = Topology.from_dict(topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



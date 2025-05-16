# ServiceNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**Dict[str, EndpointNode]**](EndpointNode.md) |  | 
**inclusive** | **bool** |  | [optional] 
**service_id** | **str** |  | 

## Example

```python
from instana_client.models.service_node import ServiceNode

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNode from a JSON string
service_node_instance = ServiceNode.from_json(json)
# print the JSON string representation of the object
print(ServiceNode.to_json())

# convert the object into a dict
service_node_dict = service_node_instance.to_dict()
# create an instance of ServiceNode from a dict
service_node_from_dict = ServiceNode.from_dict(service_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



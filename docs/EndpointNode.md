# EndpointNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** |  | 
**inclusive** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.endpoint_node import EndpointNode

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointNode from a JSON string
endpoint_node_instance = EndpointNode.from_json(json)
# print the JSON string representation of the object
print(EndpointNode.to_json())

# convert the object into a dict
endpoint_node_dict = endpoint_node_instance.to_dict()
# create an instance of EndpointNode from a dict
endpoint_node_from_dict = EndpointNode.from_dict(endpoint_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



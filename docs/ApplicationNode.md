# ApplicationNode

Selection of applications, services, and endpoints that this Smart Alert configuration is associated with. This selection is connected to the defined `tagFilterExpression` by the logical `AND` operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**inclusive** | **bool** |  | [optional] 
**services** | [**Dict[str, ServiceNode]**](ServiceNode.md) |  | 

## Example

```python
from instana_client.models.application_node import ApplicationNode

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationNode from a JSON string
application_node_instance = ApplicationNode.from_json(json)
# print the JSON string representation of the object
print(ApplicationNode.to_json())

# convert the object into a dict
application_node_dict = application_node_instance.to_dict()
# create an instance of ApplicationNode from a dict
application_node_from_dict = ApplicationNode.from_dict(application_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EndpointItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**Endpoint**](Endpoint.md) |  | 
**metrics** | **Dict[str, List[List[float]]]** |  | 

## Example

```python
from instana_client.models.endpoint_item import EndpointItem

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointItem from a JSON string
endpoint_item_instance = EndpointItem.from_json(json)
# print the JSON string representation of the object
print(EndpointItem.to_json())

# convert the object into a dict
endpoint_item_dict = endpoint_item_instance.to_dict()
# create an instance of EndpointItem from a dict
endpoint_item_from_dict = EndpointItem.from_dict(endpoint_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



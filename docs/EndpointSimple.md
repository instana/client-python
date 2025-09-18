# EndpointSimple

The destination service's endpoint where the call enters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Endpoint. Eg: &#x60;NCRq5oYnan5x-PkdTPQwLLUdu5M&#x60;. | [optional] 
**label** | **str** | Name of the Endpoint. Eg: &#x60;GET /api/fetch&#x60;. | [optional] 
**type** | **str** | The type of the Endpoint. | [optional] 

## Example

```python
from instana_client.models.endpoint_simple import EndpointSimple

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointSimple from a JSON string
endpoint_simple_instance = EndpointSimple.from_json(json)
# print the JSON string representation of the object
print(EndpointSimple.to_json())

# convert the object into a dict
endpoint_simple_dict = endpoint_simple_instance.to_dict()
# create an instance of EndpointSimple from a dict
endpoint_simple_from_dict = EndpointSimple.from_dict(endpoint_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



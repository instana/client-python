# Endpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Since, this is a Endpoint, it will be of type &#x60;ENDPOINT&#x60;. | [optional] 
**id** | **str** | Unique ID of the Endpoint. Eg: &#x60;NCRq5oYnan5x-PkdTPQwLLUdu5M&#x60;. | 
**is_synthetic** | **bool** |  | [optional] 
**label** | **str** | Name of the Endpoint. Eg: &#x60;GET /api/fetch&#x60;. | 
**service_id** | **str** | The serviceId this endpoint belongs to. | 
**synthetic** | **bool** |  | [optional] 
**synthetic_type** | **str** |  | [optional] 
**technologies** | **List[str]** | List of technologies: &#x60;Eg:[\&quot;springbootApplicationContainer\&quot;]&#x60; | 
**type** | **str** | The type of the Endpoint. | 

## Example

```python
from instana_client.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print(Endpoint.to_json())

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_from_dict = Endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[ServiceMapConnection]**](ServiceMapConnection.md) | A list which indicates which services are consumers and which are providers in the communication chain. | 
**services** | [**List[ExtendedService]**](ExtendedService.md) | List of services in the topology. | 

## Example

```python
from instana_client.models.service_map import ServiceMap

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMap from a JSON string
service_map_instance = ServiceMap.from_json(json)
# print the JSON string representation of the object
print(ServiceMap.to_json())

# convert the object into a dict
service_map_dict = service_map_instance.to_dict()
# create an instance of ServiceMap from a dict
service_map_from_dict = ServiceMap.from_dict(service_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



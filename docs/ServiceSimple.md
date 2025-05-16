# ServiceSimple

The destination service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Service. Eg: &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. | [optional] 
**label** | **str** | Name of the Service. Eg: &#x60;payment&#x60;. | [optional] 

## Example

```python
from instana_client.models.service_simple import ServiceSimple

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSimple from a JSON string
service_simple_instance = ServiceSimple.from_json(json)
# print the JSON string representation of the object
print(ServiceSimple.to_json())

# convert the object into a dict
service_simple_dict = service_simple_instance.to_dict()
# create an instance of ServiceSimple from a dict
service_simple_from_dict = ServiceSimple.from_dict(service_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Service

Returns a list of Services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Since, this is a Service, it will be of type &#x60;SERVICE&#x60;. | [optional] 
**id** | **str** | Unique ID of the Service. Eg: &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. | 
**label** | **str** | Name of the Service. Eg: &#x60;payment&#x60;. | 
**snapshot_ids** | **List[str]** | A unique identifier the metrics are assigned to. | 
**technologies** | **List[str]** | List of technologies: &#x60;Eg:[\&quot;springbootApplicationContainer\&quot;]&#x60; | 
**types** | **List[str]** | Shows types of Endpoints a Service can consist of. It may be one or more. Eg: &#x60;HTTP&#x60; &#x60;OPENTELEMETRY&#x60; can be in 1 Service. | 

## Example

```python
from instana_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



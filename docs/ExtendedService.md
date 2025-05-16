# ExtendedService

List of services in the topology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** |  | 
**entity_type** | **str** | Since, this is a Service, it will be of type &#x60;SERVICE&#x60;. | [optional] 
**id** | **str** | Unique ID of the Service. Eg: &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. | 
**label** | **str** | Name of the Service. Eg: &#x60;payment&#x60;. | 
**max_severity** | **float** |  | [optional] 
**number_of_open_issues** | **int** |  | [optional] 
**snapshot_ids** | **List[str]** | A unique identifier the metrics are assigned to. | 
**technologies** | **List[str]** | List of technologies: &#x60;Eg:[\&quot;springbootApplicationContainer\&quot;]&#x60; | 
**types** | **List[str]** | Shows types of Endpoints a Service can consist of. It may be one or more. Eg: &#x60;HTTP&#x60; &#x60;OPENTELEMETRY&#x60; can be in 1 Service. | 

## Example

```python
from instana_client.models.extended_service import ExtendedService

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedService from a JSON string
extended_service_instance = ExtendedService.from_json(json)
# print the JSON string representation of the object
print(ExtendedService.to_json())

# convert the object into a dict
extended_service_dict = extended_service_instance.to_dict()
# create an instance of ExtendedService from a dict
extended_service_from_dict = ExtendedService.from_dict(extended_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



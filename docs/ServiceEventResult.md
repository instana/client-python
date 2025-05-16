# ServiceEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**probable_root_cause** | **Dict[str, object]** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.service_event_result import ServiceEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEventResult from a JSON string
service_event_result_instance = ServiceEventResult.from_json(json)
# print the JSON string representation of the object
print(ServiceEventResult.to_json())

# convert the object into a dict
service_event_result_dict = service_event_result_instance.to_dict()
# create an instance of ServiceEventResult from a dict
service_event_result_from_dict = ServiceEventResult.from_dict(service_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EndpointEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**endpoint_id** | **str** |  | [optional] 
**endpoint_service_id** | **str** |  | [optional] 
**probable_root_cause** | **Dict[str, object]** |  | [optional] 

## Example

```python
from instana_client.models.endpoint_event_result import EndpointEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointEventResult from a JSON string
endpoint_event_result_instance = EndpointEventResult.from_json(json)
# print the JSON string representation of the object
print(EndpointEventResult.to_json())

# convert the object into a dict
endpoint_event_result_dict = endpoint_event_result_instance.to_dict()
# create an instance of EndpointEventResult from a dict
endpoint_event_result_from_dict = EndpointEventResult.from_dict(endpoint_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



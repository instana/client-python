# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | [optional] 
**endpoint_service_id** | **str** |  | [optional] 
**entity_id** | **str** |  | 
**entity_type** | **str** |  | [optional] 
**event_configuration_type** | **str** |  | [optional] 
**id** | **str** |  | 
**long_form_plugin_id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**metric_access_id** | **str** |  | [optional] 
**plugin** | **str** |  | 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**rca** | **Dict[str, object]** |  | [optional] 
**start** | **int** |  | [optional] 
**state** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from instana_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



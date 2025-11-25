# EventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Details of the event. | [optional] 
**end** | **int** | A Unix timestamp representing the end time of the Event. | [optional] 
**entity_label** | **str** | The label of the affected entity of the event. | [optional] 
**entity_name** | **str** | The name or type of the affected entity of the event. | [optional] 
**entity_type** | **str** | The category of the affected entity. | [optional] 
**event_id** | **str** | ID of this Event. | [optional] 
**event_specification_id** | **str** | ID of the configuration that created this event. | [optional] 
**fix_suggestion** | **str** | Details of the event. | [optional] 
**metrics** | **List[Dict[str, object]]** | List of metrics associated with the Event. | [optional] 
**probable_cause** | **Dict[str, object]** | Metadata of the probable root cause for this event. Only present in case of specific \&quot;Incident\&quot; type events. | [optional] 
**problem** | **str** | Main problem title of the Event. | [optional] 
**recent_events** | **List[Dict[str, object]]** | List of related recent events. Only present in case of \&quot;Incident\&quot; type events. | [optional] 
**severity** | **int** | The severity of the Event when triggered. | [optional] 
**short_code** | **str** | A short code for the event | [optional] 
**snapshot_id** | **str** | The snapshot ID of the affected entity of this event. | [optional] 
**start** | **int** | A Unix timestamp representing the start time of the Event. | [optional] 
**state** | **str** | The state of the Event, \&quot;open\&quot; or \&quot;close\&quot;.  | [optional] 
**type** | **str** | The type of Event. | [optional] 

## Example

```python
from instana_client.models.event_result import EventResult

# TODO update the JSON string below
json = "{}"
# create an instance of EventResult from a JSON string
event_result_instance = EventResult.from_json(json)
# print the JSON string representation of the object
print(EventResult.to_json())

# convert the object into a dict
event_result_dict = event_result_instance.to_dict()
# create an instance of EventResult from a dict
event_result_from_dict = EventResult.from_dict(event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



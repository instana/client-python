# ApplicationEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**probable_root_cause** | **Dict[str, object]** |  | [optional] 

## Example

```python
from instana_client.models.application_event_result import ApplicationEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEventResult from a JSON string
application_event_result_instance = ApplicationEventResult.from_json(json)
# print the JSON string representation of the object
print(ApplicationEventResult.to_json())

# convert the object into a dict
application_event_result_dict = application_event_result_instance.to_dict()
# create an instance of ApplicationEventResult from a dict
application_event_result_from_dict = ApplicationEventResult.from_dict(application_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



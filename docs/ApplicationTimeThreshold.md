# ApplicationTimeThreshold

The type of threshold to define the criteria when the event and alert triggers and resolves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.application_time_threshold import ApplicationTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationTimeThreshold from a JSON string
application_time_threshold_instance = ApplicationTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(ApplicationTimeThreshold.to_json())

# convert the object into a dict
application_time_threshold_dict = application_time_threshold_instance.to_dict()
# create an instance of ApplicationTimeThreshold from a dict
application_time_threshold_from_dict = ApplicationTimeThreshold.from_dict(application_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



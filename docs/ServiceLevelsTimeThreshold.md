# ServiceLevelsTimeThreshold

This is the warm-up and cool-down setting to emit or stop alert event after threshold reached.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **int** | This is the cooldown period when the active alert misses threshold and stop emitting notification. | 
**time_window** | **int** | This is the grace period when the threshold is reached and the alert becomes active to emit notification. | 

## Example

```python
from instana_client.models.service_levels_time_threshold import ServiceLevelsTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelsTimeThreshold from a JSON string
service_levels_time_threshold_instance = ServiceLevelsTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelsTimeThreshold.to_json())

# convert the object into a dict
service_levels_time_threshold_dict = service_levels_time_threshold_instance.to_dict()
# create an instance of ServiceLevelsTimeThreshold from a dict
service_levels_time_threshold_from_dict = ServiceLevelsTimeThreshold.from_dict(service_levels_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



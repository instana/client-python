# MonitoringState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_entities** | **bool** | Has entities | [optional] 
**host_count** | **int** | Count of hosts | [optional] 
**monitored_entities_stats** | [**MonitoredEntitiesStats**](MonitoredEntitiesStats.md) |  | [optional] 
**open_telemetry_count** | **int** | Count of open telemetry | [optional] 
**serverless_count** | **int** | Count of serverless | [optional] 

## Example

```python
from instana_client.models.monitoring_state import MonitoringState

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringState from a JSON string
monitoring_state_instance = MonitoringState.from_json(json)
# print the JSON string representation of the object
print(MonitoringState.to_json())

# convert the object into a dict
monitoring_state_dict = monitoring_state_instance.to_dict()
# create an instance of MonitoringState from a dict
monitoring_state_from_dict = MonitoringState.from_dict(monitoring_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



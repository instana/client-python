# MonitoredEntitiesStats

Statistics of monitored entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_count** | **int** |  | [optional] 
**otel_count** | **int** |  | [optional] 
**serverless_count** | **int** |  | [optional] 

## Example

```python
from instana_client.models.monitored_entities_stats import MonitoredEntitiesStats

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredEntitiesStats from a JSON string
monitored_entities_stats_instance = MonitoredEntitiesStats.from_json(json)
# print the JSON string representation of the object
print(MonitoredEntitiesStats.to_json())

# convert the object into a dict
monitored_entities_stats_dict = monitored_entities_stats_instance.to_dict()
# create an instance of MonitoredEntitiesStats from a dict
monitored_entities_stats_from_dict = MonitoredEntitiesStats.from_dict(monitored_entities_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



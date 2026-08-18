# TraceSamplingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**enabled** | **bool** |  | 
**evaluation_window_minutes** | **int** |  | [optional] 
**retention_percentage** | **float** |  | [optional] 
**sampling_frequency_hours** | **int** |  | [optional] 
**sampling_rate** | **float** |  | [optional] 
**sampling_type** | **str** |  | 
**tenant_unit_id** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**volume_strategy** | **str** |  | 

## Example

```python
from instana_client.models.trace_sampling_config import TraceSamplingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TraceSamplingConfig from a JSON string
trace_sampling_config_instance = TraceSamplingConfig.from_json(json)
# print the JSON string representation of the object
print(TraceSamplingConfig.to_json())

# convert the object into a dict
trace_sampling_config_dict = trace_sampling_config_instance.to_dict()
# create an instance of TraceSamplingConfig from a dict
trace_sampling_config_from_dict = TraceSamplingConfig.from_dict(trace_sampling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



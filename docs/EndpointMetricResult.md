# EndpointMetricResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**items** | [**List[EndpointItem]**](EndpointItem.md) |  | 
**page** | **int** | Page Number | [optional] 
**page_size** | **int** |  | [optional] 
**total_hits** | **int** |  | [optional] 

## Example

```python
from instana_client.models.endpoint_metric_result import EndpointMetricResult

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointMetricResult from a JSON string
endpoint_metric_result_instance = EndpointMetricResult.from_json(json)
# print the JSON string representation of the object
print(EndpointMetricResult.to_json())

# convert the object into a dict
endpoint_metric_result_dict = endpoint_metric_result_instance.to_dict()
# create an instance of EndpointMetricResult from a dict
endpoint_metric_result_from_dict = EndpointMetricResult.from_dict(endpoint_metric_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



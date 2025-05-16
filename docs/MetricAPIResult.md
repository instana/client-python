# MetricAPIResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**metrics** | **Dict[str, List[List[float]]]** |  | 

## Example

```python
from instana_client.models.metric_api_result import MetricAPIResult

# TODO update the JSON string below
json = "{}"
# create an instance of MetricAPIResult from a JSON string
metric_api_result_instance = MetricAPIResult.from_json(json)
# print the JSON string representation of the object
print(MetricAPIResult.to_json())

# convert the object into a dict
metric_api_result_dict = metric_api_result_instance.to_dict()
# create an instance of MetricAPIResult from a dict
metric_api_result_from_dict = MetricAPIResult.from_dict(metric_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



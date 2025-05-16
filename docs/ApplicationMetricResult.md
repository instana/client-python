# ApplicationMetricResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**items** | [**List[ApplicationItem]**](ApplicationItem.md) |  | 
**page** | **int** | Page Number | [optional] 
**page_size** | **int** |  | [optional] 
**total_hits** | **int** |  | [optional] 

## Example

```python
from instana_client.models.application_metric_result import ApplicationMetricResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetricResult from a JSON string
application_metric_result_instance = ApplicationMetricResult.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetricResult.to_json())

# convert the object into a dict
application_metric_result_dict = application_metric_result_instance.to_dict()
# create an instance of ApplicationMetricResult from a dict
application_metric_result_from_dict = ApplicationMetricResult.from_dict(application_metric_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



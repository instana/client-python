# ServiceMetricResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**items** | [**List[ServiceItem]**](ServiceItem.md) |  | 
**page** | **int** | Page Number | [optional] 
**page_size** | **int** |  | [optional] 
**total_hits** | **int** |  | [optional] 

## Example

```python
from instana_client.models.service_metric_result import ServiceMetricResult

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMetricResult from a JSON string
service_metric_result_instance = ServiceMetricResult.from_json(json)
# print the JSON string representation of the object
print(ServiceMetricResult.to_json())

# convert the object into a dict
service_metric_result_dict = service_metric_result_instance.to_dict()
# create an instance of ServiceMetricResult from a dict
service_metric_result_from_dict = ServiceMetricResult.from_dict(service_metric_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



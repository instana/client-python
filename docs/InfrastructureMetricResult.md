# InfrastructureMetricResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetricItem]**](MetricItem.md) |  | [optional] 

## Example

```python
from instana_client.models.infrastructure_metric_result import InfrastructureMetricResult

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureMetricResult from a JSON string
infrastructure_metric_result_instance = InfrastructureMetricResult.from_json(json)
# print the JSON string representation of the object
print(InfrastructureMetricResult.to_json())

# convert the object into a dict
infrastructure_metric_result_dict = infrastructure_metric_result_instance.to_dict()
# create an instance of InfrastructureMetricResult from a dict
infrastructure_metric_result_from_dict = InfrastructureMetricResult.from_dict(infrastructure_metric_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



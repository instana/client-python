# MetricsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics_result** | [**List[MetricsResultItem]**](MetricsResultItem.md) |  | 

## Example

```python
from instana_client.models.metrics_result import MetricsResult

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsResult from a JSON string
metrics_result_instance = MetricsResult.from_json(json)
# print the JSON string representation of the object
print(MetricsResult.to_json())

# convert the object into a dict
metrics_result_dict = metrics_result_instance.to_dict()
# create an instance of MetricsResult from a dict
metrics_result_from_dict = MetricsResult.from_dict(metrics_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



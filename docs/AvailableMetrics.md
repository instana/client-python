# AvailableMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[MetricMetadata]**](MetricMetadata.md) |  | [optional] 

## Example

```python
from instana_client.models.available_metrics import AvailableMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableMetrics from a JSON string
available_metrics_instance = AvailableMetrics.from_json(json)
# print the JSON string representation of the object
print(AvailableMetrics.to_json())

# convert the object into a dict
available_metrics_dict = available_metrics_instance.to_dict()
# create an instance of AvailableMetrics from a dict
available_metrics_from_dict = AvailableMetrics.from_dict(available_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



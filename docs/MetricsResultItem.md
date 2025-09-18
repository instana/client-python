# MetricsResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_tags** | **Dict[str, str]** | A map of custom properties composed of the custom property name and its value.  This information will be included if the custom properties were requested or if the query was grouped and the grouping included one or more custom properties. | [optional] 
**metrics** | **List[Dict[str, object]]** | A map of the requested metrics, composed of the metric name and its value. | 
**run_type** | **str** | Indicates whether the test was scheduled to run or run now | [optional] 
**tests** | [**List[MetricsTestResultItem]**](MetricsTestResultItem.md) | A description of the Synthetic test associated with the result item.  This information will be included if the request was grouped by synthetic.testId or if includeAggregatedTestId was true on the request. | [optional] 

## Example

```python
from instana_client.models.metrics_result_item import MetricsResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsResultItem from a JSON string
metrics_result_item_instance = MetricsResultItem.from_json(json)
# print the JSON string representation of the object
print(MetricsResultItem.to_json())

# convert the object into a dict
metrics_result_item_dict = metrics_result_item_instance.to_dict()
# create an instance of MetricsResultItem from a dict
metrics_result_item_from_dict = MetricsResultItem.from_dict(metrics_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



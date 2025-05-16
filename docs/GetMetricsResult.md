# GetMetricsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_default_groups** | **bool** |  | [optional] 
**groups** | [**List[SyntheticMetricTagGroup]**](SyntheticMetricTagGroup.md) |  Grouping of data under &#x60;groupbyTag&#x60;, where &#x60;groupbyTagEntity&#x60; and &#x60;groupbyTagSecondLevelKey&#x60; are aspects of &#x60;groupbyTag&#x60;. | [optional] 
**include_aggregated_test_ids** | **bool** |  | [optional] 
**metrics** | [**List[SyntheticMetricConfiguration]**](SyntheticMetricConfiguration.md) | A list of objects each of which defines a metric and the (statistical) aggregation -- MEAN, SUM, MAX, etc -- that should be used to summarize it for the defined time frame. Eg: &#x60;[{ &#39;metric&#39;: &#39;latency&#39;, &#39;aggregation&#39;: &#39;MEAN&#39;}]&#x60;. To know more about supported metrics and its aggregation, See &#x60;Get Metric catalog&#x60;. | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_metrics_result import GetMetricsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsResult from a JSON string
get_metrics_result_instance = GetMetricsResult.from_json(json)
# print the JSON string representation of the object
print(GetMetricsResult.to_json())

# convert the object into a dict
get_metrics_result_dict = get_metrics_result_instance.to_dict()
# create an instance of GetMetricsResult from a dict
get_metrics_result_from_dict = GetMetricsResult.from_dict(get_metrics_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



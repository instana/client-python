# GetAvailableMetricsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search term used to filter results using fields such as label, description, tag name or keywords | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | 
**type** | **str** | Entity type. Identifier for the monitored technology. | [optional] 

## Example

```python
from instana_client.models.get_available_metrics_query import GetAvailableMetricsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableMetricsQuery from a JSON string
get_available_metrics_query_instance = GetAvailableMetricsQuery.from_json(json)
# print the JSON string representation of the object
print(GetAvailableMetricsQuery.to_json())

# convert the object into a dict
get_available_metrics_query_dict = get_available_metrics_query_instance.to_dict()
# create an instance of GetAvailableMetricsQuery from a dict
get_available_metrics_query_from_dict = GetAvailableMetricsQuery.from_dict(get_available_metrics_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



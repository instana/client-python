# GetApplicationMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_internal** | **bool** |  | [optional] 
**include_synthetic** | **bool** |  | [optional] 
**metrics** | [**List[AppDataMetricConfiguration]**](AppDataMetricConfiguration.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | 

## Example

```python
from instana_client.models.get_application_metrics import GetApplicationMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationMetrics from a JSON string
get_application_metrics_instance = GetApplicationMetrics.from_json(json)
# print the JSON string representation of the object
print(GetApplicationMetrics.to_json())

# convert the object into a dict
get_application_metrics_dict = get_application_metrics_instance.to_dict()
# create an instance of GetApplicationMetrics from a dict
get_application_metrics_from_dict = GetApplicationMetrics.from_dict(get_application_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MetricQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**aggregation** | **str** |  | [optional] 
**cross_series_aggregation** | **str** |  | [optional] 
**granularity** | **int** |  | [optional] 
**metric** | **str** |  | [optional] 
**regex** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**operation** | [**ArithmeticOperation**](ArithmeticOperation.md) |  | [optional] 

## Example

```python
from instana_client.models.metric_query import MetricQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricQuery from a JSON string
metric_query_instance = MetricQuery.from_json(json)
# print the JSON string representation of the object
print(MetricQuery.to_json())

# convert the object into a dict
metric_query_dict = metric_query_instance.to_dict()
# create an instance of MetricQuery from a dict
metric_query_from_dict = MetricQuery.from_dict(metric_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



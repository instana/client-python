# TraceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**can_load_more** | **bool** | Determine if additional data is available when a new query is made using the cursor from the last item in the &#x60;items&#x60; list. | [optional] 
**items** | [**List[TraceItem]**](TraceItem.md) | Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item.  | 
**total_hits** | **int** | The total number of items that match a given filter | [optional] 
**total_represented_item_count** | **int** | For calls and EUM beacons, one row can represent multiple real items (batched call, sample multiplicity) | [optional] 
**total_retained_item_count** | **int** | For calls and EUM beacons, only a subset is retained for historic data. Each retained row can represent multiple real items due to batching. | [optional] 

## Example

```python
from instana_client.models.trace_result import TraceResult

# TODO update the JSON string below
json = "{}"
# create an instance of TraceResult from a JSON string
trace_result_instance = TraceResult.from_json(json)
# print the JSON string representation of the object
print(TraceResult.to_json())

# convert the object into a dict
trace_result_dict = trace_result_instance.to_dict()
# create an instance of TraceResult from a dict
trace_result_from_dict = TraceResult.from_dict(trace_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



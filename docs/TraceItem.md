# TraceItem

Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **object** | Cursor to use between successive queries | 
**trace** | [**Trace**](Trace.md) |  | 

## Example

```python
from instana_client.models.trace_item import TraceItem

# TODO update the JSON string below
json = "{}"
# create an instance of TraceItem from a JSON string
trace_item_instance = TraceItem.from_json(json)
# print the JSON string representation of the object
print(TraceItem.to_json())

# convert the object into a dict
trace_item_dict = trace_item_instance.to_dict()
# create an instance of TraceItem from a dict
trace_item_from_dict = TraceItem.from_dict(trace_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



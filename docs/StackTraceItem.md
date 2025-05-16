# StackTraceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** |  | [optional] 
**line** | **str** |  | [optional] 
**method** | **str** |  | [optional] 

## Example

```python
from instana_client.models.stack_trace_item import StackTraceItem

# TODO update the JSON string below
json = "{}"
# create an instance of StackTraceItem from a JSON string
stack_trace_item_instance = StackTraceItem.from_json(json)
# print the JSON string representation of the object
print(StackTraceItem.to_json())

# convert the object into a dict
stack_trace_item_dict = stack_trace_item_instance.to_dict()
# create an instance of StackTraceItem from a dict
stack_trace_item_from_dict = StackTraceItem.from_dict(stack_trace_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



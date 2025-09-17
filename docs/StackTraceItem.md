# StackTraceItem

For an erroneous call, if stack trace is available it will show a list of items containing file, method and line number of the code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The name of the file where the executed code resides. | [optional] 
**line** | **str** | The line number within the file where the error was thrown. | [optional] 
**method** | **str** | The name of the method or function being executed at the time the stack trace item was generated. | [optional] 

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



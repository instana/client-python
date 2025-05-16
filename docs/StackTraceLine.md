# StackTraceLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **int** |  | [optional] 
**file** | **str** |  | 
**line** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**translation_explanation** | **str** |  | [optional] 
**translation_status** | **int** |  | [optional] 

## Example

```python
from instana_client.models.stack_trace_line import StackTraceLine

# TODO update the JSON string below
json = "{}"
# create an instance of StackTraceLine from a JSON string
stack_trace_line_instance = StackTraceLine.from_json(json)
# print the JSON string representation of the object
print(StackTraceLine.to_json())

# convert the object into a dict
stack_trace_line_dict = stack_trace_line_instance.to_dict()
# create an instance of StackTraceLine from a dict
stack_trace_line_from_dict = StackTraceLine.from_dict(stack_trace_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



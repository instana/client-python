# JsStackTraceLine


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
from instana_client.models.js_stack_trace_line import JsStackTraceLine

# TODO update the JSON string below
json = "{}"
# create an instance of JsStackTraceLine from a JSON string
js_stack_trace_line_instance = JsStackTraceLine.from_json(json)
# print the JSON string representation of the object
print(JsStackTraceLine.to_json())

# convert the object into a dict
js_stack_trace_line_dict = js_stack_trace_line_instance.to_dict()
# create an instance of JsStackTraceLine from a dict
js_stack_trace_line_from_dict = JsStackTraceLine.from_dict(js_stack_trace_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



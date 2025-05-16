# Widget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** |  | 
**height** | **int** |  | [optional] 
**id** | **str** |  | 
**title** | **str** |  | [optional] 
**type** | **str** |  | 
**width** | **int** |  | [optional] 
**x** | **int** |  | [optional] 
**y** | **int** |  | [optional] 

## Example

```python
from instana_client.models.widget import Widget

# TODO update the JSON string below
json = "{}"
# create an instance of Widget from a JSON string
widget_instance = Widget.from_json(json)
# print the JSON string representation of the object
print(Widget.to_json())

# convert the object into a dict
widget_dict = widget_instance.to_dict()
# create an instance of Widget from a dict
widget_from_dict = Widget.from_dict(widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



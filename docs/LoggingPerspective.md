# LoggingPerspective

A filtered view of logs defined by a tag filter expression. Referred to as a Log Perspective in the UI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional free-text description shown in the UI. Set to null to clear. | [optional] 
**filter** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**perspective_id** | **str** | Server-assigned unique identifier.   Omit on create (POST).   Must match the path parameter on update (PUT). | [optional] 
**perspective_name** | **str** | Display name of the perspective. Must be unique. &#x60;Required&#x60;. | 

## Example

```python
from instana_client.models.logging_perspective import LoggingPerspective

# TODO update the JSON string below
json = "{}"
# create an instance of LoggingPerspective from a JSON string
logging_perspective_instance = LoggingPerspective.from_json(json)
# print the JSON string representation of the object
print(LoggingPerspective.to_json())

# convert the object into a dict
logging_perspective_dict = logging_perspective_instance.to_dict()
# create an instance of LoggingPerspective from a dict
logging_perspective_from_dict = LoggingPerspective.from_dict(logging_perspective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



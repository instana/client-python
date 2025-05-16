# CustomBlueprintIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_events_filter** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**good_events_filter** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 

## Example

```python
from instana_client.models.custom_blueprint_indicator import CustomBlueprintIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomBlueprintIndicator from a JSON string
custom_blueprint_indicator_instance = CustomBlueprintIndicator.from_json(json)
# print the JSON string representation of the object
print(CustomBlueprintIndicator.to_json())

# convert the object into a dict
custom_blueprint_indicator_dict = custom_blueprint_indicator_instance.to_dict()
# create an instance of CustomBlueprintIndicator from a dict
custom_blueprint_indicator_from_dict = CustomBlueprintIndicator.from_dict(custom_blueprint_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



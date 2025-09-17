# SaturationBlueprintIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_events_filter** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**good_events_filter** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**metric_name** | **str** |  | [optional] 
**threshold** | **float** | Threshold Value for the Blueprint | [optional] 

## Example

```python
from instana_client.models.saturation_blueprint_indicator import SaturationBlueprintIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of SaturationBlueprintIndicator from a JSON string
saturation_blueprint_indicator_instance = SaturationBlueprintIndicator.from_json(json)
# print the JSON string representation of the object
print(SaturationBlueprintIndicator.to_json())

# convert the object into a dict
saturation_blueprint_indicator_dict = saturation_blueprint_indicator_instance.to_dict()
# create an instance of SaturationBlueprintIndicator from a dict
saturation_blueprint_indicator_from_dict = SaturationBlueprintIndicator.from_dict(saturation_blueprint_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



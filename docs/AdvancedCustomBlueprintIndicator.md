# AdvancedCustomBlueprintIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_events** | [**AdvancedFilter**](AdvancedFilter.md) |  | [optional] 
**good_events** | [**AdvancedFilter**](AdvancedFilter.md) |  | 

## Example

```python
from instana_client.models.advanced_custom_blueprint_indicator import AdvancedCustomBlueprintIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedCustomBlueprintIndicator from a JSON string
advanced_custom_blueprint_indicator_instance = AdvancedCustomBlueprintIndicator.from_json(json)
# print the JSON string representation of the object
print(AdvancedCustomBlueprintIndicator.to_json())

# convert the object into a dict
advanced_custom_blueprint_indicator_dict = advanced_custom_blueprint_indicator_instance.to_dict()
# create an instance of AdvancedCustomBlueprintIndicator from a dict
advanced_custom_blueprint_indicator_from_dict = AdvancedCustomBlueprintIndicator.from_dict(advanced_custom_blueprint_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



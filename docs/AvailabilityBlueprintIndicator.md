# AvailabilityBlueprintIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | Threshold Value for the Blueprint | [optional] 

## Example

```python
from instana_client.models.availability_blueprint_indicator import AvailabilityBlueprintIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityBlueprintIndicator from a JSON string
availability_blueprint_indicator_instance = AvailabilityBlueprintIndicator.from_json(json)
# print the JSON string representation of the object
print(AvailabilityBlueprintIndicator.to_json())

# convert the object into a dict
availability_blueprint_indicator_dict = availability_blueprint_indicator_instance.to_dict()
# create an instance of AvailabilityBlueprintIndicator from a dict
availability_blueprint_indicator_from_dict = AvailabilityBlueprintIndicator.from_dict(availability_blueprint_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



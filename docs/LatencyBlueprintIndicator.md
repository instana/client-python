# LatencyBlueprintIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | Threshold Value for the Blueprint | [optional] 

## Example

```python
from instana_client.models.latency_blueprint_indicator import LatencyBlueprintIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of LatencyBlueprintIndicator from a JSON string
latency_blueprint_indicator_instance = LatencyBlueprintIndicator.from_json(json)
# print the JSON string representation of the object
print(LatencyBlueprintIndicator.to_json())

# convert the object into a dict
latency_blueprint_indicator_dict = latency_blueprint_indicator_instance.to_dict()
# create an instance of LatencyBlueprintIndicator from a dict
latency_blueprint_indicator_from_dict = LatencyBlueprintIndicator.from_dict(latency_blueprint_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



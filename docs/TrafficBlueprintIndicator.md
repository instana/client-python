# TrafficBlueprintIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | Threshold Value for the Blueprint | [optional] 
**traffic_type** | **str** |  | 

## Example

```python
from instana_client.models.traffic_blueprint_indicator import TrafficBlueprintIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficBlueprintIndicator from a JSON string
traffic_blueprint_indicator_instance = TrafficBlueprintIndicator.from_json(json)
# print the JSON string representation of the object
print(TrafficBlueprintIndicator.to_json())

# convert the object into a dict
traffic_blueprint_indicator_dict = traffic_blueprint_indicator_instance.to_dict()
# create an instance of TrafficBlueprintIndicator from a dict
traffic_blueprint_indicator_from_dict = TrafficBlueprintIndicator.from_dict(traffic_blueprint_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



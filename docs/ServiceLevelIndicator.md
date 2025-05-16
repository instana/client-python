# ServiceLevelIndicator

Indicator of the Service Levels Objective Configuration, it indicates the type of metric by which the SLO should be evaluated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Aggregation Type for the Threshold Value | [optional] 
**blueprint** | **str** |  | [optional] 
**operator** | **str** | Operator for the Threshold Value | [optional] 
**service_levels_measurement** | **str** | Defines Measurement Type of SLO | [optional] 
**threshold** | **float** | Threshold Value for the Blueprint | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from instana_client.models.service_level_indicator import ServiceLevelIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelIndicator from a JSON string
service_level_indicator_instance = ServiceLevelIndicator.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelIndicator.to_json())

# convert the object into a dict
service_level_indicator_dict = service_level_indicator_instance.to_dict()
# create an instance of ServiceLevelIndicator from a dict
service_level_indicator_from_dict = ServiceLevelIndicator.from_dict(service_level_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



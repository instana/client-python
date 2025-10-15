# ServiceLevelsStaticThresholdConfig

This threshold defines a static value to be evaluated with a specific operator for burn rate v2 alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated** | **int** |  | [optional] 
**operator** | **str** |  | 
**value** | **float** |  | [optional] 

## Example

```python
from instana_client.models.service_levels_static_threshold_config import ServiceLevelsStaticThresholdConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelsStaticThresholdConfig from a JSON string
service_levels_static_threshold_config_instance = ServiceLevelsStaticThresholdConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelsStaticThresholdConfig.to_json())

# convert the object into a dict
service_levels_static_threshold_config_dict = service_levels_static_threshold_config_instance.to_dict()
# create an instance of ServiceLevelsStaticThresholdConfig from a dict
service_levels_static_threshold_config_from_dict = ServiceLevelsStaticThresholdConfig.from_dict(service_levels_static_threshold_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



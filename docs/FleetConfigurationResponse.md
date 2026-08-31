# FleetConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**FleetConfiguration**](FleetConfiguration.md) |  | [optional] 
**configuration_version** | **str** |  | [optional] 
**id** | **str** |  | 
**message** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from instana_client.models.fleet_configuration_response import FleetConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConfigurationResponse from a JSON string
fleet_configuration_response_instance = FleetConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(FleetConfigurationResponse.to_json())

# convert the object into a dict
fleet_configuration_response_dict = fleet_configuration_response_instance.to_dict()
# create an instance of FleetConfigurationResponse from a dict
fleet_configuration_response_from_dict = FleetConfigurationResponse.from_dict(fleet_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



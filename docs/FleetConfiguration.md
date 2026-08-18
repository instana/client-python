# FleetConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **object** |  | 
**configuration_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 
**version** | **str** |  | 

## Example

```python
from instana_client.models.fleet_configuration import FleetConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConfiguration from a JSON string
fleet_configuration_instance = FleetConfiguration.from_json(json)
# print the JSON string representation of the object
print(FleetConfiguration.to_json())

# convert the object into a dict
fleet_configuration_dict = fleet_configuration_instance.to_dict()
# create an instance of FleetConfiguration from a dict
fleet_configuration_from_dict = FleetConfiguration.from_dict(fleet_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



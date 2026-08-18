# FleetConfigurationAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_host** | **str** |  | 
**agent_host_id** | **str** |  | 
**agent_name** | **str** |  | [optional] 
**agent_type** | **str** |  | 
**assignment_id** | **str** |  | [optional] 
**configuration_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from instana_client.models.fleet_configuration_assignment import FleetConfigurationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConfigurationAssignment from a JSON string
fleet_configuration_assignment_instance = FleetConfigurationAssignment.from_json(json)
# print the JSON string representation of the object
print(FleetConfigurationAssignment.to_json())

# convert the object into a dict
fleet_configuration_assignment_dict = fleet_configuration_assignment_instance.to_dict()
# create an instance of FleetConfigurationAssignment from a dict
fleet_configuration_assignment_from_dict = FleetConfigurationAssignment.from_dict(fleet_configuration_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



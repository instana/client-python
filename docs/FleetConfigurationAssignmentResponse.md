# FleetConfigurationAssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from instana_client.models.fleet_configuration_assignment_response import FleetConfigurationAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConfigurationAssignmentResponse from a JSON string
fleet_configuration_assignment_response_instance = FleetConfigurationAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(FleetConfigurationAssignmentResponse.to_json())

# convert the object into a dict
fleet_configuration_assignment_response_dict = fleet_configuration_assignment_response_instance.to_dict()
# create an instance of FleetConfigurationAssignmentResponse from a dict
fleet_configuration_assignment_response_from_dict = FleetConfigurationAssignmentResponse.from_dict(fleet_configuration_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



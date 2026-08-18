# UpdateFleetConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **object** |  | 
**name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from instana_client.models.update_fleet_configuration_request import UpdateFleetConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFleetConfigurationRequest from a JSON string
update_fleet_configuration_request_instance = UpdateFleetConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFleetConfigurationRequest.to_json())

# convert the object into a dict
update_fleet_configuration_request_dict = update_fleet_configuration_request_instance.to_dict()
# create an instance of UpdateFleetConfigurationRequest from a dict
update_fleet_configuration_request_from_dict = UpdateFleetConfigurationRequest.from_dict(update_fleet_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



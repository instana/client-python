# ApplicationSloEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The ID of the Application | 
**boundary_scope** | **str** | The Boundary Scope of the Application | 
**endpoint_id** | **str** | The Endpoint ID of the Application | [optional] 
**include_internal** | **bool** | A boolean value indicating whether the SLO takes Internal calls into account | [optional] 
**include_synthetic** | **bool** | A boolean value indicating whether the SLO takes Synthetic calls into account | [optional] 
**service_id** | **str** | The Service ID of the Application | [optional] 

## Example

```python
from instana_client.models.application_slo_entity import ApplicationSloEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSloEntity from a JSON string
application_slo_entity_instance = ApplicationSloEntity.from_json(json)
# print the JSON string representation of the object
print(ApplicationSloEntity.to_json())

# convert the object into a dict
application_slo_entity_dict = application_slo_entity_instance.to_dict()
# create an instance of ApplicationSloEntity from a dict
application_slo_entity_from_dict = ApplicationSloEntity.from_dict(application_slo_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



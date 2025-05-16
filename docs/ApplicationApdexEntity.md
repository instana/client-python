# ApplicationApdexEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundary_scope** | **str** | Application Boundary Scope, it could be ALL or INBOUND | 
**entity_id** | **str** | Application ID | 
**include_internal** | **bool** | A boolean value indicating whether the SLO takes Internal calls into account | [optional] 
**include_synthetic** | **bool** | A boolean value indicating whether the SLO takes Synthetic calls into account | [optional] 
**threshold** | **int** | Value of the Apdex Threshold | [optional] 

## Example

```python
from instana_client.models.application_apdex_entity import ApplicationApdexEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationApdexEntity from a JSON string
application_apdex_entity_instance = ApplicationApdexEntity.from_json(json)
# print the JSON string representation of the object
print(ApplicationApdexEntity.to_json())

# convert the object into a dict
application_apdex_entity_dict = application_apdex_entity_instance.to_dict()
# create an instance of ApplicationApdexEntity from a dict
application_apdex_entity_from_dict = ApplicationApdexEntity.from_dict(application_apdex_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



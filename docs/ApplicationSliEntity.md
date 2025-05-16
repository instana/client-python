# ApplicationSliEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Specifies the ID of the Application that is to be monitored by the SLO | [optional] 
**boundary_scope** | **str** | Defines the boundary of calls to be monitored, specifying whether to track all calls or only inbound calls | 
**endpoint_id** | **str** | Specifies the ID of the Endpoint to be monitored by the application SLO | [optional] 
**service_id** | **str** | Identifies the service to be monitored by the application SLO | [optional] 

## Example

```python
from instana_client.models.application_sli_entity import ApplicationSliEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSliEntity from a JSON string
application_sli_entity_instance = ApplicationSliEntity.from_json(json)
# print the JSON string representation of the object
print(ApplicationSliEntity.to_json())

# convert the object into a dict
application_sli_entity_dict = application_sli_entity_instance.to_dict()
# create an instance of ApplicationSliEntity from a dict
application_sli_entity_from_dict = ApplicationSliEntity.from_dict(application_sli_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceNowEnhancedIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_close_incidents** | **bool** |  | [optional] 
**enable_send_instana_notes** | **bool** |  | [optional] 
**enable_send_service_now_activities** | **bool** |  | [optional] 
**enable_send_service_now_work_notes** | **bool** |  | [optional] 
**instana_url** | **str** |  | [optional] 
**manually_closed_incidents** | **bool** |  | [optional] 
**password** | **str** |  | 
**resolution_of_incident** | **bool** |  | [optional] 
**service_now_url** | **str** |  | 
**snow_status_on_close_event** | **int** |  | [optional] 
**tenant** | **str** |  | 
**unit** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from instana_client.models.service_now_enhanced_integration import ServiceNowEnhancedIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowEnhancedIntegration from a JSON string
service_now_enhanced_integration_instance = ServiceNowEnhancedIntegration.from_json(json)
# print the JSON string representation of the object
print(ServiceNowEnhancedIntegration.to_json())

# convert the object into a dict
service_now_enhanced_integration_dict = service_now_enhanced_integration_instance.to_dict()
# create an instance of ServiceNowEnhancedIntegration from a dict
service_now_enhanced_integration_from_dict = ServiceNowEnhancedIntegration.from_dict(service_now_enhanced_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



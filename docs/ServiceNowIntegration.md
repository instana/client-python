# ServiceNowIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_close_incidents** | **bool** |  | [optional] 
**password** | **str** |  | 
**service_now_url** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from instana_client.models.service_now_integration import ServiceNowIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowIntegration from a JSON string
service_now_integration_instance = ServiceNowIntegration.from_json(json)
# print the JSON string representation of the object
print(ServiceNowIntegration.to_json())

# convert the object into a dict
service_now_integration_dict = service_now_integration_instance.to_dict()
# create an instance of ServiceNowIntegration from a dict
service_now_integration_from_dict = ServiceNowIntegration.from_dict(service_now_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



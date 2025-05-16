# SalesforceIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_token** | **str** |  | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**salesforce_url** | **str** |  | 

## Example

```python
from instana_client.models.salesforce_integration import SalesforceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceIntegration from a JSON string
salesforce_integration_instance = SalesforceIntegration.from_json(json)
# print the JSON string representation of the object
print(SalesforceIntegration.to_json())

# convert the object into a dict
salesforce_integration_dict = salesforce_integration_instance.to_dict()
# create an instance of SalesforceIntegration from a dict
salesforce_integration_from_dict = SalesforceIntegration.from_dict(salesforce_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



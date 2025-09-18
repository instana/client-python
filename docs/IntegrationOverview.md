# IntegrationOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the alert channel | 
**kind** | **str** | The type of the Alerting Channel. | 
**name** | **str** | The name of the Alerting Channel. | 
**properties** | **Dict[str, str]** | Properties of the alert channel in pairs of key/value | [optional] 
**rbac_tags** | [**List[ApiTag]**](ApiTag.md) | Team Tags that&#39;s assigned to the Alerting Channel | [optional] 

## Example

```python
from instana_client.models.integration_overview import IntegrationOverview

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationOverview from a JSON string
integration_overview_instance = IntegrationOverview.from_json(json)
# print the JSON string representation of the object
print(IntegrationOverview.to_json())

# convert the object into a dict
integration_overview_dict = integration_overview_instance.to_dict()
# create an instance of IntegrationOverview from a dict
integration_overview_from_dict = IntegrationOverview.from_dict(integration_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



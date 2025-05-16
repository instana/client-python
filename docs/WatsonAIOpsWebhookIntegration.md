# WatsonAIOpsWebhookIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[str]** |  | [optional] 
**webhook_url** | **str** |  | 

## Example

```python
from instana_client.models.watson_ai_ops_webhook_integration import WatsonAIOpsWebhookIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of WatsonAIOpsWebhookIntegration from a JSON string
watson_ai_ops_webhook_integration_instance = WatsonAIOpsWebhookIntegration.from_json(json)
# print the JSON string representation of the object
print(WatsonAIOpsWebhookIntegration.to_json())

# convert the object into a dict
watson_ai_ops_webhook_integration_dict = watson_ai_ops_webhook_integration_instance.to_dict()
# create an instance of WatsonAIOpsWebhookIntegration from a dict
watson_ai_ops_webhook_integration_from_dict = WatsonAIOpsWebhookIntegration.from_dict(watson_ai_ops_webhook_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



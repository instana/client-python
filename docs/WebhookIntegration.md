# WebhookIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[str]** |  | [optional] 
**webhook_urls** | **List[str]** |  | 

## Example

```python
from instana_client.models.webhook_integration import WebhookIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIntegration from a JSON string
webhook_integration_instance = WebhookIntegration.from_json(json)
# print the JSON string representation of the object
print(WebhookIntegration.to_json())

# convert the object into a dict
webhook_integration_dict = webhook_integration_instance.to_dict()
# create an instance of WebhookIntegration from a dict
webhook_integration_from_dict = WebhookIntegration.from_dict(webhook_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



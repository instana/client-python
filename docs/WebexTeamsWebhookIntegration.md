# WebexTeamsWebhookIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** |  | 

## Example

```python
from instana_client.models.webex_teams_webhook_integration import WebexTeamsWebhookIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of WebexTeamsWebhookIntegration from a JSON string
webex_teams_webhook_integration_instance = WebexTeamsWebhookIntegration.from_json(json)
# print the JSON string representation of the object
print(WebexTeamsWebhookIntegration.to_json())

# convert the object into a dict
webex_teams_webhook_integration_dict = webex_teams_webhook_integration_instance.to_dict()
# create an instance of WebexTeamsWebhookIntegration from a dict
webex_teams_webhook_integration_from_dict = WebexTeamsWebhookIntegration.from_dict(webex_teams_webhook_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



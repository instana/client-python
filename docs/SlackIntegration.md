# SlackIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**emoji_rendering** | **bool** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**webhook_url** | **str** |  | 

## Example

```python
from instana_client.models.slack_integration import SlackIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of SlackIntegration from a JSON string
slack_integration_instance = SlackIntegration.from_json(json)
# print the JSON string representation of the object
print(SlackIntegration.to_json())

# convert the object into a dict
slack_integration_dict = slack_integration_instance.to_dict()
# create an instance of SlackIntegration from a dict
slack_integration_from_dict = SlackIntegration.from_dict(slack_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



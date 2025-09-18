# BidirectionalSlackAppIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**emoji_rendering** | **bool** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.bidirectional_slack_app_integration import BidirectionalSlackAppIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of BidirectionalSlackAppIntegration from a JSON string
bidirectional_slack_app_integration_instance = BidirectionalSlackAppIntegration.from_json(json)
# print the JSON string representation of the object
print(BidirectionalSlackAppIntegration.to_json())

# convert the object into a dict
bidirectional_slack_app_integration_dict = bidirectional_slack_app_integration_instance.to_dict()
# create an instance of BidirectionalSlackAppIntegration from a dict
bidirectional_slack_app_integration_from_dict = BidirectionalSlackAppIntegration.from_dict(bidirectional_slack_app_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



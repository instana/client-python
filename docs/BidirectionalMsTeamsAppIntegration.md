# BidirectionalMsTeamsAppIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token_id** | **str** |  | 
**channel_id** | **str** |  | 
**channel_name** | **str** |  | 
**instana_url** | **str** |  | 
**service_url** | **str** |  | [optional] 
**team_id** | **str** |  | 
**team_name** | **str** |  | [optional] 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.bidirectional_ms_teams_app_integration import BidirectionalMsTeamsAppIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of BidirectionalMsTeamsAppIntegration from a JSON string
bidirectional_ms_teams_app_integration_instance = BidirectionalMsTeamsAppIntegration.from_json(json)
# print the JSON string representation of the object
print(BidirectionalMsTeamsAppIntegration.to_json())

# convert the object into a dict
bidirectional_ms_teams_app_integration_dict = bidirectional_ms_teams_app_integration_instance.to_dict()
# create an instance of BidirectionalMsTeamsAppIntegration from a dict
bidirectional_ms_teams_app_integration_from_dict = BidirectionalMsTeamsAppIntegration.from_dict(bidirectional_ms_teams_app_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



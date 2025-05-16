# ZChatOpsIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_auth_token** | **str** |  | 
**channels** | **List[str]** |  | [optional] 
**zchat_ops_incidents_url** | **str** |  | 

## Example

```python
from instana_client.models.z_chat_ops_integration import ZChatOpsIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ZChatOpsIntegration from a JSON string
z_chat_ops_integration_instance = ZChatOpsIntegration.from_json(json)
# print the JSON string representation of the object
print(ZChatOpsIntegration.to_json())

# convert the object into a dict
z_chat_ops_integration_dict = z_chat_ops_integration_instance.to_dict()
# create an instance of ZChatOpsIntegration from a dict
z_chat_ops_integration_from_dict = ZChatOpsIntegration.from_dict(z_chat_ops_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



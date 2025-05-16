# InvitationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_status** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 

## Example

```python
from instana_client.models.invitation_result import InvitationResult

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationResult from a JSON string
invitation_result_instance = InvitationResult.from_json(json)
# print the JSON string representation of the object
print(InvitationResult.to_json())

# convert the object into a dict
invitation_result_dict = invitation_result_instance.to_dict()
# create an instance of InvitationResult from a dict
invitation_result_from_dict = InvitationResult.from_dict(invitation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



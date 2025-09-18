# ActionMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | [optional] 
**ai_engine** | **str** |  | 
**confidence** | **str** |  | 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**score** | **float** |  | 

## Example

```python
from instana_client.models.action_match import ActionMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ActionMatch from a JSON string
action_match_instance = ActionMatch.from_json(json)
# print the JSON string representation of the object
print(ActionMatch.to_json())

# convert the object into a dict
action_match_dict = action_match_instance.to_dict()
# create an instance of ActionMatch from a dict
action_match_from_dict = ActionMatch.from_dict(action_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



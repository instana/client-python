# ActionSearchSpace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of an incident or issue. | [optional] 
**entity_type** | **str** | The entity type associated with the incident or issue. | [optional] 
**event_id** | **str** | The event identifier associated with the incident or issue. | [optional] 
**name** | **str** | The name of an incident or issue. | 

## Example

```python
from instana_client.models.action_search_space import ActionSearchSpace

# TODO update the JSON string below
json = "{}"
# create an instance of ActionSearchSpace from a JSON string
action_search_space_instance = ActionSearchSpace.from_json(json)
# print the JSON string representation of the object
print(ActionSearchSpace.to_json())

# convert the object into a dict
action_search_space_dict = action_search_space_instance.to_dict()
# create an instance of ActionSearchSpace from a dict
action_search_space_from_dict = ActionSearchSpace.from_dict(action_search_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



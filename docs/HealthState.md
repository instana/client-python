# HealthState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health** | **str** |  | [optional] 
**messages** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.health_state import HealthState

# TODO update the JSON string below
json = "{}"
# create an instance of HealthState from a JSON string
health_state_instance = HealthState.from_json(json)
# print the JSON string representation of the object
print(HealthState.to_json())

# convert the object into a dict
health_state_dict = health_state_instance.to_dict()
# create an instance of HealthState from a dict
health_state_from_dict = HealthState.from_dict(health_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



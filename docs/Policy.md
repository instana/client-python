# Policy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Policy description. | [optional] 
**id** | **str** | Policy identifier. | [readonly] 
**name** | **str** | Policy name. | 
**tags** | **List[str]** | A list of policy tags. | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | 
**type_configurations** | [**List[TypeConfiguration]**](TypeConfiguration.md) | List of configurations that contains the list of actions to run and the mode (automatic or manual) in which the policy is run. | 

## Example

```python
from instana_client.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print(Policy.to_json())

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_from_dict = Policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PolicyRunnable

Runnable associated with the policy. It can be a `workflow` or `action`. Currently only supports `action`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action identifier. | 
**run_configuration** | [**RunConfiguration**](RunConfiguration.md) |  | 
**type** | **str** | Type of runnable. Supported value is &#x60;action&#x60;. | 

## Example

```python
from instana_client.models.policy_runnable import PolicyRunnable

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRunnable from a JSON string
policy_runnable_instance = PolicyRunnable.from_json(json)
# print the JSON string representation of the object
print(PolicyRunnable.to_json())

# convert the object into a dict
policy_runnable_dict = policy_runnable_instance.to_dict()
# create an instance of PolicyRunnable from a dict
policy_runnable_from_dict = PolicyRunnable.from_dict(policy_runnable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



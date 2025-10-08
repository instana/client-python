# Trigger

The trigger is the Instana event or Smart Alert that defines the initial conditions that must be met for the policy to apply on the actions in `typeConfiguration`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description for the trigger. | [optional] 
**id** | **str** | Trigger (Instana event or Smart Alert) identifier. | [optional] 
**name** | **str** | A name of the trigger (name of Instana event or Smart Alert). | [optional] 
**scheduling** | [**PolicyScheduling**](PolicyScheduling.md) |  | [optional] 
**type** | **str** | Instana event type, Smart Alert type, or &#39;schedule&#39;. The type must be one of the enum values. | 

## Example

```python
from instana_client.models.trigger import Trigger

# TODO update the JSON string below
json = "{}"
# create an instance of Trigger from a JSON string
trigger_instance = Trigger.from_json(json)
# print the JSON string representation of the object
print(Trigger.to_json())

# convert the object into a dict
trigger_dict = trigger_instance.to_dict()
# create an instance of Trigger from a dict
trigger_from_dict = Trigger.from_dict(trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



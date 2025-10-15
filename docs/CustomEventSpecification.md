# CustomEventSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[Action]**](Action.md) |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**entity_type** | **str** |  | 
**expiration_time** | **int** |  | [optional] 
**name** | **str** |  | 
**query** | **str** |  | [optional] 
**rule_logical_operator** | **str** | Set AND / OR | [optional] 
**rules** | [**List[AbstractRule]**](AbstractRule.md) |  | 
**transient_event_alert_muted** | **bool** |  | [optional] 
**transient_event_enabled** | **bool** |  | [optional] 
**transient_event_threshold** | **int** |  | [optional] 
**triggering** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.custom_event_specification import CustomEventSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEventSpecification from a JSON string
custom_event_specification_instance = CustomEventSpecification.from_json(json)
# print the JSON string representation of the object
print(CustomEventSpecification.to_json())

# convert the object into a dict
custom_event_specification_dict = custom_event_specification_instance.to_dict()
# create an instance of CustomEventSpecification from a dict
custom_event_specification_from_dict = CustomEventSpecification.from_dict(custom_event_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



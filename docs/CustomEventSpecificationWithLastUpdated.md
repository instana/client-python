# CustomEventSpecificationWithLastUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[Action]**](Action.md) |  | [optional] 
**application_alert_config_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**entity_type** | **str** |  | 
**expiration_time** | **int** |  | [optional] 
**id** | **str** |  | 
**last_updated** | **int** |  | [optional] 
**migrated** | **bool** |  | [optional] 
**name** | **str** |  | 
**query** | **str** |  | [optional] 
**rule_logical_operator** | **str** | Set AND / OR | [optional] 
**rules** | [**List[AbstractRule]**](AbstractRule.md) |  | 
**triggering** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.custom_event_specification_with_last_updated import CustomEventSpecificationWithLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEventSpecificationWithLastUpdated from a JSON string
custom_event_specification_with_last_updated_instance = CustomEventSpecificationWithLastUpdated.from_json(json)
# print the JSON string representation of the object
print(CustomEventSpecificationWithLastUpdated.to_json())

# convert the object into a dict
custom_event_specification_with_last_updated_dict = custom_event_specification_with_last_updated_instance.to_dict()
# create an instance of CustomEventSpecificationWithLastUpdated from a dict
custom_event_specification_with_last_updated_from_dict = CustomEventSpecificationWithLastUpdated.from_dict(custom_event_specification_with_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



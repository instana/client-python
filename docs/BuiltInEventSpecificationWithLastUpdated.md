# BuiltInEventSpecificationWithLastUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of Built-in Event Specification | [optional] 
**enabled** | **bool** | Flag to show whether the Built-in Event Specification is enabled | [optional] 
**hidden** | **bool** | Flag to show whether the Built-in Event Specification is hidden | [optional] 
**hyper_params** | [**List[HyperParam]**](HyperParam.md) | List of hyper parameters of the Built-in Event Specification | 
**id** | **str** | ID of Built-in Event Specification | 
**last_updated** | **int** |  | [optional] 
**name** | **str** | Name of Built-in Event Specification | 
**rule_inputs** | [**List[RuleInput]**](RuleInput.md) | List of input rules of the Built-in Event Specification | 
**severity** | **int** | Severity level of Built-in Event Specification | [optional] 
**short_plugin_id** | **str** | ID of short plugin of Built-in Event Specification | 
**triggering** | **bool** | Flag to show whether the Built-in Event Specification is triggering | [optional] 

## Example

```python
from instana_client.models.built_in_event_specification_with_last_updated import BuiltInEventSpecificationWithLastUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of BuiltInEventSpecificationWithLastUpdated from a JSON string
built_in_event_specification_with_last_updated_instance = BuiltInEventSpecificationWithLastUpdated.from_json(json)
# print the JSON string representation of the object
print(BuiltInEventSpecificationWithLastUpdated.to_json())

# convert the object into a dict
built_in_event_specification_with_last_updated_dict = built_in_event_specification_with_last_updated_instance.to_dict()
# create an instance of BuiltInEventSpecificationWithLastUpdated from a dict
built_in_event_specification_with_last_updated_from_dict = BuiltInEventSpecificationWithLastUpdated.from_dict(built_in_event_specification_with_last_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



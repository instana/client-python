# CustomEntityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboards** | [**List[CustomDashboard]**](CustomDashboard.md) |  | [optional] 
**dependencies** | [**List[CustomDependency]**](CustomDependency.md) |  | [optional] 
**identifiers** | **List[str]** |  | 
**label** | **str** |  | 
**metrics** | **List[str]** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 

## Example

```python
from instana_client.models.custom_entity_model import CustomEntityModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityModel from a JSON string
custom_entity_model_instance = CustomEntityModel.from_json(json)
# print the JSON string representation of the object
print(CustomEntityModel.to_json())

# convert the object into a dict
custom_entity_model_dict = custom_entity_model_instance.to_dict()
# create an instance of CustomEntityModel from a dict
custom_entity_model_from_dict = CustomEntityModel.from_dict(custom_entity_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



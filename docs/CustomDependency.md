# CustomDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**entity_type** | **str** | If entityType is set, the dependency will be added to the plugin for that entity type. Otherwise, the dependency will be applied to the custom entity itself. | [optional] 
**identifiers** | **List[str]** | Will take the identifiers values for building the key of the dependency. | [optional] 
**name** | **str** |  | [optional] 
**separator** | **str** | Separator between identifiers for building the key of the dependency. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from instana_client.models.custom_dependency import CustomDependency

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDependency from a JSON string
custom_dependency_instance = CustomDependency.from_json(json)
# print the JSON string representation of the object
print(CustomDependency.to_json())

# convert the object into a dict
custom_dependency_dict = custom_dependency_instance.to_dict()
# create an instance of CustomDependency from a dict
custom_dependency_from_dict = CustomDependency.from_dict(custom_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



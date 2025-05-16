# ScopeBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_id** | **str** |  | [optional] 
**scope_role_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.scope_binding import ScopeBinding

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeBinding from a JSON string
scope_binding_instance = ScopeBinding.from_json(json)
# print the JSON string representation of the object
print(ScopeBinding.to_json())

# convert the object into a dict
scope_binding_dict = scope_binding_instance.to_dict()
# create an instance of ScopeBinding from a dict
scope_binding_from_dict = ScopeBinding.from_dict(scope_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



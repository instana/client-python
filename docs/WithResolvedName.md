# WithResolvedName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.with_resolved_name import WithResolvedName

# TODO update the JSON string below
json = "{}"
# create an instance of WithResolvedName from a JSON string
with_resolved_name_instance = WithResolvedName.from_json(json)
# print the JSON string representation of the object
print(WithResolvedName.to_json())

# convert the object into a dict
with_resolved_name_dict = with_resolved_name_instance.to_dict()
# create an instance of WithResolvedName from a dict
with_resolved_name_from_dict = WithResolvedName.from_dict(with_resolved_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReleaseScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**application_name** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.release_scope import ReleaseScope

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseScope from a JSON string
release_scope_instance = ReleaseScope.from_json(json)
# print the JSON string representation of the object
print(ReleaseScope.to_json())

# convert the object into a dict
release_scope_dict = release_scope_instance.to_dict()
# create an instance of ReleaseScope from a dict
release_scope_from_dict = ReleaseScope.from_dict(release_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



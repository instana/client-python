# ServiceScopeWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**scoped_to** | [**ServiceScopedToWithMetadata**](ServiceScopedToWithMetadata.md) |  | [optional] 

## Example

```python
from instana_client.models.service_scope_with_metadata import ServiceScopeWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceScopeWithMetadata from a JSON string
service_scope_with_metadata_instance = ServiceScopeWithMetadata.from_json(json)
# print the JSON string representation of the object
print(ServiceScopeWithMetadata.to_json())

# convert the object into a dict
service_scope_with_metadata_dict = service_scope_with_metadata_instance.to_dict()
# create an instance of ServiceScopeWithMetadata from a dict
service_scope_with_metadata_from_dict = ServiceScopeWithMetadata.from_dict(service_scope_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceScopedToWithMetadata

The release marker would be present in the service but not for other services within the Application perspective.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[ApplicationScopeWithMetadata]**](ApplicationScopeWithMetadata.md) | The list of application perspectives where the service is present.  | 

## Example

```python
from instana_client.models.service_scoped_to_with_metadata import ServiceScopedToWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceScopedToWithMetadata from a JSON string
service_scoped_to_with_metadata_instance = ServiceScopedToWithMetadata.from_json(json)
# print the JSON string representation of the object
print(ServiceScopedToWithMetadata.to_json())

# convert the object into a dict
service_scoped_to_with_metadata_dict = service_scoped_to_with_metadata_instance.to_dict()
# create an instance of ServiceScopedToWithMetadata from a dict
service_scoped_to_with_metadata_from_dict = ServiceScopedToWithMetadata.from_dict(service_scoped_to_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



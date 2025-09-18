# ApplicationScopeWithMetadata

The list of application perspectives where the release can be viewed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Application Perspective. Eg: &#x60;Av62RoIKQv-A3n6DbMQh9g&#x60;. | 
**name** | **str** | Name of the Application Perspective. Eg: &#x60;app1&#x60;. | [optional] 

## Example

```python
from instana_client.models.application_scope_with_metadata import ApplicationScopeWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationScopeWithMetadata from a JSON string
application_scope_with_metadata_instance = ApplicationScopeWithMetadata.from_json(json)
# print the JSON string representation of the object
print(ApplicationScopeWithMetadata.to_json())

# convert the object into a dict
application_scope_with_metadata_dict = application_scope_with_metadata_instance.to_dict()
# create an instance of ApplicationScopeWithMetadata from a dict
application_scope_with_metadata_from_dict = ApplicationScopeWithMetadata.from_dict(application_scope_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



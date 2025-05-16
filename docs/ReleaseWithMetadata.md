# ReleaseWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[ApplicationScopeWithMetadata]**](ApplicationScopeWithMetadata.md) |  | [optional] 
**id** | **str** |  | 
**last_updated** | **int** |  | [optional] 
**name** | **str** |  | 
**scopes** | [**List[ReleaseScope]**](ReleaseScope.md) |  | [optional] 
**services** | [**List[ServiceScopeWithMetadata]**](ServiceScopeWithMetadata.md) |  | [optional] 
**start** | **int** |  | [optional] 

## Example

```python
from instana_client.models.release_with_metadata import ReleaseWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseWithMetadata from a JSON string
release_with_metadata_instance = ReleaseWithMetadata.from_json(json)
# print the JSON string representation of the object
print(ReleaseWithMetadata.to_json())

# convert the object into a dict
release_with_metadata_dict = release_with_metadata_instance.to_dict()
# create an instance of ReleaseWithMetadata from a dict
release_with_metadata_from_dict = ReleaseWithMetadata.from_dict(release_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



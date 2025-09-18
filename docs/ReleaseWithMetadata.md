# ReleaseWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[ApplicationScopeWithMetadata]**](ApplicationScopeWithMetadata.md) | The list of application perspectives where the release can be viewed. | [optional] 
**id** | **str** | A unique id for a release. For example: &#x60;l1wgr3DsQkGLf8u18JiGsg&#x60;. | 
**last_updated** | **int** | The timestamp for when the same release is updated. The time measured is in milliseconds. For example: &#x60;1742369990000&#x60; is &#x60;Wednesday, 19 March 2025 07:39:50 GMT&#x60;. | [optional] 
**name** | **str** | The name of the release. For example: &#x60;frontend/release-2000&#x60;. | 
**scopes** | [**List[ReleaseScope]**](ReleaseScope.md) |  | [optional] 
**services** | [**List[ServiceScopeWithMetadata]**](ServiceScopeWithMetadata.md) | The list of services where the release can be viewed. | [optional] 
**start** | **int** | The timestamp for when the release is created. The time measured is in milliseconds. For example: &#x60;1742349976000&#x60; is &#x60;Wednesday, 19 March 2025 02:06:16 GMT&#x60;. | [optional] 

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



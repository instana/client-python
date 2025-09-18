# Release


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[ApplicationScope]**](ApplicationScope.md) | The list of application perspectives where the release can be viewed. | [optional] 
**name** | **str** | The name of the release. For example: &#x60;frontend/release-2000&#x60;. | 
**services** | [**List[ServiceScope]**](ServiceScope.md) | The list of services where the release can be viewed. | [optional] 
**start** | **int** | The timestamp for when the release is created. The time measured is in milliseconds. For example: &#x60;1742349976000&#x60; is &#x60;Wednesday, 19 March 2025 02:06:16 GMT&#x60;. | 

## Example

```python
from instana_client.models.release import Release

# TODO update the JSON string below
json = "{}"
# create an instance of Release from a JSON string
release_instance = Release.from_json(json)
# print the JSON string representation of the object
print(Release.to_json())

# convert the object into a dict
release_dict = release_instance.to_dict()
# create an instance of Release from a dict
release_from_dict = Release.from_dict(release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



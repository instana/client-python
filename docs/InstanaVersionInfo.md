# InstanaVersionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**commit** | **str** |  | [optional] 
**image_tag** | **str** |  | [optional] 

## Example

```python
from instana_client.models.instana_version_info import InstanaVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InstanaVersionInfo from a JSON string
instana_version_info_instance = InstanaVersionInfo.from_json(json)
# print the JSON string representation of the object
print(InstanaVersionInfo.to_json())

# convert the object into a dict
instana_version_info_dict = instana_version_info_instance.to_dict()
# create an instance of InstanaVersionInfo from a dict
instana_version_info_from_dict = InstanaVersionInfo.from_dict(instana_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



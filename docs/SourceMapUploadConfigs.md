# SourceMapUploadConfigs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[SourceMapUploadConfig]**](SourceMapUploadConfig.md) |  | [optional] 
**configs** | [**List[SourceMapUploadConfig]**](SourceMapUploadConfig.md) |  | 

## Example

```python
from instana_client.models.source_map_upload_configs import SourceMapUploadConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of SourceMapUploadConfigs from a JSON string
source_map_upload_configs_instance = SourceMapUploadConfigs.from_json(json)
# print the JSON string representation of the object
print(SourceMapUploadConfigs.to_json())

# convert the object into a dict
source_map_upload_configs_dict = source_map_upload_configs_instance.to_dict()
# create an instance of SourceMapUploadConfigs from a dict
source_map_upload_configs_from_dict = SourceMapUploadConfigs.from_dict(source_map_upload_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



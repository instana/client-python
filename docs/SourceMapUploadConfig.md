# SourceMapUploadConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**metadata** | [**List[SourceMapFileMeta]**](SourceMapFileMeta.md) |  | 
**modified_at** | **datetime** |  | [optional] 

## Example

```python
from instana_client.models.source_map_upload_config import SourceMapUploadConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceMapUploadConfig from a JSON string
source_map_upload_config_instance = SourceMapUploadConfig.from_json(json)
# print the JSON string representation of the object
print(SourceMapUploadConfig.to_json())

# convert the object into a dict
source_map_upload_config_dict = source_map_upload_config_instance.to_dict()
# create an instance of SourceMapUploadConfig from a dict
source_map_upload_config_from_dict = SourceMapUploadConfig.from_dict(source_map_upload_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



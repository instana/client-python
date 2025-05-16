# SourceMapFileMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blobs** | [**List[SourceMapFileBlob]**](SourceMapFileBlob.md) |  | [optional] 
**format** | **str** |  | 
**meta** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from instana_client.models.source_map_file_meta import SourceMapFileMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SourceMapFileMeta from a JSON string
source_map_file_meta_instance = SourceMapFileMeta.from_json(json)
# print the JSON string representation of the object
print(SourceMapFileMeta.to_json())

# convert the object into a dict
source_map_file_meta_dict = source_map_file_meta_instance.to_dict()
# create an instance of SourceMapFileMeta from a dict
source_map_file_meta_from_dict = SourceMapFileMeta.from_dict(source_map_file_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SourceMapFileBlob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob_index** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 

## Example

```python
from instana_client.models.source_map_file_blob import SourceMapFileBlob

# TODO update the JSON string below
json = "{}"
# create an instance of SourceMapFileBlob from a JSON string
source_map_file_blob_instance = SourceMapFileBlob.from_json(json)
# print the JSON string representation of the object
print(SourceMapFileBlob.to_json())

# convert the object into a dict
source_map_file_blob_dict = source_map_file_blob_instance.to_dict()
# create an instance of SourceMapFileBlob from a dict
source_map_file_blob_from_dict = SourceMapFileBlob.from_dict(source_map_file_blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



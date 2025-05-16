# TestResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** |  | [optional] 
**start_time** | **int** |  | [optional] 
**test_id** | **str** |  | 
**test_result_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.test_result_metadata import TestResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultMetadata from a JSON string
test_result_metadata_instance = TestResultMetadata.from_json(json)
# print the JSON string representation of the object
print(TestResultMetadata.to_json())

# convert the object into a dict
test_result_metadata_dict = test_result_metadata_instance.to_dict()
# create an instance of TestResultMetadata from a dict
test_result_metadata_from_dict = TestResultMetadata.from_dict(test_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



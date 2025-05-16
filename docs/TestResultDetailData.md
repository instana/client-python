# TestResultDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**har** | **Dict[str, object]** |  | [optional] 
**image_files** | **Dict[str, List[bytearray]]** |  | [optional] 
**log_files** | **Dict[str, str]** |  | [optional] 
**logs** | **str** |  | [optional] 
**subtransaction_avg_metrics** | **Dict[str, object]** |  | [optional] 
**subtransactions** | [**List[TestResultSubtransaction]**](TestResultSubtransaction.md) |  | [optional] 
**test_id** | **str** |  | [optional] 
**test_result_id** | **str** |  | [optional] 
**videos** | **List[bytearray]** |  | [optional] 

## Example

```python
from instana_client.models.test_result_detail_data import TestResultDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultDetailData from a JSON string
test_result_detail_data_instance = TestResultDetailData.from_json(json)
# print the JSON string representation of the object
print(TestResultDetailData.to_json())

# convert the object into a dict
test_result_detail_data_dict = test_result_detail_data_instance.to_dict()
# create an instance of TestResultDetailData from a dict
test_result_detail_data_from_dict = TestResultDetailData.from_dict(test_result_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



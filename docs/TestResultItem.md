# TestResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**application_ids** | **List[str]** |  | [optional] 
**custom_tags** | **Dict[str, str]** |  | [optional] 
**location_id** | **List[str]** |  | [optional] 
**metrics** | **List[Dict[str, object]]** |  | [optional] 
**mobile_application_ids** | **List[str]** |  | [optional] 
**service_id** | **str** |  | [optional] 
**test_id** | **str** |  | 
**test_name** | **str** |  | [optional] 
**website_ids** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.test_result_item import TestResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultItem from a JSON string
test_result_item_instance = TestResultItem.from_json(json)
# print the JSON string representation of the object
print(TestResultItem.to_json())

# convert the object into a dict
test_result_item_dict = test_result_item_instance.to_dict()
# create an instance of TestResultItem from a dict
test_result_item_from_dict = TestResultItem.from_dict(test_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TestResultListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **Dict[str, List[List[float]]]** |  | 
**test_result_common_properties** | [**TestResultCommonProperties**](TestResultCommonProperties.md) |  | 

## Example

```python
from instana_client.models.test_result_list_item import TestResultListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultListItem from a JSON string
test_result_list_item_instance = TestResultListItem.from_json(json)
# print the JSON string representation of the object
print(TestResultListItem.to_json())

# convert the object into a dict
test_result_list_item_dict = test_result_list_item_instance.to_dict()
# create an instance of TestResultListItem from a dict
test_result_list_item_from_dict = TestResultListItem.from_dict(test_result_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



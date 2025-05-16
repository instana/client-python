# TestResultCommonProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**custom_tags** | **Dict[str, str]** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**location_display_label** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**test_common_properties** | [**TestCommonProperties**](TestCommonProperties.md) |  | [optional] 
**test_id** | **str** |  | 
**test_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.test_result_common_properties import TestResultCommonProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultCommonProperties from a JSON string
test_result_common_properties_instance = TestResultCommonProperties.from_json(json)
# print the JSON string representation of the object
print(TestResultCommonProperties.to_json())

# convert the object into a dict
test_result_common_properties_dict = test_result_common_properties_instance.to_dict()
# create an instance of TestResultCommonProperties from a dict
test_result_common_properties_from_dict = TestResultCommonProperties.from_dict(test_result_common_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



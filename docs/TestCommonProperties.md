# TestCommonProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**application_id** | **str** |  | [optional] 
**application_ids** | **List[str]** |  | [optional] 
**application_label** | **str** |  | [optional] 
**application_labels** | **List[str]** |  | [optional] 
**created_at** | **int** |  | [optional] 
**frequency** | **int** |  | 
**get_website_labels** | **List[str]** |  | [optional] 
**id** | **str** |  | 
**label** | **str** |  | 
**location_display_labels** | **List[str]** |  | [optional] 
**location_ids** | **List[str]** |  | [optional] 
**location_labels** | **List[str]** |  | [optional] 
**location_status_list** | [**List[LocationStatus]**](LocationStatus.md) |  | [optional] 
**mobile_application_ids** | **List[str]** |  | [optional] 
**mobile_application_labels** | **List[str]** |  | [optional] 
**modified_at** | **int** |  | [optional] 
**service_id** | **str** |  | [optional] 
**type** | **str** |  | 
**website_ids** | **List[str]** |  | [optional] 
**website_labels** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.test_common_properties import TestCommonProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TestCommonProperties from a JSON string
test_common_properties_instance = TestCommonProperties.from_json(json)
# print the JSON string representation of the object
print(TestCommonProperties.to_json())

# convert the object into a dict
test_common_properties_dict = test_common_properties_instance.to_dict()
# create an instance of TestCommonProperties from a dict
test_common_properties_from_dict = TestCommonProperties.from_dict(test_common_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



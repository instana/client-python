# SyntheticTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**application_id** | **str** |  | [optional] 
**application_label** | **str** |  | [optional] [readonly] 
**application_labels** | **List[str]** |  | [optional] [readonly] 
**applications** | **List[str]** |  | [optional] 
**configuration** | [**SyntheticTypeConfiguration**](SyntheticTypeConfiguration.md) |  | 
**created_at** | **int** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] 
**custom_properties** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | 
**location_display_labels** | **List[str]** |  | [optional] [readonly] 
**location_labels** | **List[str]** |  | [optional] [readonly] 
**locations** | **List[str]** |  | 
**mobile_app_labels** | **List[str]** |  | [optional] [readonly] 
**mobile_apps** | **List[str]** |  | [optional] 
**modified_at** | **int** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**playback_mode** | **str** |  | [optional] 
**rbac_tags** | [**List[ApiTag]**](ApiTag.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**test_frequency** | **int** |  | 
**website_labels** | **List[str]** |  | [optional] [readonly] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_test import SyntheticTest

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTest from a JSON string
synthetic_test_instance = SyntheticTest.from_json(json)
# print the JSON string representation of the object
print(SyntheticTest.to_json())

# convert the object into a dict
synthetic_test_dict = synthetic_test_instance.to_dict()
# create an instance of SyntheticTest from a dict
synthetic_test_from_dict = SyntheticTest.from_dict(synthetic_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



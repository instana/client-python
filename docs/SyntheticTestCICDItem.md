# SyntheticTestCICDItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** |  | [optional] 
**completed** | **bool** |  | 
**customization** | [**SyntheticTestCICDCustomization**](SyntheticTestCICDCustomization.md) |  | 
**location_id** | **str** |  | 
**location_label** | **str** |  | 
**mobile_apps** | **List[str]** |  | [optional] 
**run_type** | **str** |  | [optional] 
**test_id** | **str** |  | 
**test_label** | **str** |  | 
**test_result_id** | **str** |  | 
**test_type** | **str** |  | 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_test_cicd_item import SyntheticTestCICDItem

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTestCICDItem from a JSON string
synthetic_test_cicd_item_instance = SyntheticTestCICDItem.from_json(json)
# print the JSON string representation of the object
print(SyntheticTestCICDItem.to_json())

# convert the object into a dict
synthetic_test_cicd_item_dict = synthetic_test_cicd_item_instance.to_dict()
# create an instance of SyntheticTestCICDItem from a dict
synthetic_test_cicd_item_from_dict = SyntheticTestCICDItem.from_dict(synthetic_test_cicd_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



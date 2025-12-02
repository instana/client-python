# SyntheticTestUpdate

Identifies the type of the synthetic tests updated on this request. Valid types are Deep and Shallow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**applications** | [**SyntheticResourceUpdateListStringListString**](SyntheticResourceUpdateListStringListString.md) |  | [optional] 
**custom_properties** | [**SyntheticResourceUpdateMapStringStringListString**](SyntheticResourceUpdateMapStringStringListString.md) |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**last_modified_at** | **List[int]** |  | [optional] 
**locations** | [**SyntheticResourceUpdateListStringListString**](SyntheticResourceUpdateListStringListString.md) |  | [optional] 
**mobile_apps** | [**SyntheticResourceUpdateListStringListString**](SyntheticResourceUpdateListStringListString.md) |  | [optional] 
**modified_by** | **str** |  | [optional] 
**shallow_update** | **bool** |  | [optional] 
**synthetic_update_type** | **str** | Indicates the type of update to apply to a set of tests of same syntheticType (Deep) or a mix of syntheticType values (Shallow). When Shallow is used, only the configuration properties retries, retryInterval and timeout can be updated  | 
**test_frequency** | **int** |  | [optional] 
**websites** | [**SyntheticResourceUpdateListStringListString**](SyntheticResourceUpdateListStringListString.md) |  | [optional] 

## Example

```python
from instana_client.models.synthetic_test_update import SyntheticTestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTestUpdate from a JSON string
synthetic_test_update_instance = SyntheticTestUpdate.from_json(json)
# print the JSON string representation of the object
print(SyntheticTestUpdate.to_json())

# convert the object into a dict
synthetic_test_update_dict = synthetic_test_update_instance.to_dict()
# create an instance of SyntheticTestUpdate from a dict
synthetic_test_update_from_dict = SyntheticTestUpdate.from_dict(synthetic_test_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



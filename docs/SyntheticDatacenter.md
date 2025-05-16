# SyntheticDatacenter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_name** | **str** |  | 
**code** | **str** |  | 
**configuration** | [**SyntheticDatacenterConfiguration**](SyntheticDatacenterConfiguration.md) |  | [optional] 
**country_name** | **str** |  | 
**datacenter_id** | **str** |  | [optional] 
**expected_active_at** | **int** |  | [optional] 
**label** | **str** |  | 
**latitude** | **float** |  | [optional] 
**location_label** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**modified_at** | **int** |  | [optional] 
**provider** | **str** |  | 
**status** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_datacenter import SyntheticDatacenter

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticDatacenter from a JSON string
synthetic_datacenter_instance = SyntheticDatacenter.from_json(json)
# print the JSON string representation of the object
print(SyntheticDatacenter.to_json())

# convert the object into a dict
synthetic_datacenter_dict = synthetic_datacenter_instance.to_dict()
# create an instance of SyntheticDatacenter from a dict
synthetic_datacenter_from_dict = SyntheticDatacenter.from_dict(synthetic_datacenter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



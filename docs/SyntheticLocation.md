# SyntheticLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**SyntheticLocationConfiguration**](SyntheticLocationConfiguration.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**custom_properties** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**display_label** | **str** |  | [optional] 
**geo_point** | [**SyntheticGeoPoint**](SyntheticGeoPoint.md) |  | 
**id** | **str** |  | [optional] 
**label** | **str** |  | 
**location_type** | **str** |  | 
**modified_at** | **int** |  | [optional] 
**observed_at** | **int** |  | [optional] 
**playback_capabilities** | [**SyntheticPlaybackCapabilities**](SyntheticPlaybackCapabilities.md) |  | 
**pop_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_tests** | **int** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_location import SyntheticLocation

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticLocation from a JSON string
synthetic_location_instance = SyntheticLocation.from_json(json)
# print the JSON string representation of the object
print(SyntheticLocation.to_json())

# convert the object into a dict
synthetic_location_dict = synthetic_location_instance.to_dict()
# create an instance of SyntheticLocation from a dict
synthetic_location_from_dict = SyntheticLocation.from_dict(synthetic_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



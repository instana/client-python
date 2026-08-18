# SamplingMetadata

Metadata about sampling applied to infrastructure metrics query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups_sampled** | **int** | Number of unique groups that were sampled | [optional] 
**groups_skipped** | **int** | Number of unique groups that were not sampled | [optional] 
**sampling_applied** | **bool** | Whether sampling was actually applied (true if any groups were sampled) | [optional] 
**total_members_after** | **int** | Total number of entity members after sampling | [optional] 
**total_members_before** | **int** | Total number of entity members before sampling | [optional] 

## Example

```python
from instana_client.models.sampling_metadata import SamplingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SamplingMetadata from a JSON string
sampling_metadata_instance = SamplingMetadata.from_json(json)
# print the JSON string representation of the object
print(SamplingMetadata.to_json())

# convert the object into a dict
sampling_metadata_dict = sampling_metadata_instance.to_dict()
# create an instance of SamplingMetadata from a dict
sampling_metadata_from_dict = SamplingMetadata.from_dict(sampling_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



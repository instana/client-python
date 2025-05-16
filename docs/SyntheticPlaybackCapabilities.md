# SyntheticPlaybackCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_type** | **List[str]** |  | 
**synthetic_type** | **List[str]** |  | 

## Example

```python
from instana_client.models.synthetic_playback_capabilities import SyntheticPlaybackCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticPlaybackCapabilities from a JSON string
synthetic_playback_capabilities_instance = SyntheticPlaybackCapabilities.from_json(json)
# print the JSON string representation of the object
print(SyntheticPlaybackCapabilities.to_json())

# convert the object into a dict
synthetic_playback_capabilities_dict = synthetic_playback_capabilities_instance.to_dict()
# create an instance of SyntheticPlaybackCapabilities from a dict
synthetic_playback_capabilities_from_dict = SyntheticPlaybackCapabilities.from_dict(synthetic_playback_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



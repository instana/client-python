# SyntheticTimeThreshold

The type of threshold to define the criteria when the event and alert triggers and resolves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**violations_count** | **int** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_time_threshold import SyntheticTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTimeThreshold from a JSON string
synthetic_time_threshold_instance = SyntheticTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(SyntheticTimeThreshold.to_json())

# convert the object into a dict
synthetic_time_threshold_dict = synthetic_time_threshold_instance.to_dict()
# create an instance of SyntheticTimeThreshold from a dict
synthetic_time_threshold_from_dict = SyntheticTimeThreshold.from_dict(synthetic_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



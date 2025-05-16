# InfraTimeThreshold

The type of threshold to define the criteria when the event and alert triggers and resolves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.infra_time_threshold import InfraTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of InfraTimeThreshold from a JSON string
infra_time_threshold_instance = InfraTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(InfraTimeThreshold.to_json())

# convert the object into a dict
infra_time_threshold_dict = infra_time_threshold_instance.to_dict()
# create an instance of InfraTimeThreshold from a dict
infra_time_threshold_from_dict = InfraTimeThreshold.from_dict(infra_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



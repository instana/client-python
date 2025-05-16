# Threshold

Indicates the type of threshold this alert rule is evaluated on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from instana_client.models.threshold import Threshold

# TODO update the JSON string below
json = "{}"
# create an instance of Threshold from a JSON string
threshold_instance = Threshold.from_json(json)
# print the JSON string representation of the object
print(Threshold.to_json())

# convert the object into a dict
threshold_dict = threshold_instance.to_dict()
# create an instance of Threshold from a dict
threshold_from_dict = Threshold.from_dict(threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



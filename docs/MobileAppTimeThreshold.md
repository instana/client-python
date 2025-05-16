# MobileAppTimeThreshold

The type of threshold to define the criteria when the event and alert triggers and resolves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.mobile_app_time_threshold import MobileAppTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppTimeThreshold from a JSON string
mobile_app_time_threshold_instance = MobileAppTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(MobileAppTimeThreshold.to_json())

# convert the object into a dict
mobile_app_time_threshold_dict = mobile_app_time_threshold_instance.to_dict()
# create an instance of MobileAppTimeThreshold from a dict
mobile_app_time_threshold_from_dict = MobileAppTimeThreshold.from_dict(mobile_app_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



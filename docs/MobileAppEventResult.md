# MobileAppEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_app_id** | **str** | ID of the mobile app. | [optional] 

## Example

```python
from instana_client.models.mobile_app_event_result import MobileAppEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppEventResult from a JSON string
mobile_app_event_result_instance = MobileAppEventResult.from_json(json)
# print the JSON string representation of the object
print(MobileAppEventResult.to_json())

# convert the object into a dict
mobile_app_event_result_dict = mobile_app_event_result_instance.to_dict()
# create an instance of MobileAppEventResult from a dict
mobile_app_event_result_from_dict = MobileAppEventResult.from_dict(mobile_app_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



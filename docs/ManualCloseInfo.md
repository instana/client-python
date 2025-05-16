# ManualCloseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_timestamp** | **int** | The closing timestamp. | [optional] 
**disable_event** | **bool** | Flag to indicate whether to disable the event. | [optional] 
**event_ids** | **List[str]** | The event IDs to manually close, in case of multi close. | [optional] 
**mute_alerts** | **bool** | Flag to indicate whether to mute alerts. | [optional] 
**reason_for_closing** | **str** | The reason for manual closing. | 
**username** | **str** | The user name. | 

## Example

```python
from instana_client.models.manual_close_info import ManualCloseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManualCloseInfo from a JSON string
manual_close_info_instance = ManualCloseInfo.from_json(json)
# print the JSON string representation of the object
print(ManualCloseInfo.to_json())

# convert the object into a dict
manual_close_info_dict = manual_close_info_instance.to_dict()
# create an instance of ManualCloseInfo from a dict
manual_close_info_from_dict = ManualCloseInfo.from_dict(manual_close_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



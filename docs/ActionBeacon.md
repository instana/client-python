# ActionBeacon

List of action beacons for the current page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon_type** | **str** | Type of beacon | 
**bytes_ingested_metadata** | **int** | Bytes ingested for metadata | [optional] 
**event_type** | **str** | Event type (e.g., st&#x3D;start, fs&#x3D;frustration signal, oc&#x3D;orientation change) | [optional] 
**frustration_signal** | **str** | Frustration signal type (e.g., rt&#x3D;rage tap) | [optional] 
**keyboard_operation** | **str** | Keyboard operation indicator | [optional] 
**mobile_app_id** | **str** | Mobile app identifier | 
**orientation_change** | **str** | Orientation change indicator (l&#x3D;landscape, p&#x3D;portrait) | [optional] 
**scroll_direction** | **str** | Scroll direction | [optional] 
**scroll_duration** | **str** | Scroll duration in milliseconds | [optional] 
**session_id** | **str** | Session identifier | 
**session_replay_version** | **str** | Session replay version | [optional] 
**timestamp** | **int** | Timestamp when the action was captured (epoch milliseconds) | 
**view_component_class_name** | **str** | View component class name | [optional] 
**view_component_id** | **str** | View component identifier | [optional] 

## Example

```python
from instana_client.models.action_beacon import ActionBeacon

# TODO update the JSON string below
json = "{}"
# create an instance of ActionBeacon from a JSON string
action_beacon_instance = ActionBeacon.from_json(json)
# print the JSON string representation of the object
print(ActionBeacon.to_json())

# convert the object into a dict
action_beacon_dict = action_beacon_instance.to_dict()
# create an instance of ActionBeacon from a dict
action_beacon_from_dict = ActionBeacon.from_dict(action_beacon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



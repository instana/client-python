# MobileAppBeaconsItem

Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon** | [**MobileAppMonitoringBeacon**](MobileAppMonitoringBeacon.md) |  | 
**cursor** | **object** | Cursor to use between successive queries | 
**impacted_beacon_info** | [**ImpactedBeaconInfo**](ImpactedBeaconInfo.md) |  | [optional] 

## Example

```python
from instana_client.models.mobile_app_beacons_item import MobileAppBeaconsItem

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppBeaconsItem from a JSON string
mobile_app_beacons_item_instance = MobileAppBeaconsItem.from_json(json)
# print the JSON string representation of the object
print(MobileAppBeaconsItem.to_json())

# convert the object into a dict
mobile_app_beacons_item_dict = mobile_app_beacons_item_instance.to_dict()
# create an instance of MobileAppBeaconsItem from a dict
mobile_app_beacons_item_from_dict = MobileAppBeaconsItem.from_dict(mobile_app_beacons_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



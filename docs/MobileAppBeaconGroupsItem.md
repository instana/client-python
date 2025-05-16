# MobileAppBeaconGroupsItem

Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **object** | Cursor to use between successive queries | 
**earliest_timestamp** | **int** |  | [optional] 
**metrics** | **Dict[str, List[List[float]]]** |  | 
**name** | **str** |  | 

## Example

```python
from instana_client.models.mobile_app_beacon_groups_item import MobileAppBeaconGroupsItem

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppBeaconGroupsItem from a JSON string
mobile_app_beacon_groups_item_instance = MobileAppBeaconGroupsItem.from_json(json)
# print the JSON string representation of the object
print(MobileAppBeaconGroupsItem.to_json())

# convert the object into a dict
mobile_app_beacon_groups_item_dict = mobile_app_beacon_groups_item_instance.to_dict()
# create an instance of MobileAppBeaconGroupsItem from a dict
mobile_app_beacon_groups_item_from_dict = MobileAppBeaconGroupsItem.from_dict(mobile_app_beacon_groups_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



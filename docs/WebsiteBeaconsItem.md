# WebsiteBeaconsItem

Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon** | [**WebsiteMonitoringBeacon**](WebsiteMonitoringBeacon.md) |  | 
**cursor** | **object** | Cursor to use between successive queries | 

## Example

```python
from instana_client.models.website_beacons_item import WebsiteBeaconsItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteBeaconsItem from a JSON string
website_beacons_item_instance = WebsiteBeaconsItem.from_json(json)
# print the JSON string representation of the object
print(WebsiteBeaconsItem.to_json())

# convert the object into a dict
website_beacons_item_dict = website_beacons_item_instance.to_dict()
# create an instance of WebsiteBeaconsItem from a dict
website_beacons_item_from_dict = WebsiteBeaconsItem.from_dict(website_beacons_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



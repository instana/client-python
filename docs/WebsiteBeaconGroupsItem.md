# WebsiteBeaconGroupsItem

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
from instana_client.models.website_beacon_groups_item import WebsiteBeaconGroupsItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteBeaconGroupsItem from a JSON string
website_beacon_groups_item_instance = WebsiteBeaconGroupsItem.from_json(json)
# print the JSON string representation of the object
print(WebsiteBeaconGroupsItem.to_json())

# convert the object into a dict
website_beacon_groups_item_dict = website_beacon_groups_item_instance.to_dict()
# create an instance of WebsiteBeaconGroupsItem from a dict
website_beacon_groups_item_from_dict = WebsiteBeaconGroupsItem.from_dict(website_beacon_groups_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



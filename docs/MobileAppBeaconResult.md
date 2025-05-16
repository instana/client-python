# MobileAppBeaconResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_timeframe** | [**AdjustedTimeframe**](AdjustedTimeframe.md) |  | [optional] 
**can_load_more** | **bool** | Determine if additional data is available when a new query is made using the cursor from the last item in the &#x60;items&#x60; list. | [optional] 
**items** | [**List[MobileAppBeaconsItem]**](MobileAppBeaconsItem.md) | Represents an array of call group item containing several attributes that describe its properties. The item includes fields such as cursor, metrics, name, and timestamp, which provide detailed information about the item.  | 
**total_hits** | **int** | The total number of items that match a given filter | [optional] 
**total_represented_item_count** | **int** | For calls and EUM beacons, one row can represent multiple real items (batched call, sample multiplicity) | [optional] 
**total_retained_item_count** | **int** | For calls and EUM beacons, only a subset is retained for historic data. Each retained row can represent multiple real items due to batching. | [optional] 

## Example

```python
from instana_client.models.mobile_app_beacon_result import MobileAppBeaconResult

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppBeaconResult from a JSON string
mobile_app_beacon_result_instance = MobileAppBeaconResult.from_json(json)
# print the JSON string representation of the object
print(MobileAppBeaconResult.to_json())

# convert the object into a dict
mobile_app_beacon_result_dict = mobile_app_beacon_result_instance.to_dict()
# create an instance of MobileAppBeaconResult from a dict
mobile_app_beacon_result_from_dict = MobileAppBeaconResult.from_dict(mobile_app_beacon_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



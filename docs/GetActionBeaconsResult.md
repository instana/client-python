# GetActionBeaconsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacons** | [**List[ActionBeacon]**](ActionBeacon.md) | List of action beacons for the current page | 
**has_more** | **bool** | Indicates whether more beacons are available beyond the current page | 
**next_cursor** | **int** | Cursor for the next page (timestamp). Use this value in the next request to fetch more beacons. | [optional] 

## Example

```python
from instana_client.models.get_action_beacons_result import GetActionBeaconsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionBeaconsResult from a JSON string
get_action_beacons_result_instance = GetActionBeaconsResult.from_json(json)
# print the JSON string representation of the object
print(GetActionBeaconsResult.to_json())

# convert the object into a dict
get_action_beacons_result_dict = get_action_beacons_result_instance.to_dict()
# create an instance of GetActionBeaconsResult from a dict
get_action_beacons_result_from_dict = GetActionBeaconsResult.from_dict(get_action_beacons_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



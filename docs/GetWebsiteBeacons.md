# GetWebsiteBeacons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**CursorPagination**](CursorPagination.md) |  | [optional] 
**tag_filters** | [**List[DeprecatedTagFilter]**](DeprecatedTagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.get_website_beacons import GetWebsiteBeacons

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebsiteBeacons from a JSON string
get_website_beacons_instance = GetWebsiteBeacons.from_json(json)
# print the JSON string representation of the object
print(GetWebsiteBeacons.to_json())

# convert the object into a dict
get_website_beacons_dict = get_website_beacons_instance.to_dict()
# create an instance of GetWebsiteBeacons from a dict
get_website_beacons_from_dict = GetWebsiteBeacons.from_dict(get_website_beacons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



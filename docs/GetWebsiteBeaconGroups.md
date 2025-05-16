# GetWebsiteBeaconGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**WebsiteBeaconTagGroup**](WebsiteBeaconTagGroup.md) |  | 
**metrics** | [**List[WebsiteMonitoringMetricsConfiguration]**](WebsiteMonitoringMetricsConfiguration.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**tag_filters** | [**List[DeprecatedTagFilter]**](DeprecatedTagFilter.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.get_website_beacon_groups import GetWebsiteBeaconGroups

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebsiteBeaconGroups from a JSON string
get_website_beacon_groups_instance = GetWebsiteBeaconGroups.from_json(json)
# print the JSON string representation of the object
print(GetWebsiteBeaconGroups.to_json())

# convert the object into a dict
get_website_beacon_groups_dict = get_website_beacon_groups_instance.to_dict()
# create an instance of GetWebsiteBeaconGroups from a dict
get_website_beacon_groups_from_dict = GetWebsiteBeaconGroups.from_dict(get_website_beacon_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



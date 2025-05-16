# GetActivities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | 
**timeframe** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_activities import GetActivities

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivities from a JSON string
get_activities_instance = GetActivities.from_json(json)
# print the JSON string representation of the object
print(GetActivities.to_json())

# convert the object into a dict
get_activities_dict = get_activities_instance.to_dict()
# create an instance of GetActivities from a dict
get_activities_from_dict = GetActivities.from_dict(get_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetAvailablePluginsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | 

## Example

```python
from instana_client.models.get_available_plugins_query import GetAvailablePluginsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailablePluginsQuery from a JSON string
get_available_plugins_query_instance = GetAvailablePluginsQuery.from_json(json)
# print the JSON string representation of the object
print(GetAvailablePluginsQuery.to_json())

# convert the object into a dict
get_available_plugins_query_dict = get_available_plugins_query_instance.to_dict()
# create an instance of GetAvailablePluginsQuery from a dict
get_available_plugins_query_from_dict = GetAvailablePluginsQuery.from_dict(get_available_plugins_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PluginResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Plugin name | [optional] 
**plugin** | **str** | Plugin ID | [optional] 

## Example

```python
from instana_client.models.plugin_result import PluginResult

# TODO update the JSON string below
json = "{}"
# create an instance of PluginResult from a JSON string
plugin_result_instance = PluginResult.from_json(json)
# print the JSON string representation of the object
print(PluginResult.to_json())

# convert the object into a dict
plugin_result_dict = plugin_result_instance.to_dict()
# create an instance of PluginResult from a dict
plugin_result_from_dict = PluginResult.from_dict(plugin_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



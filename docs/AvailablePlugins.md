# AvailablePlugins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.available_plugins import AvailablePlugins

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePlugins from a JSON string
available_plugins_instance = AvailablePlugins.from_json(json)
# print the JSON string representation of the object
print(AvailablePlugins.to_json())

# convert the object into a dict
available_plugins_dict = available_plugins_instance.to_dict()
# create an instance of AvailablePlugins from a dict
available_plugins_from_dict = AvailablePlugins.from_dict(available_plugins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



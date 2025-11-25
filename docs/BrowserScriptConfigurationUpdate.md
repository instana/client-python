# BrowserScriptConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**record_video** | **bool** |  | [optional] 
**script** | **str** |  | [optional] 
**script_type** | **str** |  | [optional] 
**scripts** | [**MultipleScriptsConfiguration**](MultipleScriptsConfiguration.md) |  | [optional] 

## Example

```python
from instana_client.models.browser_script_configuration_update import BrowserScriptConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserScriptConfigurationUpdate from a JSON string
browser_script_configuration_update_instance = BrowserScriptConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(BrowserScriptConfigurationUpdate.to_json())

# convert the object into a dict
browser_script_configuration_update_dict = browser_script_configuration_update_instance.to_dict()
# create an instance of BrowserScriptConfigurationUpdate from a dict
browser_script_configuration_update_from_dict = BrowserScriptConfigurationUpdate.from_dict(browser_script_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BrowserScriptConfiguration


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
from instana_client.models.browser_script_configuration import BrowserScriptConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserScriptConfiguration from a JSON string
browser_script_configuration_instance = BrowserScriptConfiguration.from_json(json)
# print the JSON string representation of the object
print(BrowserScriptConfiguration.to_json())

# convert the object into a dict
browser_script_configuration_dict = browser_script_configuration_instance.to_dict()
# create an instance of BrowserScriptConfiguration from a dict
browser_script_configuration_from_dict = BrowserScriptConfiguration.from_dict(browser_script_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



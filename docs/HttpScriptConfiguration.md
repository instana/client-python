# HttpScriptConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**script_type** | **str** |  | [optional] 
**scripts** | [**MultipleScriptsConfiguration**](MultipleScriptsConfiguration.md) |  | [optional] 

## Example

```python
from instana_client.models.http_script_configuration import HttpScriptConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of HttpScriptConfiguration from a JSON string
http_script_configuration_instance = HttpScriptConfiguration.from_json(json)
# print the JSON string representation of the object
print(HttpScriptConfiguration.to_json())

# convert the object into a dict
http_script_configuration_dict = http_script_configuration_instance.to_dict()
# create an instance of HttpScriptConfiguration from a dict
http_script_configuration_from_dict = HttpScriptConfiguration.from_dict(http_script_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



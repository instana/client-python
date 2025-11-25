# WebpageScriptConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**record_video** | **bool** |  | [optional] 
**script** | **str** |  | [optional] 

## Example

```python
from instana_client.models.webpage_script_configuration_update import WebpageScriptConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageScriptConfigurationUpdate from a JSON string
webpage_script_configuration_update_instance = WebpageScriptConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(WebpageScriptConfigurationUpdate.to_json())

# convert the object into a dict
webpage_script_configuration_update_dict = webpage_script_configuration_update_instance.to_dict()
# create an instance of WebpageScriptConfigurationUpdate from a dict
webpage_script_configuration_update_from_dict = WebpageScriptConfigurationUpdate.from_dict(webpage_script_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



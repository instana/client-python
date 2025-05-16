# WebpageScriptConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] 
**record_video** | **bool** |  | [optional] 
**script** | **str** |  | 

## Example

```python
from instana_client.models.webpage_script_configuration import WebpageScriptConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageScriptConfiguration from a JSON string
webpage_script_configuration_instance = WebpageScriptConfiguration.from_json(json)
# print the JSON string representation of the object
print(WebpageScriptConfiguration.to_json())

# convert the object into a dict
webpage_script_configuration_dict = webpage_script_configuration_instance.to_dict()
# create an instance of WebpageScriptConfiguration from a dict
webpage_script_configuration_from_dict = WebpageScriptConfiguration.from_dict(webpage_script_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



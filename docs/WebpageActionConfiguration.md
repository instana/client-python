# WebpageActionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] 
**record_video** | **bool** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from instana_client.models.webpage_action_configuration import WebpageActionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageActionConfiguration from a JSON string
webpage_action_configuration_instance = WebpageActionConfiguration.from_json(json)
# print the JSON string representation of the object
print(WebpageActionConfiguration.to_json())

# convert the object into a dict
webpage_action_configuration_dict = webpage_action_configuration_instance.to_dict()
# create an instance of WebpageActionConfiguration from a dict
webpage_action_configuration_from_dict = WebpageActionConfiguration.from_dict(webpage_action_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



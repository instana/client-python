# WebpageActionConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] 
**record_video** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from instana_client.models.webpage_action_configuration_update import WebpageActionConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageActionConfigurationUpdate from a JSON string
webpage_action_configuration_update_instance = WebpageActionConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(WebpageActionConfigurationUpdate.to_json())

# convert the object into a dict
webpage_action_configuration_update_dict = webpage_action_configuration_update_instance.to_dict()
# create an instance of WebpageActionConfigurationUpdate from a dict
webpage_action_configuration_update_from_dict = WebpageActionConfigurationUpdate.from_dict(webpage_action_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



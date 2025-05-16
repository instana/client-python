# MultipleScriptsConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | **str** |  | [optional] 
**script_file** | **str** |  | [optional] 

## Example

```python
from instana_client.models.multiple_scripts_configuration import MultipleScriptsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleScriptsConfiguration from a JSON string
multiple_scripts_configuration_instance = MultipleScriptsConfiguration.from_json(json)
# print the JSON string representation of the object
print(MultipleScriptsConfiguration.to_json())

# convert the object into a dict
multiple_scripts_configuration_dict = multiple_scripts_configuration_instance.to_dict()
# create an instance of MultipleScriptsConfiguration from a dict
multiple_scripts_configuration_from_dict = MultipleScriptsConfiguration.from_dict(multiple_scripts_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



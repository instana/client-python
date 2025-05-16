# ConfigVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_summary** | [**ChangeSummary**](ChangeSummary.md) |  | [optional] 
**created** | **int** | Unix timestamp representing the creation time of this revision. | [optional] 
**deleted** | **bool** | Flag to indicate whether or not the configuration was deleted. | [optional] 
**enabled** | **bool** | Flag to indicate whether or not the configuration is enabled. | [optional] 
**id** | **str** | ID of this configuration version. | 

## Example

```python
from instana_client.models.config_version import ConfigVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigVersion from a JSON string
config_version_instance = ConfigVersion.from_json(json)
# print the JSON string representation of the object
print(ConfigVersion.to_json())

# convert the object into a dict
config_version_dict = config_version_instance.to_dict()
# create an instance of ConfigVersion from a dict
config_version_from_dict = ConfigVersion.from_dict(config_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



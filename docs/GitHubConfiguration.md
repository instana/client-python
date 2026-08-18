# GitHubConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_credentials** | **List[str]** |  | [optional] 
**credential_name** | **str** |  | [optional] 
**script_file** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from instana_client.models.git_hub_configuration import GitHubConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubConfiguration from a JSON string
git_hub_configuration_instance = GitHubConfiguration.from_json(json)
# print the JSON string representation of the object
print(GitHubConfiguration.to_json())

# convert the object into a dict
git_hub_configuration_dict = git_hub_configuration_instance.to_dict()
# create an instance of GitHubConfiguration from a dict
git_hub_configuration_from_dict = GitHubConfiguration.from_dict(git_hub_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



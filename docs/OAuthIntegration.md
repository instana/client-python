# OAuthIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**OAuthConfig**](OAuthConfig.md) |  | [optional] 
**token** | [**OAuthToken**](OAuthToken.md) |  | [optional] 

## Example

```python
from instana_client.models.o_auth_integration import OAuthIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthIntegration from a JSON string
o_auth_integration_instance = OAuthIntegration.from_json(json)
# print the JSON string representation of the object
print(OAuthIntegration.to_json())

# convert the object into a dict
o_auth_integration_dict = o_auth_integration_instance.to_dict()
# create an instance of OAuthIntegration from a dict
o_auth_integration_from_dict = OAuthIntegration.from_dict(o_auth_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



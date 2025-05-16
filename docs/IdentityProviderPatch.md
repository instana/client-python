# IdentityProviderPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restrict_empty_idp_groups** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.identity_provider_patch import IdentityProviderPatch

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderPatch from a JSON string
identity_provider_patch_instance = IdentityProviderPatch.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderPatch.to_json())

# convert the object into a dict
identity_provider_patch_dict = identity_provider_patch_instance.to_dict()
# create an instance of IdentityProviderPatch from a dict
identity_provider_patch_from_dict = IdentityProviderPatch.from_dict(identity_provider_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



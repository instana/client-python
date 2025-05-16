# ApiPermissionSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_filter** | [**ScopeBinding**](ScopeBinding.md) |  | [optional] 
**application_ids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**business_perspective_ids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**infra_dfq_filter** | [**ScopeBinding**](ScopeBinding.md) |  | 
**kubernetes_cluster_uuids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**kubernetes_namespace_uids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**mobile_app_ids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**permissions** | **List[str]** |  | 
**restricted_application_filter** | [**ApiRestrictedApplicationFilter**](ApiRestrictedApplicationFilter.md) |  | [optional] 
**synthetic_credential_keys** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**synthetic_test_ids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 
**website_ids** | [**List[ScopeBinding]**](ScopeBinding.md) |  | 

## Example

```python
from instana_client.models.api_permission_set import ApiPermissionSet

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPermissionSet from a JSON string
api_permission_set_instance = ApiPermissionSet.from_json(json)
# print the JSON string representation of the object
print(ApiPermissionSet.to_json())

# convert the object into a dict
api_permission_set_dict = api_permission_set_instance.to_dict()
# create an instance of ApiPermissionSet from a dict
api_permission_set_from_dict = ApiPermissionSet.from_dict(api_permission_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



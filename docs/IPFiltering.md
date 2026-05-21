# IPFiltering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the configuration is currently enforced, can be permanent active (if verified), or temporary after creation (enabling the verification). | [optional] 
**deny_all** | **bool** | Fallback configuration, if unmatched requests should be denied. | [optional] 
**enabled** | **bool** | If the configuration should be enforced. See active status if it is actually enforced. | [optional] 
**last_changed_at** | **int** | When the configuration was last changed. | [optional] 
**last_verified_at** | **int** | When the configuration was last verified. Can be used to assume if a configuration needs to be verified. | [optional] 
**rules** | [**List[IPFilteringRuleDto]**](IPFilteringRuleDto.md) | Actual traffic rules. Enforcing allow / block based on incoming IP address. Are evaluated in given order. | 
**support_access_enabled** | **bool** | If Instana support should be able to access your environment. Instana support is still able to to deactivate the configuration for you (manual process). | [optional] 

## Example

```python
from instana_client.models.ip_filtering import IPFiltering

# TODO update the JSON string below
json = "{}"
# create an instance of IPFiltering from a JSON string
ip_filtering_instance = IPFiltering.from_json(json)
# print the JSON string representation of the object
print(IPFiltering.to_json())

# convert the object into a dict
ip_filtering_dict = ip_filtering_instance.to_dict()
# create an instance of IPFiltering from a dict
ip_filtering_from_dict = IPFiltering.from_dict(ip_filtering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



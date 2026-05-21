# IPFilteringUpsert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deny_all** | **bool** | Fallback configuration, if unmatched requests should be denied. | 
**enabled** | **bool** | If the configuration should be enforced. See active status if it is actually enforced. | 
**rules** | [**List[IPFilteringRuleDto]**](IPFilteringRuleDto.md) | Actual traffic rules. Enforcing allow / block based on incoming IP address. Are evaluated in given order. | 
**support_access_enabled** | **bool** | If Instana support should be able to access your environment. Instana support is still able to to deactivate the configuration for you (manual process). | 

## Example

```python
from instana_client.models.ip_filtering_upsert import IPFilteringUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of IPFilteringUpsert from a JSON string
ip_filtering_upsert_instance = IPFilteringUpsert.from_json(json)
# print the JSON string representation of the object
print(IPFilteringUpsert.to_json())

# convert the object into a dict
ip_filtering_upsert_dict = ip_filtering_upsert_instance.to_dict()
# create an instance of IPFilteringUpsert from a dict
ip_filtering_upsert_from_dict = IPFilteringUpsert.from_dict(ip_filtering_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



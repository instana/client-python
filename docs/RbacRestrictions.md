# RbacRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_filters** | **List[str]** |  | [optional] 
**alerting_channels** | **List[str]** |  | [optional] 
**apdex_ids** | **List[str]** |  | [optional] 
**applications** | **List[str]** |  | [optional] 
**business_perspectives** | **List[str]** |  | [optional] 
**infra_dfq_filter** | **List[str]** |  | [optional] 
**kubernetes_clusters** | **List[str]** |  | [optional] 
**kubernetes_namespaces** | **List[str]** |  | [optional] 
**log_filters** | **List[str]** |  | [optional] 
**logging_perspectives** | **List[str]** |  | [optional] 
**mobile_apps** | **List[str]** |  | [optional] 
**service_levels** | **List[str]** |  | [optional] 
**synthetic_credentials** | **List[str]** |  | [optional] 
**synthetic_tests** | **List[str]** |  | [optional] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.rbac_restrictions import RbacRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of RbacRestrictions from a JSON string
rbac_restrictions_instance = RbacRestrictions.from_json(json)
# print the JSON string representation of the object
print(RbacRestrictions.to_json())

# convert the object into a dict
rbac_restrictions_dict = rbac_restrictions_instance.to_dict()
# create an instance of RbacRestrictions from a dict
rbac_restrictions_from_dict = RbacRestrictions.from_dict(rbac_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



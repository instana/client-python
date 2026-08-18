# ApdexConfigWithRBACTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apdex_entity** | [**ApdexEntity**](ApdexEntity.md) |  | 
**apdex_name** | **str** |  | 
**created_at** | **int** | Created date of Apdex Configuration (Unix timestamp in milliseconds) | [optional] 
**id** | **str** | Apdex Configuration ID | 
**last_updated** | **int** | Last updated date of Apdex Configuration (Unix timestamp in milliseconds) | [optional] 
**rbac_tags** | [**List[ApiTag]**](ApiTag.md) |  | [optional] 
**tags** | **List[str]** | List of tags associated with Apdex Configuration | [optional] 

## Example

```python
from instana_client.models.apdex_config_with_rbac_tag import ApdexConfigWithRBACTag

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexConfigWithRBACTag from a JSON string
apdex_config_with_rbac_tag_instance = ApdexConfigWithRBACTag.from_json(json)
# print the JSON string representation of the object
print(ApdexConfigWithRBACTag.to_json())

# convert the object into a dict
apdex_config_with_rbac_tag_dict = apdex_config_with_rbac_tag_instance.to_dict()
# create an instance of ApdexConfigWithRBACTag from a dict
apdex_config_with_rbac_tag_from_dict = ApdexConfigWithRBACTag.from_dict(apdex_config_with_rbac_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



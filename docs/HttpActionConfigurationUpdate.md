# HttpActionConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_insecure** | **bool** |  | [optional] 
**body** | **str** |  | [optional] 
**expect_exists** | [**SyntheticResourceUpdateListStringListString**](SyntheticResourceUpdateListStringListString.md) |  | [optional] 
**expect_json** | **object** |  | [optional] 
**expect_match** | **str** |  | [optional] 
**expect_not_empty** | [**SyntheticResourceUpdateListStringListString**](SyntheticResourceUpdateListStringListString.md) |  | [optional] 
**expect_status** | **int** |  | [optional] 
**follow_redirect** | **bool** |  | [optional] 
**headers** | [**SyntheticResourceUpdateMapStringStringListString**](SyntheticResourceUpdateMapStringStringListString.md) |  | [optional] 
**operation** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**validation_string** | **str** |  | [optional] 

## Example

```python
from instana_client.models.http_action_configuration_update import HttpActionConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of HttpActionConfigurationUpdate from a JSON string
http_action_configuration_update_instance = HttpActionConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(HttpActionConfigurationUpdate.to_json())

# convert the object into a dict
http_action_configuration_update_dict = http_action_configuration_update_instance.to_dict()
# create an instance of HttpActionConfigurationUpdate from a dict
http_action_configuration_update_from_dict = HttpActionConfigurationUpdate.from_dict(http_action_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



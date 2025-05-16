# HttpActionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_insecure** | **bool** |  | [optional] 
**body** | **str** |  | [optional] 
**expect_exists** | **List[str]** |  | [optional] 
**expect_json** | **object** |  | [optional] 
**expect_match** | **str** |  | [optional] 
**expect_not_empty** | **List[str]** |  | [optional] 
**expect_status** | **int** |  | [optional] 
**follow_redirect** | **bool** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**operation** | **str** |  | [optional] 
**url** | **str** |  | 
**validation_string** | **str** |  | [optional] 

## Example

```python
from instana_client.models.http_action_configuration import HttpActionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of HttpActionConfiguration from a JSON string
http_action_configuration_instance = HttpActionConfiguration.from_json(json)
# print the JSON string representation of the object
print(HttpActionConfiguration.to_json())

# convert the object into a dict
http_action_configuration_dict = http_action_configuration_instance.to_dict()
# create an instance of HttpActionConfiguration from a dict
http_action_configuration_from_dict = HttpActionConfiguration.from_dict(http_action_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



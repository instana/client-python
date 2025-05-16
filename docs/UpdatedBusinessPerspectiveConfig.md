# UpdatedBusinessPerspectiveConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 

## Example

```python
from instana_client.models.updated_business_perspective_config import UpdatedBusinessPerspectiveConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedBusinessPerspectiveConfig from a JSON string
updated_business_perspective_config_instance = UpdatedBusinessPerspectiveConfig.from_json(json)
# print the JSON string representation of the object
print(UpdatedBusinessPerspectiveConfig.to_json())

# convert the object into a dict
updated_business_perspective_config_dict = updated_business_perspective_config_instance.to_dict()
# create an instance of UpdatedBusinessPerspectiveConfig from a dict
updated_business_perspective_config_from_dict = UpdatedBusinessPerspectiveConfig.from_dict(updated_business_perspective_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



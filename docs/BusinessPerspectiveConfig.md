# BusinessPerspectiveConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 

## Example

```python
from instana_client.models.business_perspective_config import BusinessPerspectiveConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessPerspectiveConfig from a JSON string
business_perspective_config_instance = BusinessPerspectiveConfig.from_json(json)
# print the JSON string representation of the object
print(BusinessPerspectiveConfig.to_json())

# convert the object into a dict
business_perspective_config_dict = business_perspective_config_instance.to_dict()
# create an instance of BusinessPerspectiveConfig from a dict
business_perspective_config_from_dict = BusinessPerspectiveConfig.from_dict(business_perspective_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



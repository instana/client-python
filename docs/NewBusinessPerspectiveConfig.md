# NewBusinessPerspectiveConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 

## Example

```python
from instana_client.models.new_business_perspective_config import NewBusinessPerspectiveConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NewBusinessPerspectiveConfig from a JSON string
new_business_perspective_config_instance = NewBusinessPerspectiveConfig.from_json(json)
# print the JSON string representation of the object
print(NewBusinessPerspectiveConfig.to_json())

# convert the object into a dict
new_business_perspective_config_dict = new_business_perspective_config_instance.to_dict()
# create an instance of NewBusinessPerspectiveConfig from a dict
new_business_perspective_config_from_dict = NewBusinessPerspectiveConfig.from_dict(new_business_perspective_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



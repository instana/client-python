# TagFilterExpressionElement

Boolean expression of tag filters to define the scope of relevant calls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from instana_client.models.tag_filter_expression_element import TagFilterExpressionElement

# TODO update the JSON string below
json = "{}"
# create an instance of TagFilterExpressionElement from a JSON string
tag_filter_expression_element_instance = TagFilterExpressionElement.from_json(json)
# print the JSON string representation of the object
print(TagFilterExpressionElement.to_json())

# convert the object into a dict
tag_filter_expression_element_dict = tag_filter_expression_element_instance.to_dict()
# create an instance of TagFilterExpressionElement from a dict
tag_filter_expression_element_from_dict = TagFilterExpressionElement.from_dict(tag_filter_expression_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



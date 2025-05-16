# TagFilterExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[TagFilterExpressionElement]**](TagFilterExpressionElement.md) |  | 
**logical_operator** | **str** | Set AND / OR | 

## Example

```python
from instana_client.models.tag_filter_expression import TagFilterExpression

# TODO update the JSON string below
json = "{}"
# create an instance of TagFilterExpression from a JSON string
tag_filter_expression_instance = TagFilterExpression.from_json(json)
# print the JSON string representation of the object
print(TagFilterExpression.to_json())

# convert the object into a dict
tag_filter_expression_dict = tag_filter_expression_instance.to_dict()
# create an instance of TagFilterExpression from a dict
tag_filter_expression_from_dict = TagFilterExpression.from_dict(tag_filter_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



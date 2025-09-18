# MatchExpressionDTO

 Specify the expression to match, For example, `endpoint.name contains health`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from instana_client.models.match_expression_dto import MatchExpressionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MatchExpressionDTO from a JSON string
match_expression_dto_instance = MatchExpressionDTO.from_json(json)
# print the JSON string representation of the object
print(MatchExpressionDTO.to_json())

# convert the object into a dict
match_expression_dto_dict = match_expression_dto_instance.to_dict()
# create an instance of MatchExpressionDTO from a dict
match_expression_dto_from_dict = MatchExpressionDTO.from_dict(match_expression_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



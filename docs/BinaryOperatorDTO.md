# BinaryOperatorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conjunction** | **str** |  | 
**left** | [**MatchExpressionDTO**](MatchExpressionDTO.md) |  | 
**right** | [**MatchExpressionDTO**](MatchExpressionDTO.md) |  | 

## Example

```python
from instana_client.models.binary_operator_dto import BinaryOperatorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryOperatorDTO from a JSON string
binary_operator_dto_instance = BinaryOperatorDTO.from_json(json)
# print the JSON string representation of the object
print(BinaryOperatorDTO.to_json())

# convert the object into a dict
binary_operator_dto_dict = binary_operator_dto_instance.to_dict()
# create an instance of BinaryOperatorDTO from a dict
binary_operator_dto_from_dict = BinaryOperatorDTO.from_dict(binary_operator_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



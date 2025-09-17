# ArithmeticOperand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | [optional] 
**cross_series_aggregation** | **str** |  | [optional] 
**granularity** | **int** |  | [optional] 
**metric** | **str** |  | [optional] 
**regex** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**operation** | [**ArithmeticOperation**](ArithmeticOperation.md) |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from instana_client.models.arithmetic_operand import ArithmeticOperand

# TODO update the JSON string below
json = "{}"
# create an instance of ArithmeticOperand from a JSON string
arithmetic_operand_instance = ArithmeticOperand.from_json(json)
# print the JSON string representation of the object
print(ArithmeticOperand.to_json())

# convert the object into a dict
arithmetic_operand_dict = arithmetic_operand_instance.to_dict()
# create an instance of ArithmeticOperand from a dict
arithmetic_operand_from_dict = ArithmeticOperand.from_dict(arithmetic_operand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



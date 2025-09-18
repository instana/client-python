# ArithmeticOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ArithmeticOperand**](ArithmeticOperand.md) |  | 
**operator** | **str** |  | 
**right** | [**ArithmeticOperand**](ArithmeticOperand.md) |  | 

## Example

```python
from instana_client.models.arithmetic_operation import ArithmeticOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ArithmeticOperation from a JSON string
arithmetic_operation_instance = ArithmeticOperation.from_json(json)
# print the JSON string representation of the object
print(ArithmeticOperation.to_json())

# convert the object into a dict
arithmetic_operation_dict = arithmetic_operation_instance.to_dict()
# create an instance of ArithmeticOperation from a dict
arithmetic_operation_from_dict = ArithmeticOperation.from_dict(arithmetic_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



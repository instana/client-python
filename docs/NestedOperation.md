# NestedOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**aggregation** | **str** |  | [optional] 
**cross_series_aggregation** | **str** |  | [optional] 
**granularity** | **int** |  | [optional] 
**metric** | **str** |  | [optional] 
**regex** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**operation** | [**ArithmeticOperation**](ArithmeticOperation.md) |  | [optional] 

## Example

```python
from instana_client.models.nested_operation import NestedOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NestedOperation from a JSON string
nested_operation_instance = NestedOperation.from_json(json)
# print the JSON string representation of the object
print(NestedOperation.to_json())

# convert the object into a dict
nested_operation_dict = nested_operation_instance.to_dict()
# create an instance of NestedOperation from a dict
nested_operation_from_dict = NestedOperation.from_dict(nested_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



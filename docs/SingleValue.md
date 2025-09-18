# SingleValue


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
from instana_client.models.single_value import SingleValue

# TODO update the JSON string below
json = "{}"
# create an instance of SingleValue from a JSON string
single_value_instance = SingleValue.from_json(json)
# print the JSON string representation of the object
print(SingleValue.to_json())

# convert the object into a dict
single_value_dict = single_value_instance.to_dict()
# create an instance of SingleValue from a dict
single_value_from_dict = SingleValue.from_dict(single_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



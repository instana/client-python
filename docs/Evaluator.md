# Evaluator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | **str** |  | 
**evaluator_id** | **str** |  | [optional] 
**evaluator_name** | **str** |  | 
**is_built_in** | **bool** |  | [optional] 
**mean_score** | **float** |  | [optional] 
**number_of_runs** | **int** |  | [optional] 
**pass_rate_mean** | **float** |  | [optional] 
**threshold** | **float** |  | 

## Example

```python
from instana_client.models.evaluator import Evaluator

# TODO update the JSON string below
json = "{}"
# create an instance of Evaluator from a JSON string
evaluator_instance = Evaluator.from_json(json)
# print the JSON string representation of the object
print(Evaluator.to_json())

# convert the object into a dict
evaluator_dict = evaluator_instance.to_dict()
# create an instance of Evaluator from a dict
evaluator_from_dict = Evaluator.from_dict(evaluator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



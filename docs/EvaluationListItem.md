# EvaluationListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_mean_ms** | **float** |  | [optional] 
**evaluation_id** | **str** |  | [optional] 
**evaluator_names** | **List[str]** |  | [optional] 
**evaluators** | **List[str]** |  | [optional] 
**last_run_start** | **int** |  | [optional] 
**metadata** | **str** |  | [optional] 
**model_names** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_runs** | **int** |  | [optional] 
**sampling_percentage** | **float** |  | [optional] 
**service_names** | **List[str]** |  | [optional] 
**time_before_run_hours** | **int** |  | [optional] 
**time_before_run_minutes** | **int** |  | [optional] 
**trace_ids** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.evaluation_list_item import EvaluationListItem

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationListItem from a JSON string
evaluation_list_item_instance = EvaluationListItem.from_json(json)
# print the JSON string representation of the object
print(EvaluationListItem.to_json())

# convert the object into a dict
evaluation_list_item_dict = evaluation_list_item_instance.to_dict()
# create an instance of EvaluationListItem from a dict
evaluation_list_item_from_dict = EvaluationListItem.from_dict(evaluation_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



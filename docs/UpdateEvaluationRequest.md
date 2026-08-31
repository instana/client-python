# UpdateEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**evaluation_id** | **str** |  | 
**evaluation_name** | **str** |  | 
**evaluator_ids** | **List[str]** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**model_names** | **List[str]** |  | [optional] 
**sampling_percentage** | **float** |  | [optional] 
**service_names** | **List[str]** |  | [optional] 
**time_before_run_hours** | **int** |  | [optional] 
**time_before_run_minutes** | **int** |  | [optional] 
**trace_ids** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.update_evaluation_request import UpdateEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEvaluationRequest from a JSON string
update_evaluation_request_instance = UpdateEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEvaluationRequest.to_json())

# convert the object into a dict
update_evaluation_request_dict = update_evaluation_request_instance.to_dict()
# create an instance of UpdateEvaluationRequest from a dict
update_evaluation_request_from_dict = UpdateEvaluationRequest.from_dict(update_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



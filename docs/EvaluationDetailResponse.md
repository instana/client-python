# EvaluationDetailResponse

Detailed evaluation information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client identifier | [optional] 
**created_at** | **int** | Creation timestamp (milliseconds since epoch) | [optional] 
**created_by** | **str** | User who created the evaluation | [optional] 
**description** | **str** | Description of the evaluation | [optional] 
**evaluation_id** | **str** | Unique identifier for the evaluation | [optional] 
**evaluation_name** | **str** | Human-readable name for the evaluation | [optional] 
**evaluator_ids** | **List[str]** | List of evaluator IDs to be used | [optional] 
**model_names** | **List[str]** | List of model names to filter traces | [optional] 
**sampling_percentage** | **float** | Percentage of traces to sample | [optional] 
**service_names** | **List[str]** | List of service names to filter traces | [optional] 
**time_before_run_hours** | **int** | Hours before run to include traces | [optional] 
**time_before_run_minutes** | **int** | Minutes before run to include traces | [optional] 
**trace_ids** | **List[str]** | List of trace IDs to evaluate | [optional] 

## Example

```python
from instana_client.models.evaluation_detail_response import EvaluationDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationDetailResponse from a JSON string
evaluation_detail_response_instance = EvaluationDetailResponse.from_json(json)
# print the JSON string representation of the object
print(EvaluationDetailResponse.to_json())

# convert the object into a dict
evaluation_detail_response_dict = evaluation_detail_response_instance.to_dict()
# create an instance of EvaluationDetailResponse from a dict
evaluation_detail_response_from_dict = EvaluationDetailResponse.from_dict(evaluation_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



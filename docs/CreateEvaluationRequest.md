# CreateEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
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
from instana_client.models.create_evaluation_request import CreateEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvaluationRequest from a JSON string
create_evaluation_request_instance = CreateEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEvaluationRequest.to_json())

# convert the object into a dict
create_evaluation_request_dict = create_evaluation_request_instance.to_dict()
# create an instance of CreateEvaluationRequest from a dict
create_evaluation_request_from_dict = CreateEvaluationRequest.from_dict(create_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RunEvaluationResponse

Response from running an evaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_name** | **str** | The LLM gateway name that will be used for evaluation | [optional] 
**message** | **str** | Status message | [optional] 
**success** | **bool** | Whether the evaluation run was initiated successfully | [optional] 

## Example

```python
from instana_client.models.run_evaluation_response import RunEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunEvaluationResponse from a JSON string
run_evaluation_response_instance = RunEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(RunEvaluationResponse.to_json())

# convert the object into a dict
run_evaluation_response_dict = run_evaluation_response_instance.to_dict()
# create an instance of RunEvaluationResponse from a dict
run_evaluation_response_from_dict = RunEvaluationResponse.from_dict(run_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



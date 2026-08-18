# CreateEvaluationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from instana_client.models.create_evaluation_response import CreateEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvaluationResponse from a JSON string
create_evaluation_response_instance = CreateEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateEvaluationResponse.to_json())

# convert the object into a dict
create_evaluation_response_dict = create_evaluation_response_instance.to_dict()
# create an instance of CreateEvaluationResponse from a dict
create_evaluation_response_from_dict = CreateEvaluationResponse.from_dict(create_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



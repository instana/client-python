# EvaluationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluations** | [**List[EvaluationListItem]**](EvaluationListItem.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from instana_client.models.evaluation_list_response import EvaluationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationListResponse from a JSON string
evaluation_list_response_instance = EvaluationListResponse.from_json(json)
# print the JSON string representation of the object
print(EvaluationListResponse.to_json())

# convert the object into a dict
evaluation_list_response_dict = evaluation_list_response_instance.to_dict()
# create an instance of EvaluationListResponse from a dict
evaluation_list_response_from_dict = EvaluationListResponse.from_dict(evaluation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



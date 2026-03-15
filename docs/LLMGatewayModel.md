# LLMGatewayModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **Dict[str, object]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.llm_gateway_model import LLMGatewayModel

# TODO update the JSON string below
json = "{}"
# create an instance of LLMGatewayModel from a JSON string
llm_gateway_model_instance = LLMGatewayModel.from_json(json)
# print the JSON string representation of the object
print(LLMGatewayModel.to_json())

# convert the object into a dict
llm_gateway_model_dict = llm_gateway_model_instance.to_dict()
# create an instance of LLMGatewayModel from a dict
llm_gateway_model_from_dict = LLMGatewayModel.from_dict(llm_gateway_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



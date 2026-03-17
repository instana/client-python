# LLMGatewayService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_parameters** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.llm_gateway_service import LLMGatewayService

# TODO update the JSON string below
json = "{}"
# create an instance of LLMGatewayService from a JSON string
llm_gateway_service_instance = LLMGatewayService.from_json(json)
# print the JSON string representation of the object
print(LLMGatewayService.to_json())

# convert the object into a dict
llm_gateway_service_dict = llm_gateway_service_instance.to_dict()
# create an instance of LLMGatewayService from a dict
llm_gateway_service_from_dict = LLMGatewayService.from_dict(llm_gateway_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



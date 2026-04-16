# LLMGatewayTestConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_parameters** | **Dict[str, str]** |  | [optional] 
**gateway_id** | **str** |  | [optional] 
**service_id** | **str** |  | 

## Example

```python
from instana_client.models.llm_gateway_test_connection_request import LLMGatewayTestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LLMGatewayTestConnectionRequest from a JSON string
llm_gateway_test_connection_request_instance = LLMGatewayTestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(LLMGatewayTestConnectionRequest.to_json())

# convert the object into a dict
llm_gateway_test_connection_request_dict = llm_gateway_test_connection_request_instance.to_dict()
# create an instance of LLMGatewayTestConnectionRequest from a dict
llm_gateway_test_connection_request_from_dict = LLMGatewayTestConnectionRequest.from_dict(llm_gateway_test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LLMGatewayCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.llm_gateway_capability import LLMGatewayCapability

# TODO update the JSON string below
json = "{}"
# create an instance of LLMGatewayCapability from a JSON string
llm_gateway_capability_instance = LLMGatewayCapability.from_json(json)
# print the JSON string representation of the object
print(LLMGatewayCapability.to_json())

# convert the object into a dict
llm_gateway_capability_dict = llm_gateway_capability_instance.to_dict()
# create an instance of LLMGatewayCapability from a dict
llm_gateway_capability_from_dict = LLMGatewayCapability.from_dict(llm_gateway_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



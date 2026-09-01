# LLMEgressGateway

Custom handler definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[LLMGatewayCapability]**](LLMGatewayCapability.md) |  | 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | 
**instana_agents** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**model** | [**LLMGatewayModel**](LLMGatewayModel.md) |  | 
**modified_at** | **str** |  | [optional] 
**name** | **str** |  | 
**prompt** | **str** |  | [optional] 
**service** | [**LLMGatewayService**](LLMGatewayService.md) |  | 
**system** | **bool** |  | [optional] 
**tenant_unit_id** | **str** |  | 

## Example

```python
from instana_client.models.llm_egress_gateway import LLMEgressGateway

# TODO update the JSON string below
json = "{}"
# create an instance of LLMEgressGateway from a JSON string
llm_egress_gateway_instance = LLMEgressGateway.from_json(json)
# print the JSON string representation of the object
print(LLMEgressGateway.to_json())

# convert the object into a dict
llm_egress_gateway_dict = llm_egress_gateway_instance.to_dict()
# create an instance of LLMEgressGateway from a dict
llm_egress_gateway_from_dict = LLMEgressGateway.from_dict(llm_egress_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LLMEgressGateway

Custom handler definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_model** | **str** |  | [optional] 
**configurations** | **object** |  | [optional] 
**created_at** | **str** |  | 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**endpoint_api_key** | **str** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**id** | **str** |  | 
**instana_agents** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**modified_at** | **str** |  | 
**name** | **str** |  | 
**prompt** | **str** |  | 
**supports** | **object** |  | 
**system** | **bool** |  | [optional] 
**tenant_unit_id** | **str** |  | 
**watsonx_key** | **str** |  | [optional] 
**watsonx_project** | **str** |  | [optional] 
**watsonx_url** | **str** |  | [optional] 

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



# GatewayStatusResponse

Gateway status for evaluation capability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether GENAI_EVALUATION capability is enabled | [optional] 
**gateway_id** | **str** | The ID of the enabled LLM gateway | [optional] 
**gateway_name** | **str** | The name of the enabled LLM gateway | [optional] 
**message** | **str** | Status message | [optional] 
**model_name** | **str** | The LLM model name configured in the gateway | [optional] 

## Example

```python
from instana_client.models.gateway_status_response import GatewayStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayStatusResponse from a JSON string
gateway_status_response_instance = GatewayStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GatewayStatusResponse.to_json())

# convert the object into a dict
gateway_status_response_dict = gateway_status_response_instance.to_dict()
# create an instance of GatewayStatusResponse from a dict
gateway_status_response_from_dict = GatewayStatusResponse.from_dict(gateway_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



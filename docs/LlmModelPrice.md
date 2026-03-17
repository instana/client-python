# LlmModelPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_input_cost** | **float** |  | [optional] 
**default_output_cost** | **float** |  | [optional] 
**has_default_price** | **bool** |  | [optional] 
**input_cost** | **float** |  | 
**is_user_defined** | **bool** |  | [optional] 
**model_name** | **str** |  | [optional] 
**output_cost** | **float** |  | 
**platform** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from instana_client.models.llm_model_price import LlmModelPrice

# TODO update the JSON string below
json = "{}"
# create an instance of LlmModelPrice from a JSON string
llm_model_price_instance = LlmModelPrice.from_json(json)
# print the JSON string representation of the object
print(LlmModelPrice.to_json())

# convert the object into a dict
llm_model_price_dict = llm_model_price_instance.to_dict()
# create an instance of LlmModelPrice from a dict
llm_model_price_from_dict = LlmModelPrice.from_dict(llm_model_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LlmModelPriceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | 

## Example

```python
from instana_client.models.llm_model_price_metadata import LlmModelPriceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LlmModelPriceMetadata from a JSON string
llm_model_price_metadata_instance = LlmModelPriceMetadata.from_json(json)
# print the JSON string representation of the object
print(LlmModelPriceMetadata.to_json())

# convert the object into a dict
llm_model_price_metadata_dict = llm_model_price_metadata_instance.to_dict()
# create an instance of LlmModelPriceMetadata from a dict
llm_model_price_metadata_from_dict = LlmModelPriceMetadata.from_dict(llm_model_price_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



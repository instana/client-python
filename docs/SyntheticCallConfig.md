# SyntheticCallConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_rules** | [**List[SyntheticCallRule]**](SyntheticCallRule.md) |  | 
**default_rules_enabled** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_call_config import SyntheticCallConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticCallConfig from a JSON string
synthetic_call_config_instance = SyntheticCallConfig.from_json(json)
# print the JSON string representation of the object
print(SyntheticCallConfig.to_json())

# convert the object into a dict
synthetic_call_config_dict = synthetic_call_config_instance.to_dict()
# create an instance of SyntheticCallConfig from a dict
synthetic_call_config_from_dict = SyntheticCallConfig.from_dict(synthetic_call_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



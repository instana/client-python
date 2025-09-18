# SyntheticCallWithDefaultsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_rules** | [**List[SyntheticCallRule]**](SyntheticCallRule.md) | The list of custom rules for synthetic endpoints defined by the user. | 
**default_rules** | [**List[SyntheticCallRule]**](SyntheticCallRule.md) |  | 
**default_rules_enabled** | **bool** | A flag to enable/disable the default synthetic endpoint configurations defined by Instana. | [optional] 

## Example

```python
from instana_client.models.synthetic_call_with_defaults_config import SyntheticCallWithDefaultsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticCallWithDefaultsConfig from a JSON string
synthetic_call_with_defaults_config_instance = SyntheticCallWithDefaultsConfig.from_json(json)
# print the JSON string representation of the object
print(SyntheticCallWithDefaultsConfig.to_json())

# convert the object into a dict
synthetic_call_with_defaults_config_dict = synthetic_call_with_defaults_config_instance.to_dict()
# create an instance of SyntheticCallWithDefaultsConfig from a dict
synthetic_call_with_defaults_config_from_dict = SyntheticCallWithDefaultsConfig.from_dict(synthetic_call_with_defaults_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



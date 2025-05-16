# ApdexConfigurationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apdex_entity** | [**ApdexEntity**](ApdexEntity.md) |  | 
**apdex_name** | **str** | Name of the Apdex Configuration | 

## Example

```python
from instana_client.models.apdex_configuration_input import ApdexConfigurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexConfigurationInput from a JSON string
apdex_configuration_input_instance = ApdexConfigurationInput.from_json(json)
# print the JSON string representation of the object
print(ApdexConfigurationInput.to_json())

# convert the object into a dict
apdex_configuration_input_dict = apdex_configuration_input_instance.to_dict()
# create an instance of ApdexConfigurationInput from a dict
apdex_configuration_input_from_dict = ApdexConfigurationInput.from_dict(apdex_configuration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



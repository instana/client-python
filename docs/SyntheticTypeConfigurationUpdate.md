# SyntheticTypeConfigurationUpdate

Synthetic test configuration that is unique to a synthetic type. Valid types are BrowserScript, DNS, HTTPAction, HTTPScript, SSLCertificate, WebpageAction, and WebpageScript.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_synthetic_call** | **bool** |  | [optional] 
**retries** | **int** |  | [optional] 
**retry_interval** | **int** |  | [optional] 
**synthetic_test** | **str** |  | [optional] 
**synthetic_type** | **str** |  | [optional] 
**timeout** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_type_configuration_update import SyntheticTypeConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTypeConfigurationUpdate from a JSON string
synthetic_type_configuration_update_instance = SyntheticTypeConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(SyntheticTypeConfigurationUpdate.to_json())

# convert the object into a dict
synthetic_type_configuration_update_dict = synthetic_type_configuration_update_instance.to_dict()
# create an instance of SyntheticTypeConfigurationUpdate from a dict
synthetic_type_configuration_update_from_dict = SyntheticTypeConfigurationUpdate.from_dict(synthetic_type_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



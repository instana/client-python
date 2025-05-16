# SyntheticTypeConfiguration

Synthetic test configuration that is unique to a synthetic type. Valid types are BrowserScript, HTTPAction, HTTPScript, SSLCertificate, WebpageAction, and WebpageScript.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_synthetic_call** | **bool** |  | 
**retries** | **int** |  | [optional] 
**retry_interval** | **int** |  | [optional] 
**synthetic_type** | **str** |  | 
**timeout** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_type_configuration import SyntheticTypeConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticTypeConfiguration from a JSON string
synthetic_type_configuration_instance = SyntheticTypeConfiguration.from_json(json)
# print the JSON string representation of the object
print(SyntheticTypeConfiguration.to_json())

# convert the object into a dict
synthetic_type_configuration_dict = synthetic_type_configuration_instance.to_dict()
# create an instance of SyntheticTypeConfiguration from a dict
synthetic_type_configuration_from_dict = SyntheticTypeConfiguration.from_dict(synthetic_type_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



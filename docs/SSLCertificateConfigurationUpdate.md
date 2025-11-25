# SSLCertificateConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_self_signed_certificate** | **bool** |  | [optional] 
**days_remaining_check** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**validation_rules** | [**SyntheticResourceUpdateListSSLCertificateValidationListSSLCertificateValidation**](SyntheticResourceUpdateListSSLCertificateValidationListSSLCertificateValidation.md) |  | [optional] 

## Example

```python
from instana_client.models.ssl_certificate_configuration_update import SSLCertificateConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SSLCertificateConfigurationUpdate from a JSON string
ssl_certificate_configuration_update_instance = SSLCertificateConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(SSLCertificateConfigurationUpdate.to_json())

# convert the object into a dict
ssl_certificate_configuration_update_dict = ssl_certificate_configuration_update_instance.to_dict()
# create an instance of SSLCertificateConfigurationUpdate from a dict
ssl_certificate_configuration_update_from_dict = SSLCertificateConfigurationUpdate.from_dict(ssl_certificate_configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



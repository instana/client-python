# SSLCertificateConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_self_signed_certificate** | **bool** |  | [optional] 
**days_remaining_check** | **int** |  | 
**hostname** | **str** |  | 
**port** | **int** |  | [optional] 
**validation_rules** | [**List[SSLCertificateValidation]**](SSLCertificateValidation.md) |  | [optional] 

## Example

```python
from instana_client.models.ssl_certificate_configuration import SSLCertificateConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SSLCertificateConfiguration from a JSON string
ssl_certificate_configuration_instance = SSLCertificateConfiguration.from_json(json)
# print the JSON string representation of the object
print(SSLCertificateConfiguration.to_json())

# convert the object into a dict
ssl_certificate_configuration_dict = ssl_certificate_configuration_instance.to_dict()
# create an instance of SSLCertificateConfiguration from a dict
ssl_certificate_configuration_from_dict = SSLCertificateConfiguration.from_dict(ssl_certificate_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



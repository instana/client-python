# SSLCertificateValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | **object** |  | 

## Example

```python
from instana_client.models.ssl_certificate_validation import SSLCertificateValidation

# TODO update the JSON string below
json = "{}"
# create an instance of SSLCertificateValidation from a JSON string
ssl_certificate_validation_instance = SSLCertificateValidation.from_json(json)
# print the JSON string representation of the object
print(SSLCertificateValidation.to_json())

# convert the object into a dict
ssl_certificate_validation_dict = ssl_certificate_validation_instance.to_dict()
# create an instance of SSLCertificateValidation from a dict
ssl_certificate_validation_from_dict = SSLCertificateValidation.from_dict(ssl_certificate_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EmailIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_email_subject_prefix** | [**CustomEmailSubjectPrefix**](CustomEmailSubjectPrefix.md) |  | [optional] 
**emails** | **List[str]** |  | 

## Example

```python
from instana_client.models.email_integration import EmailIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of EmailIntegration from a JSON string
email_integration_instance = EmailIntegration.from_json(json)
# print the JSON string representation of the object
print(EmailIntegration.to_json())

# convert the object into a dict
email_integration_dict = email_integration_instance.to_dict()
# create an instance of EmailIntegration from a dict
email_integration_from_dict = EmailIntegration.from_dict(email_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



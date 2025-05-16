# CustomEmailSubjectPrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_monitoring_issue** | **Dict[str, str]** | A map containing the open and close email subject value of a given agent monitoring issue | [optional] 
**change** | **Dict[str, str]** | A map containing the open and close email subject value of a given change event | [optional] 
**incident** | **Dict[str, str]** | A map containing the open and close email subject value of a given incident | [optional] 
**issue** | **Dict[str, str]** | A map containing the open and close email subject value of a given issue | [optional] 

## Example

```python
from instana_client.models.custom_email_subject_prefix import CustomEmailSubjectPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEmailSubjectPrefix from a JSON string
custom_email_subject_prefix_instance = CustomEmailSubjectPrefix.from_json(json)
# print the JSON string representation of the object
print(CustomEmailSubjectPrefix.to_json())

# convert the object into a dict
custom_email_subject_prefix_dict = custom_email_subject_prefix_instance.to_dict()
# create an instance of CustomEmailSubjectPrefix from a dict
custom_email_subject_prefix_from_dict = CustomEmailSubjectPrefix.from_dict(custom_email_subject_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



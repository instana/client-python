# AuditLogUiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[AuditLogEntry]**](AuditLogEntry.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from instana_client.models.audit_log_ui_response import AuditLogUiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogUiResponse from a JSON string
audit_log_ui_response_instance = AuditLogUiResponse.from_json(json)
# print the JSON string representation of the object
print(AuditLogUiResponse.to_json())

# convert the object into a dict
audit_log_ui_response_dict = audit_log_ui_response_instance.to_dict()
# create an instance of AuditLogUiResponse from a dict
audit_log_ui_response_from_dict = AuditLogUiResponse.from_dict(audit_log_ui_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



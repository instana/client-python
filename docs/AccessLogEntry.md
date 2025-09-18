# AccessLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**email** | **str** |  | 
**full_name** | **str** |  | 
**message** | **str** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**tenant_id** | **str** |  | 
**tenant_unit_id** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from instana_client.models.access_log_entry import AccessLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AccessLogEntry from a JSON string
access_log_entry_instance = AccessLogEntry.from_json(json)
# print the JSON string representation of the object
print(AccessLogEntry.to_json())

# convert the object into a dict
access_log_entry_dict = access_log_entry_instance.to_dict()
# create an instance of AccessLogEntry from a dict
access_log_entry_from_dict = AccessLogEntry.from_dict(access_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


